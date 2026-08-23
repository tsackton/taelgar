# frozen_string_literal: true

require "fileutils"
require "json"
require "minitest/autorun"
require "tmpdir"

require_relative "generate_language_pronunciation_analogues"

class GenerateLanguagePronunciationAnaloguesTest < Minitest::Test
  def test_committed_sidecar_matches_complete_authoritative_catalog
    root = Pathname.new(__dir__).parent
    expected = TaelgarLanguagePronunciationAnalogues.build(root)
    actual = JSON.parse(File.read(root.join(TaelgarLanguagePronunciationAnalogues::OUTPUT_PATH)))

    assert_equal expected, actual
    assert_equal 2, actual.fetch("schemaVersion")
    assert_equal 3, actual.fetch("families").length
    assert_equal 39, actual.fetch("languages").length

    northros = actual.fetch("families").find { |entry| entry["family"] == "Northros" }
    assert_equal "Northros languages are based on Semitic languages", northros.dig("guidance", "analogueText")
    assert_includes northros.fetch("lookupTerms"), "Northos"

    vargaldi = actual.fetch("languages").find { |entry| entry["language"] == "Vargaldi" }
    assert_equal "undetermined", vargaldi.dig("directGuidance", "mappingStatus")
    assert_equal "Not defined, although many names are Slavic reflecting Eastros influences.",
                 vargaldi.dig("directGuidance", "analogueText")
    assert_equal "Northros", vargaldi.dig("fallbackGuidance", 0, "source")

    free_orcish = actual.fetch("languages").find { |entry| entry["language"] == "Free Orcish" }
    assert_nil free_orcish["directGuidance"]
    assert_equal "Orcish", free_orcish["parentLanguage"]
    assert_equal "Turkic", free_orcish.dig("fallbackGuidance", 0, "analogueText")
    assert_equal "parent_language", free_orcish.dig("fallbackGuidance", 0, "kind")

    addermarian = actual.fetch("languages").find { |entry| entry["language"] == "Addermarian" }
    assert_includes addermarian.fetch("lookupTerms"), "Addermarch"
    mawaran = actual.fetch("languages").find { |entry| entry["language"] == "Mawaran" }
    assert_includes mawaran.fetch("lookupTerms"), "Mawarian"
  end

  def test_current_name_metadata_coverage_audit_surfaces_only_unsupported_amani
    root = Pathname.new(__dir__).parent
    data = JSON.parse(File.read(root.join(TaelgarLanguagePronunciationAnalogues::OUTPUT_PATH)))

    audit = TaelgarLanguagePronunciationAnalogues.audit_name_languages(root, data)

    assert_empty audit.fetch("parseErrors")
    assert_equal ["Amani"], audit.fetch("uncovered").map { |entry| entry.fetch("language") }
    assert_includes TaelgarLanguagePronunciationAnalogues.matching_guidance_labels(data, "Northros"), "family:Northros"
    assert_equal ["unknown"], audit.fetch("ignored").map { |entry| entry.fetch("language") }
  end

  def test_generator_extracts_direct_family_and_parent_guidance_and_checks_staleness
    Dir.mktmpdir("language-guidance-test.") do |root|
      source = File.join(root, "Background", "Languages.md")
      FileUtils.mkdir_p(File.dirname(source))
      File.write(
        source,
        <<~MARKDOWN
          # Languages

          ## Northros Language Family
          _Real world analog_: Semitic languages generally

          ##### Vargaldi
          _Real world analog_: Not defined, although many names are Slavic.

          ## Non-Human Languages
          ##### Orcish
          _Real world analog_: Turkic

          ##### Free Orcish
          A dialect of Orcish.
        MARKDOWN
      )
      FileUtils.mkdir_p(File.join(root, "_scripts"))
      output = File.join(root, TaelgarLanguagePronunciationAnalogues::OUTPUT_PATH)
      File.write(output, "{}\n")

      data = TaelgarLanguagePronunciationAnalogues.build(Pathname.new(root))
      vargaldi = data.fetch("languages").find { |entry| entry["language"] == "Vargaldi" }
      free_orcish = data.fetch("languages").find { |entry| entry["language"] == "Free Orcish" }
      assert_equal "undetermined", vargaldi.dig("directGuidance", "mappingStatus")
      assert_equal "Semitic languages generally", vargaldi.dig("fallbackGuidance", 0, "analogueText")
      assert_equal "Turkic", free_orcish.dig("fallbackGuidance", 0, "analogueText")

      older = Time.now - 60
      File.utime(older, older, output)
      assert TaelgarLanguagePronunciationAnalogues.stale?(Pathname.new(root))

      newer = Time.now + 60
      File.utime(newer, newer, output)
      refute TaelgarLanguagePronunciationAnalogues.stale?(Pathname.new(root))
    end
  end

  def test_coverage_audit_reports_unmatched_values_without_guessing
    Dir.mktmpdir("language-audit-test.") do |root|
      root_path = Pathname.new(root)
      FileUtils.mkdir_p(root_path.join("People"))
      File.write(
        root_path.join("People", "Names.md"),
        <<~MARKDOWN
          # Names

          %%^Metadata:names:v1%%
          - {name: Covered, language: Northros}
          - {name: Unknown, language: unknown}
          - {name: Uncovered, language: Amani}
          %%^End%%
        MARKDOWN
      )
      data = {
        "families" => [
          {
            "entryType" => "family",
            "family" => "Northros",
            "lookupTerms" => ["Northros"]
          }
        ],
        "languages" => []
      }

      audit = TaelgarLanguagePronunciationAnalogues.audit_name_languages(root_path, data)

      assert_equal 1, audit.dig("summary", "coveredLanguageValues")
      assert_equal ["unknown"], audit.fetch("ignored").map { |entry| entry.fetch("language") }
      assert_equal ["Amani"], audit.fetch("uncovered").map { |entry| entry.fetch("language") }
    end
  end
end
