# frozen_string_literal: true

require "fileutils"
require "json"
require "minitest/autorun"
require "tmpdir"

require_relative "generate_language_pronunciation_analogues"

class GenerateLanguagePronunciationAnaloguesTest < Minitest::Test
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

          ##### Addermarian
          _Real world analog_: Fixture guidance for a lookup alias.

          ##### Mawaran
          _Real world analog_: Fixture guidance for another lookup alias.
        MARKDOWN
      )
      FileUtils.mkdir_p(File.join(root, "_scripts"))
      output = File.join(root, TaelgarLanguagePronunciationAnalogues::OUTPUT_PATH)
      File.write(output, "{}\n")

      data = TaelgarLanguagePronunciationAnalogues.build(Pathname.new(root))
      assert_equal 2, data.fetch("schemaVersion")
      assert_equal 1, data.fetch("families").length
      assert_equal 5, data.fetch("languages").length
      assert_includes data.fetch("families").first.fetch("lookupTerms"), "Northos"
      assert_equal ["family:Northros"], TaelgarLanguagePronunciationAnalogues.matching_guidance_labels(data, "Northros")
      assert_equal ["language:Addermarian"], TaelgarLanguagePronunciationAnalogues.matching_guidance_labels(data, "Addermarch")
      assert_equal ["language:Mawaran"], TaelgarLanguagePronunciationAnalogues.matching_guidance_labels(data, "Mawarian")
      vargaldi = data.fetch("languages").find { |entry| entry["language"] == "Vargaldi" }
      free_orcish = data.fetch("languages").find { |entry| entry["language"] == "Free Orcish" }
      assert_equal "undetermined", vargaldi.dig("directGuidance", "mappingStatus")
      assert_equal "Semitic languages generally", vargaldi.dig("fallbackGuidance", 0, "analogueText")
      assert_nil free_orcish["directGuidance"]
      assert_equal "Orcish", free_orcish["parentLanguage"]
      assert_equal "parent_language", free_orcish.dig("fallbackGuidance", 0, "kind")
      assert_equal "Turkic", free_orcish.dig("fallbackGuidance", 0, "analogueText")
      File.write(output, JSON.generate(data))
      assert_equal data, TaelgarLanguagePronunciationAnalogues.read_and_validate_sidecar(Pathname.new(root))

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

      assert_empty audit.fetch("parseErrors")
      assert_equal 1, audit.dig("summary", "coveredLanguageValues")
      assert_equal ["unknown"], audit.fetch("ignored").map { |entry| entry.fetch("language") }
      assert_equal ["Amani"], audit.fetch("uncovered").map { |entry| entry.fetch("language") }
    end
  end
end
