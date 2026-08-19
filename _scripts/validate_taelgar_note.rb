#!/usr/bin/env ruby
# frozen_string_literal: true

# Deterministic validator and narrowly scoped frontmatter formatter for
# individual Taelgar notes.
#
# The validator checks note structure, selected adopted metadata rules,
# provisional campaign/audience migration rules, internal links, structured
# content markers, and simple mechanical prose defects. When given a Git
# baseline, it also lists newer vault notes and beat-facts sources that mention
# the target, prioritizing campaign, session, and DM material.
#
# It deliberately does not decide whether a newer source materially changes the
# note. Correctness, coverage, status disposition, editorial judgment, and
# development sufficiency remain responsibilities of the contextual lint pass.

require "date"
require "json"
require "open3"
require "optparse"
require "pathname"
require "time"
require "yaml"

module TaelgarNoteLint
  VERSION = "2.2"
  SCHEMA_VERSION = 3

  DEPRECATED_FRONTMATTER_FIELDS = %w[
    activeYear subTypeOf subTypeOfAlias subspecies speciesAlias deity
    timelineDescriptor pcOwner rarity leaderOf reignStart aNoDate aPast
    aPastWithStart aCurrent
  ].freeze

  DEPRECATED_FRONTMATTER_REPLACEMENTS = {
    "activeYear" => "Use created for entity existence, a Date block for passage visibility, or audience for publication scope, according to the original meaning.",
    "subTypeOf" => "Use the primary typeOf when this is the real classification; otherwise use typeOfAlias, partOf, or affiliations as appropriate.",
    "subTypeOfAlias" => "Use typeOfAlias when this is display wording; otherwise incorporate it into the replacement for subTypeOf.",
    "subspecies" => "Use species for the primary biological classification and typeOfAlias only for display wording.",
    "speciesAlias" => "Use typeOfAlias for display wording, or an accepted ancestry/species value when it is classification.",
    "deity" => "Represent the relationship with affiliations, partOf, or ordinary linked prose.",
    "timelineDescriptor" => "Use explicit lifecycle dates, Date blocks, or persistent article POV metadata according to the intended temporal meaning.",
    "pcOwner" => "Use the current player/character ownership field adopted by the applicable character template; confirm the intended semantics before migration.",
    "rarity" => "Move game-mechanical rarity to the applicable mechanics block or retained item field selected by human review.",
    "leaderOf" => "Use an affiliation entry with type: leader.",
    "reignStart" => "Put the start date on the corresponding leader affiliation.",
    "aNoDate" => "Use displayDefaults or an affiliation-level format override.",
    "aPast" => "Use displayDefaults or an affiliation-level formatPast override.",
    "aPastWithStart" => "Use displayDefaults or an affiliation-level formatPast override.",
    "aCurrent" => "Use displayDefaults or an affiliation-level formatCurrent override."
  }.freeze

  FRONTMATTER_HEAD_FIELDS = %w[
    headerVersion lintedAt lintVersion displayDefaults
  ].freeze

  FRONTMATTER_CLASSIFICATION_FIELDS = %w[
    tags typeOf typeOfAlias species ancestry
  ].freeze

  FRONTMATTER_IDENTITY_FIELDS = %w[name aliases pronunciation].freeze
  FRONTMATTER_RELATIONSHIP_FIELDS = %w[affiliations whereabouts].freeze
  FRONTMATTER_TAIL_FIELDS = %w[
    knownTo excludePublish audience dm_owner dm_notes
  ].freeze

  DESCRIPTIVE_TAGS = %w[
    ancestry background creature event group item meta object person place power
    primary-source session-note source organization
  ].freeze

  NAMED_SUBJECT_TAGS = %w[
    ancestry background creature event group item object person place power
    organization
  ].freeze

  NAME_STATUSES = %w[documented inferred proposed disputed unresolved].freeze
  PRONUNCIATION_EXCEPTIONS = %w[obvious title meta].freeze
  MAP_REQUIRED_TYPES = %w[waterway road settlement].freeze
  WORLD_HEX_PATTERN = /\A\d{2}\.\d{2}\.[A-Z]\d{2}\z/
  METADATA_BLOCK_PATTERN = /%%\^Metadata:(names|map|article)(?::v(\d+))?%%\s*(.*?)\s*%%\^End%%/m
  LINT_BLOCK_PATTERN = /%%\^Lint%%\s*(.*?)\s*%%\^End%%/m

  PLACE_TYPES = [
    "settlement", "realm", "neighborhood", "region", "watershed", "plane",
    "extraplanar domain", "planar link", "wetlands", "forest", "plain",
    "grassland", "desert", "inn", "building", "road", "holy site",
    "infrastructure", "waterway", "marine feature", "lake",
    "topographical feature", "topographic feature", "subterranean feature",
    "landform", "island"
  ].freeze

  DM_OWNERS = %w[tim mike joint player none].freeze
  DM_NOTES = %w[important color none].freeze
  SOURCE_PRIORITIES = {
    "beat-facts" => 0,
    "dm-note" => 1,
    "session-note" => 2,
    "campaign-note" => 3,
    "vault-note" => 4,
    "development-note" => 5
  }.freeze

  EDITORIAL_PATTERNS = [
    [/(?:\b)accomodate(?:\b)/i, "accommodate"],
    [/\bclimatic victory\b/i, "climactic victory"],
    [/\bcultural and spiritual capitol\b/i, "cultural and spiritual capital"],
    [/\bconfluence of with\b/i, "confluence with"],
    [/\bGoldpeak Mines mines\b/i, "Goldpeak Mines"],
    [/\bwas rebuild\b/i, "was rebuilt"],
    [/\bin to the (?:north|south|east|west)\b/i, "to the named direction"]
  ].freeze

  module_function

  def normalize(value)
    value.to_s.strip.downcase.gsub(/\s+/, " ")
  end

  def mask_markdown_code(text)
    fence = nil
    masked = text.lines.map do |line|
      if fence
        closing = line.match?(/\A {0,3}#{Regexp.escape(fence[0])}{#{fence[1]},}[ \t]*(?:\r?\n|\z)/)
        fence = nil if closing
        line.gsub(/[^\r\n]/, " ")
      elsif (match = line.match(/\A {0,3}(`{3,}|~{3,})/))
        run = match[1]
        fence = [run[0], run.length]
        line.gsub(/[^\r\n]/, " ")
      else
        line
      end
    end.join

    masked.gsub(/(`+)[^\r\n]*?\1/) { |span| span.gsub(/[^\r\n]/, " ") }
  end

  def yaml_load(text)
    # Date is permitted because unquoted Taelgar dates otherwise fail even
    # though they are valid YAML.
    YAML.safe_load(
      text,
      permitted_classes: [Date, Time],
      permitted_symbols: [],
      aliases: true
    )
  end

  def line_number(text, offset)
    text[0...offset].count("\n") + 1
  end

  def relative_path(root, path)
    Pathname.new(path).expand_path.relative_path_from(root).to_s
  end

  def read_text(path)
    decode_utf8(path).first
  end

  def decode_utf8(path)
    text = File.binread(path.to_s).force_encoding(Encoding::UTF_8)
    valid = text.valid_encoding?
    [valid ? text : text.scrub, valid]
  end

  class ParsedNote
    attr_reader :body, :body_start_line, :data, :field_lines, :field_order,
                :frontmatter_lines, :path, :text, :yaml_error

    def initialize(path, text)
      @path = path
      @text = text
      @data = {}
      @body = text
      @body_start_line = 1
      @frontmatter_lines = []
      @field_lines = {}
      @field_order = []
      @yaml_error = nil
      @frontmatter_state = :missing
      parse
    end

    def frontmatter_state
      @frontmatter_state
    end

    def tags
      value = @data["tags"]
      value.is_a?(Array) ? value.map(&:to_s) : []
    end

    def identity_names
      names = [Pathname.new(@path).basename(".md").to_s, @data["name"]]
      aliases = @data["aliases"]
      names.concat(aliases) if aliases.is_a?(Array)
      names.map(&:to_s).map(&:strip).reject(&:empty?).uniq
    end

    def field_line(field)
      @field_lines[field]
    end

    def raw_field_line(field)
      line = field_line(field)
      line ? @text.lines[line - 1].to_s.chomp : nil
    end

    private

    def parse
      lines = @text.lines
      return unless lines.first && lines.first.sub(/^\uFEFF/, "").strip == "---"

      closing_index = nil
      lines[1..-1].to_a.each_with_index do |line, index|
        if line.strip == "---"
          closing_index = index + 1
          break
        end
      end

      unless closing_index
        @frontmatter_state = :unclosed
        return
      end

      @frontmatter_state = :present
      @frontmatter_lines = lines[1...closing_index]
      @body_start_line = closing_index + 2
      @body = lines[(closing_index + 1)..-1].to_a.join

      @frontmatter_lines.each_with_index do |line, index|
        match = line.match(/^([A-Za-z][A-Za-z0-9_-]*):/)
        next unless match

        field = match[1]
        @field_order << field
        @field_lines[field] ||= index + 2
      end

      begin
        payload = TaelgarNoteLint.yaml_load(@frontmatter_lines.join)
        if payload.nil?
          @data = {}
        elsif payload.is_a?(Hash)
          @data = payload.each_with_object({}) { |(key, value), memo| memo[key.to_s] = value }
        else
          @yaml_error = "frontmatter must parse to a mapping"
        end
      rescue Psych::Exception => error
        @yaml_error = error.message.lines.first.to_s.strip
      end
    end
  end

  class FrontmatterFormatter
    class UnsafeFrontmatter < StandardError; end

    def initialize(note)
      @note = note
    end

    def format_text
      raise UnsafeFrontmatter, "frontmatter is missing or invalid" unless @note.frontmatter_state == :present && !@note.yaml_error
      raise UnsafeFrontmatter, "frontmatter has duplicate keys" unless @note.field_order.uniq.length == @note.field_order.length
      if @note.frontmatter_lines.any? { |line| line.include?("#") }
        raise UnsafeFrontmatter, "frontmatter contains comments that require preservation-aware handling"
      end
      if @note.frontmatter_lines.any? { |line| line.match?(/^\s*<<:|[&*][A-Za-z0-9_-]+/) }
        raise UnsafeFrontmatter, "frontmatter contains YAML anchors or merges"
      end

      fields = ordered_fields
      rendered = fields.flat_map { |field| render_top_level(field, @note.data.fetch(field)) }
      formatted = "---\n#{rendered.join("\n")}\n---\n#{@note.body}"
      reparsed = ParsedNote.new(@note.path, formatted)
      unless reparsed.frontmatter_state == :present && !reparsed.yaml_error &&
             comparable_data(reparsed.data) == comparable_data(@note.data)
        raise UnsafeFrontmatter, "formatted frontmatter does not preserve parsed values"
      end

      formatted
    end

    def changed?
      format_text != @note.text
    end

    private

    def ordered_fields
      source_order = (@note.field_order + @note.data.keys).uniq
      reserved = DEPRECATED_FRONTMATTER_FIELDS + FRONTMATTER_HEAD_FIELDS +
                 FRONTMATTER_CLASSIFICATION_FIELDS + FRONTMATTER_IDENTITY_FIELDS +
                 FRONTMATTER_RELATIONSHIP_FIELDS + FRONTMATTER_TAIL_FIELDS
      other = source_order.reject { |field| reserved.include?(field) }

      [
        DEPRECATED_FRONTMATTER_FIELDS,
        FRONTMATTER_HEAD_FIELDS,
        FRONTMATTER_CLASSIFICATION_FIELDS,
        other,
        FRONTMATTER_IDENTITY_FIELDS,
        FRONTMATTER_RELATIONSHIP_FIELDS,
        FRONTMATTER_TAIL_FIELDS
      ].flatten.select { |field| @note.data.key?(field) }.uniq
    end

    def render_top_level(field, value)
      return ["lintedAt: #{JSON.generate(canonical_lint_value(field, value))}"] if field == "lintedAt"
      return ["lintVersion: #{JSON.generate(value.to_s)}"] if field == "lintVersion"

      case value
      when Array
        return ["#{field}: []"] if value.empty?
        if value.all? { |entry| scalar?(entry) }
          ["#{field}: [#{value.map { |entry| render_scalar(entry) }.join(', ')}]"]
        else
          ["#{field}:"] + value.map { |entry| "  - #{render_flow(entry)}" }
        end
      when Hash
        ["#{field}: #{render_flow_hash(value)}"]
      else
        ["#{field}: #{render_scalar(value)}"]
      end
    end

    def render_flow(value)
      case value
      when Hash then render_flow_hash(value)
      when Array then "[#{value.map { |entry| render_flow(entry) }.join(', ')}]"
      else render_scalar(value)
      end
    end

    def render_flow_hash(value)
      "{#{value.map { |key, entry| "#{key}: #{render_flow(entry)}" }.join(', ')}}"
    end

    def render_scalar(value)
      case value
      when nil then "null"
      when true then "true"
      when false then "false"
      when Integer then value.to_s
      when Float then value.finite? ? value.to_s : JSON.generate(value.to_s)
      when Date then value.strftime("%Y-%m-%d")
      when Time then "!!timestamp #{JSON.generate(value.iso8601)}"
      else
        string = value.to_s
        plain_string?(string) ? string : JSON.generate(string)
      end
    end

    def scalar?(value)
      !value.is_a?(Hash) && !value.is_a?(Array)
    end

    def plain_string?(string)
      return false if string.empty? || string != string.strip || string.include?("\n")
      return false if string.match?(/\A(?:null|true|false|yes|no|on|off|~)\z/i)
      return false if string.match?(/\A[-+]?\d+(?:\.\d+)?\z/)
      return false if string.match?(/\A\d{4}-\d{2}(?:-\d{2})?\z/)
      return false if string.match?(/\A\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[-+]\d{2}:\d{2})\z/)
      return false if string.match?(/[\[\]{},#&*!|>'"%@`]|:\s|\s#/) || string.start_with?("-", "?", ":")

      true
    end

    def comparable_data(data)
      data.each_with_object({}) do |(key, value), memo|
        memo[key.to_s] = if %w[lintedAt lintVersion].include?(key.to_s)
                           canonical_lint_value(key.to_s, value)
                         else
                           value
                         end
      end
    end

    def canonical_lint_value(field, value)
      return value.iso8601 if field == "lintedAt" && value.is_a?(Time)

      value.to_s
    end
  end

  class CampaignRegistry
    attr_reader :campaigns

    def initialize(root)
      @root = root
      @campaigns = []
      @lookup = {}
      load_registry
    end

    def resolve(value)
      resolve_entry(value)&.fetch("code")
    end

    def resolve_entry(value)
      @lookup[TaelgarNoteLint.normalize(value)]
    end

    def canonical_name(value)
      resolve_entry(value)&.fetch("name")
    end

    def canonical?(value)
      resolved = resolve(value)
      resolved && resolved == value.to_s
    end

    def campaign_for_path(path)
      normalized_path = path.to_s.tr("\\", "/")
      matches = @campaigns.select do |campaign|
        root = campaign["campaignRoot"]
        root && (normalized_path == root || normalized_path.start_with?("#{root}/"))
      end
      matches.max_by { |campaign| campaign["campaignRoot"].to_s.length }
    end

    private

    def load_registry
      path = @root.join("_scripts", "session_note_campaigns.json")
      raise ArgumentError, "Campaign registry not found: #{path}" unless path.file?
      payload = JSON.parse(TaelgarNoteLint.read_text(path))
      entries = payload["campaigns"]
      unless entries.is_a?(Hash) && !entries.empty?
        raise ArgumentError, "Campaign registry must contain a nonempty campaigns object"
      end

      codes = {}
      entries.each do |slug, raw|
        unless raw.is_a?(Hash)
          raise ArgumentError, "Campaign #{slug} must be a JSON object"
        end
        name = raw["name"].to_s.strip
        code = raw["code"].to_s.strip
        raise ArgumentError, "Campaign #{slug} is missing name" if name.empty?
        unless code.match?(/\A[a-z][a-z0-9]*\z/)
          raise ArgumentError, "Campaign #{slug} code must be lowercase alphanumeric: #{code.inspect}"
        end
        if codes.key?(code)
          raise ArgumentError, "Campaign code #{code} is duplicated by #{codes[code]} and #{slug}"
        end
        codes[code] = slug

        campaign = raw.merge("slug" => slug, "name" => name, "code" => code)
        @campaigns << campaign
        ([slug, name, code] + Array(campaign["aliases"])).each do |value|
          key = TaelgarNoteLint.normalize(value)
          next if key.empty?
          if @lookup.key?(key) && @lookup[key]["code"] != code
            raise ArgumentError, "Campaign alias #{value.inspect} resolves to more than one campaign"
          end
          @lookup[key] = campaign
        end
      end
    rescue JSON::ParserError => error
      raise ArgumentError, "Campaign registry is invalid JSON: #{error.message}"
    end
  end

  class NoteIndex
    def initialize(root)
      @root = root
      @by_name = Hash.new { |hash, key| hash[key] = [] }
      @by_path = {}
      build
    end

    def resolve(target, source_path = nil)
      clean = target.to_s.split("|", 2).first.to_s.split("#", 2).first.to_s.strip
      clean = clean.split("^", 2).first.to_s.strip
      return [] if clean.empty?

      clean = clean.sub(/\.md\z/i, "").tr("\\", "/").sub(%r{\A\./}, "")
      if clean.include?("/")
        direct = @by_path[TaelgarNoteLint.normalize(clean)]
        return [direct].compact
      end

      candidates = @by_name[TaelgarNoteLint.normalize(clean)].uniq
      return candidates unless candidates.empty?

      return [] unless source_path

      source_dir = Pathname.new(source_path).dirname
      relative = source_dir.join(clean).cleanpath.to_s
      [@by_path[TaelgarNoteLint.normalize(relative)]].compact
    end

    private

    def build
      Dir.glob(@root.join("**", "*.md").to_s).sort.each do |absolute|
        path = Pathname.new(absolute)
        rel = TaelgarNoteLint.relative_path(@root, path)
        parts = Pathname.new(rel).each_filename.to_a
        next if parts.any? { |part| part.start_with?(".") }
        next if path.basename.to_s == "AGENTS.md"

        path_key = rel.sub(/\.md\z/i, "")
        @by_path[TaelgarNoteLint.normalize(path_key)] = rel

        text = TaelgarNoteLint.read_text(path)
        parsed = ParsedNote.new(rel, text)
        names = parsed.identity_names
        names.each { |name| @by_name[TaelgarNoteLint.normalize(name)] << rel }
      rescue Errno::ENOENT, Errno::EACCES
        next
      end
    end
  end

  class DMNoteScanner
    def initialize(root:, index:)
      @root = Pathname.new(root).expand_path
      @index = index
      @documents = Dir.glob(@root.join("_DM_", "**", "*.md").to_s).sort.each_with_object([]) do |absolute, documents|
        path = TaelgarNoteLint.relative_path(@root, absolute)
        documents << [path, TaelgarNoteLint.read_text(absolute)]
      rescue Errno::ENOENT, Errno::EACCES
        next
      end
    end

    def mentions(note)
      resolvable_names = note.identity_names.select do |name|
        @index.resolve(name, note.path) == [note.path]
      end
      @documents.each_with_object([]) do |(path, original_text), matches|
        text = TaelgarNoteLint.mask_markdown_code(original_text)
        lines = []
        kinds = []
        text.lines.each_with_index do |line, index|
          linked = line.scan(/(?<!!)\[\[([^\]\n]+)\]\]/).flatten.any? do |raw|
            @index.resolve(raw, path).include?(note.path)
          end
          named = resolvable_names.any? { |name| exact_name_match?(line, name) }
          next unless linked || named

          lines << index + 1
          kinds << "link" if linked
          kinds << "name" if named
        end
        next if lines.empty?

        matches << {
          "path" => path,
          "lines" => lines.uniq,
          "matchKinds" => kinds.uniq
        }
      end
    end

    private

    def exact_name_match?(text, name)
      text.match?(/(?<![[:alnum:]_])#{Regexp.escape(name)}(?![[:alnum:]_])/i)
    end
  end

  class Validator
    attr_reader :registry

    def initialize(root:, check_links: true, index: nil)
      @root = Pathname.new(root).expand_path
      @registry = CampaignRegistry.new(@root)
      @check_links = check_links
      @index = index || (check_links ? NoteIndex.new(@root) : nil)
      @dm_scanner = check_links ? DMNoteScanner.new(root: @root, index: @index) : nil
    end

    def validate_path(path)
      absolute = Pathname.new(path)
      absolute = @root.join(absolute) unless absolute.absolute?
      rel = TaelgarNoteLint.relative_path(@root, absolute)
      text, valid_encoding = TaelgarNoteLint.decode_utf8(absolute)
      report = validate_text(rel, text)
      unless valid_encoding
        report["findings"] << {
          "ruleId" => "file.invalid_utf8",
          "severity" => "error",
          "class" => "required",
          "message" => "The Markdown file contains bytes that are not valid UTF-8.",
          "line" => 1
        }
        report["findings"].sort_by! { |finding| finding_sort_key(finding) }
        report["summary"] = summarize(report["findings"])
      end
      report
    end

    def validate_text(path, text)
      note = ParsedNote.new(path, text)
      findings = []

      validate_frontmatter(note, findings)
      if note.frontmatter_state == :present && !note.yaml_error
        validate_identity_and_classification(note, findings)
        validate_campaign_metadata(note, findings)
        validate_dm_metadata(note, findings)
        validate_content_blocks(note, findings)
        validate_editorial_mechanics(note, findings)
        validate_links(note, findings) if @check_links
        validate_relationships(note, findings) if @check_links
      end

      statuses = note.tags.select { |tag| tag.start_with?("status/") }
      {
        "schemaVersion" => SCHEMA_VERSION,
        "validatorVersion" => VERSION,
        "note" => {
          "path" => path,
          "name" => note.data["name"] || Pathname.new(path).basename(".md").to_s,
          "profile" => note.tags.find { |tag| DESCRIPTIVE_TAGS.include?(tag) },
          "authority" => source_authority(note),
          "statuses" => statuses
        },
        "findings" => findings.sort_by { |finding| finding_sort_key(finding) },
        "summary" => summarize(findings)
      }
    end

    private

    def add(findings, rule_id, severity, rule_class, message, line: nil, provisional: false, details: nil)
      finding = {
        "ruleId" => rule_id,
        "severity" => severity,
        "class" => rule_class,
        "message" => message
      }
      finding["line"] = line if line
      finding["provisional"] = true if provisional
      finding["details"] = details if details
      findings << finding
    end

    def source_authority(note)
      return "session-source" if note.tags.include?("session-note")
      return "primary-source" if note.tags.include?("source") || note.tags.include?("primary-source")

      "reference"
    end

    def validate_frontmatter(note, findings)
      case note.frontmatter_state
      when :missing
        add(findings, "frontmatter.missing", "error", "required",
            "The note must begin with YAML frontmatter.", line: 1)
        return
      when :unclosed
        add(findings, "frontmatter.unclosed", "error", "required",
            "The opening frontmatter delimiter has no closing delimiter.", line: 1)
        return
      end

      if note.yaml_error
        add(findings, "frontmatter.invalid_yaml", "error", "required",
            "YAML frontmatter could not be parsed: #{note.yaml_error}", line: 1)
        return
      end

      if note.field_order.include?("tags")
        unless note.data["tags"].is_a?(Array)
          add(findings, "frontmatter.tags_shape", "error", "required",
              "tags must be a YAML list.", line: note.field_line("tags"))
        end
      else
        add(findings, "frontmatter.tags_missing", "error", "required",
            "A content note must declare tags.", line: 1)
      end

      begin
        if FrontmatterFormatter.new(note).changed?
          add(findings, "frontmatter.noncanonical_format", "warning", "required",
              "Frontmatter field order or collection formatting differs from the linter's canonical form.",
              line: 1)
        end
      rescue FrontmatterFormatter::UnsafeFrontmatter => error
        add(findings, "frontmatter.format_unsafe", "warning", "required",
            "Frontmatter cannot be safely normalized automatically: #{error.message}.", line: 1)
      end

      linted_at = note.data["lintedAt"]
      lint_version = note.data["lintVersion"]
      if linted_at || lint_version
        if linted_at.to_s.strip.empty? || lint_version.nil?
          add(findings, "lint.state_incomplete", "error", "required",
              "lintedAt and lintVersion must be written together.",
              line: note.field_line("lintedAt") || note.field_line("lintVersion") || 1)
        else
          begin
            Time.iso8601(linted_at.to_s)
          rescue ArgumentError
            add(findings, "lint.timestamp_invalid", "error", "required",
                "lintedAt must be an ISO 8601 timestamp with an explicit offset.",
                line: note.field_line("lintedAt"))
          end
          unless lint_version.is_a?(String) && lint_version.match?(/\A\d+\.\d+\z/)
            add(findings, "lint.version_invalid", "error", "required",
                "lintVersion must be a quoted major.minor version such as \"2.1\".",
                line: note.field_line("lintVersion"))
          end
          if lint_version.is_a?(String) && lint_version.match?(/\A\d+\.\d+\z/) && lint_version != VERSION
            add(findings, "lint.version_outdated", "suggestion", "recommended",
                "The note was checked with linter #{lint_version}; current version is #{VERSION}.",
                line: note.field_line("lintVersion"), provisional: true)
          end
        end
      end
    end

    def validate_identity_and_classification(note, findings)
      profile = note.tags.find { |tag| DESCRIPTIVE_TAGS.include?(tag) }
      unless profile
        add(findings, "classification.descriptive_tag_missing", "error", "required",
            "No recognized descriptive tag identifies the note profile.",
            line: note.field_line("tags"))
        return
      end

      if note.data["name"].to_s.strip.empty? && !valid_name_block_present?(note)
        add(findings, "identity.implicit_name", "suggestion", "recommended",
            "The filename supplies the name, but the full target metadata profile prefers an explicit name.",
            line: 1, provisional: true)
      end


      if NAMED_SUBJECT_TAGS.include?(profile) && note.data["pronunciation"].to_s.strip.empty? &&
         !accepted_pronunciation_exception?(note)
        add(findings, "pronunciation.missing_or_exception", "warning", "conditional",
            "This named in-world subject needs a pronunciation or a contextual obvious-name/title exception.",
            line: note.field_line("name") || 1, provisional: true)
      end

      case profile
      when "person"
        if note.data["species"].to_s.strip.empty?
          add(findings, "classification.person_species_missing", "warning", "conditional",
              "Person notes normally require species.", line: note.field_line("tags"))
        end
      when "place"
        type = note.data["typeOf"].to_s.strip
        if type.empty?
          add(findings, "classification.place_type_missing", "error", "required",
              "Place notes require typeOf.", line: note.field_line("tags"))
        elsif !PLACE_TYPES.include?(type)
          add(findings, "classification.place_type_unknown", "warning", "required",
              "Unknown place typeOf value: #{type}.", line: note.field_line("typeOf"),
              details: { "allowed" => PLACE_TYPES })
        end
      when "object", "item"
        if note.data["typeOf"].to_s.strip.empty?
          add(findings, "classification.object_type_missing", "error", "required",
              "Object notes require typeOf.", line: note.field_line("tags"))
        end
      end

      DEPRECATED_FRONTMATTER_FIELDS.each do |field|
        next unless note.data.key?(field)

        rule_id = field == "subTypeOf" ? "classification.deprecated_subtype" : "frontmatter.deprecated_field"
        replacement = deprecated_replacement(note, field)
        add(findings, rule_id, "suggestion", "recommended",
            "#{field} is deprecated or obsolete. Proposed replacement: #{replacement}",
            line: note.field_line(field), provisional: true,
            details: { "field" => field, "replacement" => replacement })
      end
    end

    def deprecated_replacement(note, field)
      value = note.data[field]
      if field == "subTypeOf" && !value.to_s.strip.empty? && note.data["typeOfAlias"].to_s.strip.empty? &&
         !note.data["typeOf"].to_s.strip.empty?
        return "typeOfAlias: #{value} preserves this note's secondary display wording alongside typeOf: #{note.data['typeOf']}."
      end

      DEPRECATED_FRONTMATTER_REPLACEMENTS.fetch(field)
    end

    def validate_campaign_metadata(note, findings)
      known_to = string_list(note.data["knownTo"])
      known_codes = validate_campaign_values(note, findings, "knownTo", known_to)

      if !(note.tags & %w[person object item]).empty? && !note.data.key?("knownTo")
        add(findings, "campaign.known_to_missing", "error", "required",
            "Person and object notes must declare knownTo, using an empty list when no campaign is recorded.",
            line: note.field_line("tags"))
      end

      campaign_value = note.data["campaign"]
      campaign_code = nil
      campaign_applicable = campaign_field_applicable?(note)
      if campaign_value && !campaign_value.to_s.strip.empty?
        campaign_entry = @registry.resolve_entry(campaign_value)
        if campaign_entry.nil?
          add(findings, "campaign.unknown_code", "error", "required",
              "Unknown campaign value: #{campaign_value}.", line: note.field_line("campaign"))
        else
          campaign_code = campaign_entry["code"]
        end
        if campaign_entry && campaign_value.to_s != campaign_entry["name"]
          add(findings, "campaign.noncanonical_name", "suggestion", "recommended",
              "campaign frontmatter uses the canonical long name: #{campaign_entry['name']}.",
              line: note.field_line("campaign"), provisional: true)
        end
        unless campaign_applicable
          add(findings, "campaign.unexpected_entity_field", "warning", "conditional",
              "campaign identifies session notes, campaign meta pages, and campaign source material; " \
              "use knownTo and audience for an in-world entity regardless of its directory.",
              line: note.field_line("campaign"), provisional: true)
        end
      end

      campaign_info_codes = []
      campaign_info = note.data["campaignInfo"]
      if campaign_info
        unless campaign_info.is_a?(Array) && campaign_info.all? { |entry| entry.is_a?(Hash) }
          add(findings, "campaign.info_shape", "error", "required",
              "campaignInfo must be a list of dictionaries.", line: note.field_line("campaignInfo"))
        else
          campaign_info.each do |entry|
            value = entry["campaign"] || entry[:campaign]
            next if value.to_s.strip.empty?

            resolved = @registry.resolve(value)
            if resolved
              campaign_info_codes << resolved
            else
              add(findings, "campaign.info_unknown_code", "error", "required",
                  "campaignInfo contains an unknown campaign value: #{value}.",
                  line: note.field_line("campaignInfo"))
            end
          end
        end
      end

      known_to_profile = !(note.tags & %w[person object item]).empty?
      missing_known_to = known_to_profile ? campaign_info_codes.uniq - known_codes : []
      unless missing_known_to.empty?
        add(findings, "campaign.missing_known_to", "warning", "conditional",
            "campaignInfo normally requires matching knownTo values: #{missing_known_to.join(', ')}.",
            line: note.field_line("campaignInfo"), provisional: true,
            details: { "campaigns" => missing_known_to })
      end

      path_campaign = @registry.campaign_for_path(note.path)
      if campaign_applicable && campaign_value.to_s.strip.empty? && note.tags.include?("session-note")
        add(findings, "campaign.session_missing", "error", "required",
            "Session notes require campaign identity.", line: 1,
            details: path_campaign ? { "campaign" => path_campaign["name"] } : nil)
      elsif campaign_applicable && path_campaign && campaign_value.to_s.strip.empty?
        add(findings, "campaign.document_missing", "warning", "conditional",
            "This campaign meta/source document should identify campaign #{path_campaign['name']}.",
            line: 1, provisional: true,
            details: { "campaign" => path_campaign["name"] })
      elsif campaign_applicable && path_campaign && campaign_code && campaign_code != path_campaign["code"]
        add(findings, "campaign.directory_mismatch", "error", "conditional",
            "The campaign field resolves to #{campaign_code}, but the directory belongs to #{path_campaign['code']}.",
            line: note.field_line("campaign"), provisional: true)
      end

      validate_audience(note, findings, string_list(note.data["audience"]))
    end

    def campaign_field_applicable?(note)
      !(note.tags & %w[session-note meta source]).empty?
    end

    def validate_campaign_values(note, findings, field, values)
      values.each_with_object([]) do |value, codes|
        resolved = @registry.resolve(value)
        if resolved.nil?
          add(findings, "campaign.unknown_code", "error", "required",
              "#{field} contains an unknown campaign value: #{value}.",
              line: note.field_line(field))
        else
          codes << resolved
          next if value.to_s == resolved

          add(findings, "campaign.noncanonical_code", "suggestion", "recommended",
              "#{field} value #{value} resolves to #{resolved}; use the canonical lowercase code.",
              line: note.field_line(field), provisional: true)
        end
      end.uniq
    end

    def validate_audience(note, findings, values)
      normalized = values.map { |value| TaelgarNoteLint.normalize(value) }
      if normalized.include?("none") && normalized.length > 1
        add(findings, "campaign.audience_none_combined", "error", "required",
            "audience: none cannot be combined with other values.",
            line: note.field_line("audience"), provisional: true)
      end

      values.each_with_object([]) do |value, positives|
        raw = value.to_s.strip
        normalized_value = TaelgarNoteLint.normalize(raw)
        next if %w[all none].include?(normalized_value)

        negated = raw.start_with?("!")
        campaign_value = negated ? raw[1..-1] : raw
        resolved = @registry.resolve(campaign_value)
        if resolved.nil?
          add(findings, "campaign.audience_unknown_code", "error", "required",
              "audience contains an unknown campaign value: #{raw}.",
              line: note.field_line("audience"), provisional: true)
        else
          canonical = negated ? "!#{resolved}" : resolved
          if raw != canonical
            add(findings, "campaign.audience_noncanonical_code", "suggestion", "recommended",
                "audience value #{raw} resolves to #{canonical}; use the canonical lowercase code.",
                line: note.field_line("audience"), provisional: true)
          end
          positives << resolved unless negated
        end
      end.tap do |positives|
        positives << "all" if normalized.include?("all")
      end.uniq
    end

    def validate_dm_metadata(note, findings)
      if note.data.key?("dm_owner") && !DM_OWNERS.include?(note.data["dm_owner"].to_s)
        add(findings, "dm.owner_unknown", "error", "required",
            "Unknown dm_owner value: #{note.data['dm_owner']}.", line: note.field_line("dm_owner"))
      end
      if note.data.key?("dm_notes") && !DM_NOTES.include?(note.data["dm_notes"].to_s)
        add(findings, "dm.notes_unknown", "error", "required",
            "Unknown dm_notes value: #{note.data['dm_notes']}.", line: note.field_line("dm_notes"))
      end

      owner = note.data["dm_owner"].to_s
      return unless %w[tim joint none].include?(owner) && @dm_scanner

      sources = @dm_scanner.mentions(note)
      dm_notes = note.data["dm_notes"].to_s
      if sources.any?
        if dm_notes.empty? || dm_notes == "none"
          add(findings, "dm.notes_private_evidence_suspect", "warning", "conditional",
              "Local-only _DM_ notes link or could link to this subject; review whether dm_notes: none is still accurate.",
              line: note.field_line("dm_notes") || note.field_line("dm_owner"), provisional: true,
              details: { "sources" => sources })
        else
          add(findings, "dm.notes_private_evidence_found", "info", "judgment",
              "Local-only _DM_ notes support reviewing the current dm_notes attestation.",
              line: note.field_line("dm_notes"), provisional: true,
              details: { "sources" => sources })
        end
      elsif %w[color important].include?(dm_notes)
        add(findings, "dm.notes_no_local_evidence", "suggestion", "judgment",
            "No local-only _DM_ note links or could link to this subject. Consider removing dm_notes, but retain it if it represents unrecorded knowledge or another off-vault source.",
            line: note.field_line("dm_notes"), provisional: true)
      end
    end

    def validate_content_blocks(note, findings)
      masked = TaelgarNoteLint.mask_markdown_code(note.text)
      validate_lint_report_state(note, findings, masked)
      text = text_without_lint_payload(masked)
      if text.include?("%%SECRET")
        add(findings, "privacy.secret_block", "info", "required",
            "A valid local-only SECRET block is present; its contents must remain excluded from GitHub and public artifacts.",
            line: TaelgarNoteLint.line_number(text, text.index("%%SECRET")), provisional: true)
      end

      shared_comment = nil
      text.to_enum(:scan, /%%(.*?)%%/m).each do
        match = Regexp.last_match
        content = match[1].strip
        next if content.start_with?("^") || content.start_with?("SECRET")

        shared_comment = match
        break
      end
      if shared_comment
        add(findings, "privacy.shared_comment", "info", "required",
            "A Git-shared, nonpublic Obsidian comment is present; it does not imply a dm_notes value.",
            line: TaelgarNoteLint.line_number(text, shared_comment.begin(0)), provisional: true)
      end

      if text.scan("%%").length.odd?
        add(findings, "syntax.unbalanced_comment", "error", "required",
            "Obsidian comment delimiters are unbalanced.", line: 1)
      end

      stack = []
      marker_pattern = /%%\^([A-Za-z]+)(?::([^%]+))?%%/
      text.to_enum(:scan, marker_pattern).each do
        match = Regexp.last_match
        line = TaelgarNoteLint.line_number(text, match.begin(0))
        kind = match[1]
        value = match[2].to_s.strip
        if kind == "End"
          if stack.empty?
            add(findings, "syntax.orphan_block_end", "error", "required",
                "Content-block end marker has no matching opener.", line: line)
          else
            stack.pop
          end
          next
        end

        stack << [kind, value, line]
        unless %w[Campaign Date Lint Metadata].include?(kind)
          add(findings, "syntax.unknown_content_marker", "error", "required",
              "Unknown structured content marker: #{kind}.", line: line)
        end
        if kind == "Campaign"
          if value.casecmp("none").zero?
            if value != "none"
              add(findings, "syntax.noncanonical_campaign_block", "suggestion", "recommended",
                  "Campaign:none is the canonical private-block sentinel.", line: line,
                  provisional: true)
            end
          else
            resolved = @registry.resolve(value)
            if resolved.nil?
              add(findings, "syntax.unknown_campaign_block", "error", "required",
                  "Campaign block uses unknown campaign value: #{value}.", line: line)
            elsif value != resolved
              add(findings, "syntax.noncanonical_campaign_block", "suggestion", "recommended",
                  "Campaign block value #{value} resolves to #{resolved}; use the canonical code.",
                  line: line, provisional: true)
            end
          end
        elsif kind == "Date" && !value.match?(/\A\d{4}(?:-\d{2}(?:-\d{2})?)?a?\z/)
          add(findings, "syntax.invalid_date_block", "error", "required",
              "Date block value is not in an accepted Taelgar date form: #{value}.", line: line)
        elsif kind == "Lint" && !value.empty?
          add(findings, "syntax.invalid_lint_marker", "error", "required",
              "The Lint marker does not take a value.", line: line)
        elsif kind == "Metadata" && !value.match?(/\A(?:names|map|article)(?::v1)?\z/)
          add(findings, "syntax.unknown_metadata_block", "error", "required",
              "Unknown Metadata block type: #{value}.", line: line)
        end
      end
      stack.each do |kind, value, line|
        add(findings, "syntax.unclosed_content_block", "error", "required",
            "#{kind}:#{value} block has no matching End marker.", line: line)
      end

      pov = text.match(/\(POV::\s*[^)]+\)/)
      if pov
        add(findings, "temporal.inline_pov", "info", "judgment",
            "A legacy note-level POV comment is present; preserve its meaning in Metadata:article before removing it.",
            line: TaelgarNoteLint.line_number(text, pov.begin(0)), provisional: true)
      end

      validate_metadata_blocks(note, findings)
      validate_meta_comment_positions(note, findings)
    end

    def validate_lint_report_state(note, findings, searchable)
      lint_match = searchable.match(LINT_BLOCK_PATTERN)
      lint_tagged = note.tags.include?("status/check/lint")

      if lint_match && !lint_tagged
        add(findings, "lint.report_without_status", "error", "required",
            "A Lint block with open work requires status/check/lint.",
            line: TaelgarNoteLint.line_number(searchable, lint_match.begin(0)))
      elsif lint_tagged && !lint_match
        add(findings, "lint.status_without_report", "error", "required",
            "status/check/lint requires a Lint block with at least one open finding.",
            line: note.field_line("tags") || 1)
      end

      return unless lint_match
      return if lint_match[1].match?(/^\s*-\s+\[ \]\s+/)

      add(findings, "lint.report_without_open_findings", "error", "required",
          "A Lint block must contain at least one unchecked error, warning, or suggestion; remove the block and status/check/lint after a clean lint.",
          line: TaelgarNoteLint.line_number(searchable, lint_match.begin(0)))
    end

    def validate_metadata_blocks(note, findings)
      blocks = Hash.new { |hash, key| hash[key] = [] }
      searchable = text_without_lint_payload(TaelgarNoteLint.mask_markdown_code(note.text))
      searchable.to_enum(:scan, METADATA_BLOCK_PATTERN).each do
        match = Regexp.last_match
        blocks[match[1]] << [
          match[3],
          TaelgarNoteLint.line_number(searchable, match.begin(0)),
          match[2],
          match.begin(0),
          match.end(0)
        ]
      end

      blocks.each do |kind, entries|
        if entries.length > 1
          add(findings, "metadata.duplicate_#{kind}_block", "error", "required",
              "Only one Metadata:#{kind} block is allowed.", line: entries[1][1])
        end
        payload, line, version, _start_offset, _end_offset = entries.first
        if version != "1"
          rule = version.nil? ? "metadata.legacy_#{kind}_marker" : "metadata.invalid_#{kind}_version"
          severity = version.nil? ? "suggestion" : "error"
          add(findings, rule, severity, version.nil? ? "recommended" : "required",
              version.nil? ? "Move the metadata version into the opener: %%^Metadata:#{kind}:v1%%." :
                             "Metadata:#{kind} uses unsupported schema version v#{version}.",
              line: line, provisional: version.nil?)
        end
        begin
          data = TaelgarNoteLint.yaml_load(payload)
        rescue Psych::Exception => error
          add(findings, "metadata.invalid_#{kind}_yaml", "error", "required",
              "Metadata:#{kind} block is not valid YAML: #{error.message.lines.first.to_s.strip}",
              line: line)
          next
        end
        if version.nil?
          data = convert_legacy_metadata(kind, data)
        end
        case kind
        when "names" then validate_name_block(data, findings, line)
        when "map" then validate_map_block(data, findings, line)
        when "article" then validate_article_block(data, findings, line)
        end
      end

      if note.data["lintedAt"] && blocks["article"].empty?
        add(findings, "metadata.article_missing", "error", "required",
            "Linted notes require a persistent Metadata:article:v1 block.", line: 1)
      end

      if map_required?(note) && blocks["map"].empty?
        add(findings, "metadata.map_missing", "error", "required",
            "Waterways, roads, and settlements require a Metadata:map:v1 block.",
            line: note.field_line("typeOf") || 1)
      end


      validate_metadata_block_positions(searchable, blocks, findings)
    end

    def validate_metadata_block_positions(searchable, blocks, findings)
      entries = blocks.values.flatten(1)
      return if entries.empty?

      first_start = entries.map { |entry| entry[3] }.min
      last_end = entries.map { |entry| entry[4] }.max
      lint_match = searchable.match(LINT_BLOCK_PATTERN)
      residue = searchable[first_start..-1].to_s
        .gsub(METADATA_BLOCK_PATTERN, "")
        .gsub(LINT_BLOCK_PATTERN, "")
        .strip
      misplaced = !residue.empty? || (lint_match && lint_match.begin(0) < last_end)
      return unless misplaced

      add(findings, "metadata.position", "error", "required",
          "Persistent Metadata blocks belong at the end of the note after article text and comments, immediately before the Lint block when present.",
          line: TaelgarNoteLint.line_number(searchable, first_start))
    end

    def validate_name_block(data, findings, line)
      unless data.is_a?(Array) && !data.empty? && data.all? { |entry| entry.is_a?(Hash) }
        add(findings, "metadata.names_shape", "error", "required",
            "Metadata:names:v1 requires a nonempty YAML list of dictionaries.", line: line)
        return
      end

      data.each do |entry|
        missing = %w[name language].select { |field| entry[field].to_s.strip.empty? }
        unless missing.empty?
          add(findings, "metadata.names_required_field", "error", "required",
              "A name entry is missing: #{missing.join(', ')}.", line: line)
        end
        status = entry["status"].to_s
        next if status.empty? || NAME_STATUSES.include?(status)

        add(findings, "metadata.names_status", "error", "required",
            "Unknown name status: #{status}.", line: line,
            details: { "allowed" => NAME_STATUSES })
      end
    end

    def valid_name_block_present?(note)
      data = name_block_data(note)
      data.is_a?(Array) && !data.empty? &&
        data.all? do |entry|
          entry.is_a?(Hash) && %w[name language].all? { |field| !entry[field].to_s.strip.empty? }
        end
    rescue Psych::Exception
      false
    end

    def accepted_pronunciation_exception?(note)
      data = name_block_data(note)
      return false unless data.is_a?(Array)

      primary = data.find { |entry| entry.is_a?(Hash) && entry["role"].to_s == "primary" } || data.first
      return false unless primary

      pronunciation = primary["pronunciation"].to_s
      PRONUNCIATION_EXCEPTIONS.include?(pronunciation) || pronunciation.start_with?("inherited")
    end

    def name_block_data(note)
      searchable = text_without_lint_payload(TaelgarNoteLint.mask_markdown_code(note.text))
      match = searchable.match(/%%\^Metadata:names:v1%%\s*(.*?)\s*%%\^End%%/m)
      return nil unless match

      TaelgarNoteLint.yaml_load(match[1])
    rescue Psych::Exception
      nil
    end

    def validate_map_block(data, findings, line)
      unless data.is_a?(Hash)
        add(findings, "metadata.map_shape", "error", "required",
            "Metadata:map:v1 requires a YAML dictionary.", line: line)
        return
      end

      locations = data["locations"]
      unless locations.is_a?(Array) && locations.all? { |entry| entry.is_a?(Hash) }
        add(findings, "metadata.map_shape", "error", "required",
            "Metadata:map:v1 requires a locations list of dictionaries.", line: line)
        return
      end

      if locations.empty? && data["status"].to_s != "missing"
        add(findings, "metadata.map_empty_without_status", "error", "required",
            "An empty map locations list requires status: missing.", line: line)
      elsif locations.empty?
        add(findings, "metadata.map_location_missing", "warning", "conditional",
            "Required map coverage is explicitly missing and needs human completion.",
            line: line, provisional: true)
      end

      locations.each do |entry|
        if entry["geometry"].to_s.strip.empty?
          add(findings, "metadata.map_geometry_missing", "error", "required",
              "Each map location requires geometry.", line: line)
        end
        world_locator = entry.any? do |key, value|
          %w[hex locator sourceHex outletHex].include?(key.to_s) && value.to_s.match?(WORLD_HEX_PATTERN)
        end
        if world_locator && entry["map"].to_s != "world"
          add(findings, "metadata.map_world_hex_mismatch", "error", "required",
              "A 13.07.F16-style locator always belongs to map: world.", line: line)
        end
      end
    end

    def validate_article_block(data, findings, line)
      unless data.is_a?(Hash)
        add(findings, "metadata.article_shape", "error", "required",
            "Metadata:article:v1 requires a YAML dictionary.", line: line)
        return
      end

      missing = %w[mode pov povNotes].select { |field| data[field].to_s.strip.empty? }
      unless missing.empty?
        add(findings, "metadata.article_required_field", "error", "required",
            "Metadata:article:v1 is missing: #{missing.join(', ')}.", line: line)
      end
      if data.key?("profile")
        add(findings, "metadata.article_redundant_profile", "suggestion", "recommended",
            "Article profile repeats the descriptive frontmatter tag; remove profile and use povNotes for useful interpretive context.",
            line: line, provisional: true)
      end
    end

    def convert_legacy_metadata(kind, data)
      return data unless data.is_a?(Hash) && data["version"] == 1

      case kind
      when "names"
        Array(data["names"]).map do |entry|
          next entry unless entry.is_a?(Hash)

          converted = { "name" => entry["form"], "language" => entry["language"] }
          converted["role"] = entry["role"] if entry["role"]
          converted["pronunciation"] = entry["pronunciation"] if entry["pronunciation"]
          status = entry["pronunciationStatus"].to_s
          converted["pronunciation"] = status.sub("exception-", "") if status.start_with?("exception-")
          converted.compact
        end
      when "map"
        data.reject { |key, _value| key.to_s == "version" }
      else
        data
      end
    end

    def map_required?(note)
      note.tags.include?("place") && MAP_REQUIRED_TYPES.include?(note.data["typeOf"].to_s)
    end

    def validate_meta_comment_positions(note, findings)
      body = TaelgarNoteLint.mask_markdown_code(note.body)
      header_end = header_block_end(body)
      return unless header_end

      prefix = body[0...header_end].gsub(METADATA_BLOCK_PATTERN, "")
      prefix.to_enum(:scan, /%%(?!\^)(.*?)%%/m).each do
        match = Regexp.last_match
        add(findings, "comment.before_header", "suggestion", "recommended",
            "Comments belong below the title and its immediately following information/header callout.",
            line: note.body_start_line + body[0...match.begin(0)].count("\n"), provisional: true)
      end
    end

    def header_block_end(body)
      title = body.match(/^#\s+.*(?:\n|\z)/)
      return nil unless title

      offset = title.end(0)
      lines = body[offset..-1].to_s.lines
      index = 0
      index += 1 while index < lines.length && lines[index].strip.empty?
      if index < lines.length && lines[index].lstrip.start_with?(">")
        index += 1 while index < lines.length && lines[index].lstrip.start_with?(">")
        index += 1 while index < lines.length && lines[index].strip.empty?
      end
      offset + lines[0...index].join.length
    end

    def validate_editorial_mechanics(note, findings)
      visible_lines(note).each do |line_number, line|
        repeated = line.match(/\b([A-Za-z][A-Za-z'-]*)\s+\1\b/i)
        link_repeated = line.match(/\[\[([^\]|]+)(?:\|([^\]]+))?\]\]\s+([A-Za-z][A-Za-z'-]*)/)
        if !repeated && link_repeated
          displayed = (link_repeated[2] || Pathname.new(link_repeated[1]).basename.to_s).split.last.to_s
          repeated = link_repeated if displayed.casecmp(link_repeated[3]).zero?
        end
        if repeated
          word = link_repeated && repeated == link_repeated ? link_repeated[3] : repeated[1]
          add(findings, "editorial.repeated_word", "suggestion", "recommended",
              "Repeated word: #{word} #{word}.", line: line_number)
        end
        EDITORIAL_PATTERNS.each do |pattern, replacement|
          match = line.match(pattern)
          next unless match

          add(findings, "editorial.common_typo", "suggestion", "recommended",
              "Possible mechanical prose error '#{match[0]}'; consider '#{replacement}'.",
              line: line_number)
        end
      end
    end

    def validate_links(note, findings)
      searchable = text_without_review_blocks(TaelgarNoteLint.mask_markdown_code(note.text))
      searchable.to_enum(:scan, /(?<!!)\[\[([^\]\n]+)\]\]/).each do
        match = Regexp.last_match
        raw = match[1]
        candidates = @index.resolve(raw, note.path)
        line = TaelgarNoteLint.line_number(note.text, match.begin(0))
        if candidates.empty?
          add(findings, "link.unresolved", "error", "required",
              "Unresolved wikilink: [[#{raw}]].", line: line)
        elsif candidates.length > 1
          add(findings, "link.ambiguous", "warning", "required",
              "Ambiguous wikilink: [[#{raw}]].", line: line,
              details: { "candidates" => candidates })
        end
      end
    end

    def validate_relationships(note, findings)
      relationships = []
      whereabouts = note.data["whereabouts"]
      if whereabouts.is_a?(String)
        relationships << ["whereabouts", whereabouts, note.field_line("whereabouts")]
      elsif whereabouts.is_a?(Array)
        whereabouts.each do |entry|
          relationships << ["whereabouts", entry["location"], note.field_line("whereabouts")] if entry.is_a?(Hash)
        end
      elsif whereabouts
        add(findings, "relationship.whereabouts_shape", "error", "required",
            "whereabouts must be a string or list of dictionaries.", line: note.field_line("whereabouts"))
      end

      affiliations = note.data["affiliations"]
      if affiliations.is_a?(Array)
        affiliations.each do |entry|
          relationships << ["affiliations", entry["org"], note.field_line("affiliations")] if entry.is_a?(Hash)
        end
      elsif affiliations
        add(findings, "relationship.affiliations_shape", "error", "required",
            "affiliations must be a list of dictionaries.", line: note.field_line("affiliations"))
      end

      %w[partOf pcOwner].each do |field|
        value = note.data[field]
        string_list(value).each { |entry| relationships << [field, entry, note.field_line(field)] }
      end

      relationships.each do |field, target, line|
        next if target.to_s.strip.empty? || TaelgarNoteLint.normalize(target) == "none"

        candidates = @index.resolve(target.to_s, note.path)
        if candidates.empty?
          add(findings, "relationship.unresolved", "warning", "required",
              "#{field} target does not resolve: #{target}.", line: line,
              details: { "field" => field, "target" => target })
        elsif candidates.length > 1
          add(findings, "relationship.ambiguous", "warning", "required",
              "#{field} target is ambiguous: #{target}.", line: line,
              details: { "field" => field, "target" => target, "candidates" => candidates })
        end
      end
    end

    def generic_comment_segments(text)
      text.scan(/%%(.*?)%%/m).map(&:first).reject do |segment|
        segment.strip.match?(/\A(?:SECRET|\^(?:Campaign|Date|Lint|Metadata|End)(?::|\z))/)
      end
    end

    def visible_lines(note)
      result = []
      in_comment = false
      in_fence = false
      in_hidden_structured_block = false
      note.body.lines.each_with_index do |original, index|
        line_number = note.body_start_line + index
        if in_hidden_structured_block
          in_hidden_structured_block = false if structured_block_end?(original)
          next
        end
        if hidden_structured_block_start?(original)
          in_hidden_structured_block = true
          next
        end
        if original.match?(/^\s*(```|~~~)/)
          in_fence = !in_fence
          next
        end
        next if in_fence

        visible = +""
        position = 0
        while (marker = original.index("%%", position))
          visible << original[position...marker] unless in_comment
          in_comment = !in_comment
          position = marker + 2
        end
        visible << original[position..-1].to_s unless in_comment
        result << [line_number, visible] unless visible.strip.empty?
      end
      result
    end

    def text_without_review_blocks(text)
      hidden = false
      text.lines.map do |line|
        if hidden
          hidden = false if structured_block_end?(line)
          line.end_with?("\n") ? "\n" : ""
        elsif review_block_start?(line)
          hidden = true
          line.end_with?("\n") ? "\n" : ""
        else
          line
        end
      end.join
    end

    def text_without_lint_payload(text)
      hidden = false
      text.lines.map do |line|
        if hidden
          if structured_block_end?(line)
            hidden = false
            line
          else
            line.end_with?("\n") ? "\n" : ""
          end
        elsif line.match?(/^\s*%%\^Lint%%\s*$/)
          hidden = true
          line
        else
          line
        end
      end.join
    end

    def hidden_structured_block_start?(line)
      line.match?(/^\s*%%\^(?:Lint|Metadata(?::[^%]+)?|Campaign:none)%%\s*$/)
    end

    def review_block_start?(line)
      line.match?(/^\s*%%\^(?:Lint|Metadata(?::[^%]+)?)%%\s*$/)
    end

    def structured_block_end?(line)
      line.match?(/^\s*%%\^End%%\s*$/)
    end

    def string_list(value)
      case value
      when nil then []
      when Array then value.map(&:to_s).map(&:strip).reject(&:empty?)
      else [value.to_s.strip].reject(&:empty?)
      end
    end

    def finding_sort_key(finding)
      severity = { "error" => 0, "warning" => 1, "suggestion" => 2, "info" => 3 }
      [severity.fetch(finding["severity"], 9), finding["line"] || 0, finding["ruleId"]]
    end

    def summarize(findings)
      counts = Hash.new(0)
      findings.each { |finding| counts[finding["severity"]] += 1 }
      {
        "errors" => counts["error"],
        "warnings" => counts["warning"],
        "suggestions" => counts["suggestion"],
        "info" => counts["info"]
      }
    end
  end

  class FreshnessScanner
    def initialize(root:, index:, baseline_ref: nil, linted_at: nil)
      @root = Pathname.new(root).expand_path
      @index = index
      @baseline_ref = baseline_ref || resolve_time_ref(linted_at)
    end

    def scan(note_report)
      return { "baselineRef" => nil, "candidates" => [], "skipped" => "No Git baseline supplied." } unless @baseline_ref

      target_path = note_report.fetch("note").fetch("path")
      target_names = target_identity_names(target_path)
      target_plain_names = target_primary_names(target_path)
      candidates = changed_paths.each_with_object([]) do |path, selected|
        next if path == target_path
        next unless invention_source?(path)

        absolute = @root.join(path)
        next unless absolute.file?

        source_mentions = mention_lines(
          path,
          TaelgarNoteLint.read_text(absolute),
          target_path,
          target_names,
          target_plain_names
        )
        next if source_mentions.empty?

        selected << build_candidate(path, source_mentions, target_path, target_names, target_plain_names)
      end

      candidates.sort_by! do |candidate|
        [SOURCE_PRIORITIES.fetch(candidate["sourceKind"], 9), candidate["path"]]
      end
      { "baselineRef" => @baseline_ref, "candidates" => candidates }
    end

    private

    def resolve_time_ref(linted_at)
      return nil unless linted_at

      output = git("rev-list", "-1", "--before=#{linted_at}", "HEAD")
      value = output.strip
      value.empty? ? nil : value
    end

    def changed_paths
      output = git("diff", "--name-only", "-z", @baseline_ref, "--")
      output.split("\0").reject(&:empty?)
    end

    def invention_source?(path)
      parts = Pathname.new(path).each_filename.to_a
      return false if parts.include?("_generated")
      return path.end_with?("beat-facts.json") if parts.first == "_sessions"
      return false if %w[.agents .codex .git .obsidian .trash _MoC _scripts _sessions _templates z_Assets].include?(parts.first)

      path.end_with?(".md") && File.basename(path) != "AGENTS.md"
    end

    def target_identity_names(path)
      parsed = ParsedNote.new(path, TaelgarNoteLint.read_text(@root.join(path)))
      parsed.identity_names
    end

    def target_primary_names(path)
      parsed = ParsedNote.new(path, TaelgarNoteLint.read_text(@root.join(path)))
      [Pathname.new(path).basename(".md").to_s, parsed.data["name"]]
        .map(&:to_s).map(&:strip).reject(&:empty?).uniq
    end

    def mention_lines(path, text, target_path, target_names, target_plain_names)
      if path.end_with?("beat-facts.json")
        lowered = target_names.map { |name| TaelgarNoteLint.normalize(name) }
        return text.lines.each_with_index.each_with_object([]) do |(line, index), lines|
          normalized_line = TaelgarNoteLint.normalize(line)
          lines << index + 1 if lowered.any? { |name| normalized_line.include?(name) }
        end
      end

      text.lines.each_with_index.each_with_object([]) do |(line, index), lines|
        links_target = line.scan(/(?<!!)\[\[([^\]\n]+)\]\]/).flatten.any? do |raw|
          @index.resolve(raw, path).include?(target_path)
        end
        names_target = target_plain_names.any? { |name| exact_name_match?(line, name) }
        lines << index + 1 if links_target || names_target
      end
    end

    def exact_name_match?(text, name)
      return false unless distinctive_plain_name?(name)

      pattern = /(?<![[:alnum:]_])#{Regexp.escape(name)}(?![[:alnum:]_])/
      text.match?(pattern)
    end

    def distinctive_plain_name?(name)
      name.length >= 7 || name.match?(/[\s'’\-]/)
    end

    def build_candidate(path, mentions, target_path, target_names, target_plain_names)
      additions, deletions = numstat(path)
      diff = git("diff", "--unified=0", @baseline_ref, "--", path)
      added_lines = diff.lines.select { |line| line.start_with?("+") && !line.start_with?("+++") }
      mention_changed = if path.end_with?("beat-facts.json")
                          lowered = target_names.map { |name| TaelgarNoteLint.normalize(name) }
                          added_lines.any? do |line|
                            normalized_line = TaelgarNoteLint.normalize(line)
                            lowered.any? { |name| normalized_line.include?(name) }
                          end
                        else
                          added_lines.any? do |line|
                            links_target = line.scan(/(?<!!)\[\[([^\]\n]+)\]\]/).flatten.any? do |raw|
                              @index.resolve(raw, path).include?(target_path)
                            end
                            links_target || target_plain_names.any? { |name| exact_name_match?(line, name) }
                          end
                        end

      log = git("log", "-1", "--format=%H%x09%cI%x09%s", "--", path).strip.split("\t", 3)
      {
        "path" => path,
        "sourceKind" => source_kind(path),
        "mentionLines" => mentions,
        "mentionChanged" => mention_changed,
        "changedLines" => { "added" => additions, "deleted" => deletions },
        "lastCommit" => log[0],
        "lastCommitAt" => log[1],
        "lastCommitSubject" => log[2]
      }
    end

    def numstat(path)
      fields = git("diff", "--numstat", @baseline_ref, "--", path).strip.split(/\s+/, 3)
      [integer_or_zero(fields[0]), integer_or_zero(fields[1])]
    end

    def integer_or_zero(value)
      Integer(value || 0)
    rescue ArgumentError
      0
    end

    def source_kind(path)
      parts = Pathname.new(path).each_filename.to_a
      return "beat-facts" if path.end_with?("beat-facts.json")
      return "dm-note" if %w[_DM_ _dm_notes].include?(parts.first)
      return "session-note" if parts.include?("Session Notes") || parts.include?("Sessions")
      return "campaign-note" if parts.first == "Campaigns"
      return "development-note" if parts.first == "Worldbuilding"

      "vault-note"
    end

    def git(*arguments)
      stdout, stderr, status = Open3.capture3("git", *arguments, chdir: @root.to_s)
      stdout = stdout.force_encoding(Encoding::UTF_8).scrub
      stderr = stderr.force_encoding(Encoding::UTF_8).scrub
      raise "Git command failed: #{stderr.strip}" unless status.success?

      stdout
    end
  end

  class CLI
    def initialize(argv)
      @argv = argv
      @options = {
        root: Pathname.pwd,
        format: "markdown",
        check_links: true,
        fix_frontmatter: false,
        baseline_ref: nil,
        linted_at: nil
      }
    end

    def run
      parser.parse!(@argv)
      if @argv.empty?
        warn parser
        return 2
      end

      root = Pathname.new(@options[:root]).expand_path
      fixes = @argv.each_with_object({}) do |path, memo|
        next unless @options[:fix_frontmatter]

        absolute = Pathname.new(path)
        absolute = root.join(absolute) unless absolute.absolute?
        text = TaelgarNoteLint.read_text(absolute)
        formatted = FrontmatterFormatter.new(ParsedNote.new(path, text)).format_text
        next if formatted == text

        File.write(absolute, formatted)
        memo[TaelgarNoteLint.relative_path(root, absolute)] = ["Normalized frontmatter order and collection formatting."]
      rescue FrontmatterFormatter::UnsafeFrontmatter
        next
      end
      index = @options[:check_links] || @options[:baseline_ref] || @options[:linted_at] ? NoteIndex.new(root) : nil
      validator = Validator.new(root: root, check_links: @options[:check_links], index: index)
      reports = @argv.map { |path| validator.validate_path(path) }
      reports.each { |report| report["fixes"] = fixes.fetch(report.dig("note", "path"), []) }

      if @options[:baseline_ref] || @options[:linted_at]
        scanner = FreshnessScanner.new(
          root: root,
          index: index,
          baseline_ref: @options[:baseline_ref],
          linted_at: @options[:linted_at]
        )
        reports.each { |report| report["freshness"] = scanner.scan(report) }
      end

      puts @options[:format] == "json" ? JSON.pretty_generate(reports) : markdown(reports)
      reports.any? { |report| report["summary"]["errors"].positive? } ? 1 : 0
    rescue OptionParser::ParseError, Errno::ENOENT, ArgumentError, RuntimeError => error
      warn error.message
      2
    end

    private

    def parser
      @parser ||= OptionParser.new do |options|
        options.banner = "Usage: validate_taelgar_note.rb [options] NOTE [NOTE ...]"
        options.on("--root PATH", "Vault root (default: current directory)") { |value| @options[:root] = value }
        options.on("--format FORMAT", %w[markdown json], "markdown or json") { |value| @options[:format] = value }
        options.on("--fix-frontmatter", "Rewrite safe frontmatter into canonical 2.1 form") { @options[:fix_frontmatter] = true }
        options.on("--since-ref REF", "Git commit/ref used as the freshness baseline") { |value| @options[:baseline_ref] = value }
        options.on("--linted-at TIME", "Resolve the last commit at or before this lint timestamp") { |value| @options[:linted_at] = value }
        options.on("--no-links", "Skip link and relationship resolution") { @options[:check_links] = false }
        options.on("-h", "--help", "Show this help") do
          puts options
          exit 0
        end
      end
    end

    def markdown(reports)
      lines = []
      reports.each do |report|
        note = report["note"]
        summary = report["summary"]
        lines << "# Deterministic lint: #{note['name']}"
        lines << ""
        lines << "- Path: `#{note['path']}`"
        lines << "- Profile: `#{note['profile'] || 'unresolved'}`"
        lines << "- Authority: `#{note['authority']}`"
        lines << "- Existing status: #{note['statuses'].empty? ? 'none' : note['statuses'].map { |tag| "`#{tag}`" }.join(', ')}"
        lines << "- Findings: #{summary['errors']} errors, #{summary['warnings']} warnings, #{summary['suggestions']} suggestions, #{summary['info']} informational"
        lines << ""
        unless report["fixes"].empty?
          lines << "## Applied deterministic fixes"
          lines << ""
          report["fixes"].each { |fix| lines << "- #{fix}" }
          lines << ""
        end
        lines << "## Findings"
        lines << ""
        if report["findings"].empty?
          lines << "No deterministic findings."
        else
          report["findings"].each do |finding|
            location = finding["line"] ? " (line #{finding['line']})" : ""
            provisional = finding["provisional"] ? " [provisional]" : ""
            lines << "- **#{finding['severity']}** `#{finding['ruleId']}`#{location}#{provisional}: #{finding['message']}"
            Array(finding.dig("details", "sources")).each do |source|
              source_lines = Array(source["lines"])
              location_text = source_lines.empty? ? "" : " (lines #{source_lines.join(', ')})"
              lines << "  - `#{source['path']}`#{location_text}"
            end
          end
        end

        freshness = report["freshness"]
        if freshness
          lines << ""
          lines << "## Newer external-source candidates"
          lines << ""
          lines << "Baseline: `#{freshness['baselineRef'] || 'none'}`"
          candidates = freshness["candidates"]
          if candidates.empty?
            lines << ""
            lines << "No newer invention-bearing source currently links or names this note."
          else
            candidates.each do |candidate|
              changed = candidate["mentionChanged"] ? "mention changed" : "mention unchanged; source changed"
              lines << "- `#{candidate['path']}` (#{candidate['sourceKind']}; #{changed}; lines #{candidate['mentionLines'].join(', ')})"
            end
          end
        end
        lines << ""
      end
      lines.join("\n").rstrip
    end
  end
end

if $PROGRAM_NAME == __FILE__
  exit TaelgarNoteLint::CLI.new(ARGV).run
end
