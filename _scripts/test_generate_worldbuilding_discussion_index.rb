# frozen_string_literal: true

require "fileutils"
require "json"
require "minitest/autorun"
require "tmpdir"

require_relative "generate_worldbuilding_discussion_index"

class GenerateWorldbuildingDiscussionIndexTest < Minitest::Test
  def test_committed_sidecar_matches_current_non_staging_worldbuilding_sources
    root = Pathname.new(__dir__).parent
    expected = TaelgarWorldbuildingDiscussionIndex.build(root)
    actual = JSON.parse(File.read(root.join(TaelgarWorldbuildingDiscussionIndex::OUTPUT_PATH)))

    assert_equal expected, actual
    assert_equal 1, actual.fetch("schemaVersion")
    refute actual.fetch("sources").any? { |source| source.fetch("path").split("/").include?("Staging") }
  end

  def test_index_keeps_every_matching_source_and_records_match_and_thread_metadata
    Dir.mktmpdir("worldbuilding-discussion-index-test.") do |directory|
      root = Pathname.new(directory)
      write_note(root, "People/Archfey Ethlenn.md", canonical_note("Archfey Ethlenn", aliases: ["Queen of the Evening Mist"]))
      write_note(root, "People/Dunmar.md", canonical_note("Dunmar"))
      write_note(
        root,
        "Worldbuilding/Chats and Emails/Chats/2024-01-01 - Ethlenn and Umbraeth.md",
        "# Conversation\n\n[[Archfey Ethlenn|Ethlenn]] is under discussion.\n"
      )
      write_note(
        root,
        "Worldbuilding/Chats and Emails/Chats/2024-01-02 - Fey Bargains.md",
        "# Conversation\n\nEthlenn appears here without a link.\n"
      )
      write_note(
        root,
        "Worldbuilding/Talk/Ethlenn Alternatives.md",
        "# Other questions\n\nThe body uses only a pronoun.\n"
      )
      write_note(
        root,
        "Worldbuilding/Staging/Ethlenn Draft.md",
        "# Staging\n\nEthlenn must not be indexed from staging.\n"
      )
      write_note(
        root,
        "Worldbuilding/staging/Ethlenn Lowercase Draft.md",
        "# Staging\n\nEthlenn must not be indexed from lowercase staging either.\n"
      )
      write_note(root, "Worldbuilding/Dunmar Notes.md", "# Dunmar Notes\n\n[[Dunmar]] is discussed here.\n")

      data = TaelgarWorldbuildingDiscussionIndex.build(root)
      subject = data.fetch("subjects").find { |record| record.fetch("path") == "People/Archfey Ethlenn.md" }

      assert_equal 3, subject.fetch("sourceCount")
      assert_equal true, subject.fetch("significant")
      assert_equal 3, subject.fetch("sources").length
      assert_includes subject.fetch("sources")[0].fetch("matchKinds"), "link"
      assert_includes subject.fetch("sources")[1].fetch("matchKinds"), "name"
      assert_includes subject.fetch("sources")[2].fetch("matchKinds"), "title"
      assert_equal "2024-01-01", subject.fetch("sources")[0].fetch("dateStart")
      assert_equal "Worldbuilding/Chats and Emails/Chats:ethlenn-and-umbraeth",
                   subject.fetch("sources")[0].fetch("threadCluster")
      root_source = data.fetch("sources").find do |source|
        source.fetch("path") == "Worldbuilding/Dunmar Notes.md"
      end
      assert_equal "Worldbuilding", root_source.fetch("sourceKind")
      refute data.fetch("sources").any? { |source| source.fetch("path").downcase.include?("/staging/") }
      assert_equal TaelgarWorldbuildingDiscussionIndex.identity_sha256(
        TaelgarNoteLint::ParsedNote.new("People/Archfey Ethlenn.md", File.read(root.join("People/Archfey Ethlenn.md")))
      ), data.fetch("identityIndex").fetch("People/Archfey Ethlenn.md")
    end
  end

  def test_sidecar_query_is_bounded_and_rejects_stale_target_identity
    Dir.mktmpdir("worldbuilding-discussion-sidecar-test.") do |directory|
      root = Pathname.new(directory)
      target = "People/Archfey Ethlenn.md"
      write_note(root, target, canonical_note("Archfey Ethlenn"))
      write_note(root, "Worldbuilding/Talk/One.md", "# One\n\n[[Archfey Ethlenn|Ethlenn]] appears here.\n")
      write_note(root, "Worldbuilding/Talk/Two.md", "# Two\n\nArchfey Ethlenn appears here.\n")
      write_sidecar(root)

      note = TaelgarNoteLint::ParsedNote.new(target, File.read(root.join(target)))
      result = TaelgarWorldbuildingDiscussionIndex::Sidecar.new(root).for(note)
      assert_equal true, result.fetch("significant")
      assert_equal 2, result.fetch("sourceCount")

      write_note(root, target, canonical_note("Archfey Ethlenn", aliases: ["Mist Queen"]))
      changed = TaelgarNoteLint::ParsedNote.new(target, File.read(root.join(target)))
      error = assert_raises(TaelgarWorldbuildingDiscussionIndex::Error) do
        TaelgarWorldbuildingDiscussionIndex::Sidecar.new(root).for(changed)
      end
      assert_includes error.message, "stale for People/Archfey Ethlenn.md"
    end
  end

  private

  def canonical_note(name, aliases: [])
    alias_line = aliases.empty? ? "" : "aliases: [#{aliases.join(', ')}]\n"
    <<~MARKDOWN
      ---
      tags: [person]
      name: #{name}
      #{alias_line}---
      # #{name}

      #{name} is a fixture subject.
    MARKDOWN
  end

  def write_note(root, relative, text)
    path = root.join(relative)
    FileUtils.mkdir_p(path.dirname)
    path.write(text, mode: "w", encoding: "UTF-8")
  end

  def write_sidecar(root)
    output = root.join(TaelgarWorldbuildingDiscussionIndex::OUTPUT_PATH)
    FileUtils.mkdir_p(output.dirname)
    output.write(
      "#{JSON.pretty_generate(TaelgarWorldbuildingDiscussionIndex.build(root))}\n",
      mode: "w",
      encoding: "UTF-8"
    )
  end
end
