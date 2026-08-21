#!/usr/bin/env ruby
# frozen_string_literal: true

# Read-only target selection for contextual Taelgar note linting.
#
# This script reuses the batch linter's path, authored-body, and completion-state
# rules. It never modifies a note. Directory scopes recurse; omitted scopes mean
# the entire vault.

require "json"
require "optparse"
require "pathname"
require "time"

require_relative "lint_taelgar_notes"

module TaelgarNoteLint
  module Selection
    SCHEMA_VERSION = 1
    STATES = %w[unlinted linted stale current all].freeze
    ORDERS = %w[alphabetical random].freeze
    FORMATS = %w[json paths].freeze
    RELINT_STATES = %w[linted stale current all].freeze

    class SelectionError < StandardError; end

    class Selector
      def initialize(root:, state: "unlinted", re_lint: false, order: "alphabetical", limit: nil, seed: nil)
        @root = Pathname.new(root).expand_path
        @root_realpath = @root.realpath
        @state = state.to_s
        @re_lint = re_lint
        @order = order.to_s
        @limit = limit.nil? ? nil : Integer(limit)
        @seed = seed.nil? ? nil : Integer(seed)
        validate_options!
      rescue Errno::ENOENT
        raise SelectionError, "Vault root does not exist: #{root}"
      rescue ArgumentError, TypeError
        raise SelectionError, "--limit and --seed must be integers."
      end

      def select(scopes = [])
        requested_scopes = scopes.empty? ? ["."] : scopes
        discovered, canonical_scopes = discover(requested_scopes)
        path_exclusions = Hash.new(0)
        no_reviewable_prose = 0
        state_counts = { "unlinted" => 0, "current" => 0, "stale" => 0 }
        eligible = []

        discovered.each do |path|
          exclusion = path_exclusion(path)
          if exclusion
            path_exclusions[exclusion] += 1
            next
          end

          note = ParsedNote.new(path, TaelgarNoteLint.read_text(@root.join(path)))
          unless Batch.objectively_lintable_note?(note)
            no_reviewable_prose += 1
            next
          end

          state = completion_state(note)
          state_counts[state] += 1
          eligible << [path, state] if state_matches?(state)
        end

        matched_paths = eligible.map(&:first)
        ordered_paths, effective_seed = order_paths(matched_paths)
        selected_paths = @limit ? ordered_paths.first(@limit) : ordered_paths

        {
          "schemaVersion" => SCHEMA_VERSION,
          "validatorVersion" => VERSION,
          "generatedAt" => Time.now.iso8601,
          "root" => @root.to_s,
          "scopes" => canonical_scopes,
          "selection" => {
            "state" => @state,
            "reLint" => @re_lint,
            "order" => @order,
            "limit" => @limit,
            "seed" => effective_seed
          },
          "selectionSummary" => {
            "discovered" => discovered.length,
            "skippedIneligiblePaths" => path_exclusions.values.sum,
            "ineligiblePathReasons" => path_exclusions.sort.to_h,
            "skippedNoReviewableProse" => no_reviewable_prose,
            "eligible" => state_counts.values.sum,
            "stateCounts" => state_counts.merge("linted" => state_counts["current"] + state_counts["stale"]),
            "matchedState" => matched_paths.length,
            "omittedByState" => state_counts.values.sum - matched_paths.length,
            "omittedByCap" => ordered_paths.length - selected_paths.length,
            "selected" => selected_paths.length
          },
          "paths" => selected_paths
        }
      end

      private

      def validate_options!
        raise SelectionError, "Vault root is not a directory: #{@root}" unless @root.directory?
        raise SelectionError, "Unknown state #{@state.inspect}; choose #{STATES.join(', ')}." unless STATES.include?(@state)
        raise SelectionError, "Unknown order #{@order.inspect}; choose #{ORDERS.join(', ')}." unless ORDERS.include?(@order)
        raise SelectionError, "--limit must be a positive integer." if @limit && !@limit.positive?
        if @order != "random" && @seed
          raise SelectionError, "--seed requires --order random."
        end
        return unless RELINT_STATES.include?(@state) && !@re_lint

        raise SelectionError, "--state #{@state} can select completed notes and therefore requires explicit --re-lint authorization."
      end

      def discover(scopes)
        paths = []
        canonical_scopes = scopes.map do |scope|
          absolute, relative = resolve_scope(scope)
          if absolute.file?
            paths << Batch.relative_note_path(@root, absolute)
          elsif absolute.directory?
            Dir.glob(absolute.join("**", "*.md").to_s, File::FNM_DOTMATCH).sort.each do |candidate|
              next unless File.file?(candidate)

              ensure_realpath_inside_root!(Pathname.new(candidate), scope)
              paths << Batch.relative_note_path(@root, candidate)
            end
          else
            raise SelectionError, "Scope is neither a file nor a directory: #{scope}"
          end
          relative
        end
        [paths.uniq.sort_by { |path| [path.downcase, path] }, canonical_scopes]
      end

      def resolve_scope(scope)
        absolute = Pathname.new(scope)
        absolute = @root.join(absolute) unless absolute.absolute?
        absolute = absolute.expand_path
        relative = relative_inside_root(absolute, scope)
        raise SelectionError, "Scope does not exist: #{scope}" unless absolute.exist?

        ensure_realpath_inside_root!(absolute, scope)
        [absolute, relative]
      end

      def relative_inside_root(path, original)
        relative = path.relative_path_from(@root).to_s
        if relative == ".." || relative.start_with?("../")
          raise SelectionError, "Scope is outside the vault: #{original}"
        end

        relative
      rescue ArgumentError
        raise SelectionError, "Scope is outside the vault: #{original}"
      end

      def ensure_realpath_inside_root!(path, original)
        realpath = path.realpath
        relative = realpath.relative_path_from(@root_realpath).to_s
        return unless relative == ".." || relative.start_with?("../")

        raise SelectionError, "Scope resolves outside the vault: #{original}"
      rescue ArgumentError
        raise SelectionError, "Scope resolves outside the vault: #{original}"
      end

      def path_exclusion(path)
        return "AGENTS.md" if File.basename(path) == "AGENTS.md"

        Batch.lint_target_exclusion(path)
      end

      def completion_state(note)
        return "unlinted" unless Batch.valid_completion_pair?(note)

        Batch.canonical_state_value(note.data["lintVersion"]) == VERSION ? "current" : "stale"
      end

      def state_matches?(state)
        case @state
        when "unlinted" then state == "unlinted"
        when "linted" then state != "unlinted"
        when "stale", "current" then state == @state
        when "all" then true
        end
      end

      def order_paths(paths)
        sorted = paths.sort_by { |path| [path.downcase, path] }
        return [sorted, nil] if @order == "alphabetical"

        effective_seed = @seed || Random.new_seed
        [sorted.shuffle(random: Random.new(effective_seed)), effective_seed]
      end
    end

    class CLI
      def initialize(argv)
        @argv = argv.dup
      end

      def run
        options = {
          root: Pathname.pwd,
          re_lint: false,
          order: "alphabetical",
          format: "json"
        }
        state_explicit = false
        parser = OptionParser.new do |opts|
          opts.banner = "Usage: select_taelgar_lint_notes.rb [options] [FILE_OR_DIRECTORY ...]"
          opts.on("--root PATH", "Vault root (default: current directory)") { |value| options[:root] = value }
          opts.on("--state STATE", STATES, "Select unlinted, linted, stale, current, or all notes") do |value|
            options[:state] = value
            state_explicit = true
          end
          opts.on("--re-lint", "Authorize selection of notes with valid prior lint state") { options[:re_lint] = true }
          opts.on("--order ORDER", ORDERS, "Order alphabetically or randomly") { |value| options[:order] = value }
          opts.on("--random", "Shortcut for --order random") { options[:order] = "random" }
          opts.on("--limit N", "--cap N", Integer, "Maximum number of selected notes") { |value| options[:limit] = value }
          opts.on("--seed N", Integer, "Random seed for a reproducible sample") { |value| options[:seed] = value }
          opts.on("--format FORMAT", FORMATS, "Output json (default) or paths") { |value| options[:format] = value }
          opts.on("--output PATH", "Write output to a file") { |value| options[:output] = value }
          opts.on("-h", "--help", "Show this help") do
            puts opts
            return 0
          end
        end
        parser.parse!(@argv)
        options[:state] = options[:re_lint] ? "all" : "unlinted" unless state_explicit

        document = Selector.new(
          root: options[:root],
          state: options[:state],
          re_lint: options[:re_lint],
          order: options[:order],
          limit: options[:limit],
          seed: options[:seed]
        ).select(@argv)
        write(document, options[:format], options[:output])
        0
      rescue OptionParser::ParseError, Errno::ENOENT, SelectionError, Batch::BatchError => error
        warn error.message
        2
      end

      private

      def write(document, format, path)
        rendered = if format == "paths"
                     selected = document.fetch("paths")
                     selected.empty? ? "" : "#{selected.join("\n")}\n"
                   else
                     "#{JSON.pretty_generate(document)}\n"
                   end
        if path
          File.write(path, rendered)
          File.chmod(0o600, path)
        else
          print(rendered)
        end
      end
    end
  end
end

exit TaelgarNoteLint::Selection::CLI.new(ARGV).run if $PROGRAM_NAME == __FILE__
