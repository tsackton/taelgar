#!/usr/bin/env ruby
# frozen_string_literal: true

# Batch preparation and guarded finalization for contextual Taelgar note linting.
#
# This script does not replace agentic review. It prepares per-note evidence
# packets using shared vault, DM-note, and Git indexes, snapshots reviewed files,
# and writes lint completion state only after every selected result passes a
# checksum, prior-state, and deterministic-validation preflight.

require "digest"
require "json"
require "open3"
require "optparse"
require "pathname"
require "tempfile"
require "time"

require_relative "validate_taelgar_note"

module TaelgarNoteLint
  module Batch
    SCHEMA_VERSION = 1
    DECISION_SCHEMA_VERSION = 1

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

        notes = relative_paths.map do |path|
          absolute = @root.join(path)
          raise BatchError, "Note does not exist: #{path}" unless absolute.file?

          ParsedNote.new(path, TaelgarNoteLint.read_text(absolute))
        end
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
        dm_freshness = dm_freshness_for(note, report)
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

      def dm_freshness_for(note, report)
        linted_at = Batch.canonical_state_value(note.data["lintedAt"])
        return { "basis" => "filesystem_mtime", "candidates" => [] } if linted_at.to_s.empty?

        lint_time = Time.iso8601(linted_at)
        sources = report.fetch("findings").each_with_object({}) do |finding, by_path|
          Array(finding.dig("details", "sources")).each do |source|
            path = source["path"].to_s
            next unless path.start_with?("_DM_/")

            by_path[path] ||= []
            by_path[path] << finding.fetch("ruleId")
          end
        end
        candidates = sources.each_with_object([]) do |(path, rule_ids), selected|
          absolute = @root.join(path)
          next unless absolute.file? && File.mtime(absolute) > lint_time

          selected << {
            "path" => path,
            "modifiedAt" => File.mtime(absolute).iso8601(6),
            "ruleIds" => rule_ids.uniq
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
          unless Batch.completion_state(note) == record.fetch("priorCompletionState")
            raise BatchError, "Lint completion state changed after preparation: #{path}"
          end

          {
            "path" => path,
            "expectedSha256" => Batch.file_sha256(@root.join(path)),
            "outcome" => "review_required",
            "lintReport" => nil
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
        return if @manifest["validatorVersion"].to_s == VERSION

        raise BatchError, "Manifest validator version #{@manifest['validatorVersion'].inspect} does not match #{VERSION}."
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
        commit(candidates) if write
        {
          "schemaVersion" => DECISION_SCHEMA_VERSION,
          "validatorVersion" => VERSION,
          "completedAt" => @completed_at,
          "wrote" => write,
          "notes" => candidates.map do |candidate|
            {
              "path" => candidate.fetch("path"),
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
        return if @decisions["manifestSha256"] == @manifest_sha256

        raise BatchError, "Decision file was created from a different manifest."
      end

      def ensure_complete_decisions!(records, decisions)
        paths = decisions.map { |decision| decision["path"] }
        raise BatchError, "Decision file contains duplicate note paths." unless paths.uniq.length == paths.length
        unless paths.sort == records.keys.sort
          raise BatchError, "Decision file must contain exactly one result for every manifest note."
        end
        unresolved = decisions.select { |decision| !%w[clean open].include?(decision["outcome"]) }
        return if unresolved.empty?

        raise BatchError, "Every note needs a clean or open outcome before finalization: #{unresolved.map { |item| item['path'] }.join(', ')}"
      end

      def build_candidate(decision, record, validator)
        path = decision.fetch("path")
        absolute = @root.join(path)
        current_text = TaelgarNoteLint.read_text(absolute)
        unless Batch.file_sha256(absolute) == decision.fetch("expectedSha256")
          raise BatchError, "Reviewed file changed after snapshot: #{path}"
        end
        current_note = ParsedNote.new(path, current_text)
        unless Batch.completion_state(current_note) == record.fetch("priorCompletionState")
          raise BatchError, "Lint completion state changed before finalization: #{path}"
        end

        outcome = decision.fetch("outcome")
        report = validate_report(decision["lintReport"], outcome, path)
        text_without_lint = current_text.gsub(LINT_BLOCK_PATTERN, "")
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
          "outcome" => outcome,
          "expectedSha256" => decision.fetch("expectedSha256"),
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
          "target" => target,
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
        options = { root: Pathname.pwd, all_linted: false, stale: false, only_needs_review: false }
        parser = OptionParser.new do |opts|
          opts.banner = "Usage: lint_taelgar_notes.rb prepare [options] [NOTE ...]"
          opts.on("--root PATH", "Vault root") { |value| options[:root] = Pathname.new(value) }
          opts.on("--all-linted", "Select every note with lint completion state") { options[:all_linted] = true }
          opts.on("--stale", "Select notes whose lintVersion is not current") { options[:stale] = true }
          opts.on("--only-needs-review", "Exclude current notes with no freshness candidates") { options[:only_needs_review] = true }
          opts.on("--output PATH", "Write JSON to a file instead of stdout") { |value| options[:output] = value }
        end
        parser.parse!(@argv)
        root = options[:root].expand_path
        paths = discover_paths(root, options)
        paths.concat(@argv)
        if paths.empty? && (options[:all_linted] || options[:stale])
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

      def finalize
        options = { root: Pathname.pwd, write: false }
        parser = OptionParser.new do |opts|
          opts.banner = "Usage: lint_taelgar_notes.rb finalize --manifest FILE --decisions FILE [options]"
          opts.on("--root PATH", "Vault root") { |value| options[:root] = Pathname.new(value) }
          opts.on("--manifest PATH", "Prepared batch manifest") { |value| options[:manifest] = value }
          opts.on("--decisions PATH", "Completed batch decisions") { |value| options[:decisions] = value }
          opts.on("--at TIME", "Completion timestamp; defaults to now") { |value| options[:at] = value }
          opts.on("--write", "Commit the prevalidated lint states") { options[:write] = true }
          opts.on("--output PATH", "Write result JSON to a file") { |value| options[:output] = value }
        end
        parser.parse!(@argv)
        raise BatchError, "--manifest and --decisions are required." unless options[:manifest] && options[:decisions]

        manifest_text = File.binread(options[:manifest]).force_encoding(Encoding::UTF_8).scrub
        manifest = JSON.parse(manifest_text)
        decisions = JSON.parse(File.binread(options[:decisions]).force_encoding(Encoding::UTF_8).scrub)
        result = Finalizer.new(
          root: options[:root],
          manifest: manifest,
          manifest_sha256: Batch.sha256(manifest_text),
          decisions: decisions,
          completed_at: options[:at]
        ).finalize(write: options[:write])
        write_json(result, options[:output])
        0
      end

      def discover_paths(root, options)
        return [] unless options[:all_linted] || options[:stale]

        Dir.glob(root.join("**", "*.md").to_s).sort.each_with_object([]) do |absolute, paths|
          relative = TaelgarNoteLint.relative_path(root, absolute)
          parts = Pathname.new(relative).each_filename.to_a
          next if parts.any? { |part| part.start_with?(".") }
          next if File.basename(relative) == "AGENTS.md"

          note = ParsedNote.new(relative, TaelgarNoteLint.read_text(absolute))
          has_lint_state = note.data.key?("lintedAt") || note.data.key?("lintVersion")
          next unless has_lint_state
          next if options[:stale] && Batch.canonical_state_value(note.data["lintVersion"]) == VERSION

          paths << relative
        end
      end

      def write_json(document, path)
        rendered = "#{JSON.pretty_generate(document)}\n"
        path ? File.write(path, rendered) : puts(rendered)
      end

      def usage
        <<~TEXT
          Usage: lint_taelgar_notes.rb COMMAND [options]
            prepare   Build shared deterministic and freshness evidence packets
            snapshot  Capture reviewed file checksums and create a decision template
            finalize  Preflight and optionally write all lint completion states
        TEXT
      end
    end
  end
end

exit TaelgarNoteLint::Batch::CLI.new(ARGV).run if $PROGRAM_NAME == __FILE__
