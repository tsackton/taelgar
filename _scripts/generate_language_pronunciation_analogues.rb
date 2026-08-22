#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"
require "optparse"
require "pathname"

module TaelgarLanguagePronunciationAnalogues
  SOURCE_PATH = "Background/Languages.md"
  OUTPUT_PATH = "_scripts/language_pronunciation_analogues.json"
  STATUSES = %w[defined provisional undetermined].freeze
  LANGUAGE_NAME_OVERRIDES = {
    "Illoria" => "Illorian"
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
    "Mawaran" => %w[Mawaran Mawakel],
    "Deno'qai" => ["Deno'qai"],
    "Vargaldi" => %w[Vargaldi],
    "Ancient Eastros" => ["Ancient Eastros"],
    "Skaegish" => %w[Skaegish Skaer],
    "Urksan" => %w[Urksan Urskan Ursk],
    "Old Tollish" => ["Old Tollish"],
    "Zimkovan" => %w[Zimkovan Zimkova Zimka],
    "Sembaran" => %w[Sembaran Sembara],
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
    languages = extract_languages(text)
    validate_languages!(languages)
    {
      "schemaVersion" => 1,
      "sourcePath" => SOURCE_PATH,
      "sourceSha256" => Digest::SHA256.hexdigest(text),
      "languages" => languages
    }
  end

  def extract_languages(text)
    current_heading = nil
    text.lines.each_with_index.each_with_object([]) do |(line, index), entries|
      if (heading = line.match(/\A(#+)\s+(.+?)\s*\z/))
        current_heading = heading[1].length == 5 ? heading[2].strip : nil
        next
      end
      next unless current_heading

      normalized = line.strip.gsub(/[*_]/, "")
      analogue = normalized.match(/\AReal world (?:analog|mapping)\s*:\s*(.+?)\s*\z/i)
      next unless analogue

      language = LANGUAGE_NAME_OVERRIDES.fetch(current_heading, current_heading)
      analogue_text = analogue[1].strip
      entries << {
        "language" => language,
        "lookupTerms" => LOOKUP_TERM_OVERRIDES.fetch(language, [language, current_heading].uniq),
        "analogues" => [analogue_text],
        "analogueText" => analogue_text,
        "status" => analogue_status(analogue_text),
        "sourceHeading" => current_heading,
        "sourceLine" => index + 1
      }
      current_heading = nil
    end
  end

  def analogue_status(text)
    normalized = text.downcase
    return "undetermined" if normalized.match?(/\A(?:not defined|undetermined|not determined|nothing specific|none specifically)/)
    return "provisional" if normalized.match?(/\b(?:likely|may change|might|possible|diverse)\b/)

    "defined"
  end

  def validate_languages!(languages)
    raise Error, "No language analogue entries were found in #{SOURCE_PATH}." if languages.empty?

    names = []
    lookup_terms = []
    languages.each do |entry|
      unless entry.is_a?(Hash) && !entry["language"].to_s.strip.empty? &&
             entry["lookupTerms"].is_a?(Array) && !entry["lookupTerms"].empty? &&
             entry["analogues"].is_a?(Array) && !entry["analogueText"].to_s.empty? &&
             STATUSES.include?(entry["status"].to_s) && !entry["sourceHeading"].to_s.strip.empty? &&
             entry["sourceLine"].to_i.positive?
        raise Error, "Every language entry needs language, lookupTerms, exact analogue text, status, heading, and source line."
      end
      unless entry["lookupTerms"].all? { |term| term.is_a?(String) && !term.strip.empty? } &&
             entry["analogues"].all? { |analogue| analogue.is_a?(String) && !analogue.strip.empty? }
        raise Error, "Language lookup terms and analogues must be nonempty strings: #{entry['language']}"
      end

      names << entry.fetch("language").downcase
      lookup_terms.concat(entry.fetch("lookupTerms").map(&:downcase))
    end
    raise Error, "Language names must be unique." unless names.uniq.length == names.length
    raise Error, "Language lookup terms must be unique." unless lookup_terms.uniq.length == lookup_terms.length
  end

  def stale?(root)
    source = root.join(SOURCE_PATH)
    output = root.join(OUTPUT_PATH)
    !output.file? || source.mtime > output.mtime
  end

  class CLI
    def initialize(argv)
      @argv = argv
    end

    def run
      options = { root: Pathname.pwd, write: false }
      parser = OptionParser.new do |opts|
        opts.banner = "Usage: generate_language_pronunciation_analogues.rb [--check|--write] [options]"
        opts.on("--root PATH", "Vault root") { |value| options[:root] = Pathname.new(value) }
        opts.on("--check", "Verify that the JSON sidecar is not older than the language note") { options[:write] = false }
        opts.on("--write", "Regenerate the JSON sidecar") { options[:write] = true }
      end
      parser.parse!(@argv)
      root = options.fetch(:root).expand_path
      output = root.join(OUTPUT_PATH)
      if options[:write]
        rendered = "#{JSON.pretty_generate(TaelgarLanguagePronunciationAnalogues.build(root))}\n"
        output.write(rendered, mode: "w", encoding: "UTF-8")
      elsif TaelgarLanguagePronunciationAnalogues.stale?(root)
        raise Error, "Language pronunciation sidecar is older than #{SOURCE_PATH}; run with --write."
      else
        data = JSON.parse(output.read(encoding: "UTF-8"))
        unless data["schemaVersion"] == 1 && data["languages"].is_a?(Array)
          raise Error, "Language pronunciation sidecar uses an unsupported schema."
        end
      end
      0
    rescue OptionParser::ParseError, Error, Errno::ENOENT, JSON::ParserError => error
      warn error.message
      2
    end
  end
end

exit TaelgarLanguagePronunciationAnalogues::CLI.new(ARGV).run if $PROGRAM_NAME == __FILE__
