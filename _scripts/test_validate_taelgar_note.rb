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
    assert_equal TaelgarNoteLint::DM_NOTES_REVIEW_VERSION, specification.data["dmNotesReviewVersion"]
    assert_equal TaelgarNoteLint::NAME_REVIEW_VERSION, specification.data["nameReviewVersion"]
    assert_equal TaelgarNoteLint::POV_REVIEW_VERSION, specification.data["povReviewVersion"]
    assert_equal "3.5", TaelgarNoteLint::VERSION
    assert_equal 5, TaelgarNoteLint::SCHEMA_VERSION
    assert_equal "3.4", TaelgarNoteLint::DM_NOTES_REVIEW_VERSION
    assert_equal "3.4", TaelgarNoteLint::NAME_REVIEW_VERSION
    assert_equal "3.4", TaelgarNoteLint::POV_REVIEW_VERSION
  end

  def test_adopted_governance_records_editorial_sufficiency_lifecycle
    specification = File.read(File.join(__dir__, "..", "_MoC", "Taelgar Note Linter.md"))
    skill = File.read(File.join(__dir__, "..", ".agents", "skills", "lint-taelgar-note", "SKILL.md"))

    ["Sufficient", "Sufficient, worth expanding", "Underdeveloped"].each do |verdict|
      assert_includes specification, verdict
      assert_includes skill, verdict
    end
    assert_includes specification, "**Sufficient, worth expanding** is a handoff-only verdict."
    assert_includes specification, "By itself, it cannot create a Lint block, `status/check/lint`, or an editorial finding."
    assert_includes specification, "Does the visible note currently perform its reference role without a central gap?"
    assert_includes specification, "`editorial.note_underdeveloped`"
    assert_includes skill, "`editorial.note_underdeveloped`"
    assert_includes skill, "uncertainty after the mechanical screen favors inclusion"
    assert_includes skill, "`gpt-5.6-sol` with `xhigh` reasoning"
    assert_includes skill, "`gpt-5.6-terra` at `high`"
    assert_includes specification, "`editorial.reference_voice`"
    assert_includes skill, "`editorial.reference_voice`"
    assert_includes specification, "Worldbuilding discussion routing"
    assert_includes skill, "generate_worldbuilding_discussion_index.rb"
    assert_includes specification, "A party visit, conversation, purchase, overnight stay, routine encounter"
    assert_includes skill, "A campaign appearance is not coverage merely because it happened."
  end

  def test_status_check_name_is_omitted_from_lint_status_summary
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    report = validator.validate_text(
      "Meta/Status Summary.md",
      <<~MARKDOWN
        ---
        tags: [meta, status/check/name, status/check/ai, status/stub]
        ---
        # Status Summary

        This note has substantive fixture prose.
      MARKDOWN
    )

    assert_equal ["status/check/ai", "status/stub"], report.dig("note", "statuses")
  end

  def test_all_contextual_review_gates_reopen_for_pre_3_4_lints
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    report = validator.validate_text(
      "People/Previous Review.md",
      <<~MARKDOWN
        ---
        lintedAt: "2026-08-20T09:00:00-04:00"
        lintVersion: "3.3"
        tags: [person]
        species: human
        knownTo: []
        dm_owner: tim
        dm_notes: none
        POV: modern
        ---
        # Previous Review

        A person recorded in the current campaign era.
      MARKDOWN
    )

    assert report.dig("reviewGates", "names", "required")
    assert report.dig("reviewGates", "pov", "required")
    assert report.dig("reviewGates", "dmNotes", "required")
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

  def test_place_vocabulary_comes_from_moc_and_distinguishes_aliases_from_unknown_values
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    building = validator.validate_text(
      "Gazetteer/Tower.md",
      "---\nheaderVersion: 1\ntags: [place]\nname: Tower\ntypeOf: building\naudience: [all]\n---\n# Tower\n"
    )
    battlefield = validator.validate_text(
      "Gazetteer/Battlefield.md",
      "---\nheaderVersion: 1\ntags: [place]\nname: Battlefield\ntypeOf: battlefield\naudience: [all]\n---\n# Battlefield\n"
    )
    legacy_alias = validator.validate_text(
      "Gazetteer/Tower.md",
      "---\nheaderVersion: 1\ntags: [place]\nname: Tower\ntypeOf: buliding\naudience: [all]\n---\n# Tower\n"
    )
    unknown = validator.validate_text(
      "Gazetteer/Sky Island.md",
      "---\nheaderVersion: 1\ntags: [place]\nname: Sky Island\ntypeOf: sky island\naudience: [all]\n---\n# Sky Island\n"
    )

    refute_includes rule_ids(building), "classification.place_type_unknown"
    refute_includes rule_ids(battlefield), "classification.place_type_unknown"
    assert_includes rule_ids(legacy_alias), "classification.place_type_noncanonical"
    refute_includes rule_ids(legacy_alias), "classification.place_type_unknown"
    assert_includes rule_ids(unknown), "classification.place_type_unknown"
  end

  def test_dm_owner_vocabulary_comes_from_moc
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    accepted = validator.validate_text(
      "People/Schwartz Subject.md",
      "---\ntags: [person]\nspecies: human\nknownTo: []\ndm_owner: schwartz\ndm_notes: none\n---\n# Schwartz Subject\n"
    )
    unknown = validator.validate_text(
      "People/New Owner.md",
      "---\ntags: [person]\nspecies: human\nknownTo: []\ndm_owner: new-human\ndm_notes: none\n---\n# New Owner\n"
    )

    refute_includes rule_ids(accepted), "dm.owner_unknown"
    assert_includes rule_ids(unknown), "dm.owner_unknown"
  end

  def test_generated_lint_value_sidecar_matches_moc_declarations
    root = File.expand_path("..", __dir__)
    stdout, stderr, status = Open3.capture3(
      "ruby", File.join(__dir__, "generate_taelgar_lint_values.rb"), "--check", "--root", root
    )

    assert status.success?, "#{stdout}\n#{stderr}"
  end

  def test_validator_rejects_a_stale_lint_value_sidecar
    root = make_vault
    status_path = File.join(root, "_MoC", "Note Status.md")
    File.open(status_path, "a") { |file| file.write("\nUnrelated prose after generation.\n") }
    TaelgarNoteLint::Validator.new(root: root, check_links: false)

    text = File.read(status_path).sub(/^linterDmOwners::.*$/) { |line| "#{line}, \"new-owner\"" }
    File.write(status_path, text)

    error = assert_raises(TaelgarLintValues::Error) do
      TaelgarNoteLint::Validator.new(root: root, check_links: false)
    end
    assert_includes error.message, "taelgar_lint_values.json is stale"
  end

  def test_validator_has_no_hand_authored_editorial_replacement_dictionary
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    report = validator.validate_text(
      "Background/Marked Prose.md",
      "---\ntags: [background]\n---\n# Marked Prose\n\nA climatic victory may accomodate unusual prose.\n"
    )

    refute TaelgarNoteLint.const_defined?(:EDITORIAL_PATTERNS, false)
    refute_includes rule_ids(report), "editorial.common_typo"
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

  def test_dot_directory_notes_do_not_create_link_or_relationship_ambiguity
    root = make_vault
    canonical_path = "Gazetteer/Old Chardon Canal.md"
    write_note(
      root,
      canonical_path,
      "---\ntags: [place]\nname: Old Chardon Canal\ntypeOf: waterway\n---\n# Old Chardon Canal\n"
    )
    write_note(
      root,
      ".backups/snapshot/Old Chardon Canal.md",
      "---\ntags: [place]\nname: Old Chardon Canal\ntypeOf: waterway\n---\n# Old Chardon Canal\n"
    )
    write_note(
      root,
      "People/Canal Keeper.md",
      "---\ntags: [person]\nspecies: human\nknownTo: []\nwhereabouts: Old Chardon Canal\n---\n# Canal Keeper\n\nSee [[Old Chardon Canal]].\n"
    )

    index = TaelgarNoteLint::NoteIndex.new(Pathname.new(root))
    report = TaelgarNoteLint::Validator.new(root: root, check_links: true, index: index)
                                    .validate_path("People/Canal Keeper.md")

    assert_equal [canonical_path], index.resolve("Old Chardon Canal", "People/Canal Keeper.md")
    assert_equal [canonical_path], index.resolve_identity("Old Chardon Canal", "People/Canal Keeper.md")
    refute_includes rule_ids(report), "link.ambiguous"
    refute_includes rule_ids(report), "relationship.ambiguous"
  end

  def test_invalid_utf8_in_markdown_is_reported_without_aborting_the_index
    root = make_vault
    path = File.join(root, "People", "Broken Encoding.md")
    FileUtils.mkdir_p(File.dirname(path))
    File.binwrite(path, "---\ntags: [person]\nspecies: human\nknownTo: []\naudience: [all]\n---\n# Broken \xFF\n\nThis record contains a complete sentence despite its damaged title.\n".b)

    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    report = validator.validate_path(path)

    assert_includes rule_ids(report), "file.invalid_utf8"
    assert_equal 1, report.fetch("summary").fetch("errors")
  end

  def test_target_eligibility_rejects_only_objectively_blank_or_generated_bodies
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    prefix = "---\ntags: [meta]\n---\n"
    ineligible_bodies = {
      "frontmatter only" => "",
      "heading only" => "# Heading Only\n",
      "setext heading only" => "Heading Only\n============\n",
      "image only" => "![[map.png]]\n",
      "markdown image only" => "![Map of the route](map.png)\n",
      "lint output only" => <<~MARKDOWN
        # Generated Only

        %%^povNotes:v1%%
        Temporal coverage: this generated sentence does not make the note lintable.
        %%^End%%

        %%^Lint%%
        - [ ] **Suggestion — test.generated:** This generated report also does not count.
        %%^End%%
      MARKDOWN
    }

    ineligible_bodies.each do |label, body|
      report = validator.validate_text("Meta/#{label}.md", "#{prefix}#{body}")

      assert_includes rule_ids(report), "lint.target_no_reviewable_prose", label
      assert_equal "ineligible", report.dig("targetEligibility", "status"), label
    end

    complete_comment = validator.validate_text(
      "Creatures/Goblins.md",
      "#{prefix}# Goblins\n\n%% Goblins often live under hobgoblin rule. %%\n"
    )
    fragment_comment = validator.validate_text(
      "Creatures/Dragonet.md",
      "#{prefix}# Dragonet\n\n%% dragonet on circular island %%\n"
    )
    title_dependent_definition = validator.validate_text(
      "Gazetteer/Northern Peak.md",
      "#{prefix}# Northern Peak\n\nA large, prominent peak in the northern mountains.\n"
    )

    refute_includes rule_ids(complete_comment), "lint.target_no_reviewable_prose"
    assert_equal "agent_confirmation_required", complete_comment.dig("targetEligibility", "status")
    refute_includes rule_ids(fragment_comment), "lint.target_no_reviewable_prose"
    assert_equal "agent_confirmation_required", fragment_comment.dig("targetEligibility", "status")
    refute_includes rule_ids(title_dependent_definition), "lint.target_no_reviewable_prose"
    assert_equal "agent_confirmation_required", title_dependent_definition.dig("targetEligibility", "status")
  end

  def test_fix_frontmatter_leaves_an_objectively_ineligible_note_unchanged
    root = make_vault
    path = "Meta/Heading Only.md"
    original = "---\ntags:\n  - meta\nheaderVersion: 1\n---\n# Heading Only\n"
    write_note(root, path, original)

    stdout, _stderr = capture_io do
      result = TaelgarNoteLint::CLI.new(
        ["--root", root, "--format", "json", "--no-links", "--fix-frontmatter", path]
      ).run
      assert_equal 1, result
    end
    report = JSON.parse(stdout).first

    assert_equal original, File.read(File.join(root, path))
    assert_includes rule_ids(report), "lint.target_no_reviewable_prose"
    assert_empty report.fetch("fixes")
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

  def test_pronunciation_requires_an_actual_value_and_uses_absence_for_contextual_exemptions
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
    placeholder = validator.validate_text(
      "People/Thomas Hawke.md",
      "---\ntags: [person]\nspecies: human\nknownTo: []\n---\n# Thomas Hawke\n\n%%^Metadata:names:v1%%\n- {name: Thomas Hawke, language: Common, pronunciation: obvious}\n%%^End%%\n"
    )

    assert_includes rule_ids(missing), "pronunciation.missing_or_exception"
    refute_includes rule_ids(present), "pronunciation.missing_or_exception"
    refute_includes rule_ids(source), "pronunciation.missing_or_exception"
    refute_includes rule_ids(placeholder), "pronunciation.missing_or_exception"
    assert_includes rule_ids(placeholder), "metadata.names_pronunciation_placeholder"
  end

  def test_name_block_applicability_is_not_inferred_from_meta_or_background_tags
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    block = "%%^Metadata:names:v1%%\n- {name: Example, language: Common}\n%%^End%%\n"
    meta = validator.validate_text("Meta/Example.md", "---\ntags: [meta]\n---\n# Example\n\n#{block}")
    background = validator.validate_text("Background/Example.md", "---\ntags: [background]\n---\n# Example\n\n#{block}")
    religion = validator.validate_text("Religion/Example.md", "---\ntags: [background, religion/example]\n---\n# Example\n\n#{block}")

    refute_includes rule_ids(meta), "metadata.names_forbidden_for_meta"
    refute_includes rule_ids(background), "metadata.names_unnecessary_for_background"
    refute_includes rule_ids(religion), "metadata.names_unnecessary_for_background"
  end

  def test_name_review_gate_skips_contextual_findings_after_threshold
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    current = validator.validate_text(
      "People/Reviewed Person.md",
      <<~MARKDOWN
        ---
        lintedAt: "2026-08-20T09:00:00-04:00"
        lintVersion: "#{TaelgarNoteLint::NAME_REVIEW_VERSION}"
        tags: [person]
        species: human
        ---
        # Reviewed Person
      MARKDOWN
    )
    stale = validator.validate_text(
      "People/Stale Person.md",
      <<~MARKDOWN
        ---
        lintedAt: "2026-08-20T09:00:00-04:00"
        lintVersion: "2.10"
        tags: [person]
        species: human
        ---
        # Stale Person
      MARKDOWN
    )

    refute_includes rule_ids(current), "identity.implicit_name"
    refute_includes rule_ids(current), "pronunciation.missing_or_exception"
    assert_includes rule_ids(stale), "identity.implicit_name"
    assert_includes rule_ids(stale), "pronunciation.missing_or_exception"
    refute current.dig("reviewGates", "names", "required")
    assert stale.dig("reviewGates", "names", "required")
  end

  def test_unresolved_name_entries_remain_deterministic_open_work_without_recalculation
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    report = validator.validate_text(
      "People/Reviewed Names.md",
      <<~MARKDOWN
        ---
        lintedAt: "2026-08-20T09:00:00-04:00"
        lintVersion: "#{TaelgarNoteLint::NAME_REVIEW_VERSION}"
        tags: [person]
        species: human
        name: Reviewed Names
        ---
        # Reviewed Names

        %%^Metadata:names:v1%%
        - {name: Reviewed Names, language: Common, pronunciation: ree-VYOOD, status: proposed, notes: Spelling-based proposal}
        - {name: Older Name, language: Common, status: disputed}
        - {name: Hidden Name, language: unknown, status: unresolved}
        %%^End%%
      MARKDOWN
    )

    assert_equal 3, rule_ids(report).count("metadata.names_unresolved_status")
    refute_includes rule_ids(report), "pronunciation.missing_or_exception"
  end

  def test_name_block_pronunciation_requires_notes_only_when_frontmatter_does_not_match
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    matching = validator.validate_text(
      "People/Matching.md",
      "---\ntags: [person]\nspecies: human\npronunciation: MATCH-ing\n---\n# Matching\n\n%%^Metadata:names:v1%%\n- {name: Matching, language: Common, pronunciation: MATCH-ing, status: documented}\n%%^End%%\n"
    )
    unexplained = validator.validate_text(
      "People/Unexplained.md",
      "---\ntags: [person]\nspecies: human\n---\n# Unexplained\n\n%%^Metadata:names:v1%%\n- {name: Unexplained, language: Common, pronunciation: un-PLAYND, status: documented}\n%%^End%%\n"
    )
    explained = validator.validate_text(
      "People/Explained.md",
      "---\ntags: [person]\nspecies: human\n---\n# Explained\n\n%%^Metadata:names:v1%%\n- {name: Explained, language: Common, pronunciation: ex-PLAYND, status: documented, notes: Recorded in [[Pronunciation Source]]}\n%%^End%%\n"
    )

    refute_includes rule_ids(matching), "metadata.names_pronunciation_notes_missing"
    assert_includes rule_ids(unexplained), "metadata.names_pronunciation_notes_missing"
    refute_includes rule_ids(explained), "metadata.names_pronunciation_notes_missing"
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
        lintVersion: "#{TaelgarNoteLint::VERSION}"
        tags: [place]
        typeOf: waterway
        pronunciation: RIH-ver
        POV: 1750
        ---
        # River

        %%^povNotes:v1%%
        Temporal coverage: modern; the geographic prose has no narrower campaign-relative limitation.
        %%^End%%

        %%^Metadata:names:v1%%
        - {name: River, language: Common, pronunciation: RIH-ver}
        %%^End%%

        %%^Metadata:map:v1%%
        locations:
          - {role: source, feature: , map: world, locator: "01.01.A01"}
          - {role: outlet, feature: , map: world, locator: "01.01.B02"}
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
    refute_includes rule_ids(report), "metadata.pov_notes_empty"
  end

  def test_clean_lint_has_no_report_or_status
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    report = validator.validate_text(
      "Campaigns/Great Library Campaign/Session Notes/Session 1.md",
      <<~MARKDOWN
        ---
        lintedAt: "2026-08-19T09:00:00-04:00"
        lintVersion: "#{TaelgarNoteLint::VERSION}"
        tags: [session-note]
        campaign: Great Library
        POV: 1748
        ---
        # Session 1

        The party crossed the river during this session.
      MARKDOWN
    )

    refute_includes rule_ids(report), "lint.report_without_status"
    refute_includes rule_ids(report), "lint.status_without_report"
    refute_includes rule_ids(report), "lint.report_without_open_findings"
    refute_includes rule_ids(report), "metadata.pov_notes_not_applicable"
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

        %%^povNotes:v1%%
        Temporal coverage: this note describes the current vault workflow.
        %%^End%%
      MARKDOWN
    )

    assert_includes rule_ids(report), "lint.version_outdated"
    assert_equal TaelgarNoteLint::VERSION, report.fetch("validatorVersion")
  end

  def test_completed_lints_require_scalar_frontmatter_pov_and_pov_notes
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    missing = validator.validate_text(
      "Meta.md",
      <<~MARKDOWN
        ---
        lintedAt: "2026-08-19T09:00:00-04:00"
        lintVersion: "#{TaelgarNoteLint::VERSION}"
        tags: [meta]
        ---
        # Meta

        %%^povNotes:v1%%
        Temporal coverage: this note is not tied to in-world chronology.
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
    assert_includes rule_ids(legacy), "metadata.legacy_article_block"
    refute_includes rule_ids(legacy), "metadata.pov_notes_empty"
  end

  def test_pov_review_gate_and_campaign_record_pov_notes_profile
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    current_session = validator.validate_text(
      "Campaigns/Test Campaign/Session Notes/Session 1.md",
      <<~MARKDOWN
        ---
        lintedAt: "2026-08-20T09:00:00-04:00"
        lintVersion: "#{TaelgarNoteLint::POV_REVIEW_VERSION}"
        tags: [session-note]
        POV: 1748
        ---
        # Session 1

        The party crossed the river during this session.
      MARKDOWN
    )
    session_with_notes = validator.validate_text(
      "Campaigns/Test Campaign/Session Notes/Session 2.md",
      <<~MARKDOWN
        ---
        lintedAt: "2026-08-20T09:00:00-04:00"
        lintVersion: "#{TaelgarNoteLint::POV_REVIEW_VERSION}"
        tags: [session-note]
        POV: 1748
        ---
        # Session 2

        The party returned during this session.

        %%^povNotes:v1%%
        Temporal coverage: the DR 1748 session chronology.
        %%^End%%
      MARKDOWN
    )
    campaign_meta = validator.validate_text(
      "Campaigns/Test Campaign/Home.md",
      "---\nlintedAt: \"2026-08-20T09:00:00-04:00\"\nlintVersion: \"#{TaelgarNoteLint::POV_REVIEW_VERSION}\"\ntags: [meta]\nPOV: 1740s\n---\n# Home\n\nThis page summarizes the campaign.\n"
    )
    campaign_source = validator.validate_text(
      "Campaigns/Test Campaign/Letter.md",
      "---\nlintedAt: \"2026-08-20T09:00:00-04:00\"\nlintVersion: \"#{TaelgarNoteLint::POV_REVIEW_VERSION}\"\ntags: [source]\nPOV: 1748\n---\n# Letter\n\nThe letter records a warning.\n"
    )
    campaign_legacy = validator.validate_text(
      "Campaigns/Test Campaign/Legacy Letter.md",
      "---\ntags: [source]\nPOV: 1748\n---\n# Legacy Letter\n\nThe letter records a warning.\n\n%%^Metadata:article:v1%%\nmode: source\npovNotes: The letter was received in DR 1748.\n%%^End%%\n"
    )
    current_missing_pov = validator.validate_text(
      "Campaigns/Test Campaign/Missing POV.md",
      "---\nlintedAt: \"2026-08-20T09:00:00-04:00\"\nlintVersion: \"#{TaelgarNoteLint::POV_REVIEW_VERSION}\"\ntags: [meta]\n---\n# Missing POV\n\nThis page summarizes the campaign.\n"
    )
    campaign_entity = validator.validate_text(
      "Campaigns/Test Campaign/Place.md",
      "---\nlintedAt: \"2026-08-20T09:00:00-04:00\"\nlintVersion: \"#{TaelgarNoteLint::POV_REVIEW_VERSION}\"\ntags: [place]\ntypeOf: settlement\nPOV: 1748\n---\n# Place\n\nThis settlement appears in the campaign.\n"
    )
    noncampaign_source = validator.validate_text(
      "Primary Sources/Letter.md",
      "---\nlintedAt: \"2026-08-20T09:00:00-04:00\"\nlintVersion: \"#{TaelgarNoteLint::POV_REVIEW_VERSION}\"\ntags: [source]\nPOV: 1748\n---\n# Letter\n\nThe letter records a warning.\n"
    )
    current_with_notes = validator.validate_text(
      "People/Current POV.md",
      "---\nlintedAt: \"2026-08-20T09:00:00-04:00\"\nlintVersion: \"#{TaelgarNoteLint::POV_REVIEW_VERSION}\"\ntags: [person]\nspecies: human\nPOV: 1748\n---\n# Current POV\n\nThis person is recorded in the campaign era.\n\n%%^povNotes:v1%%\nTemporal coverage: the DR 1748 campaign era.\n%%^End%%\n"
    )
    stale = validator.validate_text(
      "People/Stale POV.md",
      "---\nlintedAt: \"2026-08-20T09:00:00-04:00\"\nlintVersion: \"3.1\"\ntags: [person]\nspecies: human\nPOV: 1748\n---\n# Stale POV\n\nThis person is recorded in the campaign era.\n"
    )

    refute current_session.dig("reviewGates", "pov", "required")
    refute current_session.dig("reviewGates", "pov", "povNotesApplicable")
    refute_includes rule_ids(current_session), "metadata.pov_notes_missing"
    assert session_with_notes.dig("reviewGates", "pov", "required")
    assert_includes rule_ids(session_with_notes), "metadata.pov_notes_not_applicable"
    [campaign_meta, campaign_source].each do |report|
      refute report.dig("reviewGates", "pov", "required")
      refute report.dig("reviewGates", "pov", "povNotesApplicable")
      refute_includes rule_ids(report), "metadata.pov_notes_missing"
    end
    legacy_finding = campaign_legacy.fetch("findings").find { |finding| finding["ruleId"] == "metadata.legacy_article_block" }
    refute_nil legacy_finding
    assert_nil legacy_finding.dig("details", "candidate")
    assert_includes legacy_finding.fetch("message"), "do not use povNotes"
    refute current_missing_pov.dig("reviewGates", "pov", "required")
    assert_includes rule_ids(current_missing_pov), "metadata.pov_missing"
    [campaign_entity, noncampaign_source].each do |report|
      refute report.dig("reviewGates", "pov", "required")
      assert report.dig("reviewGates", "pov", "povNotesApplicable")
      refute_includes rule_ids(report), "metadata.pov_notes_missing"
    end
    assert current_with_notes.dig("reviewGates", "pov", "required")
    assert stale.dig("reviewGates", "pov", "required")
    assert_includes rule_ids(stale), "metadata.pov_notes_missing"
    assert_equal TaelgarNoteLint::POV_REVIEW_VERSION, stale.dig("reviewGates", "pov", "minimumVersion")
  end

  def test_pov_notes_blocks_require_v1_nonempty_plain_text_and_are_unique
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    valid = validator.validate_text(
      "Meta/Valid.md",
      "---\ntags: [meta]\n---\n# Valid\n\n%%^povNotes:v1%%\nTemporal coverage: modern; plain text needs no YAML quoting.\n%%^End%%\n"
    )
    unversioned = validator.validate_text(
      "Meta/Unversioned.md",
      "---\ntags: [meta]\n---\n# Unversioned\n\n%%^povNotes%%\nTemporal coverage: modern.\n%%^End%%\n"
    )
    empty = validator.validate_text(
      "Meta/Empty.md",
      "---\ntags: [meta]\n---\n# Empty\n\n%%^povNotes:v1%%\n%%^End%%\n"
    )
    duplicate = validator.validate_text(
      "Meta/Duplicate.md",
      "---\ntags: [meta]\n---\n# Duplicate\n\n%%^povNotes:v1%%\nTemporal coverage: modern.\n%%^End%%\n\n%%^povNotes:v1%%\nTemporal coverage: modern.\n%%^End%%\n"
    )
    stale_missing = validator.validate_text(
      "Meta/Missing.md",
      "---\nlintedAt: \"2026-08-20T09:00:00-04:00\"\nlintVersion: \"3.1\"\ntags: [meta]\nPOV: modern\n---\n# Missing\n"
    )

    refute_includes rule_ids(valid), "syntax.unknown_content_marker"
    refute_includes rule_ids(valid), "metadata.invalid_pov_notes_version"
    refute_includes rule_ids(valid), "metadata.pov_notes_empty"
    assert_includes rule_ids(unversioned), "metadata.invalid_pov_notes_version"
    assert_includes rule_ids(empty), "metadata.pov_notes_empty"
    assert_includes rule_ids(duplicate), "metadata.duplicate_pov_notes_block"
    assert_includes rule_ids(stale_missing), "metadata.pov_notes_missing"
  end

  def test_completed_lints_accept_undated_pov_when_temporal_support_is_absent
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    report = validator.validate_text(
      "Background/Undated Example.md",
      <<~MARKDOWN
        ---
        lintedAt: "2026-08-20T09:00:00-04:00"
        lintVersion: "#{TaelgarNoteLint::VERSION}"
        tags: [background]
        POV: undated
        ---
        # Undated Example

        The available material does not establish when this account should be read.

        %%^povNotes:v1%%
        Temporal coverage: undated; the available evidence does not support a modern, decade, or year reading position.
        %%^End%%
      MARKDOWN
    )

    refute_includes rule_ids(report), "metadata.pov_missing"
    refute_includes rule_ids(report), "metadata.pov_shape"
    assert_equal TaelgarNoteLint::VERSION, report.fetch("validatorVersion")
  end

  def test_current_name_review_still_validates_malformed_existing_blocks
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    report = validator.validate_text(
      "People/Julius.md",
      "---\nlintedAt: \"2026-08-20T09:00:00-04:00\"\nlintVersion: \"#{TaelgarNoteLint::NAME_REVIEW_VERSION}\"\ntags: [person]\nspecies: human\nknownTo: []\n---\n# Julius\n\n%%^Metadata:names:v1%%\n- not-a-mapping\n%%^End%%\n"
    )

    refute_includes rule_ids(report), "identity.implicit_name"
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

  def test_missing_map_findings_supply_profile_specific_skeletons
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    expected = {
      "waterway" => <<~BLOCK.chomp,
        %%^Metadata:map:v1%%
        locations:
          - {role: source, feature: , map: world, locator: }
          - {role: outlet, feature: , map: world, locator: }
        %%^End%%
      BLOCK
      "road" => <<~BLOCK.chomp,
        %%^Metadata:map:v1%%
        locations:
          - {feature: , map: world, locator: }
          - {feature: , map: world, locator: }
        %%^End%%
      BLOCK
      "settlement" => <<~BLOCK.chomp
        %%^Metadata:map:v1%%
        locations:
          - {map: world, locator: }
        %%^End%%
      BLOCK
    }

    expected.each do |type, candidate|
      report = validator.validate_text(
        "Gazetteer/Test.md",
        "---\ntags: [place]\ntypeOf: #{type}\n---\n# Test\n"
      )
      finding = report.fetch("findings").find { |item| item["ruleId"] == "metadata.map_missing" }

      refute_nil finding
      assert_equal candidate, finding.dig("details", "candidate")
      refute_includes candidate, "status: missing"
    end
  end

  def test_typed_map_skeletons_remain_open_until_positions_are_filled
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    cases = {
      "waterway" => [
        TaelgarNoteLint.map_block_template("waterway"),
        %w[source.locator outlet.locator]
      ],
      "road" => [
        TaelgarNoteLint.map_block_template("road"),
        ["endpoint 1.locator", "endpoint 2.locator"]
      ],
      "settlement" => [TaelgarNoteLint.map_block_template("settlement"), %w[locator]]
    }

    cases.each do |type, (block, missing_fields)|
      report = validator.validate_text(
        "Gazetteer/Test.md",
        "---\ntags: [place]\ntypeOf: #{type}\n---\n# Test\n\n#{block}\n"
      )
      finding = report.fetch("findings").find { |item| item["ruleId"] == "metadata.map_location_missing" }

      refute_nil finding
      assert_equal missing_fields, finding.dig("details", "missingFields")
      refute_includes rule_ids(report), "metadata.map_geometry_missing"
    end
  end

  def test_completed_typed_map_entries_clear_the_missing_location_finding
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    blocks = {
      "waterway" => <<~BLOCK.chomp,
        %%^Metadata:map:v1%%
        locations:
          - {role: source, feature: , map: world, locator: "13.07.F16"}
          - {role: outlet, feature: Gulf of Chardon, map: world, locator: "13.07.C18"}
        %%^End%%
      BLOCK
      "road" => <<~BLOCK.chomp,
        %%^Metadata:map:v1%%
        locations:
          - {feature: Chardon, map: world, locator: "13.07.F16"}
          - {feature: Tollen, map: world, locator: "13.07.C18"}
        %%^End%%
      BLOCK
      "settlement" => <<~BLOCK.chomp
        %%^Metadata:map:v1%%
        locations:
          - {map: world, locator: "13.07.F16"}
        %%^End%%
      BLOCK
    }

    blocks.each do |type, block|
      report = validator.validate_text(
        "Gazetteer/Test.md",
        "---\ntags: [place]\ntypeOf: #{type}\n---\n# Test\n\n#{block}\n"
      )

      refute_includes rule_ids(report), "metadata.map_location_missing"
    end
  end

  def test_legacy_empty_map_placeholder_proposes_the_typed_replacement
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    report = validator.validate_text(
      "Gazetteer/Test.md",
      "---\ntags: [place]\ntypeOf: settlement\n---\n# Test\n\n%%^Metadata:map:v1%%\nstatus: missing\nlocations: []\n%%^End%%\n"
    )
    finding = report.fetch("findings").find { |item| item["ruleId"] == "metadata.map_location_missing" }

    refute_nil finding
    assert_equal TaelgarNoteLint.map_block_template("settlement"), finding.dig("details", "candidate")
  end

  def test_world_hex_locator_requires_world_map
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    report = validator.validate_text(
      "Gazetteer/Test Road.md",
      "---\ntags: [place]\ntypeOf: road\n---\n%%^Metadata:map:v1%%\nlocations:\n  - {feature: Chardon, map: regional, locator: 13.07.F16}\n  - {feature: Tollen, map: world, locator: 13.07.C18}\n%%^End%%\n# Test Road\n"
    )

    assert_includes rule_ids(report), "metadata.map_world_hex_mismatch"
  end

  def test_map_profile_shapes_and_required_map_field_are_validated
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)

    road = validator.validate_text(
      "Gazetteer/Test Road.md",
      "---\ntags: [place]\ntypeOf: road\n---\n%%^Metadata:map:v1%%\nlocations:\n  - {feature: Chardon, map: world, locator: 13.07.F16}\n%%^End%%\n# Test Road\n"
    )
    assert_includes rule_ids(road), "metadata.map_profile_shape"

    waterway = validator.validate_text(
      "Gazetteer/Test River.md",
      "---\ntags: [place]\ntypeOf: waterway\n---\n%%^Metadata:map:v1%%\nlocations:\n  - {role: source, feature: , map: world, locator: 13.07.F16}\n  - {role: source, feature: , map: world, locator: 13.07.C18}\n%%^End%%\n# Test River\n"
    )
    assert_includes rule_ids(waterway), "metadata.map_profile_shape"

    settlement = validator.validate_text(
      "Gazetteer/Test Settlement.md",
      "---\ntags: [place]\ntypeOf: settlement\n---\n%%^Metadata:map:v1%%\nlocations:\n  - {locator: 13.07.F16}\n%%^End%%\n# Test Settlement\n"
    )
    assert_includes rule_ids(settlement), "metadata.map_required_field"
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
    hidden_source_path = ".backups/Research/Julius Notes.md"
    write_note(
      root,
      hidden_source_path,
      "---\ntags: [meta]\naudience: [none]\n---\n# Julius Notes\n\n[[Julius]] once crossed this region.\n"
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
    assert_equal "vault-note", by_path.fetch(hidden_source_path).fetch("sourceKind")
    assert_equal true, by_path.fetch(hidden_source_path).fetch("mentionChanged")
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

  def test_persistent_blocks_are_at_note_end_and_legacy_article_blocks_get_a_copy_ready_migration
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    block = "%%^povNotes:v1%%\nTemporal coverage: modern; the geography has no narrower established limitation.\n%%^End%%"
    misplaced = validator.validate_text(
      "Gazetteer/Test.md",
      "---\ntags: [place]\ntypeOf: forest\n---\n#{block}\n\n# Test\n\nBody.\n"
    )
    placed = validator.validate_text(
      "Gazetteer/Test.md",
      "---\ntags: [place]\ntypeOf: forest\n---\n# Test\n\nBody.\n\n#{block}\n"
    )
    legacy = validator.validate_text(
      "Gazetteer/Test.md",
      "---\ntags: [place]\ntypeOf: forest\n---\n# Test\n\nBody.\n\n%%^Metadata:article:v1%%\nmode: geographic reference\npovNotes: \"Temporal coverage: modern; the geography has no narrower established limitation.\"\n%%^End%%\n"
    )

    assert_includes rule_ids(misplaced), "metadata.position"
    refute_includes rule_ids(placed), "metadata.position"
    finding = legacy.fetch("findings").find { |item| item["ruleId"] == "metadata.legacy_article_block" }
    refute_nil finding
    assert_equal block, finding.dig("details", "candidate")
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

  def test_inline_campaign_block_in_header_callout_is_not_a_meta_comment
    root = make_vault
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: false)
    report = validator.validate_text(
      "People/Test.md",
      "---\ntags: [person]\nspecies: human\n---\n# Test\n> [!info] Header\n>> %%^Campaign:dufr%% Met by the party. %%^End%%\n\nBody.\n"
    )

    refute_includes rule_ids(report), "comment.before_header"
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

  def test_dm_notes_review_uses_four_state_table_without_secret_block_influence
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
    write_note(
      root,
      "People/No Private Needed.md",
      "---\ntags: [person]\nspecies: human\nknownTo: []\ndm_owner: tim\ndm_notes: none\n---\n# No Private Needed\n"
    )
    index = TaelgarNoteLint::NoteIndex.new(Pathname.new(root))
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: true, index: index)
    review = validator.validate_path("Groups/Aatmaji Dynasty.md")
    supported = validator.validate_path("Groups/Positive Dynasty.md")
    secret = validator.validate_path("People/Secret Subject.md")
    unsupported = validator.validate_path("People/No Private File.md")
    clean_none = validator.validate_path("People/No Private Needed.md")
    finding = review.fetch("findings").find { |item| item["ruleId"] == "dm.notes_private_evidence_review" }

    refute_nil finding
    assert_equal "info", finding.fetch("severity")
    assert_equal ["_DM_/Dunmar Notes.md"], finding.dig("details", "sources").map { |source| source["path"] }
    assert_includes rule_ids(supported), "dm.notes_private_evidence_found"
    refute_includes rule_ids(supported), "dm.notes_no_local_evidence"
    assert_includes rule_ids(secret), "dm.notes_private_evidence_review"
    assert_includes rule_ids(unsupported), "dm.notes_no_local_evidence"
    refute rule_ids(clean_none).any? { |rule_id| rule_id.start_with?("dm.notes_") }

    review["fixes"] = []
    markdown = TaelgarNoteLint::CLI.new([]).send(:markdown, [review])
    assert_includes markdown, "[[_DM_/Dunmar Notes]]"
    refute_includes markdown, "`_DM_/Dunmar Notes.md`"
  end

  def test_dm_notes_review_uses_linted_at_until_matching_private_source_is_modified
    root = make_vault
    linted_at = "2026-08-20T09:00:00-04:00"
    note_path = "Groups/Validated Dynasty.md"
    write_note(
      root,
      note_path,
      <<~MARKDOWN
        ---
        lintedAt: "#{linted_at}"
        lintVersion: "#{TaelgarNoteLint::DM_NOTES_REVIEW_VERSION}"
        tags: [group]
        name: Validated Dynasty
        dm_owner: tim
        dm_notes: none
        POV: undated
        ---
        # Validated Dynasty

        %%^povNotes:v1%%
        Temporal coverage: undated; the available evidence does not support a modern, decade, or year reading position.
        %%^End%%
      MARKDOWN
    )
    dm_path = File.join(root, "_DM_", "Validated Notes.md")
    write_note(root, "_DM_/Validated Notes.md", "# Validated Notes\n\n[[Validated Dynasty]] has private material.\n")
    old_time = Time.iso8601("2026-08-20T08:00:00-04:00")
    File.utime(old_time, old_time, dm_path)

    old_validator = TaelgarNoteLint::Validator.new(root: root, check_links: true)
    old_report = old_validator.validate_path(note_path)

    refute_includes rule_ids(old_report), "dm.notes_private_evidence_review"
    refute old_report.dig("reviewGates", "dmNotes", "required")

    new_time = Time.iso8601("2026-08-20T10:00:00-04:00")
    File.utime(new_time, new_time, dm_path)
    new_validator = TaelgarNoteLint::Validator.new(root: root, check_links: true)
    new_report = new_validator.validate_path(note_path)
    finding = new_report.fetch("findings").find { |item| item["ruleId"] == "dm.notes_private_evidence_review" }

    refute_nil finding
    assert new_report.dig("reviewGates", "dmNotes", "required")
    assert_equal "_DM_/Validated Notes.md", finding.dig("details", "sources", 0, "path")
    assert_operator Time.iso8601(finding.dig("details", "sources", 0, "modifiedAt")), :>, Time.iso8601(linted_at)
  end

  def test_dm_notes_review_can_be_forced_for_an_explicit_targeted_repair
    root = make_vault
    linted_at = "2026-08-20T09:00:00-04:00"
    note_path = "Groups/Forced Review.md"
    write_note(
      root,
      note_path,
      <<~MARKDOWN
        ---
        lintedAt: "#{linted_at}"
        lintVersion: "#{TaelgarNoteLint::DM_NOTES_REVIEW_VERSION}"
        tags: [group]
        name: Forced Review
        dm_owner: tim
        dm_notes: none
        POV: undated
        ---
        # Forced Review

        This dynasty is documented in the test vault.

        %%^povNotes:v1%%
        Temporal coverage: undated; the available evidence does not support a modern, decade, or year reading position.
        %%^End%%
      MARKDOWN
    )
    dm_path = File.join(root, "_DM_", "Forced Review Notes.md")
    write_note(root, "_DM_/Forced Review Notes.md", "# Notes\n\n[[Forced Review]] has private material.\n")
    old_time = Time.iso8601("2026-08-20T08:00:00-04:00")
    File.utime(old_time, old_time, dm_path)

    ordinary = TaelgarNoteLint::Validator.new(root: root, check_links: true).validate_path(note_path)
    forced = TaelgarNoteLint::Validator.new(
      root: root,
      check_links: true,
      force_dm_notes_review: true
    ).validate_path(note_path)

    refute ordinary.dig("reviewGates", "dmNotes", "required")
    refute_includes rule_ids(ordinary), "dm.notes_private_evidence_review"
    assert forced.dig("reviewGates", "dmNotes", "required")
    assert_includes rule_ids(forced), "dm.notes_private_evidence_review"
    assert_equal "_DM_/Forced Review Notes.md",
                 forced.fetch("findings").find { |item| item["ruleId"] == "dm.notes_private_evidence_review" }
                       .dig("details", "sources", 0, "path")
  end

  def test_dm_notes_review_rechecks_versions_below_threshold_and_always_validates_vocabulary
    root = make_vault
    note_path = "Groups/Legacy Dynasty.md"
    write_note(
      root,
      note_path,
      <<~MARKDOWN
        ---
        lintedAt: "2026-08-20T09:00:00-04:00"
        lintVersion: "2.7"
        tags: [group]
        name: Legacy Dynasty
        dm_owner: tim
        dm_notes: none
        ---
        # Legacy Dynasty
      MARKDOWN
    )
    dm_path = File.join(root, "_DM_", "Legacy Notes.md")
    write_note(root, "_DM_/Legacy Notes.md", "# Legacy Notes\n\n[[Legacy Dynasty]] has private material.\n")
    old_time = Time.iso8601("2026-08-20T08:00:00-04:00")
    File.utime(old_time, old_time, dm_path)
    write_note(
      root,
      "Groups/Validated Positive.md",
      <<~MARKDOWN
        ---
        lintedAt: "2026-08-20T09:00:00-04:00"
        lintVersion: "#{TaelgarNoteLint::VERSION}"
        tags: [group]
        name: Validated Positive
        dm_owner: tim
        dm_notes: important
        ---
        # Validated Positive
      MARKDOWN
    )
    unrelated_path = File.join(root, "_DM_", "Unrelated New Notes.md")
    write_note(root, "_DM_/Unrelated New Notes.md", "# Unrelated New Notes\n\nNothing matches the validated subject.\n")
    new_time = Time.iso8601("2026-08-20T10:00:00-04:00")
    File.utime(new_time, new_time, unrelated_path)
    write_note(
      root,
      "Groups/Invalid Attestation.md",
      <<~MARKDOWN
        ---
        lintedAt: "2026-08-20T09:00:00-04:00"
        lintVersion: "#{TaelgarNoteLint::DM_NOTES_REVIEW_VERSION}"
        tags: [group]
        name: Invalid Attestation
        dm_owner: tim
        dm_notes: tim
        ---
        # Invalid Attestation
      MARKDOWN
    )
    validator = TaelgarNoteLint::Validator.new(root: root, check_links: true)

    assert_includes rule_ids(validator.validate_path(note_path)), "dm.notes_private_evidence_review"
    refute_includes rule_ids(validator.validate_path("Groups/Validated Positive.md")), "dm.notes_no_local_evidence"
    assert_includes rule_ids(validator.validate_path("Groups/Invalid Attestation.md")), "dm.notes_unknown"
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
    copy_lint_value_catalog(root)
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

  def copy_lint_value_catalog(root)
    repository_root = File.expand_path("..", __dir__)
    source_sidecar = File.join(__dir__, "taelgar_lint_values.json")
    sidecar = JSON.parse(File.read(source_sidecar))
    FileUtils.cp(source_sidecar, File.join(root, "_scripts", "taelgar_lint_values.json"))
    sidecar.fetch("sources").each do |source|
      relative_path = source.fetch("path")
      destination = File.join(root, relative_path)
      FileUtils.mkdir_p(File.dirname(destination))
      FileUtils.cp(File.join(repository_root, relative_path), destination)
    end
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
