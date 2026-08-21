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

  def test_freshness_scanner_keeps_target_ineligible_markdown_notes_as_evidence
    root = make_vault
    target = "People/Alpha Person.md"
    write_note(root, target, person_note("Alpha Person", linted: true))
    git(root, "init", "-q")
    git(root, "config", "user.email", "lint-test@example.invalid")
    git(root, "config", "user.name", "Lint Test")
    git(root, "add", ".")
    git(root, "commit", "-q", "-m", "base")

    evidence_paths = [
      ".chatgpt/Hidden Evidence.md",
      "Campaigns/.chatgpt/Nested Hidden Evidence.md",
      "Campaigns/_generated/Generated Evidence.md",
      "Worldbuilding/Provisional Evidence.md"
    ]
    modified = Time.iso8601("2026-08-19T10:00:00-04:00")
    evidence_paths.each do |path|
      write_note(root, path, "# Evidence\n\n[[Alpha Person]] changed.\n")
      File.utime(modified, modified, File.join(root, path))
    end
    index = TaelgarNoteLint::NoteIndex.new(Pathname.new(root))
    assert_empty index.resolve("Hidden Evidence")
    assert_empty index.resolve("Nested Hidden Evidence")
    assert_equal ["Campaigns/_generated/Generated Evidence.md"], index.resolve("Generated Evidence")
    scanner = TaelgarNoteLint::FreshnessScanner.new(root: root, index: index, baseline_ref: "HEAD")

    freshness = scanner.scan(
      { "note" => { "path" => target } },
      linted_at: "2026-08-19T09:00:00-04:00"
    )

    assert_equal evidence_paths.sort, freshness.fetch("candidates").map { |item| item.fetch("path") }.sort
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

  def test_preparer_carries_the_pov_review_gate_without_changing_linter_version
    root = make_vault
    path = "Campaigns/Great Library Campaign/Session Notes/Session 1.md"
    write_note(
      root,
      path,
      <<~MARKDOWN
        ---
        lintedAt: "2026-08-19T09:00:00-04:00"
        lintVersion: "#{TaelgarNoteLint::POV_REVIEW_VERSION}"
        tags: [session-note]
        campaign: Great Library
        POV: 1748
        ---
        # Session 1

        The party crossed the river during this session.
      MARKDOWN
    )
    git(root, "init", "-q")
    git(root, "config", "user.email", "lint-test@example.invalid")
    git(root, "config", "user.name", "Lint Test")
    git(root, "add", ".")
    git(root, "commit", "-q", "-m", "record lint state")

    manifest = TaelgarNoteLint::Batch::Preparer.new(root: root).prepare([path])
    record = manifest.fetch("notes").first

    assert_equal "3.3", manifest.fetch("validatorVersion")
    refute record.dig("deterministic", "reviewGates", "pov", "required")
    refute record.dig("deterministic", "reviewGates", "pov", "povNotesApplicable")
    refute_includes record.dig("deterministic", "findings").map { |finding| finding.fetch("ruleId") },
                    "metadata.pov_notes_missing"
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
    report = { "summary" => { "errors" => 0 }, "findings" => [] }
    sources = [{ "path" => dm_path, "modifiedAt" => modified.iso8601(6), "matchKinds" => ["link"] }]
    preparer = TaelgarNoteLint::Batch::Preparer.allocate
    preparer.instance_variable_set(:@root, Pathname.new(root))

    dm_freshness = preparer.send(:dm_freshness_for, note, sources)
    routing = preparer.send(
      :routing_for,
      note,
      { "candidates" => [] },
      dm_freshness,
      report
    )

    assert_equal [dm_path], dm_freshness.fetch("candidates").map { |item| item.fetch("path") }
    assert_equal ["link"], dm_freshness.dig("candidates", 0, "matchKinds")
    assert routing.fetch("reviewRecommended")
    assert_equal "newer_private_dm_evidence", routing.fetch("reason")
  end

  def test_older_local_dm_evidence_does_not_route_a_validated_note
    root = make_vault
    path = "People/Alpha Person.md"
    text = person_note("Alpha Person", linted: true)
    write_note(root, path, text)
    note = TaelgarNoteLint::ParsedNote.new(path, text)
    sources = [
      {
        "path" => "_DM_/Existing Secret.md",
        "modifiedAt" => "2026-08-19T08:00:00-04:00",
        "matchKinds" => ["link"]
      }
    ]
    report = { "summary" => { "errors" => 0 }, "findings" => [] }
    preparer = TaelgarNoteLint::Batch::Preparer.allocate
    preparer.instance_variable_set(:@root, Pathname.new(root))

    dm_freshness = preparer.send(:dm_freshness_for, note, sources)
    routing = preparer.send(:routing_for, note, { "candidates" => [] }, dm_freshness, report)

    assert_empty dm_freshness.fetch("candidates")
    refute routing.fetch("reviewRecommended")
    assert_equal "current_with_no_newer_invention_candidate", routing.fetch("reason")
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
    write_note(root, "Campaigns/_generated/Linted.md", meta_note("Generated Lint", version: "2.2"))
    write_note(root, "Campaigns/.chatgpt/Linted.md", meta_note("Hidden Lint", version: "2.2"))
    cli = TaelgarNoteLint::Batch::CLI.new([])

    all = cli.send(:discover_paths, Pathname.new(root), all_linted: true, stale: false)
    stale = cli.send(:discover_paths, Pathname.new(root), all_linted: false, stale: true)

    assert_equal ["Meta/Current.md", "Meta/Stale.md"], all
    assert_equal ["Meta/Stale.md"], stale
  end

  def test_preparer_rejects_any_worldbuilding_dot_or_underscore_directory_segment
    root = make_vault
    paths = [
      "Worldbuilding/Idea.md",
      "Campaigns/Worldbuilding/Idea.md",
      ".chatgpt/Idea.md",
      "Campaigns/.chatgpt/Idea.md",
      "_generated/Idea.md",
      "Campaigns/_generated/Idea.md"
    ]
    paths.each { |path| write_note(root, path, "# Idea\n") }

    paths.each do |path|
      error = assert_raises(TaelgarNoteLint::Batch::BatchError) do
        TaelgarNoteLint::Batch::Preparer.new(root: root).prepare([path])
      end

      assert_includes error.message, "outside Taelgar Note Linter scope"
    end
  end

  def test_cli_skips_objectively_sentence_less_notes_before_preparation
    root = make_vault
    notes = {
      "Meta/Frontmatter Only.md" => "---\ntags: [meta]\n---\n",
      "Meta/Heading Only.md" => "---\ntags: [meta]\n---\n# Heading Only\n",
      "Meta/Image Only.md" => "---\ntags: [source]\n---\n![[map.png]]\n",
      "Meta/Comment Sentence.md" => "---\ntags: [meta]\n---\n# Comment Sentence\n\n%% This comment records a complete subject-matter sentence. %%\n"
    }
    notes.each { |path, text| write_note(root, path, text) }
    output = File.join(root, "manifest.json")

    result = TaelgarNoteLint::Batch::CLI.new(
      ["prepare", "--root", root, "--output", output, *notes.keys]
    ).run
    manifest = JSON.parse(File.read(output))

    assert_equal 0, result
    assert_equal ["Meta/Comment Sentence.md"], manifest.fetch("notes").map { |note| note.fetch("path") }
    assert_equal 4, manifest.dig("selectionSummary", "requested")
    assert_equal 3, manifest.dig("selectionSummary", "skippedNoReviewableProse")
    assert_equal [
      "Meta/Frontmatter Only.md",
      "Meta/Heading Only.md",
      "Meta/Image Only.md"
    ], manifest.dig("selectionSummary", "skippedNoReviewableProsePaths").sort
    assert_equal 0, manifest.dig("selectionSummary", "skippedAlreadyLinted")
  end

  def test_preparer_snapshot_and_finalizer_reject_objectively_sentence_less_notes
    root = make_vault
    path = "Meta/Heading Only.md"
    write_note(root, path, "---\ntags: [meta]\n---\n# Heading Only\n")

    prepare_error = assert_raises(TaelgarNoteLint::Batch::BatchError) do
      TaelgarNoteLint::Batch::Preparer.new(root: root).prepare([path])
    end

    manifest, manifest_sha = manifest_for(root, [path])
    snapshot_error = assert_raises(TaelgarNoteLint::Batch::BatchError) do
      snapshot(root, manifest, manifest_sha)
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

    [prepare_error, snapshot_error, finalize_error].each do |error|
      assert_includes error.message, "no authored body candidate"
    end
  end

  def test_snapshot_and_finalizer_reject_legacy_ineligible_manifests
    root = make_vault
    path = "Campaigns/_generated/Old Lint.md"
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

    assert_includes snapshot_error.message, "outside Taelgar Note Linter scope"
    assert_includes finalize_error.message, "outside Taelgar Note Linter scope"
  end

  def test_cli_skips_valid_prior_lints_unless_relint_is_explicit
    root = make_vault
    current = "Meta/Current.md"
    stale = "Meta/Stale.md"
    unlinted = "People/Unlinted.md"
    write_note(root, current, meta_note("Current", version: TaelgarNoteLint::VERSION))
    write_note(root, stale, meta_note("Stale", version: "2.2"))
    write_note(root, unlinted, person_note("Unlinted"))
    git(root, "init", "-q")
    git(root, "config", "user.email", "lint-test@example.invalid")
    git(root, "config", "user.name", "Lint Test")
    git(root, "add", ".")
    git(root, "commit", "-q", "-m", "base")
    ordinary_output = File.join(root, "ordinary.json")
    relint_output = File.join(root, "relint.json")

    ordinary_result = TaelgarNoteLint::Batch::CLI.new(
      ["prepare", "--root", root, "--output", ordinary_output, current, stale, unlinted]
    ).run
    relint_result = TaelgarNoteLint::Batch::CLI.new(
      ["prepare", "--root", root, "--re-lint", "--output", relint_output, current, stale]
    ).run
    ordinary = JSON.parse(File.read(ordinary_output))
    relint = JSON.parse(File.read(relint_output))

    assert_equal 0, ordinary_result
    assert_equal [unlinted], ordinary.fetch("notes").map { |note| note.fetch("path") }
    assert_equal 2, ordinary.dig("selectionSummary", "skippedAlreadyLinted")
    assert_equal 0, relint_result
    assert_equal [current, stale].sort, relint.fetch("notes").map { |note| note.fetch("path") }.sort
  end

  def test_cli_requires_explicit_relint_for_linted_discovery_flags
    root = make_vault
    _stdout, stderr = capture_io do
      result = TaelgarNoteLint::Batch::CLI.new(["prepare", "--root", root, "--all-linted"]).run
      assert_equal 2, result
    end

    assert_includes stderr, "require --re-lint"
  end

  def test_cli_rejects_broad_discovery_mixed_with_named_scope
    root = make_vault
    _stdout, stderr = capture_io do
      result = TaelgarNoteLint::Batch::CLI.new(
        ["prepare", "--root", root, "--re-lint", "--all-linted", "Meta/Named.md"]
      ).run
      assert_equal 2, result
    end

    assert_includes stderr, "cannot be combined with named targets"
  end

  def test_cli_returns_an_empty_manifest_when_no_stale_notes_exist
    root = make_vault
    write_note(root, "Meta/Current.md", meta_note("Current", version: TaelgarNoteLint::VERSION))
    output = File.join(root, "empty-stale-manifest.json")

    result = TaelgarNoteLint::Batch::CLI.new(
      ["prepare", "--root", root, "--re-lint", "--stale", "--output", output]
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
    result.fetch("notes").each do |record|
      assert_equal record.fetch("sha256"), TaelgarNoteLint::Batch.file_sha256(File.join(root, record.fetch("path")))
    end
  end

  def test_finalizer_rolls_back_a_post_write_checksum_mismatch
    root = make_vault
    path = "Meta/Clean.md"
    write_note(root, path, meta_note("Clean", version: "2.2"))
    original = File.read(File.join(root, path))
    manifest, manifest_sha = manifest_for(root, [path])
    decisions = snapshot(root, manifest, manifest_sha)
    decisions.fetch("notes").first["outcome"] = "clean"
    corrupting_finalizer = Class.new(TaelgarNoteLint::Batch::Finalizer) do
      private

      def stage_candidate(candidate)
        entry = super
        File.open(entry.fetch("new_file").path, "ab") { |file| file.write("\ncorrupted after staging\n") }
        entry
      end
    end

    error = assert_raises(TaelgarNoteLint::Batch::BatchError) do
      corrupting_finalizer.new(
        root: root,
        manifest: manifest,
        manifest_sha256: manifest_sha,
        decisions: decisions,
        completed_at: COMPLETED_AT
      ).finalize(write: true)
    end

    assert_includes error.message, "Written file checksum mismatch"
    assert_equal original, File.read(File.join(root, path))
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

      #{name} is a documented person in this test vault.

      %%^Metadata:names:v1%%
      - {name: #{name}, language: Common, pronunciation: NAYM}
      %%^End%%

      %%^povNotes:v1%%
      Temporal coverage: a DR 1750 biographical portrait.
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

      #{name} describes a lint workflow fixture in this test vault.

      %%^povNotes:v1%%
      Temporal coverage: modern; this meta reference has no narrower in-world limitation.
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
