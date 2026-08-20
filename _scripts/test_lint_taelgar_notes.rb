# frozen_string_literal: true

require "fileutils"
require "json"
require "minitest/autorun"
require "open3"
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
        when ["ls-files", "--others", "--exclude-standard", "-z", "--"]
          ""
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

  def test_freshness_scanner_includes_newer_untracked_invention_sources
    root = make_vault
    write_note(root, "People/Alpha Person.md", person_note("Alpha Person", linted: true))
    git(root, "init", "-q")
    git(root, "config", "user.email", "lint-test@example.invalid")
    git(root, "config", "user.name", "Lint Test")
    git(root, "add", ".")
    git(
      root,
      "commit",
      "-q",
      "-m",
      "base",
      env: {
        "GIT_AUTHOR_DATE" => "2026-08-19T08:00:00-04:00",
        "GIT_COMMITTER_DATE" => "2026-08-19T08:00:00-04:00"
      }
    )
    source = File.join(root, "Campaigns", "New Invention.md")
    write_note(root, "Campaigns/New Invention.md", "# New Invention\n\n[[Alpha Person]] gained a title.\n")
    modified = Time.iso8601("2026-08-19T10:00:00-04:00")
    File.utime(modified, modified, source)
    index = TaelgarNoteLint::NoteIndex.new(Pathname.new(root))
    scanner = TaelgarNoteLint::FreshnessScanner.new(root: root, index: index, baseline_ref: "HEAD")

    freshness = scanner.scan(
      { "note" => { "path" => "People/Alpha Person.md" } },
      linted_at: "2026-08-19T09:00:00-04:00"
    )
    candidate = freshness.fetch("candidates").first

    refute_nil candidate
    assert_equal "Campaigns/New Invention.md", candidate.fetch("path")
    assert candidate.fetch("mentionChanged")
    assert candidate.fetch("workingTreeChanged")
    assert_nil candidate.fetch("lastCommit")
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

  def test_newer_local_dm_evidence_routes_a_current_note_for_review
    root = make_vault
    path = "People/Alpha Person.md"
    text = person_note("Alpha Person", linted: true)
    write_note(root, path, text)
    dm_path = "_DM_/New Secret.md"
    write_note(root, dm_path, "# New Secret\n\n[[Alpha Person]] has a new secret.\n")
    modified = Time.iso8601("2026-08-19T10:00:00-04:00")
    File.utime(modified, modified, File.join(root, dm_path))
    note = TaelgarNoteLint::ParsedNote.new(path, text)
    report = {
      "summary" => { "errors" => 0 },
      "findings" => [
        {
          "ruleId" => "dm.notes_private_evidence_found",
          "details" => { "sources" => [{ "path" => dm_path }] }
        }
      ]
    }
    preparer = TaelgarNoteLint::Batch::Preparer.allocate
    preparer.instance_variable_set(:@root, Pathname.new(root))

    dm_freshness = preparer.send(:dm_freshness_for, note, report)
    routing = preparer.send(
      :routing_for,
      note,
      { "candidates" => [] },
      dm_freshness,
      report
    )

    assert_equal [dm_path], dm_freshness.fetch("candidates").map { |item| item.fetch("path") }
    assert routing.fetch("reviewRecommended")
    assert_equal "newer_private_dm_evidence", routing.fetch("reason")
  end

  def test_git_baseline_prefers_the_commit_that_records_the_lint_state
    root = make_vault
    write_note(root, "Meta/Current.md", meta_note("Current", version: TaelgarNoteLint::VERSION))
    git(root, "init", "-q")
    git(root, "config", "user.email", "lint-test@example.invalid")
    git(root, "config", "user.name", "Lint Test")
    git(root, "add", ".")
    commit = git(
      root,
      "commit",
      "-q",
      "-m",
      "record lint state",
      env: {
        "GIT_AUTHOR_DATE" => "2026-08-19T10:00:00-04:00",
        "GIT_COMMITTER_DATE" => "2026-08-19T10:00:00-04:00"
      }
    )
    ref = git(root, "rev-parse", "HEAD").strip
    path = "Meta/Current.md"
    note = TaelgarNoteLint::ParsedNote.new(path, File.read(File.join(root, path)))

    baseline = TaelgarNoteLint::Batch::GitBaselineResolver.new(root).resolve(note)

    assert_equal ref, baseline.fetch("ref")
    assert_equal "lint_state_commit", baseline.fetch("kind")
    assert_equal "", commit
  end

  def test_git_baseline_falls_back_to_the_timestamp_commit_while_lint_state_is_uncommitted
    root = make_vault
    write_note(root, "Meta/Current.md", "---\ntags: [meta]\nname: Current\n---\n# Current\n")
    git(root, "init", "-q")
    git(root, "config", "user.email", "lint-test@example.invalid")
    git(root, "config", "user.name", "Lint Test")
    git(root, "add", ".")
    git(
      root,
      "commit",
      "-q",
      "-m",
      "base",
      env: {
        "GIT_AUTHOR_DATE" => "2026-08-19T08:00:00-04:00",
        "GIT_COMMITTER_DATE" => "2026-08-19T08:00:00-04:00"
      }
    )
    ref = git(root, "rev-parse", "HEAD").strip
    write_note(root, "Meta/Current.md", meta_note("Current", version: TaelgarNoteLint::VERSION))
    path = "Meta/Current.md"
    note = TaelgarNoteLint::ParsedNote.new(path, File.read(File.join(root, path)))

    baseline = TaelgarNoteLint::Batch::GitBaselineResolver.new(root).resolve(note)

    assert_equal ref, baseline.fetch("ref")
    assert_equal "timestamp_commit", baseline.fetch("kind")
  end

  def test_git_baseline_survives_human_clearing_of_report_and_tag
    root = make_vault
    write_note(root, "Meta/Current.md", meta_note("Current", version: TaelgarNoteLint::VERSION, open: true))
    git(root, "init", "-q")
    git(root, "config", "user.email", "lint-test@example.invalid")
    git(root, "config", "user.name", "Lint Test")
    git(root, "add", ".")
    git(
      root,
      "commit",
      "-q",
      "-m",
      "record open lint",
      env: {
        "GIT_AUTHOR_DATE" => "2026-08-19T10:00:00-04:00",
        "GIT_COMMITTER_DATE" => "2026-08-19T10:00:00-04:00"
      }
    )
    ref = git(root, "rev-parse", "HEAD").strip
    write_note(root, "Meta/Current.md", meta_note("Current", version: TaelgarNoteLint::VERSION))
    path = "Meta/Current.md"
    note = TaelgarNoteLint::ParsedNote.new(path, File.read(File.join(root, path)))

    baseline = TaelgarNoteLint::Batch::GitBaselineResolver.new(root).resolve(note)

    assert_equal ref, baseline.fetch("ref")
    assert_equal "lint_state_commit", baseline.fetch("kind")
  end

  def test_cli_discovers_linted_notes_on_the_vault_ruby_version
    root = make_vault
    write_note(root, "Meta/Current.md", meta_note("Current", version: TaelgarNoteLint::VERSION))
    write_note(root, "Meta/Stale.md", meta_note("Stale", version: "2.2"))
    write_note(root, "Worldbuilding/Linted.md", meta_note("Linted Worldbuilding", version: "2.2"))
    cli = TaelgarNoteLint::Batch::CLI.new([])

    all = cli.send(:discover_paths, Pathname.new(root), all_linted: true, stale: false)
    stale = cli.send(:discover_paths, Pathname.new(root), all_linted: false, stale: true)

    assert_equal ["Meta/Current.md", "Meta/Stale.md"], all
    assert_equal ["Meta/Stale.md"], stale
  end

  def test_preparer_rejects_explicit_worldbuilding_targets
    root = make_vault
    write_note(root, "Worldbuilding/Idea.md", "# Idea\n")

    error = assert_raises(TaelgarNoteLint::Batch::BatchError) do
      TaelgarNoteLint::Batch::Preparer.new(root: root).prepare(["Worldbuilding/Idea.md"])
    end

    assert_includes error.message, "Worldbuilding notes are outside"
  end

  def test_snapshot_and_finalizer_reject_legacy_worldbuilding_manifests
    root = make_vault
    path = "Worldbuilding/Old Lint.md"
    write_note(root, path, meta_note("Old Lint", version: TaelgarNoteLint::VERSION))
    manifest, manifest_sha = manifest_for(root, [path])

    snapshot_error = assert_raises(TaelgarNoteLint::Batch::BatchError) do
      TaelgarNoteLint::Batch::Snapshotter.new(
        root: root,
        manifest: manifest,
        manifest_sha256: manifest_sha
      ).snapshot
    end

    decisions = {
      "schemaVersion" => TaelgarNoteLint::Batch::DECISION_SCHEMA_VERSION,
      "validatorVersion" => TaelgarNoteLint::VERSION,
      "manifestSha256" => manifest_sha,
      "notes" => [
        {
          "path" => path,
          "expectedSha256" => TaelgarNoteLint::Batch.file_sha256(File.join(root, path)),
          "outcome" => "clean",
          "lintReport" => nil
        }
      ]
    }
    finalize_error = assert_raises(TaelgarNoteLint::Batch::BatchError) do
      finalizer(root, manifest, manifest_sha, decisions).finalize
    end

    assert_includes snapshot_error.message, "Worldbuilding notes are outside"
    assert_includes finalize_error.message, "Worldbuilding notes are outside"
  end

  def test_cli_returns_an_empty_manifest_when_no_stale_notes_exist
    root = make_vault
    write_note(root, "Meta/Current.md", meta_note("Current", version: TaelgarNoteLint::VERSION))
    output = File.join(root, "empty-stale-manifest.json")

    result = TaelgarNoteLint::Batch::CLI.new(
      ["prepare", "--root", root, "--stale", "--output", output]
    ).run
    manifest = JSON.parse(File.read(output))

    assert_equal 0, result
    assert_equal [], manifest.fetch("notes")
    assert_equal 0, manifest.dig("selectionSummary", "selected")
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

  def test_finalizer_replaces_old_report_containing_copy_ready_block_markers
    root = make_vault
    path = "Meta/Open.md"
    text = meta_note("Open", version: "2.2", open: true).sub(
      "- [ ] **Suggestion — old.review:** Old review item.",
      "- [ ] **Suggestion — old.review:** Copy `%%^Campaign:dufr%% Example. %%^End%%`."
    )
    write_note(root, path, text)
    manifest, manifest_sha = manifest_for(root, [path])
    decisions = snapshot(root, manifest, manifest_sha)
    decision = decisions.fetch("notes").first
    decision["outcome"] = "open"
    decision["lintReport"] = <<~REPORT.strip
      %%^Lint%%
      - [ ] **Suggestion — review.current:** Human review is still required.
      %%^End%%
    REPORT

    finalizer(root, manifest, manifest_sha, decisions).finalize(write: true)
    result = File.read(File.join(root, path))

    refute_includes result, "old.review"
    refute_includes result, "Campaign:dufr"
    assert_equal 1, result.scan("%%^Lint%%").length
    assert_includes result, "review.current"
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
    lint_fields = linted ? "lintedAt: \"2026-08-19T09:00:00-04:00\"\nlintVersion: \"#{TaelgarNoteLint::VERSION}\"\n" : ""
    <<~MARKDOWN
      ---
      headerVersion: 1
      #{lint_fields}tags: [person]
      name: #{name}
      species: human
      pronunciation: NAYM
      knownTo: []
      POV: 1750
      ---
      # #{name}

      %%^Metadata:names:v1%%
      - {name: #{name}, language: Common, pronunciation: NAYM}
      %%^End%%

      %%^Metadata:article:v1%%
      mode: biographical reference
      povNotes: "Temporal coverage: a DR 1750 biographical portrait."
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
      POV: modern
      ---
      # #{name}

      %%^Metadata:article:v1%%
      mode: meta reference
      povNotes: "Temporal coverage: modern; this meta reference has no narrower in-world limitation."
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

  def git(root, *arguments, env: {})
    stdout, stderr, status = Open3.capture3(env, "git", *arguments, chdir: root)
    raise "git #{arguments.join(' ')} failed: #{stderr}" unless status.success?

    stdout
  end
end
