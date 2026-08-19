# frozen_string_literal: true

require "fileutils"
require "json"
require "minitest/autorun"
require "open3"
require "tmpdir"

require_relative "validate_taelgar_note"

class ValidateTaelgarNoteTest < Minitest::Test
  FIXTURE_PATH = File.join(__dir__, "tests", "fixtures", "taelgar_note_lint_trial.json")

  def test_adopted_specification_records_the_validator_version
    specification = TaelgarNoteLint::ParsedNote.new(
      "_MoC/Taelgar Note Linter.md",
      File.read(File.join(__dir__, "..", "_MoC", "Taelgar Note Linter.md"))
    )

    assert_nil specification.yaml_error
    assert_equal TaelgarNoteLint::VERSION, specification.data["linterVersion"]
  end

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
      "---\ntags: [person]\nname: Julius\nspecies: human\nwhereabouts: Voltara\nknownTo: [grli]\n---\n# Julius\n\nSee [[Voltara]] and [[Missing Manor]].\n"
    )
    index = TaelgarNoteLint::NoteIndex.new(Pathname.new(root))
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: true, index: index)
    report = validator.validate_path("People/Julius.md")

    assert_equal 1, report.fetch("findings").count { |finding| finding["ruleId"] == "link.unresolved" }
    refute(report.fetch("findings").any? do |finding|
      finding["ruleId"] == "relationship.unresolved" && finding.dig("details", "target") == "Voltara"
    end)
  end

  def test_wikilinks_resolve_filenames_not_frontmatter_aliases
    root = make_vault
    write_note(root, "Gazetteer/Drankor.md", "---\ntags: [place]\nname: City of Drankor\ntypeOf: settlement\n---\n# Drankor\n")
    write_note(
      root,
      "History/Drankorian Empire.md",
      "---\ntags: [place]\nname: Drankorian Empire\naliases: [Drankor, Old Drankor]\ntypeOf: realm\n---\n# Drankorian Empire\n"
    )
    write_note(
      root,
      "People/Apollyon.md",
      "---\ntags: [person]\nspecies: human\nknownTo: []\naffiliations: [{org: Old Drankor}]\nwhereabouts: traveling east to Tokra\n---\n# Apollyon\n\nImprisoned in [[Drankor]], not [[Old Drankor]].\n"
    )
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: true)
    report = validator.validate_path("People/Apollyon.md")

    refute_includes rule_ids(report), "link.ambiguous"
    assert_equal 1, report.fetch("findings").count { |finding| finding["ruleId"] == "link.unresolved" }
    refute(report.fetch("findings").any? do |finding|
      finding["ruleId"] == "relationship.unresolved" && finding.dig("details", "target") == "Old Drankor"
    end)
    refute(report.fetch("findings").any? do |finding|
      finding["ruleId"].start_with?("relationship.") && finding.dig("details", "target") == "traveling east to Tokra"
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
      "---\ntags: [object]\ntypeOf: weapon\nknownTo: [grli]\n---\n# Hammer\n"
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
      "---\ntags: [object]\ntypeOf: weapon\ncampaign: Great Library\n---\n# Hammer\n"
    )
    assert_includes rule_ids(misplaced), "campaign.unexpected_entity_field"
    refute_includes rule_ids(misplaced), "campaign.audience_unclassified"
  end

  def test_known_to_is_required_for_people_and_objects_but_audience_is_not_universal
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)

    person = validator.validate_text(
      "People/Julius.md",
      "---\ntags: [person]\nspecies: human\ncampaignInfo: [{campaign: grli, date: 1748}]\n---\n# Julius\n"
    )
    object = validator.validate_text(
      "Campaigns/Great Library Campaign/Treasure/Hammer.md",
      "---\ntags: [object]\ntypeOf: weapon\ncampaignInfo: [{campaign: grli, date: 1748}]\n---\n# Hammer\n"
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
      "---\ntags: [source]\ncampaign: Great Library\n---\n# Letter\n"
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
        lintVersion: "2.3"
        tags: [place]
        typeOf: waterway
        pronunciation: RIH-ver
        POV: 1750
        ---
        # River

        %%^Metadata:article:v1%%
        mode: geographic reference
        povNotes: Stable geographic prose with no campaign-relative temporal language.
        %%^End%%

        %%^Metadata:names:v1%%
        - {name: River, language: Common, pronunciation: RIH-ver}
        %%^End%%

        %%^Metadata:map:v1%%
        locations:
          - {geometry: path, map: world, sourceHex: "01.01.A01", outletHex: "01.01.B02"}
        %%^End%%

        %%^Lint%%
        - [ ] **Suggestion — trial.open:** Review this trial finding.
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
    refute_includes rule_ids(report), "metadata.position"
    refute_includes rule_ids(report), "metadata.article_redundant_profile"
  end

  def test_clean_lint_has_no_report_or_status
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    report = validator.validate_text(
      "Campaigns/Great Library Campaign/Session Notes/Session 1.md",
      <<~MARKDOWN
        ---
        lintedAt: "2026-08-19T09:00:00-04:00"
        lintVersion: "2.3"
        tags: [session-note]
        campaign: Great Library
        POV: 1748
        ---
        # Session 1

        %%^Metadata:article:v1%%
        mode: campaign record
        povNotes: The session note is authoritative for what occurred in play.
        %%^End%%
      MARKDOWN
    )

    refute_includes rule_ids(report), "lint.report_without_status"
    refute_includes rule_ids(report), "lint.status_without_report"
    refute_includes rule_ids(report), "lint.report_without_open_findings"
  end

  def test_lint_report_and_status_require_each_other_and_open_work
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    report_without_status = validator.validate_text(
      "Meta.md",
      "---\ntags: [meta]\n---\n# Meta\n\n%%^Lint%%\n- [ ] **Suggestion — test.open:** Review.\n%%^End%%\n"
    )
    status_without_report = validator.validate_text(
      "Meta.md",
      "---\ntags: [meta, status/check/lint]\n---\n# Meta\n"
    )
    closed_report = validator.validate_text(
      "Meta.md",
      "---\ntags: [meta, status/check/lint]\n---\n# Meta\n\n%%^Lint%%\n- [x] **Suggestion — test.closed:** Reviewed.\n%%^End%%\n"
    )

    assert_includes rule_ids(report_without_status), "lint.report_without_status"
    assert_includes rule_ids(status_without_report), "lint.status_without_report"
    assert_includes rule_ids(closed_report), "lint.report_without_open_findings"
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

  def test_stale_lint_version_is_reported_against_the_current_version
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    report = validator.validate_text(
      "Meta.md",
      <<~MARKDOWN
        ---
        lintedAt: "2026-08-19T09:00:00-04:00"
        lintVersion: "2.2"
        tags: [meta]
        name: Meta
        POV: timeless
        ---
        # Meta

        %%^Metadata:article:v1%%
        mode: meta
        povNotes: This note describes the current vault workflow.
        %%^End%%
      MARKDOWN
    )

    assert_includes rule_ids(report), "lint.version_outdated"
    assert_equal "2.3", report.fetch("validatorVersion")
  end

  def test_completed_lints_require_scalar_frontmatter_pov_and_article_notes
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    missing = validator.validate_text(
      "Meta.md",
      <<~MARKDOWN
        ---
        lintedAt: "2026-08-19T09:00:00-04:00"
        lintVersion: "2.3"
        tags: [meta]
        ---
        # Meta

        %%^Metadata:article:v1%%
        mode: meta
        povNotes: This note is not tied to in-world chronology.
        %%^End%%
      MARKDOWN
    )
    malformed = validator.validate_text(
      "Meta.md",
      "---\ntags: [meta]\nPOV: []\n---\n# Meta\n"
    )
    legacy = validator.validate_text(
      "Meta.md",
      <<~MARKDOWN
        ---
        tags: [meta]
        POV: timeless
        ---
        # Meta

        %%^Metadata:article:v1%%
        mode: meta
        pov: current operational reference
        povNotes: This note is not tied to in-world chronology.
        %%^End%%
      MARKDOWN
    )

    assert_includes rule_ids(missing), "metadata.pov_missing"
    assert_includes rule_ids(malformed), "metadata.pov_shape"
    assert_includes rule_ids(legacy), "metadata.article_legacy_pov"
    refute_includes rule_ids(legacy), "metadata.article_required_field"
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
        POV: 1740s
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
    expected_fields = %w[subTypeOf headerVersion lintedAt lintVersion displayDefaults tags species customField name aliases whereabouts knownTo dm_notes POV]
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
      "---\ntags: [person]\nname: Julius Prime\nspecies: human\nknownTo: [grli]\n---\n# Julius\n"
    )
    session_path = "Campaigns/Great Library Campaign/Session Notes/Session 1.md"
    write_note(
      root,
      session_path,
      "---\ntags: [session-note]\ncampaign: Great Library\n---\n# Session 1\n\n[[Julius]] greets the party.\n"
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

  def test_authoritative_campaign_registry_has_the_adopted_names_and_codes
    root = Pathname.new(__dir__).parent
    registry = TaelgarNoteLint::CampaignRegistry.new(root)
    expected = {
      "Addermarch" => "adma",
      "Dunmar Frontier" => "dufr",
      "Cleenseau" => "clee",
      "Great Library" => "grli",
      "Mawar Adventures" => "mawar",
      "Into the Chasm" => "itc",
      "Labyrinths of the Lost" => "lablost",
      "Lost in the Feywild" => "feywild"
    }

    assert_equal expected, registry.campaigns.to_h { |campaign| [campaign.fetch("name"), campaign.fetch("code")] }
    assert_equal "dufr", registry.resolve("Dunmari Frontier")
    assert_equal "Dunmar Frontier", registry.canonical_name("DuFr")
  end

  def test_runtime_campaign_compatibility_metadata_matches_the_authoritative_registry
    root = Pathname.new(__dir__).parent
    registry = TaelgarNoteLint::CampaignRegistry.new(root)
    compatibility = JSON.parse(root.join(".obsidian", "metadata.json").read).fetch("campaigns")
    by_code = compatibility.to_h { |campaign| [campaign.fetch("code"), campaign] }

    assert_equal registry.campaigns.map { |campaign| campaign.fetch("code") }.sort, by_code.keys.sort
    registry.campaigns.each do |campaign|
      compatible = by_code.fetch(campaign.fetch("code"))
      expected_folder = Pathname.new(campaign.fetch("campaignRoot"))
        .join(Pathname.new(campaign.fetch("notePattern")).dirname).cleanpath.to_s
      recognized_names = [compatible.fetch("code"), *compatible.fetch("aliases", [])]
        .map { |value| TaelgarNoteLint.normalize(value) }

      assert_includes recognized_names, TaelgarNoteLint.normalize(campaign.fetch("name"))
      assert_equal expected_folder, compatible.fetch("sessionNoteFolder")
      if campaign["partyPage"]
        assert_equal campaign.fetch("partyPage"), compatible.fetch("partyPage")
      end
    end
  end

  def test_campaign_frontmatter_uses_long_name_and_scoped_metadata_uses_lowercase_code
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    canonical = validator.validate_text(
      "Campaigns/Great Library Campaign/Session Notes/Session 1.md",
      "---\ntags: [session-note]\ncampaign: Great Library\n---\n# Session 1\n"
    )
    aliases = validator.validate_text(
      "Campaigns/Great Library Campaign/Session Notes/Session 1.md",
      "---\ntags: [session-note]\ncampaign: GL\n---\n# Session 1\n"
    )
    known = validator.validate_text(
      "People/Julius.md",
      "---\ntags: [person]\nspecies: human\nknownTo: [GL]\n---\n# Julius\n"
    )

    refute_includes rule_ids(canonical), "campaign.noncanonical_name"
    assert_includes rule_ids(aliases), "campaign.noncanonical_name"
    assert_includes rule_ids(known), "campaign.noncanonical_code"
  end

  def test_metadata_blocks_are_at_note_end_and_article_metadata_does_not_repeat_profile
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    block = "%%^Metadata:article:v1%%\nmode: geographic reference\npovNotes: Stable present-day geography.\n%%^End%%"
    misplaced = validator.validate_text(
      "Gazetteer/Test.md",
      "---\ntags: [place]\ntypeOf: forest\n---\n#{block}\n\n# Test\n\nBody.\n"
    )
    placed = validator.validate_text(
      "Gazetteer/Test.md",
      "---\ntags: [place]\ntypeOf: forest\n---\n# Test\n\nBody.\n\n#{block}\n"
    )
    redundant = validator.validate_text(
      "Gazetteer/Test.md",
      "---\ntags: [place]\ntypeOf: forest\n---\n# Test\n\nBody.\n\n#{block.sub('mode:', "profile: place\nmode:")}\n"
    )

    assert_includes rule_ids(misplaced), "metadata.position"
    refute_includes rule_ids(placed), "metadata.position"
    assert_includes rule_ids(redundant), "metadata.article_redundant_profile"
  end

  def test_comments_belong_below_title_and_header_callout
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    above = validator.validate_text(
      "Gazetteer/Test.md",
      "---\ntags: [place]\ntypeOf: forest\n---\n%% editorial comment %%\n# Test\n> [!info] Header\n\nBody.\n"
    )
    below = validator.validate_text(
      "Gazetteer/Test.md",
      "---\ntags: [place]\ntypeOf: forest\n---\n# Test\n> [!info] Header\n\n%% editorial comment %%\n\nBody.\n"
    )

    assert_includes rule_ids(above), "comment.before_header"
    refute_includes rule_ids(below), "comment.before_header"
  end

  def test_markdown_code_examples_are_not_parsed_as_live_blocks_or_links
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: true)
    report = validator.validate_text(
      "_MoC/Examples.md",
      <<~MARKDOWN
        ---
        tags: [meta]
        ---
        # Examples

        Inline example: `%%^Campaign:dufr%%` and `[[Missing Inline Example]]`.

        ```yaml
        %%^Metadata:names:v1%%
        - {name: Example, language: unknown, source: "[[Missing Fenced Example]]"}
        %%^End%%
        ```
      MARKDOWN
    )

    refute rule_ids(report).any? { |rule_id| rule_id.start_with?("syntax.") }
    refute rule_ids(report).any? { |rule_id| rule_id.start_with?("metadata.") }
    refute_includes rule_ids(report), "link.unresolved"
  end

  def test_dm_notes_review_uses_local_dm_mentions_without_overriding_human_attestation
    root = make_vault
    write_note(
      root,
      "Groups/Aatmaji Dynasty.md",
      "---\ntags: [group]\nname: Aatmaji Dynasty\ndm_owner: tim\ndm_notes: none\n---\n# Aatmaji Dynasty\n"
    )
    write_note(root, "_DM_/Dunmar Notes.md", "# Dunmar Notes\n\n[[Aatmaji Dynasty]] has a private ruler list.\n")
    write_note(
      root,
      "Groups/Positive Dynasty.md",
      "---\ntags: [group]\nname: Positive Dynasty\ndm_owner: tim\ndm_notes: color\n---\n# Positive Dynasty\n"
    )
    write_note(root, "_DM_/Positive Notes.md", "# Positive Notes\n\n[[Positive Dynasty]] has private color.\n")
    write_note(
      root,
      "People/Secret Subject.md",
      "---\ntags: [person]\nspecies: human\nknownTo: []\ndm_owner: none\ndm_notes: none\n---\n# Secret Subject\n\n%%SECRET\n[[_DM_/Secret Detail]]\n%%\n"
    )
    write_note(root, "_DM_/Secret Detail.md", "# Secret Detail\n\n[[Secret Subject]] has hidden material.\n")
    write_note(
      root,
      "People/No Private File.md",
      "---\ntags: [person]\nspecies: human\nknownTo: []\ndm_owner: tim\ndm_notes: important\n---\n# No Private File\n"
    )
    index = TaelgarNoteLint::NoteIndex.new(Pathname.new(root))
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: true, index: index)
    suspect = validator.validate_path("Groups/Aatmaji Dynasty.md")
    supported = validator.validate_path("Groups/Positive Dynasty.md")
    accounted = validator.validate_path("People/Secret Subject.md")
    unsupported = validator.validate_path("People/No Private File.md")
    finding = suspect.fetch("findings").find { |item| item["ruleId"] == "dm.notes_private_evidence_suspect" }

    refute_nil finding
    assert_equal ["_DM_/Dunmar Notes.md"], finding.dig("details", "sources").map { |source| source["path"] }
    assert_includes rule_ids(supported), "dm.notes_private_evidence_found"
    refute_includes rule_ids(supported), "dm.notes_no_local_evidence"
    refute_includes rule_ids(accounted), "dm.notes_private_evidence_suspect"
    assert_includes rule_ids(accounted), "dm.notes_secret_evidence_accounted"
    assert_includes rule_ids(unsupported), "dm.notes_no_local_evidence"

    suspect["fixes"] = []
    markdown = TaelgarNoteLint::CLI.new([]).send(:markdown, [suspect])
    assert_includes markdown, "[[_DM_/Dunmar Notes]]"
    refute_includes markdown, "`_DM_/Dunmar Notes.md`"
  end

  def test_deprecated_fields_include_replacement_guidance
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    report = validator.validate_text(
      "Groups/Dynasty.md",
      "---\ntags: [group]\ntypeOf: family\nsubTypeOf: dynasty\n---\n# Dynasty\n"
    )
    finding = report.fetch("findings").find { |item| item["ruleId"] == "classification.deprecated_subtype" }

    refute_nil finding
    assert_includes finding.fetch("message"), "typeOfAlias: dynasty"
  end

  def test_session_and_primary_source_authority_are_explicit_in_reports
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    session = validator.validate_text(
      "Campaigns/Great Library Campaign/Session Notes/Session 1.md",
      "---\ntags: [session-note]\ncampaign: Great Library\n---\n# Session 1\n"
    )
    source = validator.validate_text(
      "Primary Sources/Letter.md",
      "---\ntags: [source]\n---\n# Letter\n"
    )

    assert_equal "session-source", session.dig("note", "authority")
    assert_equal "primary-source", source.dig("note", "authority")
  end

  private

  def make_vault
    root = Dir.mktmpdir("taelgar-note-lint-test.")
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
            "aliases" => ["Great Library Campaign", "GL", "gl"],
            "partyPage" => "Silver Tempests",
            "sessionRoot" => "great-library",
            "campaignRoot" => "Campaigns/Great Library Campaign",
            "notePattern" => "Session Notes/Great Library Session Notes - Arc {session}.md",
            "defaultTemplate" => "composable-session-note.md"
          }
        }
      )
    )
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
