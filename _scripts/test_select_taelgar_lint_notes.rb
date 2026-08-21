# frozen_string_literal: true

require "fileutils"
require "json"
require "minitest/autorun"
require "tmpdir"

require_relative "select_taelgar_lint_notes"

class SelectTaelgarLintNotesTest < Minitest::Test
  def setup
    @roots = []
  end

  def teardown
    @roots.each { |root| FileUtils.remove_entry(root) if File.exist?(root) }
  end

  def test_default_selection_excludes_ineligible_paths_and_objective_blank_stubs
    root = make_vault
    write_note(root, "People/Eligible.md", note("Eligible"))
    write_note(root, "People/Heading Only.md", "---\ntags: [person]\n---\n# Heading Only\n")
    write_note(root, "Worldbuilding/Idea.md", note("Idea"))
    write_note(root, "People/_generated/Generated.md", note("Generated"))
    write_note(root, "People/.hidden/Hidden.md", note("Hidden"))
    write_note(root, "AGENTS.md", note("Instructions"))

    document = selector(root).select(["."])

    assert_equal ["People/Eligible.md"], document.fetch("paths")
    assert_equal 6, document.dig("selectionSummary", "discovered")
    assert_equal 4, document.dig("selectionSummary", "skippedIneligiblePaths")
    assert_equal 1, document.dig("selectionSummary", "skippedNoReviewableProse")
    assert_equal 1, document.dig("selectionSummary", "eligible")
    assert_equal({
      "AGENTS.md" => 1,
      "Worldbuilding" => 1,
      "dot directory" => 1,
      "underscore directory" => 1
    }, document.dig("selectionSummary", "ineligiblePathReasons"))
  end

  def test_alphabetical_order_and_cap_apply_after_state_filtering
    root = make_vault
    write_note(root, "People/Chardonians/zeta.md", note("Zeta"))
    write_note(root, "People/Chardonians/Alpha.md", note("Alpha"))
    write_note(root, "People/Chardonians/beta.md", note("Beta"))
    write_note(root, "People/Chardonians/Already Linted.md", note("Already Linted", version: TaelgarNoteLint::VERSION))

    document = selector(root, limit: 2).select(["People/Chardonians"])

    assert_equal [
      "People/Chardonians/Alpha.md",
      "People/Chardonians/beta.md"
    ], document.fetch("paths")
    assert_equal 3, document.dig("selectionSummary", "matchedState")
    assert_equal 1, document.dig("selectionSummary", "omittedByCap")
    assert_equal 1, document.dig("selectionSummary", "omittedByState")
  end

  def test_seeded_random_sample_is_reproducible
    root = make_vault
    8.times { |number| write_note(root, "People/Person #{number}.md", note("Person #{number}")) }

    first = selector(root, order: "random", limit: 3, seed: 340).select(["People"])
    second = selector(root, order: "random", limit: 3, seed: 340).select(["People"])

    assert_equal first.fetch("paths"), second.fetch("paths")
    assert_equal 3, first.fetch("paths").length
    assert_equal 340, first.dig("selection", "seed")
    assert_equal 5, first.dig("selectionSummary", "omittedByCap")
  end

  def test_state_filters_distinguish_unlinted_current_stale_and_any_linted
    root = make_vault
    write_note(root, "People/Unlinted.md", note("Unlinted"))
    write_note(root, "People/Invalid Pair.md", note("Invalid Pair", version: "not-a-version"))
    write_note(root, "People/Current.md", note("Current", version: TaelgarNoteLint::VERSION))
    write_note(root, "People/Stale.md", note("Stale", version: "3.3"))

    assert_equal ["People/Invalid Pair.md", "People/Unlinted.md"],
                 selector(root).select(["People"]).fetch("paths")
    assert_equal ["People/Current.md", "People/Stale.md"],
                 selector(root, state: "linted", re_lint: true).select(["People"]).fetch("paths")
    assert_equal ["People/Current.md"],
                 selector(root, state: "current", re_lint: true).select(["People"]).fetch("paths")
    assert_equal ["People/Stale.md"],
                 selector(root, state: "stale", re_lint: true).select(["People"]).fetch("paths")
    assert_equal 4, selector(root, state: "all", re_lint: true).select(["People"]).fetch("paths").length
  end

  def test_completed_state_filters_require_explicit_relint_authorization
    root = make_vault

    %w[linted stale current all].each do |state|
      error = assert_raises(TaelgarNoteLint::Selection::SelectionError) do
        selector(root, state: state)
      end

      assert_includes error.message, "requires explicit --re-lint authorization"
    end
  end

  def test_omitting_a_cap_selects_the_entire_matching_directory
    root = make_vault
    paths = [
      "People/Chardonians/One.md",
      "People/Chardonians/Three.md",
      "People/Chardonians/Two.md"
    ]
    paths.each { |path| write_note(root, path, note(File.basename(path, ".md"))) }

    document = selector(root).select(["People/Chardonians"])

    assert_equal paths.sort, document.fetch("paths")
    assert_nil document.dig("selection", "limit")
    assert_equal 0, document.dig("selectionSummary", "omittedByCap")
  end

  def test_cli_cap_alias_and_owner_only_output
    root = make_vault
    3.times { |number| write_note(root, "People/Person #{number}.md", note("Person #{number}")) }
    output = File.join(root, "selection.json")

    result = TaelgarNoteLint::Selection::CLI.new(
      ["--root", root, "--cap", "2", "--output", output, "People"]
    ).run
    document = JSON.parse(File.read(output))

    assert_equal 0, result
    assert_equal 2, document.fetch("paths").length
    assert_equal 0o600, File.stat(output).mode & 0o777
  end

  def test_cli_relint_without_an_explicit_state_selects_all_eligible_notes
    root = make_vault
    write_note(root, "People/Unlinted.md", note("Unlinted"))
    write_note(root, "People/Current.md", note("Current", version: TaelgarNoteLint::VERSION))
    output = File.join(root, "selection.json")

    result = TaelgarNoteLint::Selection::CLI.new(
      ["--root", root, "--re-lint", "--output", output, "People"]
    ).run
    document = JSON.parse(File.read(output))

    assert_equal 0, result
    assert_equal "all", document.dig("selection", "state")
    assert_equal ["People/Current.md", "People/Unlinted.md"], document.fetch("paths")
  end

  private

  def make_vault
    root = Dir.mktmpdir("taelgar-lint-selector-")
    @roots << root
    root
  end

  def selector(root, **options)
    TaelgarNoteLint::Selection::Selector.new(root: root, **options)
  end

  def write_note(root, relative_path, text)
    path = File.join(root, relative_path)
    FileUtils.mkdir_p(File.dirname(path))
    File.write(path, text)
  end

  def note(name, version: nil)
    lint_state = if version
                   "lintedAt: \"2026-08-19T09:00:00-04:00\"\nlintVersion: \"#{version}\"\n"
                 else
                   ""
                 end
    <<~MARKDOWN
      ---
      #{lint_state}tags: [person]
      name: #{name}
      ---
      # #{name}

      #{name} is a documented person in this test vault.
    MARKDOWN
  end
end
