#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"
require "optparse"
require "pathname"

require_relative "validate_taelgar_note"

module TaelgarWorldbuildingDiscussionIndex
  SOURCE_ROOT = "Worldbuilding"
  OUTPUT_PATH = "_scripts/worldbuilding_discussion_index.json"
  SCHEMA_VERSION = 1
  EXCLUDED_DIRECTORY_SEGMENTS = %w[Staging].freeze
  MATCH_KIND_ORDER = %w[title link embed name].freeze

  class Error < StandardError; end

  module_function

  def build(root)
    root = Pathname.new(root).expand_path
    source_paths = discussion_source_paths(root)
    subjects = subject_notes(root)
    note_index = TaelgarNoteLint::NoteIndex.new(root)
    subject_paths = subjects.to_h { |note| [note.path, true] }
    source_documents = source_paths.map do |absolute|
      path = TaelgarNoteLint.relative_path(root, absolute)
      text = TaelgarNoteLint.read_text(absolute)
      [path, text, source_metadata(path, text)]
    end
    link_aliases = discover_link_aliases(source_documents, note_index, subject_paths)
    identity_targets = unique_targets_by_identity(subjects, link_aliases)
    targets_by_identity = identity_targets.to_h do |identity, target|
      [TaelgarNoteLint.normalize(identity), target]
    end
    identity_matcher = build_identity_matcher(identity_targets.keys)
    mentions_by_target = Hash.new { |hash, key| hash[key] = [] }

    sources = source_documents.map do |path, text, metadata|
      matches = scan_source(
        path: path,
        text: text,
        metadata: metadata,
        note_index: note_index,
        subject_paths: subject_paths,
        targets_by_identity: targets_by_identity,
        identity_matcher: identity_matcher
      )
      matches.each { |target, record| mentions_by_target[target] << record }
      metadata.merge("sha256" => Digest::SHA256.hexdigest(text))
    end

    subject_records = subjects.each_with_object([]) do |note, records|
      mentions = mentions_by_target[note.path].sort_by { |record| record.fetch("path") }
      next if mentions.empty?

      records << {
        "path" => note.path,
        "name" => note.data["name"] || Pathname.new(note.path).basename(".md").to_s,
        "identitySha256" => identity_sha256(note),
        "sourceCount" => mentions.length,
        "threadCount" => mentions.map { |record| record.fetch("threadCluster") }.uniq.length,
        "significant" => mentions.length >= 2,
        "sources" => mentions
      }
    end

    {
      "schemaVersion" => SCHEMA_VERSION,
      "sourceRoot" => SOURCE_ROOT,
      "excludedDirectorySegments" => EXCLUDED_DIRECTORY_SEGMENTS,
      "sourceInventorySha256" => inventory_sha256(sources),
      "sources" => sources,
      "identityIndex" => subjects.to_h { |note| [note.path, identity_sha256(note)] },
      "subjects" => subject_records
    }
  end

  def discussion_source_paths(root)
    root.glob("#{SOURCE_ROOT}/**/*.md").select do |path|
      relative = path.relative_path_from(root)
      directories = relative.each_filename.to_a[0...-1]
      directories.none? do |segment|
        EXCLUDED_DIRECTORY_SEGMENTS.any? { |excluded| segment.casecmp?(excluded) }
      end
    end.sort
  end

  def subject_notes(root)
    root.glob("**/*.md").each_with_object([]) do |path, notes|
      relative = path.relative_path_from(root)
      next if path.basename.to_s == "AGENTS.md"

      directories = relative.each_filename.to_a[0...-1]
      next if directories.any? { |segment| segment == SOURCE_ROOT || segment.start_with?(".", "_") }

      notes << TaelgarNoteLint::ParsedNote.new(relative.to_s, TaelgarNoteLint.read_text(path))
    rescue Errno::ENOENT, Errno::EACCES
      next
    end.sort_by(&:path)
  end

  def discover_link_aliases(source_documents, note_index, subject_paths)
    aliases = Hash.new { |hash, key| hash[key] = [] }
    source_documents.each do |path, text, _metadata|
      TaelgarNoteLint.mask_markdown_code(text).scan(/!?\[\[([^\]\n]+)\]\]/).flatten.each do |raw|
        _target_text, display = raw.split("|", 2)
        next unless plausible_display_identity?(display)

        note_index.resolve(raw, path).each do |target|
          aliases[target] << display.strip if subject_paths[target]
        end
      end
    end
    aliases.transform_values { |values| values.uniq }
  end

  def plausible_display_identity?(display)
    value = display.to_s.strip
    return false unless distinctive_plain_identity?(value)
    return false unless value.match?(/\A[[:upper:]]/)
    return false unless value.match?(/\A[[:alnum:]'’\-]+(?:\s+[[:alnum:]'’\-]+)*\z/)

    !value.match?(/\A(?:The|This|That|Here|Source|Note)\b/i)
  end

  def unique_targets_by_identity(subjects, link_aliases = {})
    owners = Hash.new { |hash, key| hash[key] = [] }
    labels = {}
    subjects.each do |note|
      (note.identity_names + Array(link_aliases[note.path])).each do |identity|
        next unless distinctive_plain_identity?(identity)

        normalized = TaelgarNoteLint.normalize(identity)
        owners[normalized] << note.path
        labels[normalized] ||= identity
      end
    end
    owners.each_with_object({}) do |(normalized, paths), unique|
      next unless paths.uniq.length == 1

      unique[labels.fetch(normalized)] = paths.first
    end
  end

  def distinctive_plain_identity?(identity)
    value = identity.to_s.strip
    value.length >= 7 || value.match?(/[\s'’\-]/)
  end

  def build_identity_matcher(identities)
    buckets = Hash.new { |hash, key| hash[key] = [] }
    identities.each do |identity|
      token = identity.to_s[/[[:alnum:]'’\-]+/]
      next unless token

      buckets[TaelgarNoteLint.normalize(token)] << identity
    end
    {
      "buckets" => buckets.transform_values { |values| values.uniq.sort_by { |value| [-value.length, value.downcase] } },
      "patterns" => identities.to_h do |identity|
        [identity, /(?<![[:alnum:]_])#{Regexp.escape(identity)}(?![[:alnum:]_])/i]
      end
    }
  end

  def matched_identities(text, matcher)
    tokens = text.to_s.scan(/[[:alnum:]'’\-]+/).map { |token| TaelgarNoteLint.normalize(token) }.uniq
    candidates = tokens.flat_map { |token| Array(matcher.fetch("buckets")[token]) }.uniq
    patterns = matcher.fetch("patterns")
    candidates.select { |identity| text.match?(patterns.fetch(identity)) }
  end

  def scan_source(path:, text:, metadata:, note_index:, subject_paths:, targets_by_identity:, identity_matcher:)
    records = {}
    title_matches = matched_identities(metadata.fetch("title"), identity_matcher)
    title_matches.each do |identity|
      target = targets_by_identity[TaelgarNoteLint.normalize(identity)]
      add_match(records, target, metadata, "title", identity: identity) if target
    end

    masked = TaelgarNoteLint.mask_markdown_code(text)
    masked.lines.each_with_index do |line, index|
      line.scan(/(?<!!)\[\[([^\]\n]+)\]\]/).flatten.each do |raw|
        note_index.resolve(raw, path).each do |target|
          add_match(records, target, metadata, "link", line: index + 1, link: raw) if subject_paths[target]
        end
      end
      line.scan(/!\[\[([^\]\n]+)\]\]/).flatten.each do |raw|
        note_index.resolve(raw, path).each do |target|
          add_match(records, target, metadata, "embed", line: index + 1, link: raw) if subject_paths[target]
        end
      end

      plain_line = line.gsub(/!?\[\[[^\]\n]+\]\]/, " ")
      matched_identities(plain_line, identity_matcher).each do |identity|
        target = targets_by_identity[TaelgarNoteLint.normalize(identity)]
        add_match(records, target, metadata, "name", line: index + 1, identity: identity) if target
      end
    end

    records.each_value do |record|
      record["matchKinds"] = MATCH_KIND_ORDER.select { |kind| record.fetch("matchKinds").include?(kind) }
      record["mentionLines"] = record.fetch("mentionLines").uniq.sort
      record["matchedIdentities"] = record.fetch("matchedIdentities").uniq.sort_by(&:downcase)
      record["matchedLinks"] = record.fetch("matchedLinks").uniq.sort_by(&:downcase)
      record.delete("mentionLines") if record["mentionLines"].empty?
      record.delete("matchedIdentities") if record["matchedIdentities"].empty?
      record.delete("matchedLinks") if record["matchedLinks"].empty?
    end
    records
  end

  def add_match(records, target, metadata, kind, line: nil, identity: nil, link: nil)
    return unless target

    record = records[target] ||= metadata.merge(
      "matchKinds" => [],
      "mentionLines" => [],
      "matchedIdentities" => [],
      "matchedLinks" => []
    )
    record["matchKinds"] << kind
    record["mentionLines"] << line if line
    record["matchedIdentities"] << identity if identity
    record["matchedLinks"] << link if link
  end

  def source_metadata(path, _text)
    filename = Pathname.new(path).basename(".md").to_s
    dated = filename.match(/\A(\d{4}-\d{2}-\d{2})(?: to (\d{4}-\d{2}-\d{2}))? - (.+)\z/)
    title = dated ? dated[3].strip : filename
    folder = Pathname.new(path).dirname.to_s
    thread_title = TaelgarNoteLint.normalize(title).gsub(/\s+/, "-")
    {
      "path" => path,
      "title" => title,
      "folder" => folder,
      "sourceKind" => Pathname.new(path).dirname.each_filename.to_a[1] || SOURCE_ROOT,
      "dateStart" => dated && dated[1],
      "dateEnd" => dated && (dated[2] || dated[1]),
      "threadCluster" => dated ? "#{folder}:#{thread_title}" : path.sub(/\.md\z/i, "")
    }.reject { |_key, value| value.nil? }
  end

  def identity_sha256(note)
    payload = {
      "path" => note.path,
      "identities" => note.identity_names.sort_by(&:downcase)
    }
    Digest::SHA256.hexdigest(JSON.generate(payload))
  end

  def inventory_sha256(sources)
    payload = sources.map { |source| [source.fetch("path"), source.fetch("sha256")] }
    Digest::SHA256.hexdigest(JSON.generate(payload))
  end

  def read_and_validate(root)
    root = Pathname.new(root).expand_path
    path = root.join(OUTPUT_PATH)
    data = JSON.parse(TaelgarNoteLint.read_text(path))
    unless data["schemaVersion"] == SCHEMA_VERSION && data["sourceRoot"] == SOURCE_ROOT &&
           data["excludedDirectorySegments"] == EXCLUDED_DIRECTORY_SEGMENTS && data["sources"].is_a?(Array) &&
           data["subjects"].is_a?(Array) && data["identityIndex"].is_a?(Hash)
      raise Error, "Worldbuilding discussion sidecar uses an unsupported schema."
    end
    paths = data.fetch("sources").map { |source| source.fetch("path") }
    raise Error, "Worldbuilding discussion sidecar contains duplicate source paths." unless paths.uniq.length == paths.length

    data
  rescue JSON::ParserError => error
    raise Error, "Worldbuilding discussion sidecar is invalid JSON: #{error.message}"
  end

  def exact_current?(root, data)
    build(root) == data
  end

  class Sidecar
    attr_reader :reference

    def initialize(root)
      @root = Pathname.new(root).expand_path
      @path = @root.join(OUTPUT_PATH)
      @data = TaelgarWorldbuildingDiscussionIndex.read_and_validate(@root)
      validate_source_freshness!
      @subjects = @data.fetch("subjects").to_h { |record| [record.fetch("path"), record] }
      @reference = {
        "path" => OUTPUT_PATH,
        "schemaVersion" => SCHEMA_VERSION,
        "sha256" => Digest::SHA256.file(@path).hexdigest
      }
    rescue Errno::ENOENT
      raise Error, "Worldbuilding discussion sidecar is missing; run the generator with --write."
    end

    def for(note)
      expected_identity = @data.fetch("identityIndex")[note.path]
      unless expected_identity == TaelgarWorldbuildingDiscussionIndex.identity_sha256(note)
        raise Error, "Worldbuilding discussion sidecar is stale for #{note.path}; run the generator with --write."
      end

      @subjects[note.path] || {
        "path" => note.path,
        "name" => note.data["name"] || Pathname.new(note.path).basename(".md").to_s,
        "identitySha256" => expected_identity,
        "sourceCount" => 0,
        "threadCount" => 0,
        "significant" => false,
        "sources" => []
      }
    end

    private

    def validate_source_freshness!
      current_paths = TaelgarWorldbuildingDiscussionIndex.discussion_source_paths(@root)
        .map { |path| path.relative_path_from(@root).to_s }
      stored_paths = @data.fetch("sources").map { |source| source.fetch("path") }
      unless current_paths == stored_paths
        raise Error, "Worldbuilding discussion sidecar source inventory is stale; run the generator with --write."
      end
      return unless current_paths.any? { |path| @root.join(path).mtime > @path.mtime }

      raise Error, "Worldbuilding discussion sidecar is older than a non-Staging Worldbuilding source; run the generator with --write."
    end
  end

  class CLI
    def initialize(argv)
      @argv = argv
    end

    def run
      options = { root: Pathname.pwd, mode: :check, query: nil }
      parser = OptionParser.new do |opts|
        opts.banner = "Usage: generate_worldbuilding_discussion_index.rb [--check|--write|--query PATH] [options]"
        opts.on("--root PATH", "Vault root") { |value| options[:root] = Pathname.new(value) }
        opts.on("--check", "Verify the committed sidecar against current sources and identities") { options[:mode] = :check }
        opts.on("--write", "Regenerate the JSON sidecar") { options[:mode] = :write }
        opts.on("--query PATH", "Return the complete discussion record for one canonical note") do |value|
          options[:mode] = :query
          options[:query] = value
        end
      end
      parser.parse!(@argv)
      root = options.fetch(:root).expand_path
      output = root.join(OUTPUT_PATH)
      case options.fetch(:mode)
      when :write
        output.write("#{JSON.pretty_generate(TaelgarWorldbuildingDiscussionIndex.build(root))}\n", mode: "w", encoding: "UTF-8")
      when :query
        relative = Pathname.new(options.fetch(:query))
        relative = relative.relative_path_from(root) if relative.absolute?
        note = TaelgarNoteLint::ParsedNote.new(relative.to_s, TaelgarNoteLint.read_text(root.join(relative)))
        puts JSON.pretty_generate(Sidecar.new(root).for(note))
      else
        data = TaelgarWorldbuildingDiscussionIndex.read_and_validate(root)
        unless TaelgarWorldbuildingDiscussionIndex.exact_current?(root, data)
          raise Error, "Worldbuilding discussion sidecar does not match the current vault; run with --write."
        end
      end
      0
    rescue OptionParser::ParseError, Error, Errno::ENOENT, ArgumentError => error
      warn error.message
      2
    end
  end
end

exit TaelgarWorldbuildingDiscussionIndex::CLI.new(ARGV).run if $PROGRAM_NAME == __FILE__
