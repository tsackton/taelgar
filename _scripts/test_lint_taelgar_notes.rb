# frozen_string_literal: true

require "fileutils"
require "json"
require "minitest/autorun"
require "tmpdir"

require_relative "lint_taelgar_notes"

class BatchLintTaelgarNotesTest < Minitest::Test
  COMPLETED_AT = "2026-08-19T18:30:00-04:00"

  def setup
    @temporary_roots = []
  end

  def teardown
    @temporary_roots.each { |path| FileUtils.remove_entry(path) if File.exist?(path) }
  end

  def test_batch_dm_preload_preserves_per_note_results
    root = make_vault
    write_note(root, "People/Alpha Person.md", person_note("Alpha Person"))
    write_note(root, "People/Beta Person.md", person_note("Beta Person"))
    write_note(
      root,
      "_DM_/Shared Notes.md",
      "# Shared Notes\n\n[[Alpha Person]] is linked. Beta Person is named.\n"
    )
    index = TaelgarNoteLint::NoteIndex.new(Pathname.new(root))
    notes = %w[Alpha\ Person Beta\ Person].map do |name|
      path = "People/#{name}.md"
      TaelgarNoteLint::ParsedNote.new(path, File.read(File.join(root, path)))
    end
    individual = TaelgarNoteLint::DMNoteScanner.new(root: root, index: index)
    expected = notes.to_h { |note| [note.path, individual.mentions(note)] }
    batched = TaelgarNoteLint::DMNoteScanner.new(root: root, index: index)

    batched.preload(notes)

    assert_equal expected, notes.to_h { |note| [note.path, batched.mentions(note)] }
  end

  def test_freshness_scanner_reuses_git_evidence_for_notes_with_one_baseline
    root = make_vault
    write_note(root, "People/Alpha Person.md", person_note("Alpha Person"))
    write_note(root, "People/Beta Person.md", person_note("Beta Person"))
    write_note(root, "Campaigns/Shared Update.md", "# Shared Update\n\n[[Alpha Person]] and [[Beta Person]] changed.\n")
    index = TaelgarNoteLint::NoteIndex.new(Pathname.new(root))
    scanner_class = Class.new(TaelgarNoteLint::FreshnessScanner) do
      attr_reader :calls

      def initialize(**arguments)
        @calls = []
        super
      end

      private

      def git(*arguments)
        @calls << arguments
        case arguments
        when ["diff", "--name-only", "-z", "baseline", "--"]
          "Campaigns/Shared Update.md\0"
        when ["diff", "--unified=0", "baseline", "--", "Campaigns/Shared Update.md"]
          "+[[Alpha Person]] and [[Beta Person]] changed.\n"
        when ["diff", "--numstat", "baseline", "--", "Campaigns/Shared Update.md"]
          "1\t0\tCampaigns/Shared Update.md\n"
        when ["log", "-1", "--format=%H%x09%cI%x09%s", "--", "Campaigns/Shared Update.md"]
          "abc123\t2026-08-19T12:00:00-04:00\tUpdate\n"
        else
          raise "Unexpected fake git call: #{arguments.inspect}"
        end
      end
    end
    scanner = scanner_class.new(root: root, index: index, baseline_ref: "baseline")

    ["Alpha Person", "Beta Person"].each do |name|
      scanner.scan("note" => { "path" => "People/#{name}.md" })
    end

    assert_equal 1, scanner.calls.count { |call| call[0, 3] == ["diff", "--name-only", "-z"] }
    assert_equal 1, scanner.calls.count { |call| call[0, 2] == ["diff", "--unified=0"] }
    assert_equal 1, scanner.calls.count { |call| call[0, 2] == ["diff", "--numstat"] }
    assert_equal 1, scanner.calls.count { |call| call[0] == "log" }
  end

  def test_preparer_marks_unlinted_notes_for_review_without_a_git_baseline
    root = make_vault
    write_note(root, "People/Alpha Person.md", person_note("Alpha Person", linted: false))

    manifest = TaelgarNoteLint::Batch::Preparer.new(root: root).prepare(["People/Alpha Person.md"])
    record = manifest.fetch("notes").first

    assert_equal "unlinted", record.dig("routing", "reason")
    assert record.dig("routing", "reviewRecommended")
    assert_equal "The note has no prior lint timestamp.", record.dig("freshness", "skipped")
    assert_equal TaelgarNoteLint::VERSION, manifest.fetch("validatorVersion")
  end

  def test_cli_discovers_linted_notes_on_the_vault_ruby_version
    root = make_vault
    write_note(root, "Meta/Current.md", meta_note("Current", version: TaelgarNoteLint::VERSION))
    write_note(root, "Meta/Stale.md", meta_note("Stale", version: "2.2"))
    cli = TaelgarNoteLint::Batch::CLI.new([])

    all = cli.send(:discover_paths, Pathname.new(root), all_linted: true, stale: false)
    stale = cli.send(:discover_paths, Pathname.new(root), all_linted: false, stale: true)

    assert_equal ["Meta/Current.md", "Meta/Stale.md"], all
    assert_equal ["Meta/Stale.md"], stale
  end

  def test_snapshot_and_finalizer_write_clean_and_open_states_together
    root = make_vault
    write_note(root, "Meta/Clean.md", meta_note("Clean", version: "2.2"))
    write_note(root, "Meta/Open.md", meta_note("Open", version: "2.2", open: true))
    manifest, manifest_sha = manifest_for(root, ["Meta/Clean.md", "Meta/Open.md"])

    clean_path = File.join(root, "Meta", "Clean.md")
    File.write(clean_path, File.read(clean_path).sub("name: Clean\n", "name: Clean\naliases: [Clean Note]\n"))
    decisions = TaelgarNoteLint::Batch::Snapshotter.new(
      root: root,
      manifest: manifest,
      manifest_sha256: manifest_sha
    ).snapshot
    decisions.fetch("notes").each do |decision|
      if decision["path"] == "Meta/Clean.md"
        decision["outcome"] = "clean"
      else
        decision["outcome"] = "open"
        decision["lintReport"] = <<~REPORT.strip
          %%^Lint%%
          - [ ] **Suggestion — review.open:** Human review is still required.
          %%^End%%
        REPORT
      end
    end

    result = finalizer(root, manifest, manifest_sha, decisions).finalize(write: true)
    clean = File.read(clean_path)
    open = File.read(File.join(root, "Meta", "Open.md"))

    assert result.fetch("wrote")
    assert_includes clean, "lintedAt: \"#{COMPLETED_AT}\""
    assert_includes clean, "lintVersion: \"#{TaelgarNoteLint::VERSION}\""
    assert_includes clean, "aliases: [Clean Note]"
    refute_includes clean, "status/check/lint"
    refute_includes clean, "%%^Lint%%"
    assert_includes open, "status/check/lint"
    assert_includes open, "review.open"
    assert_equal COMPLETED_AT, result.fetch("completedAt")
  end

  def test_finalizer_rejects_a_file_changed_after_snapshot
    root = make_vault
    write_note(root, "Meta/Clean.md", meta_note("Clean", version: "2.2"))
    manifest, manifest_sha = manifest_for(root, ["Meta/Clean.md"])
    decisions = snapshot(root, manifest, manifest_sha)
    decisions.fetch("notes").first["outcome"] = "clean"
    path = File.join(root, "Meta", "Clean.md")
    File.write(path, File.read(path).sub("# Clean", "# Clean changed elsewhere"))

    error = assert_raises(TaelgarNoteLint::Batch::BatchError) do
      finalizer(root, manifest, manifest_sha, decisions).finalize(write: true)
    end

    assert_includes error.message, "changed after snapshot"
    assert_includes File.read(path), 'lintVersion: "2.2"'
  end

  def test_finalizer_preflights_every_result_before_writing_any_note
    root = make_vault
    write_note(root, "Meta/First.md", meta_note("First", version: "2.2"))
    write_note(root, "Meta/Second.md", meta_note("Second", version: "2.2"))
    manifest, manifest_sha = manifest_for(root, ["Meta/First.md", "Meta/Second.md"])
    decisions = snapshot(root, manifest, manifest_sha)
    decisions.fetch("notes")[0]["outcome"] = "clean"
    decisions.fetch("notes")[1]["outcome"] = "open"
    decisions.fetch("notes")[1]["lintReport"] = "%%^Lint%%\nNo task.\n%%^End%%"

    assert_raises(TaelgarNoteLint::Batch::BatchError) do
      finalizer(root, manifest, manifest_sha, decisions).finalize(write: true)
    end

    assert_includes File.read(File.join(root, "Meta", "First.md")), 'lintVersion: "2.2"'
    assert_includes File.read(File.join(root, "Meta", "Second.md")), 'lintVersion: "2.2"'
  end

  private

  def make_vault
    root = Dir.mktmpdir("taelgar-batch-lint-test.")
    @temporary_roots << root
    FileUtils.mkdir_p(File.join(root, "_scripts"))
    File.write(
      File.join(root, "_scripts", "session_note_campaigns.json"),
      JSON.pretty_generate(
        "schemaVersion" => 2,
        "campaigns" => {
          "great-library" => {
            "name" => "Great Library",
            "code" => "grli",
            "aliases" => ["Great Library Campaign"]
          }
        }
      )
    )
    root
  end

  def write_note(root, relative_path, text)
    path = File.join(root, relative_path)
    FileUtils.mkdir_p(File.dirname(path))
    File.write(path, text)
  end

  def person_note(name, linted: false)
    lint_fields = linted ? "lintedAt: \"2026-08-19T09:00:00-04:00\"\nlintVersion: \"2.3\"\n" : ""
    <<~MARKDOWN
      ---
      headerVersion: 1
      #{lint_fields}tags: [person]
      name: #{name}
      species: human
      pronunciation: obvious
      knownTo: []
      POV: 1750
      ---
      # #{name}

      %%^Metadata:names:v1%%
      - {name: #{name}, language: Common, pronunciation: obvious}
      %%^End%%

      %%^Metadata:article:v1%%
      mode: biographical reference
      povNotes: Accuracy is centered on DR 1750.
      %%^End%%
    MARKDOWN
  end

  def meta_note(name, version:, open: false)
    tag = open ? "[meta, status/check/lint]" : "[meta]"
    report = if open
               <<~REPORT

                 %%^Lint%%
                 - [ ] **Suggestion — old.review:** Old review item.
                 %%^End%%
               REPORT
             else
               ""
             end
    <<~MARKDOWN
      ---
      headerVersion: 1
      lintedAt: "2026-08-19T09:00:00-04:00"
      lintVersion: "#{version}"
      tags: #{tag}
      name: #{name}
      POV: timeless
      ---
      # #{name}

      %%^Metadata:article:v1%%
      mode: meta reference
      povNotes: This note is not tied to an in-world date.
      %%^End%%
      #{report}
    MARKDOWN
  end

  def manifest_for(root, paths)
    records = paths.map do |path|
      text = File.read(File.join(root, path))
      note = TaelgarNoteLint::ParsedNote.new(path, text)
      {
        "path" => path,
        "priorCompletionState" => TaelgarNoteLint::Batch.completion_state(note)
      }
    end
    manifest = {
      "schemaVersion" => TaelgarNoteLint::Batch::SCHEMA_VERSION,
      "validatorVersion" => TaelgarNoteLint::VERSION,
      "notes" => records
    }
    manifest_text = "#{JSON.pretty_generate(manifest)}\n"
    [manifest, TaelgarNoteLint::Batch.sha256(manifest_text)]
  end

  def snapshot(root, manifest, manifest_sha)
    TaelgarNoteLint::Batch::Snapshotter.new(
      root: root,
      manifest: manifest,
      manifest_sha256: manifest_sha
    ).snapshot
  end

  def finalizer(root, manifest, manifest_sha, decisions)
    TaelgarNoteLint::Batch::Finalizer.new(
      root: root,
      manifest: manifest,
      manifest_sha256: manifest_sha,
      decisions: decisions,
      completed_at: COMPLETED_AT
    )
  end
end
