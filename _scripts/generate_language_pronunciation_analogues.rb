#!/usr/bin/env ruby
# frozen_string_literal: true

require "date"
require "digest"
require "json"
require "optparse"
require "pathname"
require "yaml"

module TaelgarLanguagePronunciationAnalogues
  SOURCE_PATH = "Background/Languages.md"
  OUTPUT_PATH = "_scripts/language_pronunciation_analogues.json"
  SCHEMA_VERSION = 2
  AUDIT_SCHEMA_VERSION = 1
  MAPPING_STATUSES = %w[defined provisional undetermined].freeze
  AUDIT_IGNORED_VALUES = %w[unknown].freeze

  LANGUAGE_NAME_OVERRIDES = {
    "Illoria" => "Illorian"
  }.freeze
  FAMILY_NAME_OVERRIDES = {
    "Drankorian Language Family" => "Drankorian",
    "Northros Language Family" => "Northros",
    "Eastros Language Family" => "Eastros"
  }.freeze
  FAMILY_LOOKUP_TERM_OVERRIDES = {
    "Drankorian" => ["Drankorian Language Family"],
    "Northros" => ["Northros", "Northos", "Northros Language Family"],
    "Eastros" => ["Eastros Language Family"]
  }.freeze
  PARENT_LANGUAGE_OVERRIDES = {
    "Free Orcish" => "Orcish"
  }.freeze
  LOOKUP_TERM_OVERRIDES = {
    "Common" => %w[Common],
    "Eastros" => %w[Eastros],
    "Drankorian" => %w[Drankorian Drankor],
    "Cymean" => %w[Cymean Cymea],
    "Isinguese" => %w[Isinguese Isingue],
    "Chardonian" => %w[Chardonian Chardonians Chardon],
    "Illorian" => %w[Illorian Illoria],
    "Old Northros" => ["Old Northros"],
    "Old Zimkovan" => ["Old Zimkovan"],
    "Mawaran" => %w[Mawaran Mawarian Mawakel],
    "Deno'qai" => ["Deno'qai"],
    "Vargaldi" => %w[Vargaldi],
    "Ancient Eastros" => ["Ancient Eastros"],
    "Skaegish" => %w[Skaegish Skaer],
    "Urksan" => %w[Urksan Urskan Ursk],
    "Old Tollish" => ["Old Tollish"],
    "Zimkovan" => %w[Zimkovan Zimkova Zimka],
    "Sembaran" => %w[Sembaran Sembara],
    "Addermarian" => %w[Addermarian Addermarians Addermarch],
    "Tollish" => %w[Tollish Tollen Tollender],
    "Dunmari" => %w[Dunmari Dunmar],
    "Vosic" => %w[Vosic Vos Vostok],
    "Tyrwinghan" => %w[Tyrwinghan Tyrwinghans Tyrwingha],
    "Hkaran" => %w[Hkaran Hkar],
    "Dwarvish" => %w[Dwarvish Dwarven Dwarf Dwarves],
    "Elvish" => %w[Elvish Elven Elf Elves],
    "Lizardling" => %w[Lizardling Lizardfolk],
    "Stoneborn" => %w[Stoneborn],
    "Orcish" => %w[Orcish Orc Orcs],
    "Free Orcish" => ["Free Orcish", "Free Orcs", "People of the Rainbow"],
    "Goblin" => %w[Goblin Goblins Hobgoblin Hobgoblins Katonylev],
    "Halfling" => %w[Halfling Halflings],
    "Centaur" => %w[Centaur Centaurs],
    "Giant" => %w[Giant Giants Titan Titans],
    "Kenku" => %w[Kenku],
    "Merfolk" => %w[Merfolk],
    "Gnoll" => %w[Gnoll Gnolls],
    "Sylvan" => %w[Sylvan Feywild Fey],
    "Primordial" => %w[Primordial Aquan Auran Ignan Terran Elemental Elementals]
  }.freeze

  class Error < StandardError; end

  module_function

  def build(root)
    source = root.join(SOURCE_PATH)
    raise Error, "Language source note is missing: #{SOURCE_PATH}" unless source.file?

    text = source.read(encoding: "UTF-8")
    catalog = extract_catalog(text)
    resolve_fallback_guidance!(catalog.fetch("families"), catalog.fetch("languages"))
    validate_catalog!(catalog.fetch("families"), catalog.fetch("languages"))
    {
      "schemaVersion" => SCHEMA_VERSION,
      "sourcePath" => SOURCE_PATH,
      "sourceSha256" => Digest::SHA256.hexdigest(text),
      "families" => catalog.fetch("families"),
      "languages" => catalog.fetch("languages")
    }
  end

  def extract_catalog(text)
    families = []
    languages = []
    current_family = nil
    current_language = nil

    text.lines.each_with_index do |line, index|
      if (heading = line.match(/\A(#+)\s+(.+?)\s*\z/))
        level = heading[1].length
        title = heading[2].strip
        current_language = nil
        if level == 2
          family_name = FAMILY_NAME_OVERRIDES[title]
          current_family = if family_name
                             record = {
                               "entryType" => "family",
                               "family" => family_name,
                               "lookupTerms" => FAMILY_LOOKUP_TERM_OVERRIDES.fetch(family_name, [title]),
                               "guidance" => nil,
                               "sourceHeading" => title,
                               "sourceHeadingLine" => index + 1
                             }
                             families << record
                             record
                           end
        elsif level == 5
          language = LANGUAGE_NAME_OVERRIDES.fetch(title, title)
          current_language = {
            "entryType" => "language",
            "language" => language,
            "lookupTerms" => LOOKUP_TERM_OVERRIDES.fetch(language, [language, title].uniq),
            "family" => current_family && current_family.fetch("family"),
            "parentLanguage" => PARENT_LANGUAGE_OVERRIDES[language],
            "directGuidance" => nil,
            "fallbackGuidance" => [],
            "sourceHeading" => title,
            "sourceHeadingLine" => index + 1
          }.reject { |_key, value| value.nil? }
          languages << current_language
        end
        next
      end

      analogue_text = extract_analogue_text(line)
      next unless analogue_text

      if current_language
        raise Error, "Multiple analogue lines found for #{current_language.fetch('language')}." if current_language["directGuidance"]

        current_language["directGuidance"] = guidance_record(
          kind: "direct",
          analogue_text: analogue_text,
          source_heading: current_language.fetch("sourceHeading"),
          source_line: index + 1
        )
      elsif current_family
        raise Error, "Multiple analogue lines found for #{current_family.fetch('family')} language family." if current_family["guidance"]

        current_family["guidance"] = guidance_record(
          kind: "family",
          analogue_text: analogue_text,
          source_heading: current_family.fetch("sourceHeading"),
          source_line: index + 1
        )
      end
    end

    { "families" => families, "languages" => languages }
  end

  def extract_analogue_text(line)
    normalized = line.strip.gsub(/[*_]/, "")
    match = normalized.match(/\AReal world (?:analog|mapping)\s*:\s*(.+?)\s*\z/i)
    match && match[1].strip
  end

  def guidance_record(kind:, analogue_text:, source_heading:, source_line:, source: nil)
    {
      "kind" => kind,
      "source" => source,
      "mappingStatus" => mapping_status(analogue_text),
      "analogueText" => analogue_text,
      "sourceHeading" => source_heading,
      "sourceLine" => source_line
    }.reject { |_key, value| value.nil? }
  end

  def resolve_fallback_guidance!(families, languages)
    families_by_name = families.to_h { |entry| [entry.fetch("family"), entry] }
    languages_by_name = languages.to_h { |entry| [entry.fetch("language"), entry] }

    languages.each do |language|
      fallbacks = []
      if (parent_name = language["parentLanguage"])
        parent = languages_by_name[parent_name]
        raise Error, "Parent language is missing for #{language.fetch('language')}: #{parent_name}" unless parent

        source_guidance = parent["directGuidance"] || Array(parent["fallbackGuidance"]).first
        raise Error, "Parent language has no pronunciation guidance for #{language.fetch('language')}: #{parent_name}" unless source_guidance

        fallbacks << source_guidance.merge("kind" => "parent_language", "source" => parent_name)
      end
      if (family_name = language["family"])
        family = families_by_name[family_name]
        raise Error, "Language family is missing for #{language.fetch('language')}: #{family_name}" unless family
        raise Error, "Language family has no pronunciation guidance: #{family_name}" unless family["guidance"]

        fallbacks << family.fetch("guidance").merge("source" => family_name)
      end
      language["fallbackGuidance"] = fallbacks
    end
  end

  def mapping_status(text)
    normalized = text.downcase
    return "undetermined" if normalized.match?(/\A(?:not defined|undetermined|not determined|nothing specific|none\s*,?\s*specifically)/)
    return "provisional" if normalized.match?(/\b(?:likely|may change|might|possible|diverse)\b/)

    "defined"
  end

  def validate_catalog!(families, languages)
    raise Error, "No language entries were found in #{SOURCE_PATH}." if languages.empty?

    family_names = []
    language_names = []
    family_lookup_terms = []
    language_lookup_terms = []
    families.each do |entry|
      validate_identity_entry!(entry, "family", "family", family_names, family_lookup_terms)
      validate_guidance!(entry["guidance"], "language family #{entry['family']}")
    end
    languages.each do |entry|
      validate_identity_entry!(entry, "language", "language", language_names, language_lookup_terms)
      direct = entry["directGuidance"]
      fallbacks = entry["fallbackGuidance"]
      validate_guidance!(direct, "language #{entry['language']}") if direct
      unless fallbacks.is_a?(Array)
        raise Error, "fallbackGuidance must be a list: #{entry['language']}"
      end
      fallbacks.each { |guidance| validate_guidance!(guidance, "language #{entry['language']} fallback") }
      if direct.nil? && fallbacks.empty?
        raise Error, "Every language needs direct or inherited pronunciation guidance: #{entry['language']}"
      end
    end

    raise Error, "Language family names must be unique." unless family_names.uniq.length == family_names.length
    raise Error, "Language names must be unique." unless language_names.uniq.length == language_names.length
    raise Error, "Language family lookup terms must be unique." unless family_lookup_terms.uniq.length == family_lookup_terms.length
    raise Error, "Language lookup terms must be unique." unless language_lookup_terms.uniq.length == language_lookup_terms.length
  end

  def validate_identity_entry!(entry, expected_type, identity_key, names, lookup_terms)
    identity = entry[identity_key].to_s.strip
    terms = entry["lookupTerms"]
    unless entry["entryType"] == expected_type && !identity.empty? && terms.is_a?(Array) && !terms.empty? &&
           !entry["sourceHeading"].to_s.strip.empty? && entry["sourceHeadingLine"].to_i.positive?
      raise Error, "Invalid #{expected_type} pronunciation-guidance entry: #{identity}"
    end
    unless terms.all? { |term| term.is_a?(String) && !term.strip.empty? }
      raise Error, "#{expected_type} lookup terms must be nonempty strings: #{identity}"
    end

    names << identity.downcase
    lookup_terms.concat(terms.map(&:downcase))
  end

  def validate_guidance!(guidance, label)
    unless guidance.is_a?(Hash) && %w[direct family parent_language].include?(guidance["kind"]) &&
           MAPPING_STATUSES.include?(guidance["mappingStatus"].to_s) &&
           !guidance["analogueText"].to_s.strip.empty? && !guidance["sourceHeading"].to_s.strip.empty? &&
           guidance["sourceLine"].to_i.positive?
      raise Error, "Invalid pronunciation guidance for #{label}."
    end
  end

  def audit_name_languages(root, data)
    values = Hash.new { |hash, key| hash[key] = [] }
    parse_errors = []
    root.glob("**/*.md").sort.each do |path|
      relative = path.relative_path_from(root)
      next if excluded_note_path?(relative)

      text = path.read(encoding: "UTF-8")
      text.scan(/%%\^Metadata:names:v1%%\s*(.*?)\s*%%\^End%%/m).each do |match|
        begin
          entries = YAML.safe_load(
            match.first,
            permitted_classes: [Date, Time],
            permitted_symbols: [],
            aliases: true
          )
          next unless entries.is_a?(Array)

          entries.each do |entry|
            next unless entry.is_a?(Hash)

            language = entry["language"].to_s.strip
            values[language] << relative.to_s unless language.empty?
          end
        rescue Psych::Exception => error
          parse_errors << { "path" => relative.to_s, "error" => error.message.lines.first.to_s.strip }
        end
      end
    end

    ignored = []
    covered_value_count = 0
    covered_entry_count = 0
    uncovered = []
    values.keys.sort.each do |language|
      record = { "language" => language, "count" => values[language].length, "paths" => values[language].uniq.sort }
      if AUDIT_IGNORED_VALUES.include?(language.downcase)
        ignored << record
      elsif (matches = matching_guidance_labels(data, language)).empty?
        uncovered << record
      else
        covered_value_count += 1
        covered_entry_count += record.fetch("count")
      end
    end

    {
      "schemaVersion" => AUDIT_SCHEMA_VERSION,
      "sourcePath" => SOURCE_PATH,
      "summary" => {
        "languageValues" => values.length,
        "nameEntries" => values.values.sum(&:length),
        "coveredLanguageValues" => covered_value_count,
        "coveredNameEntries" => covered_entry_count,
        "ignoredLanguageValues" => ignored.length,
        "uncoveredLanguageValues" => uncovered.length
      },
      "ignored" => ignored,
      "uncovered" => uncovered,
      "parseErrors" => parse_errors
    }
  end

  def matching_guidance_labels(data, value)
    entries = Array(data["languages"]) + Array(data["families"])
    entries.each_with_object([]) do |entry, labels|
      next unless Array(entry["lookupTerms"]).any? { |term| lookup_match?(value, term) }

      identity = entry["entryType"] == "family" ? entry["family"] : entry["language"]
      labels << "#{entry.fetch('entryType')}:#{identity}"
    end.sort
  end

  def lookup_match?(value, term)
    value.to_s.match?(/(?<![[:alnum:]_])#{Regexp.escape(term)}(?![[:alnum:]_])/i)
  end

  def excluded_note_path?(relative)
    directories = relative.each_filename.to_a[0...-1]
    directories.any? { |segment| segment == "Worldbuilding" || segment.start_with?(".", "_") }
  end

  def stale?(root)
    source = root.join(SOURCE_PATH)
    output = root.join(OUTPUT_PATH)
    !output.file? || source.mtime > output.mtime
  end

  def read_and_validate_sidecar(root)
    output = root.join(OUTPUT_PATH)
    data = JSON.parse(output.read(encoding: "UTF-8"))
    unless data["schemaVersion"] == SCHEMA_VERSION && data["families"].is_a?(Array) && data["languages"].is_a?(Array)
      raise Error, "Language pronunciation sidecar uses an unsupported schema."
    end
    validate_catalog!(data.fetch("families"), data.fetch("languages"))
    data
  end

  class CLI
    def initialize(argv)
      @argv = argv
    end

    def run
      options = { root: Pathname.pwd, mode: :check }
      parser = OptionParser.new do |opts|
        opts.banner = "Usage: generate_language_pronunciation_analogues.rb [--check|--write|--audit] [options]"
        opts.on("--root PATH", "Vault root") { |value| options[:root] = Pathname.new(value) }
        opts.on("--check", "Verify sidecar freshness and schema") { options[:mode] = :check }
        opts.on("--write", "Regenerate the JSON sidecar") { options[:mode] = :write }
        opts.on("--audit", "Report name-block language values not covered by the sidecar") { options[:mode] = :audit }
      end
      parser.parse!(@argv)
      root = options.fetch(:root).expand_path
      output = root.join(OUTPUT_PATH)
      if options[:mode] == :write
        rendered = "#{JSON.pretty_generate(TaelgarLanguagePronunciationAnalogues.build(root))}\n"
        output.write(rendered, mode: "w", encoding: "UTF-8")
      else
        if TaelgarLanguagePronunciationAnalogues.stale?(root)
          raise Error, "Language pronunciation sidecar is older than #{SOURCE_PATH}; run with --write."
        end
        data = TaelgarLanguagePronunciationAnalogues.read_and_validate_sidecar(root)
        puts JSON.pretty_generate(TaelgarLanguagePronunciationAnalogues.audit_name_languages(root, data)) if options[:mode] == :audit
      end
      0
    rescue OptionParser::ParseError, Error, Errno::ENOENT, JSON::ParserError => error
      warn error.message
      2
    end
  end
end

exit TaelgarLanguagePronunciationAnalogues::CLI.new(ARGV).run if $PROGRAM_NAME == __FILE__
