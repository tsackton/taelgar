#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"
require "optparse"
require "pathname"
require "yaml"

module TaelgarLintValues
  SCHEMA_VERSION = 1
  OUTPUT_PATH = "_scripts/taelgar_lint_values.json"

  VALUE_FIELDS = {
    "descriptiveTags" => ["_MoC/Note Categorization.md", "linterDescriptiveTags"],
    "campaignRecordTags" => ["_MoC/Note Categorization.md", "linterCampaignRecordTags"],
    "knownToRequiredTags" => ["_MoC/Note Categorization.md", "linterKnownToRequiredTags"],
    "nameStatuses" => ["_MoC/Name Metadata.md", "linterNameStatuses"],
    "openNameStatuses" => ["_MoC/Name Metadata.md", "linterOpenNameStatuses"],
    "commonNamedSubjectTags" => ["_MoC/Name Metadata.md", "linterCommonNamedSubjectTags"],
    "pronunciationPlaceholders" => ["_MoC/Name Metadata.md", "linterPronunciationPlaceholders"],
    "pronunciationPlaceholderPrefixes" => ["_MoC/Name Metadata.md", "linterPronunciationPlaceholderPrefixes"],
    "placeTypes" => ["_MoC/Data Categorization/Place Categories.md", "canonical"],
    "dmOwners" => ["_MoC/Note Status.md", "linterDmOwners"],
    "dmNotes" => ["_MoC/Note Status.md", "linterDmNotes"],
    "localDmReviewOwners" => ["_MoC/Note Status.md", "linterLocalDmReviewOwners"],
    "audienceSpecialValues" => ["_MoC/Campaign Registry.md", "linterAudienceSpecialValues"],
    "mapRequiredPlaceTypes" => ["_MoC/Note Categorization.md", "linterMapRequiredPlaceTypes"]
  }.freeze

  ALIAS_FIELDS = {
    "descriptiveTags" => ["_MoC/Note Categorization.md", "linterDescriptiveTagAliases"],
    "placeTypes" => ["_MoC/Data Categorization/Place Categories.md", "linterAliases"]
  }.freeze

  class Error < RuntimeError; end

  module_function

  def build(root)
    root = Pathname.new(root).expand_path
    source_texts = source_paths.to_h do |relative_path|
      path = root.join(relative_path)
      raise Error, "Lint value source is missing: #{relative_path}" unless path.file?

      [relative_path, path.read(encoding: "UTF-8")]
    end

    data = {
      "schemaVersion" => SCHEMA_VERSION,
      "sources" => source_texts.map do |relative_path, text|
        fields = source_fields.fetch(relative_path)
        {
          "path" => relative_path,
          "fields" => fields,
          "sha256" => declaration_digest(text, relative_path, fields)
        }
      end,
      "values" => VALUE_FIELDS.to_h do |key, (relative_path, field)|
        [key, parse_list(source_texts.fetch(relative_path), relative_path, field)]
      end,
      "aliases" => ALIAS_FIELDS.to_h do |key, (relative_path, field)|
        [key, parse_map(source_texts.fetch(relative_path), relative_path, field)]
      end,
      "provenance" => provenance
    }
    validate!(data)
    data
  end

  def source_paths
    (VALUE_FIELDS.values + ALIAS_FIELDS.values).map(&:first).uniq.sort
  end

  def source_fields
    fields = Hash.new { |hash, key| hash[key] = [] }
    (VALUE_FIELDS.values + ALIAS_FIELDS.values).each do |path, field|
      fields[path] << field
    end
    fields.transform_values { |items| items.uniq.sort }.sort.to_h
  end

  def provenance
    entries = {}
    VALUE_FIELDS.each do |key, (path, field)|
      entries["values.#{key}"] = { "path" => path, "field" => field }
    end
    ALIAS_FIELDS.each do |key, (path, field)|
      entries["aliases.#{key}"] = { "path" => path, "field" => field }
    end
    entries
  end

  def parse_list(text, path, field)
    raw = declaration(text, path, field)
    parsed = YAML.safe_load("[#{raw}]", permitted_classes: [], permitted_symbols: [], aliases: false)
    unless parsed.is_a?(Array) && !parsed.empty? && parsed.all? { |value| value.is_a?(String) && !value.strip.empty? }
      raise Error, "#{path} #{field} must be a nonempty comma-separated list of quoted strings."
    end

    parsed
  rescue Psych::Exception => error
    raise Error, "#{path} #{field} is not valid list data: #{error.message.lines.first.to_s.strip}"
  end

  def parse_map(text, path, field)
    raw = declaration(text, path, field)
    parsed = YAML.safe_load(raw, permitted_classes: [], permitted_symbols: [], aliases: false)
    unless parsed.is_a?(Hash) && parsed.all? do |key, value|
             key.is_a?(String) && !key.strip.empty? && value.is_a?(String) && !value.strip.empty?
           end
      raise Error, "#{path} #{field} must be a string-to-string mapping."
    end

    parsed
  rescue Psych::Exception => error
    raise Error, "#{path} #{field} is not valid mapping data: #{error.message.lines.first.to_s.strip}"
  end

  def declaration(text, path, field)
    matches = text.scan(/^#{Regexp.escape(field)}::[ \t]*(.*)$/)
    raise Error, "#{path} must contain exactly one #{field}:: declaration." unless matches.length == 1

    matches.first.first.strip
  end

  def declaration_digest(text, path, fields)
    declarations = fields.to_h { |field| [field, declaration(text, path, field)] }
    Digest::SHA256.hexdigest(JSON.generate(declarations))
  end

  def validate!(data)
    unless data.is_a?(Hash) && data["schemaVersion"] == SCHEMA_VERSION
      raise Error, "Lint value sidecar uses an unsupported schema."
    end

    values = data["values"]
    aliases = data["aliases"]
    unless values.is_a?(Hash) && aliases.is_a?(Hash)
      raise Error, "Lint value sidecar must contain values and aliases objects."
    end

    VALUE_FIELDS.each_key do |key|
      list = values[key]
      unless list.is_a?(Array) && !list.empty? && list.all? { |value| value.is_a?(String) && value == value.strip && !value.empty? }
        raise Error, "Lint value list #{key} must contain nonempty strings."
      end
      raise Error, "Lint value list #{key} contains duplicates." unless list.uniq.length == list.length
    end

    ALIAS_FIELDS.each_key do |key|
      mapping = aliases[key]
      unless mapping.is_a?(Hash) && mapping.all? { |source, target| source.is_a?(String) && target.is_a?(String) }
        raise Error, "Lint alias map #{key} must contain string pairs."
      end
      unless mapping.values.all? { |target| values.fetch(key).include?(target) }
        raise Error, "Lint alias map #{key} points to a value outside its accepted list."
      end
      if (mapping.keys & values.fetch(key)).any?
        raise Error, "Lint alias map #{key} repeats an already accepted value."
      end
    end

    require_subset!(values, "openNameStatuses", "nameStatuses")
    require_subset!(values, "commonNamedSubjectTags", "descriptiveTags")
    require_subset!(values, "campaignRecordTags", "descriptiveTags")
    require_subset!(values, "knownToRequiredTags", "descriptiveTags")
    require_subset!(values, "localDmReviewOwners", "dmOwners")
    require_subset!(values, "mapRequiredPlaceTypes", "placeTypes")

    sources = data["sources"]
    unless sources.is_a?(Array) && sources.all? { |entry| entry.is_a?(Hash) } &&
           sources.map { |entry| entry["path"] } == source_paths &&
           sources.all? do |entry|
             entry["fields"] == source_fields.fetch(entry["path"]) &&
               entry["sha256"].to_s.match?(/\A[0-9a-f]{64}\z/)
           end
      raise Error, "Lint value sidecar source records are incomplete or unordered."
    end
    true
  end

  def require_subset!(values, subset_key, superset_key)
    extras = values.fetch(subset_key) - values.fetch(superset_key)
    return if extras.empty?

    raise Error, "#{subset_key} contains values absent from #{superset_key}: #{extras.join(', ')}"
  end

  def read(root)
    path = Pathname.new(root).expand_path.join(OUTPUT_PATH)
    data = JSON.parse(path.read(encoding: "UTF-8"))
    validate!(data)
    data
  rescue JSON::ParserError => error
    raise Error, "#{OUTPUT_PATH} is not valid JSON: #{error.message}"
  end

  class CLI
    def initialize(argv)
      @argv = argv
    end

    def run
      options = { root: Pathname.pwd, write: false }
      parser = OptionParser.new do |opts|
        opts.banner = "Usage: generate_taelgar_lint_values.rb [--check|--write] [options]"
        opts.on("--root PATH", "Vault root") { |value| options[:root] = Pathname.new(value) }
        opts.on("--check", "Verify the generated sidecar") { options[:write] = false }
        opts.on("--write", "Regenerate the JSON sidecar") { options[:write] = true }
      end
      parser.parse!(@argv)
      root = options.fetch(:root).expand_path
      expected = TaelgarLintValues.build(root)
      output = root.join(OUTPUT_PATH)

      if options[:write]
        output.write("#{JSON.pretty_generate(expected)}\n", mode: "w", encoding: "UTF-8")
      else
        actual = TaelgarLintValues.read(root)
        raise Error, "#{OUTPUT_PATH} is stale; run with --write." unless actual == expected
      end
      0
    rescue OptionParser::ParseError, Error, Errno::ENOENT => error
      warn error.message
      2
    end
  end
end

exit TaelgarLintValues::CLI.new(ARGV).run if $PROGRAM_NAME == __FILE__
