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
    SCHEMA_VERSION = 4
    DECISION_SCHEMA_VERSION = 6
    WORKSPACE_SCHEMA_VERSION = 2
    DEFAULT_MAX_TOKENS = 40_000
    ESTIMATED_CHARACTERS_PER_TOKEN = 3
    DM_DOSSIER_SCHEMA_VERSION = 1
    LANGUAGE_GUIDANCE_SCHEMA_VERSION = 2
    LANGUAGE_GUIDANCE_PATH = "_scripts/language_pronunciation_analogues.json"
    SELF_REVIEW_KEYS = %w[evidenceAndVerdict privacySanity candidateValidation].freeze
    EDITORIAL_VERDICTS = [
      "Sufficient",
      "Sufficient, worth expanding",
      "Underdeveloped"
    ].freeze
    COMPLETION_FIELDS = %w[lintedAt lintVersion].freeze
    PRIVACY_VISIBILITY_FIELDS = %w[knownTo excludePublish audience dm_owner dm_notes].freeze
    REVIEW_CATEGORIES = %w[
      completion_lifecycle
      frontmatter_formatting
      metadata
      persistent_metadata
      body_prose
      private_or_visibility_sensitive
      non_lint_status
      custom_syntax
    ].freeze
    TARGETED_REVIEW_CATEGORIES = %w[
      metadata
      persistent_metadata
      body_prose
      private_or_visibility_sensitive
      non_lint_status
      custom_syntax
    ].freeze
    BODY_EDIT_BASES = %w[objective_typo objective_punctuation objective_duplication objective_grammar source_correction].freeze
    SHARED_NONPUBLIC_DISPOSITIONS = %w[
      redundant_with_public
      public_adoption_candidate
      dm_only
      speculative_or_unresolved
      source_pointer
      no_useful_material
    ].freeze
    DM_SOURCE_DISPOSITIONS = %w[matching not_matching].freeze
    DM_RECOVERY_DISPOSITIONS = %w[
      not_applicable
      no_recoverable_material
      public_candidate
      private_candidate
    ].freeze
    SECRET_RECOVERY_DISPOSITIONS = %w[
      no_recoverable_material
      public_candidate
      private_candidate
      speculative_or_unresolved
    ].freeze
    OPEN_SHARED_NONPUBLIC_RULES = {
      "redundant_with_public" => "editorial.shared_material_redundant",
      "public_adoption_candidate" => "editorial.public_material_candidate"
    }.freeze
    EXPANSION_CERTAINTIES = %w[established reported assumed provisional uninvented].freeze

    class BatchError < StandardError; end

    module_function

    def sha256(text)
      Digest::SHA256.hexdigest(text)
    end

    def file_sha256(path)
      Digest::SHA256.file(path.to_s).hexdigest
    end

    def canonical_review_value(value)
      case value
      when Hash
        value.keys.map(&:to_s).sort.to_h do |key|
          source_key = value.key?(key) ? key : value.keys.find { |candidate| candidate.to_s == key }
          [key, canonical_review_value(value[source_key])]
        end
      when Array
        value.map { |item| canonical_review_value(item) }
      when Date, Time
        value.iso8601
      else
        value
      end
    end

    def review_frontmatter(note)
      data = note.data.each_with_object({}) do |(key, value), memo|
        next if COMPLETION_FIELDS.include?(key.to_s)

        memo[key.to_s] = value
      end
      data["tags"] = Array(data["tags"]).reject { |tag| tag.to_s == "status/check/lint" }
      canonical_review_value(data)
    end

    def non_lint_statuses(note)
      note.tags.grep(/\Astatus\//).reject { |tag| tag == "status/check/lint" }.sort
    end

    def body_without_lint(note)
      note.body.gsub(LINT_BLOCK_PATTERN, "").sub(/\n*\z/, "\n")
    end

    def body_without_persistent_lint_metadata(note)
      body = body_without_lint(note)
      [METADATA_BLOCK_PATTERN, POV_NOTES_BLOCK_PATTERN, LEGACY_ARTICLE_BLOCK_PATTERN].each do |pattern|
        body = body.gsub(pattern, "")
      end
      body.sub(/\n*\z/, "\n")
    end

    def persistent_lint_metadata(note)
      [METADATA_BLOCK_PATTERN, POV_NOTES_BLOCK_PATTERN, LEGACY_ARTICLE_BLOCK_PATTERN].flat_map do |pattern|
        note.body.to_enum(:scan, pattern).map { Regexp.last_match[0] }
      end
    end

    def sensitive_content(note)
      body = body_without_lint(note)
      scoped = body.scan(SCOPED_CONTENT_BLOCK_PATTERN)
      comments = body.scan(/%%(.*?)%%/m).map(&:first).reject do |segment|
        segment.strip.match?(/\A\^(?:Lint|Metadata|povNotes|End)(?::|\z)/)
      end
      [scoped, comments]
    end

    def shared_nonpublic_units(note)
      body = body_without_lint(note)
      [METADATA_BLOCK_PATTERN, POV_NOTES_BLOCK_PATTERN, LEGACY_ARTICLE_BLOCK_PATTERN].each do |pattern|
        body = body.gsub(pattern, "")
      end
      units = []
      body.to_enum(:scan, SCOPED_CONTENT_BLOCK_PATTERN).each do
        match = Regexp.last_match[0]
        next unless match.match?(/\A%%\^Campaign:none%%/)

        units << shared_nonpublic_unit("Campaign:none", match)
      end
      without_scoped = body.gsub(SCOPED_CONTENT_BLOCK_PATTERN, "")
      without_scoped.to_enum(:scan, /%%(.*?)%%/m).each do
        match = Regexp.last_match
        payload = match[1].to_s
        stripped = payload.strip
        next if stripped.empty? || stripped.start_with?("SECRET") || stripped.start_with?("^")
        next unless stripped.match?(/[[:alnum:]]/)

        units << shared_nonpublic_unit("comment", match[0])
      end
      units
    end

    def shared_nonpublic_unit(kind, text)
      {
        "kind" => kind,
        "contentSha256" => sha256(text)
      }
    end

    def shared_nonpublic_review_template(note)
      shared_nonpublic_units(note).map do |unit|
        unit.merge("disposition" => "review_required", "summary" => nil)
      end
    end

    def secret_units(note)
      body = body_without_lint(note)
      [METADATA_BLOCK_PATTERN, POV_NOTES_BLOCK_PATTERN, LEGACY_ARTICLE_BLOCK_PATTERN].each do |pattern|
        body = body.gsub(pattern, "")
      end
      body.to_enum(:scan, /%%SECRET\b.*?%%/m).each_with_index.map do |_match, index|
        {
          "kind" => "SECRET",
          "ordinal" => index + 1,
          "contentSha256" => sha256(Regexp.last_match[0])
        }
      end
    end

    def secret_review_template(note)
      secret_units(note).map do |unit|
        unit.merge(
          "disposition" => "review_required",
          "summary" => nil,
          "candidate" => nil
        )
      end
    end

    def dm_notes_candidate_sources(record)
      Array(record.dig("dmEvidence", "sources")).map { |source| source["path"].to_s }.reject(&:empty?).uniq.sort
    end

    def dm_notes_review_template(record)
      required = record.dig("deterministic", "reviewGates", "dmNotes", "required") == true
      {
        "required" => required,
        "clusterReviews" => (required ? Array(record.dig("dmEvidence", "clusters")) : []).map do |cluster|
          {
            "clusterId" => cluster.fetch("id"),
            "disposition" => "review_required",
            "summary" => nil,
            "recovery" => "review_required",
            "chatSummary" => nil,
            "candidate" => nil
          }
        end
      }
    end

    def self_review_template
      {
        "complete" => false,
        "evidenceAndVerdict" => false,
        "privacySanity" => false,
        "candidateValidation" => false,
        "notes" => nil
      }
    end

    def dm_cluster_sources(record, cluster_id)
      cluster = Array(record.dig("dmEvidence", "clusters")).find { |item| item["id"] == cluster_id }
      cluster ? Array(cluster["sourcePaths"]).sort : []
    end

    def dm_note_wikilink(path)
      "[[#{path.sub(/\.md\z/, '')}]]"
    end

    def dm_note_wikilink_pattern(path)
      target = Regexp.escape(path.sub(/\.md\z/, ""))
      /\[\[#{target}(?:\.md)?(?:\|[^\]\r\n]+)?\]\]/
    end

    def contains_dm_note_wikilink?(text, path)
      text.to_s.match?(dm_note_wikilink_pattern(path))
    end

    def markdown_list_contains_wikilink?(text, path)
      link = dm_note_wikilink_pattern(path)
      text.to_s.lines.any? { |line| line.match?(/\A\s*-\s+#{link}(?:\s.*)?\z/) }
    end

    def recovery_destination_marker(disposition)
      disposition == "public_candidate" ? "Destination: public" : "Destination: private"
    end

    def name_block_data(note)
      match = note.body.match(/%%\^Metadata:names:v1%%\s*(.*?)\s*%%\^End%%/m)
      return [] unless match

      data = TaelgarNoteLint.yaml_load(match[1])
      data.is_a?(Array) ? data : []
    rescue Psych::Exception
      []
    end

    def populated_documented_value?(value)
      return false if value.nil?
      return !value.strip.empty? if value.is_a?(String)
      return !value.empty? if value.respond_to?(:empty?)

      true
    end

    def documented_name_identity(entry)
      [canonical_review_value(entry["name"]), canonical_review_value(entry["role"])]
    end

    def semantic_body_for_edit_declaration(note)
      body_without_persistent_lint_metadata(note)
        .gsub(/[ \t]+(?=\r?$)/, "")
        .sub(/\n*\z/, "\n")
    end

    def custom_syntax_lines(note)
      body_without_lint(note).lines.each_with_object([]) do |line, selected|
        stripped = line.strip
        next if stripped.match?(/\A%%\^(?:Lint|Metadata|povNotes|End)(?::|%%|\z)/)
        next unless stripped.match?(/(?:%%\^(?:Campaign|Date):|%%SECRET|!\[\[|>\s*\[!|\A```|\A~~~|\$=|\((?:DR|POV)::)/)

        selected << line
      end
    end

    def classify_change(before_text, after_text)
      before_note = ParsedNote.new("before.md", before_text)
      after_note = ParsedNote.new("after.md", after_text)
      categories = []
      categories << "completion_lifecycle" if completion_state(before_note) != completion_state(after_note)

      before_frontmatter = review_frontmatter(before_note)
      after_frontmatter = review_frontmatter(after_note)
      if before_frontmatter != after_frontmatter
        categories << "metadata"
      elsif before_note.frontmatter_lines != after_note.frontmatter_lines
        categories << "frontmatter_formatting"
      end

      categories << "persistent_metadata" if persistent_lint_metadata(before_note) != persistent_lint_metadata(after_note)
      if body_without_persistent_lint_metadata(before_note) != body_without_persistent_lint_metadata(after_note)
        categories << "body_prose"
      end
      privacy_fields_changed = PRIVACY_VISIBILITY_FIELDS.any? do |field|
        canonical_review_value(before_note.data[field]) != canonical_review_value(after_note.data[field])
      end
      if privacy_fields_changed || sensitive_content(before_note) != sensitive_content(after_note)
        categories << "private_or_visibility_sensitive"
      end
      categories << "non_lint_status" if non_lint_statuses(before_note) != non_lint_statuses(after_note)
      categories << "custom_syntax" if custom_syntax_lines(before_note) != custom_syntax_lines(after_note)
      categories = REVIEW_CATEGORIES.select { |category| categories.include?(category) }
      categories = ["completion_lifecycle"] if categories.empty? && before_text != after_text
      targeted = (categories & TARGETED_REVIEW_CATEGORIES).any?
      {
        "level" => targeted ? "targeted" : "mechanical",
        "categories" => categories
      }
    end

    def introduced_whitespace_errors(before_text, after_text)
      Tempfile.create(["taelgar-lint-before-", ".md"]) do |before_file|
        Tempfile.create(["taelgar-lint-after-", ".md"]) do |after_file|
          before_file.binmode
          after_file.binmode
          before_file.write(before_text)
          after_file.write(after_text)
          before_file.flush
          after_file.flush
          # Keep the no-index comparison outside the vault so its Markdown
          # attributes cannot invoke the repository's required secret filter.
          stdout, stderr, status = Open3.capture3(
            "git", "diff", "--no-index", "--check", "--no-ext-diff", "--",
            before_file.path, after_file.path,
            chdir: File.dirname(before_file.path)
          )
          unless [0, 1].include?(status.exitstatus) || (!stdout.empty? && stderr.empty?)
            raise BatchError, "Whitespace preflight failed: #{stderr.strip}"
          end

          stdout.lines.grep(/:(?:\d+): (?:trailing whitespace|space before tab|new blank line at EOF)/)
        end
      end
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
      serialized_tokens = ((bytes + packet_bytes).to_f / ESTIMATED_CHARACTERS_PER_TOKEN).ceil
      evidence_complexity = Array(record.dig("dmEvidence", "clusters")).length * 300 +
                            Array(record.dig("freshness", "candidates")).length * 150 +
                            Array(record.dig("deterministic", "findings")).length * 40
      serialized_tokens + evidence_complexity
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

    class DMEvidenceDossier
      CONTEXT_RADIUS = 2
      NEAR_DUPLICATE_THRESHOLD = 0.8

      def initialize(root)
        @root = Pathname.new(root).expand_path
      end

      def build(sources)
        source_records = Array(sources).sort_by { |source| source.fetch("path") }.map do |source|
          build_source(source)
        end
        contexts = source_records.flat_map { |source| source.fetch("contexts") }
        {
          "schemaVersion" => DM_DOSSIER_SCHEMA_VERSION,
          "generatedBy" => "mechanical",
          "sourceCount" => source_records.length,
          "matchCount" => source_records.sum { |source| source.fetch("matchedLines").length },
          "matchTypeCounts" => source_records.flat_map { |source| source.fetch("matchKinds") }
                                            .each_with_object(Hash.new(0)) { |kind, counts| counts[kind] += 1 }
                                            .sort.to_h,
          "sources" => source_records,
          "clusters" => cluster_contexts(contexts)
        }
      end

      private

      def build_source(source)
        path = source.fetch("path")
        lines = TaelgarNoteLint.read_text(@root.join(path)).lines
        matched_lines = Array(source["lines"]).map(&:to_i).select(&:positive?).uniq.sort
        ranges = matched_lines.map do |line|
          [[line - CONTEXT_RADIUS, 1].max, [line + CONTEXT_RADIUS, lines.length].min]
        end
        merged = ranges.each_with_object([]) do |range, combined|
          if combined.any? && range.first <= combined.last.last + 1
            combined.last[1] = [combined.last.last, range.last].max
          else
            combined << range.dup
          end
        end
        contexts = merged.map.with_index do |(start_line, end_line), index|
          text = lines[(start_line - 1)..(end_line - 1)].join
          {
            "id" => "#{Digest::SHA256.hexdigest("#{path}:#{start_line}:#{end_line}")[0, 12]}",
            "path" => path,
            "ordinal" => index + 1,
            "startLine" => start_line,
            "endLine" => end_line,
            "text" => text,
            "contentSha256" => Batch.sha256(text),
            "normalizedSha256" => Batch.sha256(normalize_context(text))
          }
        end
        {
          "path" => path,
          "sourceFamily" => Pathname.new(path).dirname.to_s,
          "modifiedAt" => source["modifiedAt"],
          "matchKinds" => Array(source["matchKinds"]).uniq.sort,
          "matchedLines" => matched_lines,
          "contexts" => contexts
        }
      end

      def cluster_contexts(contexts)
        groups = []
        contexts.sort_by { |context| [context.fetch("path"), context.fetch("startLine")] }.each do |context|
          normalized = normalize_context(context.fetch("text"))
          tokens = normalized.scan(/[[:alnum:]]+/).uniq
          group = groups.find do |candidate|
            candidate[:normalized] == normalized || jaccard(candidate[:tokens], tokens) >= NEAR_DUPLICATE_THRESHOLD
          end
          if group
            group[:contexts] << context
          else
            groups << { normalized: normalized, tokens: tokens, contexts: [context] }
          end
        end
        groups.each_with_index.map do |group, index|
          normalized_values = group.fetch(:contexts).map { |context| normalize_context(context.fetch("text")) }.uniq
          {
            "id" => format("dm-cluster-%03d", index + 1),
            "duplicateKind" => if group.fetch(:contexts).length == 1
                                 "single"
                               elsif normalized_values.length == 1
                                 "exact"
                               else
                                 "near"
                               end,
            "sourcePaths" => group.fetch(:contexts).map { |context| context.fetch("path") }.uniq.sort,
            "contextCount" => group.fetch(:contexts).length,
            "contexts" => group.fetch(:contexts).map do |context|
              %w[id path ordinal startLine endLine contentSha256].to_h { |key| [key, context.fetch(key)] }
            end
          }
        end
      end

      def normalize_context(text)
        text.to_s
            .gsub(/\[\[([^\]|]+)(?:\|[^\]]+)?\]\]/, '\\1')
            .gsub(/[^[:alnum:]'\s]/, " ")
            .downcase
            .gsub(/\s+/, " ")
            .strip
      end

      def jaccard(left, right)
        union = left | right
        return 0.0 if union.empty?

        (left & right).length.to_f / union.length
      end
    end

    class LanguageGuidance
      attr_reader :reference

      def initialize(root)
        @root = Pathname.new(root).expand_path
        path = @root.join(LANGUAGE_GUIDANCE_PATH)
        raise BatchError, "Generated language guidance is missing: #{LANGUAGE_GUIDANCE_PATH}" unless path.file?

        @data = JSON.parse(TaelgarNoteLint.read_text(path))
        unless @data["schemaVersion"] == LANGUAGE_GUIDANCE_SCHEMA_VERSION &&
               @data["families"].is_a?(Array) && @data["languages"].is_a?(Array)
          raise BatchError, "Generated language guidance uses an unsupported schema."
        end
        source = @root.join(@data.fetch("sourcePath"))
        raise BatchError, "Language guidance source is missing: #{@data.fetch('sourcePath')}" unless source.file?
        if source.mtime > path.mtime
          raise BatchError, "Generated language guidance is stale; regenerate it because #{@data.fetch('sourcePath')} is newer."
        end
        @reference = {
          "path" => LANGUAGE_GUIDANCE_PATH,
          "schemaVersion" => LANGUAGE_GUIDANCE_SCHEMA_VERSION,
          "sha256" => Batch.file_sha256(path),
          "sourcePath" => @data.fetch("sourcePath"),
          "sourceSha256" => @data.fetch("sourceSha256")
        }
      rescue JSON::ParserError => error
        raise BatchError, "Generated language guidance is invalid JSON: #{error.message}"
      end

      def for(note)
        values = [note.path, note.data["name"], *Array(note.data["aliases"]), note.data["ancestry"], note.data["species"]]
        Batch.name_block_data(note).each do |entry|
          values << entry["language"] if entry.is_a?(Hash)
        end
        haystack = values.compact.join("\n")
        entries = (@data.fetch("languages") + @data.fetch("families")).each_with_object([]) do |entry, selected|
          matches = entry.fetch("lookupTerms").select { |term| haystack.match?(/(?<![[:alnum:]_])#{Regexp.escape(term)}(?![[:alnum:]_])/i) }
          next if matches.empty?

          selected << entry.merge("matchedLookupTerms" => matches)
        end
        {
          "sidecar" => @reference,
          "entries" => entries
        }
      end
    end

    class Preparer
      def initialize(root:, force_dm_notes_review: false)
        @root = Pathname.new(root).expand_path
        @force_dm_notes_review = force_dm_notes_review
        @index = NoteIndex.new(@root)
        @validator = Validator.new(
          root: @root,
          check_links: true,
          index: @index,
          force_dm_notes_review: force_dm_notes_review
        )
        @baselines = GitBaselineResolver.new(@root)
        @freshness_scanners = {}
        @dm_dossiers = DMEvidenceDossier.new(@root)
        @language_guidance = LanguageGuidance.new(@root)
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
          "forcedReviewGates" => @force_dm_notes_review ? ["dmNotes"] : [],
          "generatedAt" => Time.now.iso8601,
          "root" => @root.to_s,
          "languageGuidance" => @language_guidance.reference,
          "notes" => records
        }
      end

      private

      def prepare_note(note)
        absolute = @root.join(note.path)
        report = @validator.validate_path(note.path)
        freshness = freshness_for(note, report)
        dm_sources = @validator.dm_sources(note)
        dm_evidence = @dm_dossiers.build(dm_sources)
        language_guidance = @language_guidance.for(note)
        dm_freshness = dm_freshness_for(note, dm_sources)
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
          "dmFreshness" => dm_freshness,
          "dmEvidence" => dm_evidence,
          "languageGuidance" => language_guidance,
          "evidenceSummary" => {
            "freshnessCandidates" => Array(freshness["candidates"]).length,
            "dmSources" => dm_sources.length,
            "dmClusters" => dm_evidence.fetch("clusters").length,
            "languageEntries" => language_guidance.fetch("entries").length
          }
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
            "bodyEdits" => [],
            "dmNotesReview" => Batch.dm_notes_review_template(record),
            "secretReview" => Batch.secret_review_template(note),
            "sharedNonpublicReview" => Batch.shared_nonpublic_review_template(note),
            "editorialAssessment" => nil,
            "expansionCandidate" => nil,
            "selfReview" => Batch.self_review_template
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
      def initialize(root:, manifest:, manifest_sha256:, output_dir:, max_tokens: DEFAULT_MAX_TOKENS)
        @root = Pathname.new(root).expand_path
        @manifest = manifest
        @manifest_sha256 = manifest_sha256
        @output_dir = Batch.ensure_external_review_dir!(@root, output_dir)
        @max_tokens = Integer(max_tokens)
        raise BatchError, "Shard token limit must be positive." unless @max_tokens.positive?
      rescue ArgumentError, TypeError
        raise BatchError, "Shard token limit must be a positive integer."
      end

      def build
        records = validate_manifest!
        prepare_output_dir!
        shards = build_shards(records)
        shard_records = shards.each_with_index.map { |shard, index| write_shard(shard, index + 1) }
        workspace = {
          "schemaVersion" => WORKSPACE_SCHEMA_VERSION,
          "decisionSchemaVersion" => DECISION_SCHEMA_VERSION,
          "validatorVersion" => VERSION,
          "manifestSha256" => @manifest_sha256,
          "createdAt" => Time.now.iso8601,
          "maxEstimatedInputTokens" => @max_tokens,
          "shardingStrategy" => "largest-estimate-first balanced bins with soft path locality",
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
        weighted = records.map { |record| [record, Batch.estimated_input_tokens(record)] }
        oversize, ordinary = weighted.partition { |_record, estimate| estimate > @max_tokens }
        desired_bins = [(ordinary.sum { |_record, estimate| estimate }.to_f / @max_tokens).ceil, 1].max
        bins = Array.new(ordinary.empty? ? 0 : desired_bins) { [] }
        ordinary.sort_by { |record, estimate| [-estimate, record.fetch("path")] }.each do |item|
          record, estimate = item
          candidates = bins.each_index.select do |index|
            bins[index].sum { |_existing, tokens| tokens } + estimate <= @max_tokens
          end
          if candidates.empty?
            bins << [item]
            next
          end
          parent = Pathname.new(record.fetch("path")).dirname.to_s
          selected = candidates.min_by do |index|
            tokens = bins[index].sum { |_existing, value| value }
            same_parent = bins[index].count { |existing, _value| Pathname.new(existing.fetch("path")).dirname.to_s == parent }
            [tokens, -same_parent, index]
          end
          bins[selected] << item
        end
        (bins.reject(&:empty?) + oversize.map { |item| [item] })
          .map { |shard| shard.sort_by { |record, _estimate| record.fetch("path") } }
          .sort_by { |shard| shard.first.first.fetch("path") }
      end

      def write_shard(shard, number)
        shard_id = format("shard-%03d", number)
        packet_path = "packets/#{shard_id}.json"
        result_path = "results/#{shard_id}.json"
        estimated_tokens = shard.sum { |_record, estimate| estimate }
        shard.each { |record, _estimate| copy_candidate(record, shard_id) }
        packet_notes = shard.map do |record, estimate|
          record.merge(
            "candidateRelativePath" => "candidates/#{shard_id}/#{record.fetch('path')}",
            "estimatedInputTokens" => estimate
          )
        end
        result_notes = shard.map do |record, _estimate|
          path = record.fetch("path")
          note = ParsedNote.new(path, TaelgarNoteLint.read_text(@root.join(path)))
          {
            "path" => path,
            "candidateSha256" => record.dig("file", "sha256"),
            "eligibility" => "review_required",
            "eligibilityReason" => nil,
            "editorialVerdict" => nil,
            "outcome" => "review_required",
            "lintReport" => nil,
            "handoff" => nil,
            "bodyEdits" => [],
            "dmNotesReview" => Batch.dm_notes_review_template(record),
            "secretReview" => Batch.secret_review_template(note),
            "sharedNonpublicReview" => Batch.shared_nonpublic_review_template(note),
            "editorialAssessment" => nil,
            "expansionCandidate" => nil,
            "selfReview" => Batch.self_review_template
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

      def copy_candidate(record, shard_id)
        path = record.fetch("path")
        destination = @output_dir.join("candidates", shard_id, path)
        FileUtils.mkdir_p(destination.dirname)
        destination.dirname.ascend do |directory|
          break if directory == @output_dir

          File.chmod(0o700, directory)
        end
        File.binwrite(destination, File.binread(@root.join(path)))
        File.chmod(0o600, destination)
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
          candidate = safe_candidate_path(shard.fetch("id"), path)
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

      def safe_candidate_path(shard_id, note_path)
        base = @review_dir.join("candidates", shard_id).expand_path
        path = base.join(note_path).expand_path
        unless path.to_s.start_with?("#{base}#{File::SEPARATOR}")
          raise BatchError, "Review workspace contains an unsafe candidate path: #{note_path}"
        end

        path
      end
    end

    class HandoffRenderer
      def initialize(decisions:, records:, candidates:)
        @decisions = decisions
        @records = records
        @candidates = candidates.to_h { |candidate| [candidate.fetch("path"), candidate] }
      end

      def render
        eligible = @decisions.select { |decision| decision["eligibility"] == "eligible" }
        open = eligible.select { |decision| decision["outcome"] == "open" }
        lines = [
          "## Taelgar lint review handoff",
          "",
          "Reviewed #{eligible.length} eligible notes: #{open.length} open and #{eligible.length - open.length} clean."
        ]
        render_note_outcomes(lines)
        render_expansions(lines, eligible)
        render_dm_recoveries(lines, eligible)
        render_secret_recoveries(lines, eligible)
        render_worker_notes(lines, eligible)
        lines.join("\n").sub(/\n*\z/, "\n")
      end

      private

      def render_note_outcomes(lines)
        return if @decisions.empty?

        lines.concat(["", "### Note outcomes", ""])
        @decisions.sort_by { |decision| decision.fetch("path") }.each do |decision|
          if decision["eligibility"] == "ineligible"
            lines << "- #{wikilink(decision.fetch('path'))} — ineligible: #{decision.fetch('eligibilityReason')}"
            next
          end

          rules = decision["lintReport"].to_s.scan(/\*\*(?:Error|Warning|Suggestion)\s+—\s+([a-z0-9_.-]+):/i).flatten.uniq
          suffix = rules.empty? ? "" : " — #{rules.join(', ')}"
          lines << "- #{wikilink(decision.fetch('path'))} — #{decision.fetch('outcome')}; #{decision.fetch('editorialVerdict')}#{suffix}"
        end
      end

      def render_expansions(lines, decisions)
        expansions = decisions.select { |decision| decision["expansionCandidate"].is_a?(Hash) }
        return if expansions.empty?

        lines.concat(["", "### Bounded expansion candidates"])
        expansions.sort_by { |decision| decision.fetch("path") }.each do |decision|
          expansion = decision.fetch("expansionCandidate")
          lines.concat([
            "",
            "#### #{wikilink(decision.fetch('path'))}",
            "",
            "Benefit: #{expansion.fetch('benefit')}",
            "",
            "Copy-paste-ready statement:",
            "",
            blockquote(expansion.fetch("addition")),
            "",
            "Sources:"
          ])
          expansion.fetch("sources").each do |source|
            lines << "- #{wikilink(source.fetch('path'))} — #{source.fetch('certainty')}: #{source.fetch('evidence')}"
          end
        end
      end

      def render_dm_recoveries(lines, decisions)
        sections = []
        decisions.sort_by { |decision| decision.fetch("path") }.each do |decision|
          record = @records.fetch(decision.fetch("path"))
          reviews = Array(decision.dig("dmNotesReview", "clusterReviews"))
          dm_notes = ParsedNote.new(decision.fetch("path"), @candidates.fetch(decision.fetch("path")).fetch("text")).data["dm_notes"].to_s
          reviews.each do |review|
            next unless review["disposition"] == "matching"

            sources = Batch.dm_cluster_sources(record, review.fetch("clusterId"))
            if %w[public_candidate private_candidate].include?(review["recovery"])
              sections << [decision, review, sources, :recovery]
            elsif %w[color important].include?(dm_notes) && decision["outcome"] == "clean"
              sections << [decision, review, sources, :attestation]
            end
          end
        end
        return if sections.empty?

        lines.concat(["", "### DM evidence and recoveries"])
        sections.each do |decision, review, sources, kind|
          lines.concat(["", "#### #{wikilink(decision.fetch('path'))}", ""])
          if kind == :recovery
            lines << Batch.recovery_destination_marker(review.fetch("recovery"))
            lines.concat(["", review.fetch("chatSummary"), "", "Copy-paste-ready statement:", "", blockquote(review.fetch("candidate"))])
          else
            lines << "Confirmed local-only evidence supports the positive `dm_notes` attestation."
          end
          if decision["outcome"] == "open"
            lines.concat(["", "Sources: recorded in the note's Lint block."])
          else
            lines.concat(["", "Sources:"])
            sources.each { |source| lines << "- #{wikilink(source)}" }
          end
        end
      end

      def render_secret_recoveries(lines, decisions)
        recoveries = decisions.flat_map do |decision|
          Array(decision["secretReview"]).each_with_object([]) do |review, selected|
            next unless %w[public_candidate private_candidate].include?(review["disposition"])

            selected << [decision, review]
          end
        end
        return if recoveries.empty?

        lines.concat(["", "### SECRET recoveries"])
        recoveries.each do |decision, review|
          lines.concat([
            "",
            "#### #{wikilink(decision.fetch('path'))}",
            "",
            Batch.recovery_destination_marker(review.fetch("disposition")),
            "",
            review.fetch("summary"),
            "",
            "Copy-paste-ready statement:",
            "",
            blockquote(review.fetch("candidate"))
          ])
        end
      end

      def render_worker_notes(lines, decisions)
        notes = decisions.reject { |decision| decision["handoff"].to_s.strip.empty? }
        return if notes.empty?

        lines.concat(["", "### Additional worker notes"])
        notes.sort_by { |decision| decision.fetch("path") }.each do |decision|
          lines.concat(["", "#### #{wikilink(decision.fetch('path'))}", "", decision.fetch("handoff").to_s.strip])
        end
      end

      def wikilink(path)
        "[[#{path.to_s.sub(/\.md\z/, '')}]]"
      end

      def blockquote(text)
        text.to_s.lines.map { |line| "> #{line.chomp}" }.join("\n")
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
        review_summary = review_summary(candidates)
        handoff = HandoffRenderer.new(decisions: decision_list, records: records, candidates: candidates).render
        commit(candidates.reject { |candidate| candidate["skipWrite"] }) if write
        {
          "schemaVersion" => DECISION_SCHEMA_VERSION,
          "validatorVersion" => VERSION,
          "completedAt" => @completed_at,
          "wrote" => write,
          "reviewSummary" => review_summary,
          "handoff" => handoff,
          "notes" => candidates.map do |candidate|
            {
              "path" => candidate.fetch("path"),
              "eligibility" => candidate.fetch("eligibility"),
              "editorialVerdict" => candidate["editorialVerdict"],
              "outcome" => candidate.fetch("outcome"),
              "sha256" => Batch.sha256(candidate.fetch("text")),
              "review" => candidate.fetch("review")
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
            "review" => { "level" => "mechanical", "categories" => [] },
            "skipWrite" => true
          }
        end

        staged_note = ParsedNote.new(path, staged_text)
        Batch.ensure_objectively_lintable_note!(staged_note)
        unless Batch.completion_state(staged_note) == record.fetch("priorCompletionState")
          raise BatchError, "Staged lint completion state changed before finalization: #{path}"
        end
        outcome = decision.fetch("outcome")
        report_value = add_dm_evidence_links(decision["lintReport"], decision, record, staged_note, outcome)
        report = validate_report(report_value, outcome, path)
        validate_editorial_consistency!(decision, report)
        validate_declared_body_edits!(decision, live_note, staged_note, path)
        validate_dm_notes_review!(decision, record, staged_note, report, outcome, path)
        validate_secret_review!(decision, staged_note, report, path)
        validate_shared_nonpublic_review!(decision, staged_note, report, outcome, path)
        validate_documented_names_preserved!(live_note, staged_note, path)
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
        whitespace_errors = Batch.introduced_whitespace_errors(live_text, formatted)
        unless whitespace_errors.empty?
          details = whitespace_errors.first(5).map(&:strip).join("; ")
          raise BatchError, "Final candidate introduces whitespace errors in #{path}: #{details}"
        end

        {
          "path" => path,
          "eligibility" => "eligible",
          "editorialVerdict" => decision.fetch("editorialVerdict"),
          "outcome" => outcome,
          "expectedSha256" => expected_sha,
          "text" => formatted,
          "review" => Batch.classify_change(live_text, formatted)
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
        report.lines.each do |line|
          dm_links = line.scan(/\[\[_DM_\/[^\]]+\]\]/)
          next if dm_links.empty?

          list_item = line.match?(/\A\s*-\s+\[\[_DM_\/[^\]]+\]\](?:\s.*)?\z/)
          unless dm_links.length == 1 && list_item
            raise BatchError, "Every _DM_ wikilink in a Lint report must be its own Markdown list item: #{path}"
          end
        end

        report
      end

      def validate_completed_decision!(decision)
        path = decision.fetch("path")
        validate_self_review!(decision, path)

        case decision["eligibility"]
        when "ineligible"
          if decision["eligibilityReason"].to_s.strip.empty?
            raise BatchError, "A semantically ineligible result requires a concise reason: #{path}"
          end
          unless decision["editorialVerdict"].nil? && decision["outcome"].nil? &&
                 decision["lintReport"].to_s.strip.empty? && decision["handoff"].to_s.strip.empty? &&
                 Array(decision["bodyEdits"]).empty? && decision["dmNotesReview"].nil? &&
                 Array(decision["secretReview"]).empty? &&
                 Array(decision["sharedNonpublicReview"]).empty? &&
                 decision["editorialAssessment"].to_s.strip.empty? && decision["expansionCandidate"].nil?
            raise BatchError, "A semantically ineligible result cannot carry a verdict, outcome, report, handoff, or review payload: #{path}"
          end
        when "eligible"
          verdict = decision["editorialVerdict"]
          unless EDITORIAL_VERDICTS.include?(verdict) && %w[clean open].include?(decision["outcome"])
            raise BatchError, "Every eligible note needs an editorial verdict and clean or open outcome: #{path}"
          end
          if verdict == "Underdeveloped" && decision["outcome"] != "open"
            raise BatchError, "An Underdeveloped verdict must remain open: #{path}"
          end
          unless decision["dmNotesReview"].is_a?(Hash)
            raise BatchError, "Every eligible note needs a structured dm_notes review result: #{path}"
          end
          unless decision["secretReview"].is_a?(Array)
            raise BatchError, "Every eligible note needs a structured SECRET review result: #{path}"
          end
          validate_expansion_candidate!(decision, path)
          validate_editorial_assessment!(decision, path)
        else
          raise BatchError, "Every note needs completed semantic eligibility review: #{path}"
        end
      end

      def validate_self_review!(decision, path)
        review = decision["selfReview"]
        unless review.is_a?(Hash) && review["complete"] == true &&
               SELF_REVIEW_KEYS.all? { |key| review[key] == true }
          raise BatchError, "Every worker result requires completed evidence, privacy-sanity, and candidate self-review: #{path}"
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

        unless report.to_s.match?(/^### Editorial assessment\s*$.*?\*\*Underdeveloped\*\*/m)
          raise BatchError, "An Underdeveloped report must include an explicit editorial assessment: #{path}"
        end

        central_gap = rule_ids.include?("editorial.note_underdeveloped") ||
                      rule_ids.any? { |rule_id| rule_id.start_with?("coverage.") }
        unless central_gap
          raise BatchError, "An Underdeveloped verdict requires a coverage or editorial.note_underdeveloped finding: #{path}"
        end
      end

      def report_rule_ids(report)
        report.to_s.scan(/\*\*(?:Error|Warning|Suggestion)\s+—\s+([a-z0-9_.-]+):/i).flatten
      end

      def validate_expansion_candidate!(decision, path)
        expansion = decision["expansionCandidate"]
        if decision["editorialVerdict"] != "Sufficient, worth expanding"
          unless expansion.nil?
            raise BatchError, "Only a Sufficient, worth expanding verdict may carry an expansion candidate: #{path}"
          end
          return
        end
        unless expansion.is_a?(Hash) && !expansion["addition"].to_s.strip.empty? &&
               !expansion["benefit"].to_s.strip.empty? && expansion["sources"].is_a?(Array) &&
               !expansion["sources"].empty?
          raise BatchError, "Sufficient, worth expanding requires a concrete structured expansion candidate: #{path}"
        end
        expansion.fetch("sources").each do |source|
          unless source.is_a?(Hash) && !source["path"].to_s.strip.empty? &&
                 !source["evidence"].to_s.strip.empty? && EXPANSION_CERTAINTIES.include?(source["certainty"].to_s)
            raise BatchError, "Every expansion source needs path, evidence, and supported certainty: #{path}"
          end
        end
      end

      def validate_editorial_assessment!(decision, path)
        assessment = decision["editorialAssessment"]
        if decision["editorialVerdict"] == "Underdeveloped"
          if assessment.to_s.strip.empty?
            raise BatchError, "An Underdeveloped verdict requires an explicit editorial assessment: #{path}"
          end
        elsif !assessment.nil?
          raise BatchError, "Only an Underdeveloped verdict may carry an editorial assessment: #{path}"
        end
      end

      def validate_declared_body_edits!(decision, live_note, staged_note, path)
        before = Batch.semantic_body_for_edit_declaration(live_note)
        after = Batch.semantic_body_for_edit_declaration(staged_note)
        edits = Array(decision["bodyEdits"])
        if before == after
          raise BatchError, "A result without body prose changes cannot declare body edits: #{path}" unless edits.empty?
          return
        end
        if edits.empty?
          raise BatchError, "Every body prose change requires a declared objective edit: #{path}"
        end
        edits.each do |edit|
          unless edit.is_a?(Hash) && !edit["original"].to_s.empty? && !edit["replacement"].to_s.empty? &&
                 BODY_EDIT_BASES.include?(edit["basis"].to_s)
            raise BatchError, "Every body edit needs original, replacement, and an objective basis: #{path}"
          end
          unless before.include?(edit.fetch("original")) && after.include?(edit.fetch("replacement"))
            raise BatchError, "A declared body edit does not match the staged prose: #{path}"
          end
          if edit["basis"] == "source_correction" && edit["sourcePath"].to_s.strip.empty?
            raise BatchError, "A source correction body edit needs sourcePath: #{path}"
          end
        end
      end

      def validate_dm_notes_review!(decision, record, staged_note, report, outcome, path)
        review = decision.fetch("dmNotesReview")
        expected_required = record.dig("deterministic", "reviewGates", "dmNotes", "required") == true
        unless review["required"] == expected_required
          raise BatchError, "The dm_notes review result does not match the manifest review gate: #{path}"
        end

        expected_clusters = Array(record.dig("dmEvidence", "clusters"))
        expected_ids = expected_clusters.map { |cluster| cluster.fetch("id") }
        cluster_reviews = Array(review["clusterReviews"])
        actual_ids = cluster_reviews.map { |cluster| cluster["clusterId"].to_s }
        unless actual_ids.sort == expected_ids.sort && actual_ids.uniq.length == actual_ids.length
          raise BatchError, "The dm_notes review must disposition every evidence cluster exactly once: #{path}"
        end

        unless expected_required
          unless cluster_reviews.empty?
            raise BatchError, "A skipped dm_notes review cannot carry cluster dispositions: #{path}"
          end
          return
        end

        cluster_reviews.each do |cluster|
          unless DM_SOURCE_DISPOSITIONS.include?(cluster["disposition"].to_s) && !cluster["summary"].to_s.strip.empty?
            raise BatchError, "Every dm_notes cluster needs matching or not_matching disposition and a summary: #{path}"
          end

          disposition = cluster["disposition"].to_s
          recovery = cluster["recovery"].to_s
          dm_notes = staged_note.data["dm_notes"].to_s
          none_attestation = dm_notes.empty? || dm_notes == "none"
          if disposition != "matching" || !none_attestation
            unless recovery == "not_applicable" && cluster["chatSummary"].to_s.strip.empty? &&
                   cluster["candidate"].to_s.strip.empty?
              raise BatchError, "Only a confirmed match for dm_notes: none may carry private recovery content: #{path}"
            end
            next
          end

          unless DM_RECOVERY_DISPOSITIONS.include?(recovery) && recovery != "not_applicable"
            raise BatchError, "Every confirmed dm_notes cluster for dm_notes: none needs a recovery disposition: #{path}"
          end
          if %w[public_candidate private_candidate].include?(recovery)
            if cluster["chatSummary"].to_s.strip.empty? || cluster["candidate"].to_s.strip.empty?
              raise BatchError, "Every recoverable dm_notes cluster needs a chat summary and copy-ready candidate: #{path}"
            end
          elsif !cluster["chatSummary"].to_s.strip.empty? || !cluster["candidate"].to_s.strip.empty?
            raise BatchError, "A dm_notes cluster without recoverable material cannot carry recovery content: #{path}"
          end
        end

        reportable_paths = cluster_reviews.flat_map do |cluster|
          next [] unless cluster["disposition"] == "matching"

          dm_notes = staged_note.data["dm_notes"].to_s
          positive = %w[color important].include?(dm_notes)
          recoverable = %w[public_candidate private_candidate].include?(cluster["recovery"])
          next [] unless positive || recoverable

          Batch.dm_cluster_sources(record, cluster.fetch("clusterId"))
        end
        if outcome == "open"
          missing = reportable_paths.uniq.reject { |source_path| Batch.markdown_list_contains_wikilink?(report, source_path) }
          unless missing.empty?
            raise BatchError, "Reportable _DM_ links in an open note must be Markdown list items in the Lint report: #{path}"
          end
        end

        return if cluster_reviews.any? { |cluster| cluster["disposition"] == "matching" }

        dm_notes = staged_note.data["dm_notes"].to_s
        return unless %w[color important].include?(dm_notes)
        unless outcome == "open" && report_rule_ids(report).include?("dm.notes_no_local_evidence")
          raise BatchError, "A positive dm_notes attestation without a confirmed match requires open dm.notes_no_local_evidence: #{path}"
        end
      end

      def add_dm_evidence_links(report, decision, record, staged_note, outcome)
        return report unless outcome == "open"

        dm_notes = staged_note.data["dm_notes"].to_s
        positive = %w[color important].include?(dm_notes)
        paths = Array(decision.dig("dmNotesReview", "clusterReviews")).flat_map do |cluster|
          next [] unless cluster["disposition"] == "matching"
          next [] unless positive || %w[public_candidate private_candidate].include?(cluster["recovery"])

          Batch.dm_cluster_sources(record, cluster.fetch("clusterId"))
        end.uniq.sort
        return report if paths.empty?

        missing = paths.reject { |source_path| Batch.contains_dm_note_wikilink?(report, source_path) }
        return report if missing.empty?

        section = "### DM evidence\n" + missing.map { |source_path| "- #{Batch.dm_note_wikilink(source_path)}" }.join("\n")
        report.to_s.strip.sub(/\n?%%\^End%%\z/, "\n\n#{section}\n%%^End%%")
      end

      def validate_secret_review!(decision, staged_note, report, path)
        expected = Batch.secret_units(staged_note)
        reviews = Array(decision["secretReview"])
        expected_keys = expected.map { |unit| [unit["kind"], unit["ordinal"], unit["contentSha256"]] }.sort
        review_keys = reviews.map { |unit| [unit["kind"], unit["ordinal"], unit["contentSha256"]] }.sort
        unless expected_keys == review_keys && review_keys.uniq.length == review_keys.length
          raise BatchError, "SECRET review must disposition every current SECRET block exactly once: #{path}"
        end

        reviews.each do |review|
          disposition = review["disposition"].to_s
          unless SECRET_RECOVERY_DISPOSITIONS.include?(disposition) && !review["summary"].to_s.strip.empty?
            raise BatchError, "Every SECRET block needs a supported recovery disposition and summary: #{path}"
          end
          if %w[public_candidate private_candidate].include?(disposition)
            if review["candidate"].to_s.strip.empty?
              raise BatchError, "Every recoverable SECRET block needs a copy-ready candidate: #{path}"
            end
          elsif !review["candidate"].to_s.strip.empty?
            raise BatchError, "A SECRET block without recoverable material cannot carry a candidate addition: #{path}"
          end
        end
      end

      def validate_shared_nonpublic_review!(decision, staged_note, report, outcome, path)
        expected = Batch.shared_nonpublic_units(staged_note)
        reviews = Array(decision["sharedNonpublicReview"])
        expected_keys = expected.map { |unit| [unit["kind"], unit["contentSha256"]] }.sort
        review_keys = reviews.map { |unit| [unit["kind"], unit["contentSha256"]] }.sort
        unless expected_keys == review_keys && review_keys.uniq.length == review_keys.length
          raise BatchError, "Shared nonpublic review must disposition every current comment and Campaign:none block exactly once: #{path}"
        end
        rule_ids = report_rule_ids(report)
        reviews.each do |review|
          disposition = review["disposition"].to_s
          unless SHARED_NONPUBLIC_DISPOSITIONS.include?(disposition) && !review["summary"].to_s.strip.empty?
            raise BatchError, "Every shared nonpublic unit needs a supported disposition and summary: #{path}"
          end
          required_rule = OPEN_SHARED_NONPUBLIC_RULES[disposition]
          next unless required_rule
          unless outcome == "open" && rule_ids.include?(required_rule)
            raise BatchError, "#{disposition} requires open #{required_rule}: #{path}"
          end
        end
        OPEN_SHARED_NONPUBLIC_RULES.each do |disposition, rule_id|
          next unless rule_ids.include?(rule_id)
          next if reviews.any? { |review| review["disposition"] == disposition }

          raise BatchError, "#{rule_id} requires a matching shared nonpublic disposition: #{path}"
        end
      end

      def validate_documented_names_preserved!(live_note, staged_note, path)
        before = Batch.name_block_data(live_note).select { |entry| entry.is_a?(Hash) && entry["status"] == "documented" }
        after = Batch.name_block_data(staged_note).select { |entry| entry.is_a?(Hash) }
        before.each do |original|
          identity = Batch.documented_name_identity(original)
          candidate = after.find { |entry| Batch.documented_name_identity(entry) == identity }
          unless candidate && candidate["status"] == "documented"
            raise BatchError, "A documented name entry was removed or downgraded: #{path}"
          end
          original.each do |key, value|
            next unless Batch.populated_documented_value?(value)
            next if Batch.canonical_review_value(candidate[key]) == Batch.canonical_review_value(value)

            raise BatchError, "A populated documented name value changed (#{key}): #{path}"
          end
        end
      end

      def review_summary(candidates)
        changed = candidates.reject { |candidate| candidate.fetch("text") == TaelgarNoteLint.read_text(@root.join(candidate.fetch("path"))) }
        targeted = changed.select { |candidate| candidate.dig("review", "level") == "targeted" }
        mechanical = changed - targeted
        summary = {
          "changedPaths" => changed.map { |candidate| candidate.fetch("path") },
          "mechanicalOnlyPaths" => mechanical.map { |candidate| candidate.fetch("path") },
          "targetedReviewPaths" => targeted.map { |candidate| candidate.fetch("path") },
          "categories" => {}
        }
        REVIEW_CATEGORIES.each do |category|
          paths = changed.select { |candidate| candidate.dig("review", "categories").include?(category) }
                         .map { |candidate| candidate.fetch("path") }
          summary.fetch("categories")[category] = paths unless paths.empty?
        end
        summary
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
        options = {
          root: Pathname.pwd,
          all_linted: false,
          stale: false,
          only_needs_review: false,
          re_lint: false,
          force_dm_review: false
        }
        parser = OptionParser.new do |opts|
          opts.banner = "Usage: lint_taelgar_notes.rb prepare [options] [NOTE ...]"
          opts.on("--root PATH", "Vault root") { |value| options[:root] = Pathname.new(value) }
          opts.on("--re-lint", "Include notes with valid prior lint completion state") { options[:re_lint] = true }
          opts.on("--force-dm-review", "Re-run dm_notes evidence review for named re-lint targets") do
            options[:force_dm_review] = true
          end
          opts.on("--all-linted", "Select every note with lint completion state") { options[:all_linted] = true }
          opts.on("--stale", "Select notes whose lintVersion is not current") { options[:stale] = true }
          opts.on("--only-needs-review", "Exclude current notes with no freshness candidates") { options[:only_needs_review] = true }
          opts.on("--output PATH", "Write JSON to a file instead of stdout") { |value| options[:output] = value }
        end
        parser.parse!(@argv)
        if (options[:all_linted] || options[:stale]) && !options[:re_lint]
          raise BatchError, "--all-linted and --stale require --re-lint because completed notes are excluded by default."
        end
        if options[:force_dm_review] && !options[:re_lint]
          raise BatchError, "--force-dm-review requires --re-lint."
        end
        if options[:force_dm_review] && @argv.empty?
          raise BatchError, "--force-dm-review requires explicitly named targets."
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
          manifest = Preparer.new(root: root, force_dm_notes_review: options[:force_dm_review]).prepare(paths)
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
          max_tokens: DEFAULT_MAX_TOKENS
        }
        parser = OptionParser.new do |opts|
          opts.banner = "Usage: lint_taelgar_notes.rb workspace --manifest FILE --review-dir DIR [options]"
          opts.on("--root PATH", "Vault root") { |value| options[:root] = Pathname.new(value) }
          opts.on("--manifest PATH", "Prepared batch manifest") { |value| options[:manifest] = value }
          opts.on("--review-dir PATH", "Temporary staged review workspace") { |value| options[:review_dir] = value }
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
