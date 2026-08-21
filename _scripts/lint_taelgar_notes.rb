#!/usr/bin/env ruby
# frozen_string_literal: true

# Batch preparation and guarded finalization for contextual Taelgar note linting.
#
# This script does not replace agentic review. It prepares per-note evidence
# packets using shared vault, DM-note, and Git indexes, snapshots reviewed files,
# and writes lint completion state only after every selected result passes a
# checksum, prior-state, and deterministic-validation preflight.

require "digest"
require "fileutils"
require "json"
require "open3"
require "optparse"
require "pathname"
require "tempfile"
require "time"

require_relative "validate_taelgar_note"

module TaelgarNoteLint
  module Batch
    SCHEMA_VERSION = 2
    DECISION_SCHEMA_VERSION = 2
    WORKSPACE_SCHEMA_VERSION = 1
    DEFAULT_MAX_NOTES = 10
    DEFAULT_MAX_TOKENS = 30_000
    ESTIMATED_CHARACTERS_PER_TOKEN = 3
    EDITORIAL_VERDICTS = [
      "Sufficient",
      "Sufficient, worth expanding",
      "Underdeveloped"
    ].freeze

    class BatchError < StandardError; end

    module_function

    def sha256(text)
      Digest::SHA256.hexdigest(text)
    end

    def file_sha256(path)
      Digest::SHA256.file(path.to_s).hexdigest
    end

    def canonical_state_value(value)
      value.is_a?(Time) ? value.iso8601 : value&.to_s
    end

    def completion_state(note)
      lint_blocks = note.text.to_enum(:scan, LINT_BLOCK_PATTERN).map { Regexp.last_match[0] }
      {
        "lintedAt" => canonical_state_value(note.data["lintedAt"]),
        "lintVersion" => canonical_state_value(note.data["lintVersion"]),
        "lintTagged" => note.tags.include?("status/check/lint"),
        "lintBlockCount" => lint_blocks.length,
        "lintBlockSha256" => lint_blocks.empty? ? nil : sha256(lint_blocks.join("\0"))
      }
    end

    def completion_identity(note)
      {
        "lintedAt" => canonical_state_value(note.data["lintedAt"]),
        "lintVersion" => canonical_state_value(note.data["lintVersion"])
      }
    end

    def relative_note_path(root, path)
      absolute = Pathname.new(path)
      absolute = root.join(absolute) unless absolute.absolute?
      absolute = absolute.expand_path
      relative = absolute.relative_path_from(root).to_s
      if relative == ".." || relative.start_with?("../") || !relative.end_with?(".md")
        raise BatchError, "Target is not a Markdown note inside the vault: #{path}"
      end

      relative
    rescue ArgumentError
      raise BatchError, "Target is not inside the vault: #{path}"
    end

    def lint_target_exclusion(path)
      directories = Pathname.new(path).each_filename.to_a[0...-1]
      return "Worldbuilding" if directories.include?("Worldbuilding")
      return "dot directory" if directories.any? { |part| part.start_with?(".") }
      return "underscore directory" if directories.any? { |part| part.start_with?("_") }

      nil
    end

    def lintable_path?(path)
      lint_target_exclusion(path).nil?
    end

    def ensure_lintable_path!(path)
      exclusion = lint_target_exclusion(path)
      return unless exclusion

      raise BatchError, "Notes under dot directories, underscore directories, or Worldbuilding are outside Taelgar Note Linter scope (matched #{exclusion}): #{path}"
    end

    def objectively_lintable_note?(note)
      TaelgarNoteLint.authored_body_candidate?(note)
    end

    def ensure_objectively_lintable_note!(note)
      return if objectively_lintable_note?(note)

      raise BatchError, "Note has no authored body candidate after objective blank-stub screening and is not lintable: #{note.path}"
    end

    def estimated_input_tokens(record)
      bytes = record.dig("file", "bytes").to_i
      packet = record.merge(
        "candidateRelativePath" => "candidates/#{record.fetch('path')}",
        "estimatedInputTokens" => 0
      )
      packet_bytes = JSON.pretty_generate(packet).bytesize + 256
      ((bytes + packet_bytes).to_f / ESTIMATED_CHARACTERS_PER_TOKEN).ceil
    end

    def ensure_external_review_dir!(root, path)
      root = Pathname.new(root).expand_path
      path = Pathname.new(path).expand_path
      if path == root || path.to_s.start_with?("#{root}#{File::SEPARATOR}")
        raise BatchError, "Review workspace must be outside the vault: #{path}"
      end

      path
    end

    def valid_completion_pair?(note)
      linted_at = canonical_state_value(note.data["lintedAt"])
      lint_version = canonical_state_value(note.data["lintVersion"])
      return false if linted_at.to_s.empty? || lint_version.to_s.empty?

      Time.iso8601(linted_at)
      Gem::Version.new(lint_version)
      true
    rescue ArgumentError
      false
    end

    class GitBaselineResolver
      def initialize(root)
        @root = Pathname.new(root).expand_path
        @cache = {}
      end

      def resolve(note)
        value = Batch.canonical_state_value(note.data["lintedAt"])
        return { "ref" => nil, "kind" => nil } if value.to_s.empty?

        Time.iso8601(value)
        state = Batch.completion_identity(note)
        cache_key = [note.path, state]
        completion_ref = @cache[cache_key] ||= completion_state_commit(note.path, value, state)
        return { "ref" => completion_ref, "kind" => "lint_state_commit" } if completion_ref

        time_ref = @cache[value] ||= begin
          output = git("rev-list", "-1", "--before=#{value}", "HEAD").strip
          output.empty? ? nil : output
        end
        { "ref" => time_ref, "kind" => time_ref ? "timestamp_commit" : nil }
      rescue ArgumentError
        { "ref" => nil, "kind" => nil }
      end

      private

      def completion_state_commit(path, linted_at, state)
        commits = git("log", "--format=%H", "--reverse", "--since=#{linted_at}", "--", path).lines.map(&:strip)
        commits.find do |commit|
          text = git("show", "#{commit}:#{path}")
          Batch.completion_identity(ParsedNote.new(path, text)) == state
        end
      end

      def git(*arguments)
        stdout, stderr, status = Open3.capture3("git", *arguments, chdir: @root.to_s)
        stdout = stdout.force_encoding(Encoding::UTF_8).scrub
        stderr = stderr.force_encoding(Encoding::UTF_8).scrub
        raise BatchError, "Git command failed: #{stderr.strip}" unless status.success?

        stdout
      end
    end

    class Preparer
      def initialize(root:)
        @root = Pathname.new(root).expand_path
        @index = NoteIndex.new(@root)
        @validator = Validator.new(root: @root, check_links: true, index: @index)
        @baselines = GitBaselineResolver.new(@root)
        @freshness_scanners = {}
      end

      def prepare(paths)
        relative_paths = paths.map { |path| Batch.relative_note_path(@root, path) }.uniq.sort
        raise BatchError, "No notes were selected." if relative_paths.empty?
        relative_paths.each { |path| Batch.ensure_lintable_path!(path) }

        notes = relative_paths.map do |path|
          absolute = @root.join(path)
          raise BatchError, "Note does not exist: #{path}" unless absolute.file?

          ParsedNote.new(path, TaelgarNoteLint.read_text(absolute))
        end
        notes.each { |note| Batch.ensure_objectively_lintable_note!(note) }
        @validator.preload_dm_notes(notes)

        records = notes.map { |note| prepare_note(note) }
        {
          "schemaVersion" => SCHEMA_VERSION,
          "validatorVersion" => VERSION,
          "generatedAt" => Time.now.iso8601,
          "root" => @root.to_s,
          "notes" => records
        }
      end

      private

      def prepare_note(note)
        absolute = @root.join(note.path)
        report = @validator.validate_path(note.path)
        freshness = freshness_for(note, report)
        dm_freshness = dm_freshness_for(note, @validator.dm_sources(note))
        routing = routing_for(note, freshness, dm_freshness, report)
        {
          "path" => note.path,
          "file" => {
            "sha256" => Batch.file_sha256(absolute),
            "bytes" => File.size(absolute),
            "modifiedAt" => File.mtime(absolute).iso8601(6)
          },
          "priorCompletionState" => Batch.completion_state(note),
          "routing" => routing,
          "deterministic" => report,
          "freshness" => freshness,
          "dmFreshness" => dm_freshness
        }
      end

      def freshness_for(note, report)
        linted_at = note.data["lintedAt"]
        return { "baselineRef" => nil, "candidates" => [], "skipped" => "The note has no prior lint timestamp." } unless linted_at

        baseline = @baselines.resolve(note)
        unless baseline["ref"]
          return { "baselineRef" => nil, "baselineKind" => nil, "candidates" => [], "skipped" => "The prior lint timestamp is invalid or predates Git history." }
        end

        scanner = @freshness_scanners[baseline.fetch("ref")] ||= FreshnessScanner.new(
          root: @root,
          index: @index,
          baseline_ref: baseline.fetch("ref")
        )
        scanner.scan(report, linted_at: Batch.canonical_state_value(linted_at)).merge("baselineKind" => baseline.fetch("kind"))
      end

      def dm_freshness_for(note, sources)
        linted_at = Batch.canonical_state_value(note.data["lintedAt"])
        return { "basis" => "filesystem_mtime", "candidates" => [] } if linted_at.to_s.empty?

        lint_time = Time.iso8601(linted_at)
        candidates = sources.each_with_object([]) do |source, selected|
          path = source["path"].to_s
          modified_at = source["modifiedAt"].to_s
          next unless path.start_with?("_DM_/") && Time.iso8601(modified_at) > lint_time

          selected << {
            "path" => path,
            "modifiedAt" => modified_at,
            "matchKinds" => Array(source["matchKinds"]).uniq
          }
        end
        { "basis" => "filesystem_mtime", "candidates" => candidates.sort_by { |item| item.fetch("path") } }
      rescue ArgumentError
        { "basis" => "filesystem_mtime", "candidates" => [], "skipped" => "The prior lint timestamp is invalid." }
      end

      def routing_for(note, freshness, dm_freshness, report)
        prior_version = Batch.canonical_state_value(note.data["lintVersion"])
        candidates = freshness.fetch("candidates", [])
        if note.data["lintedAt"].nil? || prior_version.nil?
          reason = "unlinted"
          review = true
        elsif prior_version != VERSION
          reason = "stale_linter_version"
          review = true
        elsif report.dig("summary", "errors").to_i.positive?
          reason = "deterministic_error"
          review = true
        elsif dm_freshness.fetch("candidates", []).any?
          reason = "newer_private_dm_evidence"
          review = true
        elsif candidates.any? { |candidate| candidate["mentionChanged"] }
          reason = "newer_mention_changed"
          review = true
        elsif candidates.any?
          reason = "newer_source_mentions_subject"
          review = true
        else
          reason = "current_with_no_newer_invention_candidate"
          review = false
        end
        {
          "reviewRecommended" => review,
          "reason" => reason,
          "previousLintVersion" => prior_version,
          "currentLintVersion" => VERSION
        }
      end
    end

    class Snapshotter
      def initialize(root:, manifest:, manifest_sha256:)
        @root = Pathname.new(root).expand_path
        @manifest = manifest
        @manifest_sha256 = manifest_sha256
      end

      def snapshot
        validate_manifest!
        decisions = @manifest.fetch("notes").map do |record|
          path = record.fetch("path")
          text = TaelgarNoteLint.read_text(@root.join(path))
          note = ParsedNote.new(path, text)
          Batch.ensure_objectively_lintable_note!(note)
          unless Batch.completion_state(note) == record.fetch("priorCompletionState")
            raise BatchError, "Lint completion state changed after preparation: #{path}"
          end

          {
            "path" => path,
            "expectedSha256" => Batch.file_sha256(@root.join(path)),
            "candidateSha256" => Batch.file_sha256(@root.join(path)),
            "eligibility" => "eligible",
            "eligibilityReason" => nil,
            "editorialVerdict" => nil,
            "outcome" => "review_required",
            "lintReport" => nil,
            "handoff" => nil,
            "needsAdjudication" => false,
            "adjudication" => "not_required"
          }
        end
        {
          "schemaVersion" => DECISION_SCHEMA_VERSION,
          "validatorVersion" => VERSION,
          "manifestSha256" => @manifest_sha256,
          "snapshottedAt" => Time.now.iso8601,
          "notes" => decisions
        }
      end

      private

      def validate_manifest!
        unless @manifest["schemaVersion"] == SCHEMA_VERSION
          raise BatchError, "Unsupported batch manifest schema: #{@manifest['schemaVersion'].inspect}"
        end
        @manifest.fetch("notes").each { |record| Batch.ensure_lintable_path!(record.fetch("path")) }
        return if @manifest["validatorVersion"].to_s == VERSION

        raise BatchError, "Manifest validator version #{@manifest['validatorVersion'].inspect} does not match #{VERSION}."
      end
    end

    class WorkspaceBuilder
      def initialize(root:, manifest:, manifest_sha256:, output_dir:, max_notes: DEFAULT_MAX_NOTES,
                     max_tokens: DEFAULT_MAX_TOKENS)
        @root = Pathname.new(root).expand_path
        @manifest = manifest
        @manifest_sha256 = manifest_sha256
        @output_dir = Batch.ensure_external_review_dir!(@root, output_dir)
        @max_notes = Integer(max_notes)
        @max_tokens = Integer(max_tokens)
        raise BatchError, "Shard limits must be positive." unless @max_notes.positive? && @max_tokens.positive?
      rescue ArgumentError, TypeError
        raise BatchError, "Shard limits must be positive integers."
      end

      def build
        records = validate_manifest!
        prepare_output_dir!
        shards = build_shards(records)
        copy_candidates(records)
        shard_records = shards.each_with_index.map { |shard, index| write_shard(shard, index + 1) }
        workspace = {
          "schemaVersion" => WORKSPACE_SCHEMA_VERSION,
          "decisionSchemaVersion" => DECISION_SCHEMA_VERSION,
          "validatorVersion" => VERSION,
          "manifestSha256" => @manifest_sha256,
          "createdAt" => Time.now.iso8601,
          "maxNotes" => @max_notes,
          "maxEstimatedInputTokens" => @max_tokens,
          "shards" => shard_records
        }
        write_json(@output_dir.join("workspace.json"), workspace)
        workspace
      end

      private

      def validate_manifest!
        unless @manifest["schemaVersion"] == SCHEMA_VERSION
          raise BatchError, "Unsupported batch manifest schema: #{@manifest['schemaVersion'].inspect}"
        end
        unless @manifest["validatorVersion"].to_s == VERSION
          raise BatchError, "Manifest validator version #{@manifest['validatorVersion'].inspect} does not match #{VERSION}."
        end

        records = @manifest.fetch("notes").sort_by { |record| record.fetch("path") }
        paths = records.map { |record| record.fetch("path") }
        raise BatchError, "Manifest contains duplicate note paths." unless paths.uniq.length == paths.length

        records.each do |record|
          path = record.fetch("path")
          Batch.ensure_lintable_path!(path)
          unless Batch.relative_note_path(@root, path) == path
            raise BatchError, "Manifest contains a noncanonical note path: #{path}"
          end
          absolute = @root.join(path)
          raise BatchError, "Note does not exist: #{path}" unless absolute.file?
          expected_sha = record.dig("file", "sha256").to_s
          if expected_sha.empty? || Batch.file_sha256(absolute) != expected_sha
            raise BatchError, "Live note changed after preparation: #{path}"
          end
          note = ParsedNote.new(path, TaelgarNoteLint.read_text(absolute))
          Batch.ensure_objectively_lintable_note!(note)
          unless Batch.completion_state(note) == record.fetch("priorCompletionState")
            raise BatchError, "Lint completion state changed after preparation: #{path}"
          end
        end
        records
      end

      def prepare_output_dir!
        if @output_dir.exist? && (!@output_dir.directory? || @output_dir.children.any?)
          raise BatchError, "Review workspace must be absent or empty: #{@output_dir}"
        end
        FileUtils.mkdir_p(@output_dir.join("candidates"))
        FileUtils.mkdir_p(@output_dir.join("packets"))
        FileUtils.mkdir_p(@output_dir.join("results"))
        [@output_dir, @output_dir.join("candidates"), @output_dir.join("packets"), @output_dir.join("results")].each do |directory|
          File.chmod(0o700, directory)
        end
      end

      def build_shards(records)
        shards = []
        current = []
        current_tokens = 0
        records.each do |record|
          estimate = Batch.estimated_input_tokens(record)
          if current.any? && (current.length >= @max_notes || current_tokens + estimate > @max_tokens)
            shards << current
            current = []
            current_tokens = 0
          end
          current << [record, estimate]
          current_tokens += estimate
        end
        shards << current unless current.empty?
        shards
      end

      def copy_candidates(records)
        records.each do |record|
          path = record.fetch("path")
          destination = @output_dir.join("candidates", path)
          FileUtils.mkdir_p(destination.dirname)
          destination.dirname.ascend do |directory|
            break if directory == @output_dir

            File.chmod(0o700, directory)
          end
          File.binwrite(destination, File.binread(@root.join(path)))
          File.chmod(0o600, destination)
        end
      end

      def write_shard(shard, number)
        shard_id = format("shard-%03d", number)
        packet_path = "packets/#{shard_id}.json"
        result_path = "results/#{shard_id}.json"
        estimated_tokens = shard.sum { |_record, estimate| estimate }
        packet_notes = shard.map do |record, estimate|
          record.merge(
            "candidateRelativePath" => "candidates/#{record.fetch('path')}",
            "estimatedInputTokens" => estimate
          )
        end
        result_notes = shard.map do |record, _estimate|
          {
            "path" => record.fetch("path"),
            "candidateSha256" => record.dig("file", "sha256"),
            "eligibility" => "review_required",
            "eligibilityReason" => nil,
            "editorialVerdict" => nil,
            "outcome" => "review_required",
            "lintReport" => nil,
            "handoff" => nil,
            "needsAdjudication" => false,
            "adjudication" => "not_required"
          }
        end
        packet = {
          "schemaVersion" => SCHEMA_VERSION,
          "validatorVersion" => VERSION,
          "manifestSha256" => @manifest_sha256,
          "shardId" => shard_id,
          "estimatedInputTokens" => estimated_tokens,
          "notes" => packet_notes
        }
        result = {
          "schemaVersion" => DECISION_SCHEMA_VERSION,
          "validatorVersion" => VERSION,
          "manifestSha256" => @manifest_sha256,
          "shardId" => shard_id,
          "notes" => result_notes
        }
        write_json(@output_dir.join(packet_path), packet)
        write_json(@output_dir.join(result_path), result)
        {
          "id" => shard_id,
          "packet" => packet_path,
          "result" => result_path,
          "noteCount" => shard.length,
          "estimatedInputTokens" => estimated_tokens,
          "paths" => shard.map { |record, _estimate| record.fetch("path") }
        }
      end

      def write_json(path, document)
        File.write(path, "#{JSON.pretty_generate(document)}\n")
        File.chmod(0o600, path)
      end
    end

    class WorkspaceLoader
      def initialize(root:, manifest:, manifest_sha256:, review_dir:)
        @root = Pathname.new(root).expand_path
        @manifest = manifest
        @manifest_sha256 = manifest_sha256
        @review_dir = Batch.ensure_external_review_dir!(@root, review_dir)
      end

      def decisions
        workspace = JSON.parse(File.binread(@review_dir.join("workspace.json")).force_encoding(Encoding::UTF_8).scrub)
        validate_workspace!(workspace)
        expected_paths = @manifest.fetch("notes").map { |record| record.fetch("path") }.sort
        assigned_paths = workspace.fetch("shards").flat_map { |shard| shard.fetch("paths") }
        raise BatchError, "Review workspace assigns a note more than once." unless assigned_paths.uniq.length == assigned_paths.length
        unless assigned_paths.sort == expected_paths
          raise BatchError, "Review workspace must assign every manifest note exactly once."
        end

        notes = workspace.fetch("shards").sort_by { |shard| shard.fetch("id") }.flat_map do |shard|
          load_shard_result(shard)
        end
        paths = notes.map { |note| note.fetch("path") }
        raise BatchError, "Shard results contain duplicate note paths." unless paths.uniq.length == paths.length
        unless paths.sort == expected_paths
          raise BatchError, "Shard results must contain exactly one result for every manifest note."
        end
        {
          "schemaVersion" => DECISION_SCHEMA_VERSION,
          "validatorVersion" => VERSION,
          "manifestSha256" => @manifest_sha256,
          "workspaceMode" => true,
          "notes" => notes.sort_by { |note| note.fetch("path") }
        }
      end

      private

      def validate_workspace!(workspace)
        unless workspace["schemaVersion"] == WORKSPACE_SCHEMA_VERSION &&
               workspace["decisionSchemaVersion"] == DECISION_SCHEMA_VERSION
          raise BatchError, "Unsupported review workspace schema."
        end
        unless workspace["validatorVersion"].to_s == VERSION && workspace["manifestSha256"] == @manifest_sha256
          raise BatchError, "Review workspace does not match the manifest or validator version."
        end
      end

      def load_shard_result(shard)
        result_relative = shard.fetch("result")
        result_path = safe_workspace_path(result_relative)
        result = JSON.parse(File.binread(result_path).force_encoding(Encoding::UTF_8).scrub)
        unless result["schemaVersion"] == DECISION_SCHEMA_VERSION && result["validatorVersion"].to_s == VERSION &&
               result["manifestSha256"] == @manifest_sha256 && result["shardId"] == shard.fetch("id")
          raise BatchError, "Shard result does not match its workspace assignment: #{shard.fetch('id')}"
        end
        expected_paths = shard.fetch("paths").sort
        actual_paths = result.fetch("notes").map { |note| note.fetch("path") }.sort
        unless actual_paths == expected_paths && actual_paths.uniq.length == actual_paths.length
          raise BatchError, "Shard result paths do not match its assignment: #{shard.fetch('id')}"
        end

        result.fetch("notes").map do |decision|
          path = decision.fetch("path")
          candidate = safe_candidate_path(path)
          raise BatchError, "Staged candidate is missing: #{path}" unless candidate.file?

          decision.merge("_candidatePath" => candidate.to_s)
        end
      end

      def safe_workspace_path(relative)
        base = @review_dir.expand_path
        path = base.join(relative).expand_path
        unless path.to_s.start_with?("#{base}#{File::SEPARATOR}")
          raise BatchError, "Review workspace contains an unsafe path: #{relative}"
        end

        path
      end

      def safe_candidate_path(note_path)
        base = @review_dir.join("candidates").expand_path
        path = base.join(note_path).expand_path
        unless path.to_s.start_with?("#{base}#{File::SEPARATOR}")
          raise BatchError, "Review workspace contains an unsafe candidate path: #{note_path}"
        end

        path
      end
    end

    class Finalizer
      def initialize(root:, manifest:, manifest_sha256:, decisions:, completed_at: nil)
        @root = Pathname.new(root).expand_path
        @manifest = manifest
        @manifest_sha256 = manifest_sha256
        @decisions = decisions
        @completed_at = completed_at ? Time.iso8601(completed_at).iso8601 : Time.now.iso8601
      rescue ArgumentError
        raise BatchError, "--at must be an ISO 8601 timestamp with an offset."
      end

      def finalize(write: false)
        validate_documents!
        records = @manifest.fetch("notes").each_with_object({}) { |record, memo| memo[record.fetch("path")] = record }
        decision_list = @decisions.fetch("notes")
        ensure_complete_decisions!(records, decision_list)

        index = NoteIndex.new(@root)
        validator = Validator.new(root: @root, check_links: true, index: index)
        current_notes = decision_list.map do |decision|
          path = decision.fetch("path")
          ParsedNote.new(path, TaelgarNoteLint.read_text(@root.join(path)))
        end
        validator.preload_dm_notes(current_notes)

        candidates = decision_list.map do |decision|
          build_candidate(decision, records.fetch(decision.fetch("path")), validator)
        end
        commit(candidates.reject { |candidate| candidate["skipWrite"] }) if write
        {
          "schemaVersion" => DECISION_SCHEMA_VERSION,
          "validatorVersion" => VERSION,
          "completedAt" => @completed_at,
          "wrote" => write,
          "notes" => candidates.map do |candidate|
            {
              "path" => candidate.fetch("path"),
              "eligibility" => candidate.fetch("eligibility"),
              "editorialVerdict" => candidate["editorialVerdict"],
              "outcome" => candidate.fetch("outcome"),
              "sha256" => Batch.sha256(candidate.fetch("text"))
            }
          end
        }
      end

      private

      def validate_documents!
        unless @manifest["schemaVersion"] == SCHEMA_VERSION && @decisions["schemaVersion"] == DECISION_SCHEMA_VERSION
          raise BatchError, "Unsupported batch manifest or decision schema."
        end
        unless @manifest["validatorVersion"].to_s == VERSION && @decisions["validatorVersion"].to_s == VERSION
          raise BatchError, "Batch files do not match validator version #{VERSION}."
        end
        @manifest.fetch("notes").each { |record| Batch.ensure_lintable_path!(record.fetch("path")) }
        @decisions.fetch("notes").each { |decision| Batch.ensure_lintable_path!(decision.fetch("path")) }
        return if @decisions["manifestSha256"] == @manifest_sha256

        raise BatchError, "Decision file was created from a different manifest."
      end

      def ensure_complete_decisions!(records, decisions)
        paths = decisions.map { |decision| decision["path"] }
        raise BatchError, "Decision file contains duplicate note paths." unless paths.uniq.length == paths.length
        unless paths.sort == records.keys.sort
          raise BatchError, "Decision file must contain exactly one result for every manifest note."
        end
        decisions.each { |decision| validate_completed_decision!(decision) }
      end

      def build_candidate(decision, record, validator)
        path = decision.fetch("path")
        absolute = @root.join(path)
        expected_sha = if @decisions["workspaceMode"]
                         record.dig("file", "sha256").to_s
                       else
                         decision.fetch("expectedSha256")
                       end
        unless Batch.file_sha256(absolute) == expected_sha
          boundary = @decisions["workspaceMode"] ? "preparation" : "snapshot"
          raise BatchError, "Reviewed file changed after #{boundary}: #{path}"
        end
        live_text = TaelgarNoteLint.read_text(absolute)
        live_note = ParsedNote.new(path, live_text)
        Batch.ensure_objectively_lintable_note!(live_note)
        unless Batch.completion_state(live_note) == record.fetch("priorCompletionState")
          raise BatchError, "Lint completion state changed before finalization: #{path}"
        end

        staged_text = decision["_candidatePath"] ? TaelgarNoteLint.read_text(decision.fetch("_candidatePath")) : live_text
        candidate_sha = decision["candidateSha256"].to_s
        candidate_sha = decision["expectedSha256"].to_s if candidate_sha.empty? && !@decisions["workspaceMode"]
        unless candidate_sha.match?(/\A[0-9a-f]{64}\z/) && Batch.sha256(staged_text) == candidate_sha
          raise BatchError, "Staged candidate changed after its review result was completed: #{path}"
        end
        if decision.fetch("eligibility") == "ineligible"
          unless staged_text == live_text
            raise BatchError, "A semantically ineligible staged candidate must remain unchanged: #{path}"
          end
          return {
            "path" => path,
            "eligibility" => "ineligible",
            "editorialVerdict" => nil,
            "outcome" => "ineligible",
            "expectedSha256" => expected_sha,
            "text" => live_text,
            "skipWrite" => true
          }
        end

        staged_note = ParsedNote.new(path, staged_text)
        Batch.ensure_objectively_lintable_note!(staged_note)
        unless Batch.completion_state(staged_note) == record.fetch("priorCompletionState")
          raise BatchError, "Staged lint completion state changed before finalization: #{path}"
        end
        outcome = decision.fetch("outcome")
        report = validate_report(decision["lintReport"], outcome, path)
        validate_editorial_consistency!(decision, report)
        text_without_lint = staged_text.gsub(LINT_BLOCK_PATTERN, "")
        note = ParsedNote.new(path, text_without_lint)
        raise BatchError, "Cannot finalize invalid frontmatter in #{path}: #{note.yaml_error || note.frontmatter_state}" unless note.frontmatter_state == :present && !note.yaml_error

        tags = note.tags.reject { |tag| tag == "status/check/lint" }
        tags << "status/check/lint" if outcome == "open"
        note.data["tags"] = tags.uniq
        note.data["lintedAt"] = @completed_at
        note.data["lintVersion"] = VERSION
        formatted = FrontmatterFormatter.new(note).format_text.sub(/\n*\z/, "\n")
        formatted = "#{formatted}\n#{report}\n" if report

        validation = validator.validate_text(path, formatted)
        errors = validation.fetch("findings").select { |finding| finding["severity"] == "error" }
        unless errors.empty?
          rules = errors.map { |finding| finding["ruleId"] }.uniq.join(", ")
          raise BatchError, "Final deterministic validation failed for #{path}: #{rules}"
        end

        {
          "path" => path,
          "eligibility" => "eligible",
          "editorialVerdict" => decision.fetch("editorialVerdict"),
          "outcome" => outcome,
          "expectedSha256" => expected_sha,
          "text" => formatted
        }
      rescue FrontmatterFormatter::UnsafeFrontmatter => error
        raise BatchError, "Cannot safely format #{path}: #{error.message}"
      end

      def validate_report(value, outcome, path)
        if outcome == "clean"
          raise BatchError, "A clean outcome cannot retain a Lint report: #{path}" unless value.nil? || value.to_s.strip.empty?

          return nil
        end

        report = value.to_s.strip
        match = report.match(/\A%%\^Lint%%\s*(.*?)\s*%%\^End%%\z/m)
        unless match && match[1].match?(/^\s*-\s+\[ \]\s+/)
          raise BatchError, "An open outcome requires one complete Lint block with an unchecked task: #{path}"
        end
        unless match[1].match?(/\*\*(?:Error|Warning|Suggestion)\s+—\s+[a-z0-9_.-]+:/i)
          raise BatchError, "Open Lint tasks must include a severity and stable rule ID: #{path}"
        end

        report
      end

      def validate_completed_decision!(decision)
        path = decision.fetch("path")
        if decision["needsAdjudication"] == true
          raise BatchError, "A shard result still requires adjudication: #{path}"
        end

        case decision["eligibility"]
        when "ineligible"
          if decision["eligibilityReason"].to_s.strip.empty?
            raise BatchError, "A semantically ineligible result requires a concise reason: #{path}"
          end
          unless decision["adjudication"] == "complete"
            raise BatchError, "A semantically ineligible result requires completed Sol xhigh adjudication: #{path}"
          end
          unless decision["editorialVerdict"].nil? && decision["outcome"].nil? &&
                 decision["lintReport"].to_s.strip.empty? && decision["handoff"].to_s.strip.empty?
            raise BatchError, "A semantically ineligible result cannot carry a verdict, outcome, Lint report, or handoff: #{path}"
          end
        when "eligible"
          verdict = decision["editorialVerdict"]
          unless EDITORIAL_VERDICTS.include?(verdict) && %w[clean open].include?(decision["outcome"])
            raise BatchError, "Every eligible note needs an editorial verdict and clean or open outcome: #{path}"
          end
          if verdict == "Underdeveloped" && decision["outcome"] != "open"
            raise BatchError, "An Underdeveloped verdict must remain open: #{path}"
          end
          if report_rule_ids(decision["lintReport"]).include?("editorial.note_underdeveloped") &&
             decision["adjudication"] != "complete"
            raise BatchError, "Invention-based underdevelopment requires completed Sol xhigh adjudication: #{path}"
          end
        else
          raise BatchError, "Every note needs completed semantic eligibility review: #{path}"
        end
      end

      def validate_editorial_consistency!(decision, report)
        path = decision.fetch("path")
        verdict = decision.fetch("editorialVerdict")
        rule_ids = report_rule_ids(report)
        if rule_ids.any? { |rule_id| rule_id.include?("worth_expanding") }
          raise BatchError, "Worth expanding cannot be represented as a persistent lint finding: #{path}"
        end
        if rule_ids.include?("editorial.note_underdeveloped") && verdict != "Underdeveloped"
          raise BatchError, "editorial.note_underdeveloped requires an Underdeveloped verdict: #{path}"
        end
        return unless verdict == "Underdeveloped"

        central_gap = rule_ids.include?("editorial.note_underdeveloped") ||
                      rule_ids.any? { |rule_id| rule_id.start_with?("coverage.") }
        unless central_gap
          raise BatchError, "An Underdeveloped verdict requires a coverage or editorial.note_underdeveloped finding: #{path}"
        end
      end

      def report_rule_ids(report)
        report.to_s.scan(/\*\*(?:Error|Warning|Suggestion)\s+—\s+([a-z0-9_.-]+):/i).flatten
      end

      def commit(candidates)
        candidates.each do |candidate|
          current_path = @root.join(candidate.fetch("path"))
          unless Batch.file_sha256(current_path) == candidate.fetch("expectedSha256")
            raise BatchError, "Reviewed file changed during finalization: #{candidate.fetch('path')}"
          end
        end

        staged = candidates.map { |candidate| stage_candidate(candidate) }
        committed = []
        begin
          staged.each do |entry|
            File.rename(entry.fetch("new_file").path, entry.fetch("target"))
            committed << entry
          end
          staged.each do |entry|
            next if Batch.file_sha256(entry.fetch("target")) == entry.fetch("expectedSha256")

            raise BatchError, "Written file checksum mismatch: #{entry.fetch('path')}"
          end
        rescue StandardError => error
          committed.reverse_each do |entry|
            rollback_path = entry.fetch("rollback_file").path
            File.rename(rollback_path, entry.fetch("target")) if File.exist?(rollback_path)
          end
          raise BatchError, "Batch commit failed and was rolled back: #{error.message}"
        ensure
          staged.each do |entry|
            entry.fetch("new_file").close!
            entry.fetch("rollback_file").close!
          end
        end
      end

      def stage_candidate(candidate)
        target = @root.join(candidate.fetch("path")).to_s
        mode = File.stat(target).mode
        new_file = Tempfile.new([".taelgar-lint-new-", ".md"], File.dirname(target))
        rollback_file = Tempfile.new([".taelgar-lint-old-", ".md"], File.dirname(target))
        write_tempfile(new_file, candidate.fetch("text"), mode)
        write_tempfile(rollback_file, TaelgarNoteLint.read_text(target), mode)
        {
          "path" => candidate.fetch("path"),
          "target" => target,
          "expectedSha256" => Batch.sha256(candidate.fetch("text")),
          "new_file" => new_file,
          "rollback_file" => rollback_file
        }
      end

      def write_tempfile(tempfile, text, mode)
        tempfile.binmode
        tempfile.write(text)
        tempfile.flush
        tempfile.fsync
        File.chmod(mode & 0o7777, tempfile.path)
        tempfile.close
      end
    end

    class CLI
      def initialize(argv)
        @argv = argv.dup
      end

      def run
        command = @argv.shift
        case command
        when "prepare" then prepare
        when "workspace" then workspace
        when "snapshot" then snapshot
        when "finalize" then finalize
        else
          warn usage
          2
        end
      rescue OptionParser::ParseError, Errno::ENOENT, KeyError, JSON::ParserError, BatchError => error
        warn error.message
        2
      end

      private

      def prepare
        options = { root: Pathname.pwd, all_linted: false, stale: false, only_needs_review: false, re_lint: false }
        parser = OptionParser.new do |opts|
          opts.banner = "Usage: lint_taelgar_notes.rb prepare [options] [NOTE ...]"
          opts.on("--root PATH", "Vault root") { |value| options[:root] = Pathname.new(value) }
          opts.on("--re-lint", "Include notes with valid prior lint completion state") { options[:re_lint] = true }
          opts.on("--all-linted", "Select every note with lint completion state") { options[:all_linted] = true }
          opts.on("--stale", "Select notes whose lintVersion is not current") { options[:stale] = true }
          opts.on("--only-needs-review", "Exclude current notes with no freshness candidates") { options[:only_needs_review] = true }
          opts.on("--output PATH", "Write JSON to a file instead of stdout") { |value| options[:output] = value }
        end
        parser.parse!(@argv)
        if (options[:all_linted] || options[:stale]) && !options[:re_lint]
          raise BatchError, "--all-linted and --stale require --re-lint because completed notes are excluded by default."
        end
        if (options[:all_linted] || options[:stale]) && @argv.any?
          raise BatchError, "Broad linted-note discovery cannot be combined with named targets; resolve the user's scope first."
        end
        root = options[:root].expand_path
        paths = discover_paths(root, options)
        paths.concat(@argv)
        paths = paths.map { |path| Batch.relative_note_path(root, path) }.uniq.sort
        paths.each { |path| Batch.ensure_lintable_path!(path) }
        requested_count = paths.length
        skipped_no_reviewable_prose = []
        paths.reject! do |path|
          absolute = root.join(path)
          next false unless absolute.file?

          note = ParsedNote.new(path, TaelgarNoteLint.read_text(absolute))
          next false if Batch.objectively_lintable_note?(note)

          skipped_no_reviewable_prose << path
          true
        end
        lintable_candidate_count = paths.length
        unless options[:re_lint]
          paths.reject! do |path|
            absolute = root.join(path)
            next false unless absolute.file?

            note = ParsedNote.new(path, TaelgarNoteLint.read_text(absolute))
            Batch.valid_completion_pair?(note)
          end
        end
        skipped_already_linted = lintable_candidate_count - paths.length
        if paths.empty?
          manifest = {
            "schemaVersion" => SCHEMA_VERSION,
            "validatorVersion" => VERSION,
            "generatedAt" => Time.now.iso8601,
            "root" => root.to_s,
            "notes" => []
          }
        else
          manifest = Preparer.new(root: root).prepare(paths)
        end
        selected_count = manifest.fetch("notes").length
        review_count = manifest.fetch("notes").count { |record| record.dig("routing", "reviewRecommended") }
        if options[:only_needs_review]
          manifest["notes"].select! { |record| record.dig("routing", "reviewRecommended") }
        end
        manifest["selectionSummary"] = {
          "requested" => requested_count,
          "skippedNoReviewableProse" => skipped_no_reviewable_prose.length,
          "skippedNoReviewableProsePaths" => skipped_no_reviewable_prose,
          "skippedAlreadyLinted" => skipped_already_linted,
          "selected" => selected_count,
          "reviewRecommended" => review_count,
          "noOpEligible" => selected_count - review_count,
          "included" => manifest.fetch("notes").length
        }
        write_json(manifest, options[:output])
        0
      end

      def snapshot
        options = { root: Pathname.pwd }
        parser = OptionParser.new do |opts|
          opts.banner = "Usage: lint_taelgar_notes.rb snapshot --manifest FILE [options]"
          opts.on("--root PATH", "Vault root") { |value| options[:root] = Pathname.new(value) }
          opts.on("--manifest PATH", "Prepared batch manifest") { |value| options[:manifest] = value }
          opts.on("--output PATH", "Write decision template to a file") { |value| options[:output] = value }
        end
        parser.parse!(@argv)
        raise BatchError, "--manifest is required." unless options[:manifest]

        manifest_text = File.binread(options[:manifest]).force_encoding(Encoding::UTF_8).scrub
        manifest = JSON.parse(manifest_text)
        document = Snapshotter.new(
          root: options[:root],
          manifest: manifest,
          manifest_sha256: Batch.sha256(manifest_text)
        ).snapshot
        write_json(document, options[:output])
        0
      end

      def workspace
        options = {
          root: Pathname.pwd,
          max_notes: DEFAULT_MAX_NOTES,
          max_tokens: DEFAULT_MAX_TOKENS
        }
        parser = OptionParser.new do |opts|
          opts.banner = "Usage: lint_taelgar_notes.rb workspace --manifest FILE --review-dir DIR [options]"
          opts.on("--root PATH", "Vault root") { |value| options[:root] = Pathname.new(value) }
          opts.on("--manifest PATH", "Prepared batch manifest") { |value| options[:manifest] = value }
          opts.on("--review-dir PATH", "Temporary staged review workspace") { |value| options[:review_dir] = value }
          opts.on("--max-notes N", Integer, "Maximum notes per shard (default #{DEFAULT_MAX_NOTES})") { |value| options[:max_notes] = value }
          opts.on("--max-tokens N", Integer, "Maximum estimated input tokens per shard (default #{DEFAULT_MAX_TOKENS})") { |value| options[:max_tokens] = value }
          opts.on("--output PATH", "Write workspace summary JSON to a file") { |value| options[:output] = value }
        end
        parser.parse!(@argv)
        raise BatchError, "--manifest and --review-dir are required." unless options[:manifest] && options[:review_dir]

        manifest_text = File.binread(options[:manifest]).force_encoding(Encoding::UTF_8).scrub
        manifest = JSON.parse(manifest_text)
        document = WorkspaceBuilder.new(
          root: options[:root],
          manifest: manifest,
          manifest_sha256: Batch.sha256(manifest_text),
          output_dir: options[:review_dir],
          max_notes: options[:max_notes],
          max_tokens: options[:max_tokens]
        ).build
        write_json(document, options[:output])
        0
      end

      def finalize
        options = { root: Pathname.pwd, write: false }
        parser = OptionParser.new do |opts|
          opts.banner = "Usage: lint_taelgar_notes.rb finalize --manifest FILE --decisions FILE [options]"
          opts.on("--root PATH", "Vault root") { |value| options[:root] = Pathname.new(value) }
          opts.on("--manifest PATH", "Prepared batch manifest") { |value| options[:manifest] = value }
          opts.on("--decisions PATH", "Completed batch decisions") { |value| options[:decisions] = value }
          opts.on("--review-dir PATH", "Completed staged review workspace") { |value| options[:review_dir] = value }
          opts.on("--at TIME", "Completion timestamp; defaults to now") { |value| options[:at] = value }
          opts.on("--write", "Commit the prevalidated lint states") { options[:write] = true }
          opts.on("--output PATH", "Write result JSON to a file") { |value| options[:output] = value }
        end
        parser.parse!(@argv)
        raise BatchError, "--manifest is required." unless options[:manifest]
        if options[:decisions] && options[:review_dir] || !options[:decisions] && !options[:review_dir]
          raise BatchError, "Provide exactly one of --decisions or --review-dir."
        end

        manifest_text = File.binread(options[:manifest]).force_encoding(Encoding::UTF_8).scrub
        manifest = JSON.parse(manifest_text)
        manifest_sha = Batch.sha256(manifest_text)
        decisions = if options[:review_dir]
                      WorkspaceLoader.new(
                        root: options[:root],
                        manifest: manifest,
                        manifest_sha256: manifest_sha,
                        review_dir: options[:review_dir]
                      ).decisions
                    else
                      JSON.parse(File.binread(options[:decisions]).force_encoding(Encoding::UTF_8).scrub)
                    end
        result = Finalizer.new(
          root: options[:root],
          manifest: manifest,
          manifest_sha256: manifest_sha,
          decisions: decisions,
          completed_at: options[:at]
        ).finalize(write: options[:write])
        write_json(result, options[:output])
        0
      end

      def discover_paths(root, options)
        return [] unless options[:all_linted] || options[:stale]

        Dir.glob(root.join("**", "*.md").to_s, File::FNM_DOTMATCH).sort.each_with_object([]) do |absolute, paths|
          relative = TaelgarNoteLint.relative_path(root, absolute)
          next if File.basename(relative) == "AGENTS.md"
          next unless Batch.lintable_path?(relative)

          note = ParsedNote.new(relative, TaelgarNoteLint.read_text(absolute))
          has_lint_state = note.data.key?("lintedAt") || note.data.key?("lintVersion")
          next unless has_lint_state
          next if options[:stale] && Batch.canonical_state_value(note.data["lintVersion"]) == VERSION

          paths << relative
        end
      end

      def write_json(document, path)
        rendered = "#{JSON.pretty_generate(document)}\n"
        if path
          File.write(path, rendered)
          File.chmod(0o600, path)
        else
          puts(rendered)
        end
      end

      def usage
        <<~TEXT
          Usage: lint_taelgar_notes.rb COMMAND [options]
            prepare   Build shared deterministic and freshness evidence packets
            workspace Create bounded shards and staged candidate copies
            snapshot  Compatibility mode for a legacy live-note review
            finalize  Preflight and optionally write all lint completion states
        TEXT
      end
    end
  end
end

exit TaelgarNoteLint::Batch::CLI.new(ARGV).run if $PROGRAM_NAME == __FILE__
