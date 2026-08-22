# frozen_string_literal: true

require "fileutils"
require "json"
require "minitest/autorun"
require "tmpdir"

require_relative "generate_language_pronunciation_analogues"

class GenerateLanguagePronunciationAnaloguesTest < Minitest::Test
  def test_committed_sidecar_matches_the_authoritative_source_block
    root = Pathname.new(__dir__).parent
    expected = TaelgarLanguagePronunciationAnalogues.build(root)
    actual = JSON.parse(File.read(root.join(TaelgarLanguagePronunciationAnalogues::OUTPUT_PATH)))

    assert_equal expected, actual
    assert actual.fetch("languages").any? { |entry| entry["language"] == "Chardonian" }
    assert actual.fetch("languages").any? { |entry| entry["status"] == "undetermined" }
    vargaldi = actual.fetch("languages").find { |entry| entry["language"] == "Vargaldi" }
    assert_equal "undetermined", vargaldi.fetch("status")
    assert_equal "Not defined, although many names are Slavic reflecting Eastros influences.",
                 vargaldi.fetch("analogueText")
  end

  def test_generator_extracts_prose_and_uses_sidecar_mtime_for_staleness
    Dir.mktmpdir("language-guidance-test.") do |root|
      source = File.join(root, "Background", "Languages.md")
      FileUtils.mkdir_p(File.dirname(source))
      File.write(
        source,
        <<~MARKDOWN
          # Languages

          ##### Vargaldi
          _Real world analog_: Not defined, although many names are Slavic reflecting Eastros influences.
        MARKDOWN
      )
      FileUtils.mkdir_p(File.join(root, "_scripts"))
      output = File.join(root, TaelgarLanguagePronunciationAnalogues::OUTPUT_PATH)
      File.write(output, "{}\n")

      data = TaelgarLanguagePronunciationAnalogues.build(Pathname.new(root))
      entry = data.fetch("languages").first
      assert_equal "Vargaldi", entry.fetch("language")
      assert_equal "undetermined", entry.fetch("status")
      assert_equal [entry.fetch("analogueText")], entry.fetch("analogues")

      older = Time.now - 60
      File.utime(older, older, output)
      assert TaelgarLanguagePronunciationAnalogues.stale?(Pathname.new(root))

      newer = Time.now + 60
      File.utime(newer, newer, output)
      refute TaelgarLanguagePronunciationAnalogues.stale?(Pathname.new(root))
    end
  end
end
