# frozen_string_literal: true

require "fileutils"
require "json"
require "minitest/autorun"
require "open3"
require "tmpdir"

require_relative "validate_taelgar_note"

class ValidateTaelgarNoteTest < Minitest::Test
  FIXTURE_PATH = File.join(__dir__, "tests", "fixtures", "taelgar_note_lint_trial.json")

  def setup
    @temporary_roots = []
  end

  def teardown
    @temporary_roots.each { |path| FileUtils.remove_entry(path) if File.exist?(path) }
  end

  def test_six_note_trial_fixtures_preserve_expected_deterministic_findings
    fixture = JSON.parse(File.read(FIXTURE_PATH))
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)

    fixture.fetch("cases").each do |test_case|
      path = File.join(root, test_case.fetch("path"))
      FileUtils.mkdir_p(File.dirname(path))
      File.write(path, test_case.fetch("note"))
      before = File.binread(path)

      report = validator.validate_path(path)
      rule_ids = report.fetch("findings").map { |finding| finding.fetch("ruleId") }

      test_case.fetch("expectedRuleIds").each do |rule_id|
        assert_includes rule_ids, rule_id, "#{test_case.fetch('id')} should include #{rule_id}"
      end
      assert_equal before, File.binread(path), "validation must not modify #{test_case.fetch('id')}"
      assert_equal 0, report.fetch("summary").fetch("errors"), "#{test_case.fetch('id')} should have no structural errors"
    end
  end

  def test_detailed_place_vocabulary_accepts_building_and_rejects_the_documentation_typo
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    valid = validator.validate_text(
      "Gazetteer/Tower.md",
      "---\nheaderVersion: 1\ntags: [place]\nname: Tower\ntypeOf: building\naudience: [all]\n---\n# Tower\n"
    )
    invalid = validator.validate_text(
      "Gazetteer/Tower.md",
      "---\nheaderVersion: 1\ntags: [place]\nname: Tower\ntypeOf: buliding\naudience: [all]\n---\n# Tower\n"
    )

    refute_includes rule_ids(valid), "classification.place_type_unknown"
    assert_includes rule_ids(invalid), "classification.place_type_unknown"
  end

  def test_link_and_relationship_resolution_are_scoped_to_the_target_note
    root = make_vault
    write_note(root, "Gazetteer/Voltara.md", "---\ntags: [place]\nname: Voltara\ntypeOf: settlement\naudience: [all]\n---\n# Voltara\n")
    write_note(
      root,
      "People/Julius.md",
      "---\ntags: [person]\nname: Julius\nspecies: human\nwhereabouts: Voltara\nknownTo: [GL]\n---\n# Julius\n\nSee [[Voltara]] and [[Missing Manor]].\n"
    )
    index = TaelgarNoteLint::NoteIndex.new(Pathname.new(root))
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: true, index: index)
    report = validator.validate_path("People/Julius.md")

    assert_equal 1, report.fetch("findings").count { |finding| finding["ruleId"] == "link.unresolved" }
    refute(report.fetch("findings").any? do |finding|
      finding["ruleId"] == "relationship.unresolved" && finding.dig("details", "target") == "Voltara"
    end)
  end

  def test_invalid_utf8_in_markdown_is_reported_without_aborting_the_index
    root = make_vault
    path = File.join(root, "People", "Broken Encoding.md")
    FileUtils.mkdir_p(File.dirname(path))
    File.binwrite(path, "---\ntags: [person]\nspecies: human\nknownTo: []\naudience: [all]\n---\n# Broken \xFF\n".b)

    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    report = validator.validate_path(path)

    assert_includes rule_ids(report), "file.invalid_utf8"
    assert_equal 1, report.fetch("summary").fetch("errors")
  end

  def test_unknown_structured_content_marker_is_an_error
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    report = validator.validate_text(
      "Campaigns/Great Library Campaign/Typo.md",
      "---\ntags: [meta]\ncampaign: GL\n---\n%%^Campagin:GL%%\nHidden text\n%%^End%%\n"
    )

    assert_includes rule_ids(report), "syntax.unknown_content_marker"
    assert_equal 1, report.fetch("summary").fetch("errors")
  end

  def test_campaign_identity_applies_to_documents_not_entities_in_campaign_directories
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)

    entity = validator.validate_text(
      "Campaigns/Great Library Campaign/Treasure/Hammer.md",
      "---\ntags: [object]\ntypeOf: weapon\nknownTo: [GL]\n---\n# Hammer\n"
    )
    refute_includes rule_ids(entity), "campaign.document_missing"
    refute_includes rule_ids(entity), "campaign.directory_missing"
    refute_includes rule_ids(entity), "campaign.session_missing"

    source = validator.validate_text(
      "Campaigns/Great Library Campaign/Handouts/Letter.md",
      "---\ntags: [source]\naudience: [all]\n---\n# Letter\n"
    )
    assert_includes rule_ids(source), "campaign.document_missing"
    refute_includes rule_ids(source), "classification.descriptive_tag_missing"

    session = validator.validate_text(
      "Campaigns/Great Library Campaign/Session Notes/Session 2.md",
      "---\ntags: [session-note]\n---\n# Session 2\n"
    )
    assert_includes rule_ids(session), "campaign.session_missing"

    misplaced = validator.validate_text(
      "Campaigns/Great Library Campaign/Treasure/Hammer.md",
      "---\ntags: [object]\ntypeOf: weapon\ncampaign: GL\n---\n# Hammer\n"
    )
    assert_includes rule_ids(misplaced), "campaign.unexpected_entity_field"
    refute_includes rule_ids(misplaced), "campaign.audience_unclassified"
  end

  def test_known_to_is_required_for_people_and_objects_but_audience_is_not_universal
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)

    person = validator.validate_text(
      "People/Julius.md",
      "---\ntags: [person]\nspecies: human\ncampaignInfo: [{campaign: GL, date: 1748}]\n---\n# Julius\n"
    )
    object = validator.validate_text(
      "Campaigns/Great Library Campaign/Treasure/Hammer.md",
      "---\ntags: [object]\ntypeOf: weapon\ncampaignInfo: [{campaign: GL, date: 1748}]\n---\n# Hammer\n"
    )

    assert_includes rule_ids(person), "campaign.missing_known_to"
    assert_includes rule_ids(object), "campaign.missing_known_to"
    assert_includes rule_ids(person), "campaign.known_to_missing"
    assert_includes rule_ids(object), "campaign.known_to_missing"
    refute_includes rule_ids(person), "campaign.audience_unclassified"
    refute_includes rule_ids(object), "campaign.audience_unclassified"
  end

  def test_pronunciation_requires_contextual_disposition_for_named_subjects
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    missing = validator.validate_text(
      "People/Julius.md",
      "---\ntags: [person]\nspecies: human\n---\n# Julius\n"
    )
    present = validator.validate_text(
      "People/Julius.md",
      "---\ntags: [person]\nspecies: human\npronunciation: JOO-lee-us\n---\n# Julius\n"
    )
    source = validator.validate_text(
      "Campaigns/Great Library Campaign/Handouts/Letter.md",
      "---\ntags: [source]\ncampaign: GL\n---\n# Letter\n"
    )
    obvious = validator.validate_text(
      "People/Thomas Hawke.md",
      "---\ntags: [person]\nspecies: human\nknownTo: []\n---\n# Thomas Hawke\n\n%%^Metadata:names:v1%%\n- {name: Thomas Hawke, language: Common, pronunciation: obvious}\n%%^End%%\n"
    )

    assert_includes rule_ids(missing), "pronunciation.missing_or_exception"
    refute_includes rule_ids(present), "pronunciation.missing_or_exception"
    refute_includes rule_ids(source), "pronunciation.missing_or_exception"
    refute_includes rule_ids(obvious), "pronunciation.missing_or_exception"
  end

  def test_trial_metadata_and_lint_blocks_are_recognized_and_validated
    root = make_vault
    index = TaelgarNoteLint::NoteIndex.new(Pathname.new(root))
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: true, index: index)
    report = validator.validate_text(
      "Gazetteer/River.md",
      <<~MARKDOWN
        ---
        lintedAt: "2026-08-19T00:00:00-04:00"
        lintVersion: "2.1"
        tags: [place]
        typeOf: waterway
        pronunciation: RIH-ver
        ---
        %%^Metadata:article:v1%%
        profile: place
        mode: geographic reference
        pov: current
        %%^End%%

        %%^Metadata:names:v1%%
        - {name: River, language: Common, pronunciation: RIH-ver}
        %%^End%%

        %%^Metadata:map:v1%%
        locations:
          - {geometry: path, map: world, sourceHex: "01.01.A01", outletHex: "01.01.B02"}
        %%^End%%

        # River

        %%^Lint%%
        Trial report quotes a fixed typo: climatic victory.
        It may also mention a deliberately unresolved report-only link: [[Missing Review Source]].
        Copy candidate: %% (POV:: 1748) %%
        %%^End%%
      MARKDOWN
    )

    refute rule_ids(report).any? { |rule_id| rule_id == "syntax.unknown_content_marker" }
    refute rule_ids(report).any? { |rule_id| rule_id.start_with?("metadata.invalid_") }
    refute_includes rule_ids(report), "lint.state_incomplete"
    refute_includes rule_ids(report), "identity.implicit_name"
    refute_includes rule_ids(report), "editorial.common_typo"
    refute_includes rule_ids(report), "link.unresolved"
    refute_includes rule_ids(report), "privacy.shared_comment"
    refute_includes rule_ids(report), "temporal.inline_pov"
  end

  def test_lint_state_fields_must_be_written_together
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    report = validator.validate_text(
      "People/Julius.md",
      "---\ntags: [person]\nspecies: human\npronunciation: JOO-lee-us\nlintedAt: invalid\n---\n# Julius\n"
    )

    assert_includes rule_ids(report), "lint.state_incomplete"
  end

  def test_malformed_name_block_reports_errors_without_aborting_identity_checks
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    report = validator.validate_text(
      "People/Julius.md",
      "---\ntags: [person]\nspecies: human\nknownTo: []\n---\n# Julius\n\n%%^Metadata:names:v1%%\n- not-a-mapping\n%%^End%%\n"
    )

    assert_includes rule_ids(report), "identity.implicit_name"
    assert_includes rule_ids(report), "metadata.names_shape"
  end

  def test_frontmatter_formatter_applies_full_order_and_collection_shapes
    note = TaelgarNoteLint::ParsedNote.new(
      "People/Test.md",
      <<~MARKDOWN
        ---
        dm_notes: none
        aliases:
          - First
          - Second
        subTypeOf: obsolete
        whereabouts:
          - type: home
            location: Voltara
        tags:
          - person
          - status/check/lint
        displayDefaults:
          endStatus: absent
        lintVersion: 2.1
        headerVersion: 2023.11.25
        lintedAt: 2026-08-19T09:00:00-04:00
        customField: keep-me
        name: Test
        species: human
        knownTo:
          - GL
        ---
        # Test
      MARKDOWN
    )

    formatted = TaelgarNoteLint::FrontmatterFormatter.new(note).format_text
    expected_fields = %w[subTypeOf headerVersion lintedAt lintVersion displayDefaults tags species customField name aliases whereabouts knownTo dm_notes]
    reparsed = TaelgarNoteLint::ParsedNote.new("People/Test.md", formatted)

    assert_equal expected_fields, reparsed.field_order
    assert_includes formatted, "tags: [person, status/check/lint]"
    assert_includes formatted, "aliases: [First, Second]"
    assert_includes formatted, "displayDefaults: {endStatus: absent}"
    assert_includes formatted, "whereabouts:\n  - {type: home, location: Voltara}"
    assert_includes formatted, 'lintedAt: "2026-08-19T09:00:00-04:00"'
    assert_includes formatted, 'lintVersion: "2.1"'
    assert_equal formatted, TaelgarNoteLint::FrontmatterFormatter.new(reparsed).format_text
  end

  def test_frontmatter_formatter_refuses_comments_it_cannot_preserve_safely
    note = TaelgarNoteLint::ParsedNote.new(
      "People/Test.md",
      "---\ntags: [person] # explain this\nspecies: human\nknownTo: []\n---\n# Test\n"
    )

    assert_raises(TaelgarNoteLint::FrontmatterFormatter::UnsafeFrontmatter) do
      TaelgarNoteLint::FrontmatterFormatter.new(note).format_text
    end
  end

  def test_map_blocks_are_required_for_waterways_roads_and_settlements
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)

    %w[waterway road settlement].each do |type|
      report = validator.validate_text(
        "Gazetteer/Test.md",
        "---\ntags: [place]\ntypeOf: #{type}\n---\n# Test\n"
      )
      assert_includes rule_ids(report), "metadata.map_missing"
    end

    optional = validator.validate_text(
      "Gazetteer/Test.md",
      "---\ntags: [place]\ntypeOf: forest\n---\n# Test\n"
    )
    refute_includes rule_ids(optional), "metadata.map_missing"
  end

  def test_world_hex_locator_requires_world_map
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    report = validator.validate_text(
      "Gazetteer/Test Road.md",
      "---\ntags: [place]\ntypeOf: road\n---\n%%^Metadata:map:v1%%\nlocations:\n  - {geometry: path, map: regional, hex: 13.07.F16}\n%%^End%%\n# Test Road\n"
    )

    assert_includes rule_ids(report), "metadata.map_world_hex_mismatch"
  end

  def test_private_comment_forms_remain_semantically_distinct
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)

    secret = validator.validate_text(
      "People/Hidden.md",
      "---\ntags: [person]\nspecies: human\naudience: [all]\n---\n# Hidden\n\n%%SECRET\nLocal secret.\n%%\n"
    )
    assert_includes rule_ids(secret), "privacy.secret_block"
    refute_includes rule_ids(secret), "privacy.shared_comment"
    refute rule_ids(secret).any? { |rule_id| rule_id.include?("legacy") }

    shared = validator.validate_text(
      "People/Shared.md",
      "---\ntags: [person]\nspecies: human\naudience: [all]\n---\n# Shared\n\n%% Shared DM context. %%\n"
    )
    assert_includes rule_ids(shared), "privacy.shared_comment"
    refute_includes rule_ids(shared), "dm.metadata_missing"

    structured = validator.validate_text(
      "People/Structured.md",
      "---\ntags: [person]\nspecies: human\naudience: [all]\n---\n# Structured\n\n%%^Campaign:none%%\nShared structured DM context.\n%%^End%%\n"
    )
    refute_includes rule_ids(structured), "privacy.shared_comment"
    refute_includes rule_ids(structured), "privacy.secret_block"

    legacy_case = validator.validate_text(
      "People/Legacy Case.md",
      "---\ntags: [person]\nspecies: human\naudience: [all]\n---\n# Legacy Case\n\n%%^Campaign:None%%\nShared structured DM context.\n%%^End%%\n"
    )
    assert_includes rule_ids(legacy_case), "syntax.noncanonical_campaign_block"
    refute_includes rule_ids(legacy_case), "syntax.unknown_campaign_block"

    alias_code = validator.validate_text(
      "People/Campaign Alias.md",
      "---\ntags: [person]\nspecies: human\naudience: [all]\n---\n# Campaign Alias\n\n%%^Campaign:gl%%\nCampaign material.\n%%^End%%\n"
    )
    assert_includes rule_ids(alias_code), "syntax.noncanonical_campaign_block"
    refute_includes rule_ids(alias_code), "syntax.unknown_campaign_block"
  end

  def test_git_freshness_nominates_sources_without_deciding_materiality
    root = make_vault
    write_note(
      root,
      "People/Julius.md",
      "---\ntags: [person]\nname: Julius Prime\nspecies: human\nknownTo: [GL]\n---\n# Julius\n"
    )
    session_path = "Campaigns/Great Library Campaign/Session Notes/Session 1.md"
    write_note(
      root,
      session_path,
      "---\ntags: [session-note]\ncampaign: GL\n---\n# Session 1\n\n[[Julius]] greets the party.\n"
    )
    git(root, "init", "-q")
    git(root, "add", ".")
    git_commit(root, "baseline")
    baseline = git(root, "rev-parse", "HEAD").strip

    File.open(File.join(root, session_path), "a") { |file| file << "\nThe city changes while he is away.\n" }
    write_note(
      root,
      "_dm_notes/Current Plans.md",
      "---\ntags: [meta]\naudience: [none]\n---\n# Current Plans\n\n[[Julius]] has an unresolved fate.\n"
    )
    write_note(
      root,
      "Gazetteer/Recent Regional Synthesis.md",
      "---\ntags: [place]\ntypeOf: region\naudience: [all]\n---\n# Recent Regional Synthesis\n\nJulius Prime is relevant here.\n"
    )
    binary_path = File.join(root, "_dm_notes", "map.png")
    File.binwrite(binary_path, "\x89PNG\x00[[Julius]]\xFF".b)
    git(root, "add", ".")
    git_commit(root, "new external invention")

    index = TaelgarNoteLint::NoteIndex.new(Pathname.new(root))
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: true, index: index)
    report = validator.validate_path("People/Julius.md")
    freshness = TaelgarNoteLint::FreshnessScanner.new(
      root: root,
      index: index,
      baseline_ref: baseline
    ).scan(report)

    by_path = freshness.fetch("candidates").each_with_object({}) do |candidate, memo|
      memo[candidate.fetch("path")] = candidate
    end
    assert_equal false, by_path.fetch(session_path).fetch("mentionChanged")
    assert_equal true, by_path.fetch("_dm_notes/Current Plans.md").fetch("mentionChanged")
    assert_equal "vault-note", by_path.fetch("Gazetteer/Recent Regional Synthesis.md").fetch("sourceKind")
    assert_equal true, by_path.fetch("Gazetteer/Recent Regional Synthesis.md").fetch("mentionChanged")
    refute_includes by_path.keys, "_dm_notes/map.png"
    refute report.fetch("findings").any? { |finding| finding["ruleId"].start_with?("freshness.") }
  end

  private

  def make_vault
    root = Dir.mktmpdir("taelgar-note-lint-test.")
    @temporary_roots << root
    FileUtils.mkdir_p(File.join(root, ".obsidian"))
    File.write(
      File.join(root, ".obsidian", "metadata.json"),
      JSON.pretty_generate(
        "campaigns" => [
          {
            "code" => "GL",
            "sessionNoteFolder" => "Campaigns/Great Library Campaign/Session Notes",
            "aliases" => ["gl", "Great Library", "Great Library Campaign"]
          }
        ]
      )
    )
    root
  end

  def write_note(root, relative_path, text)
    path = File.join(root, relative_path)
    FileUtils.mkdir_p(File.dirname(path))
    File.write(path, text)
  end

  def rule_ids(report)
    report.fetch("findings").map { |finding| finding.fetch("ruleId") }
  end

  def git(root, *arguments)
    stdout, stderr, status = Open3.capture3("git", *arguments, chdir: root)
    raise "git #{arguments.join(' ')} failed: #{stderr}" unless status.success?

    stdout
  end

  def git_commit(root, message)
    env = {
      "GIT_AUTHOR_NAME" => "Taelgar Lint Test",
      "GIT_AUTHOR_EMAIL" => "lint-test@example.invalid",
      "GIT_COMMITTER_NAME" => "Taelgar Lint Test",
      "GIT_COMMITTER_EMAIL" => "lint-test@example.invalid"
    }
    _stdout, stderr, status = Open3.capture3(env, "git", "commit", "-q", "-m", message, chdir: root)
    raise "git commit failed: #{stderr}" unless status.success?
  end
end
