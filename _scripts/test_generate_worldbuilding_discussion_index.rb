# frozen_string_literal: true

require "fileutils"
require "json"
require "minitest/autorun"
require "tmpdir"

require_relative "generate_worldbuilding_discussion_index"

class GenerateWorldbuildingDiscussionIndexTest < Minitest::Test
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
      write_note(root, "Worldbuilding/Agentic Review/Local Review.md", "[[Archfey Ethlenn]] must stay local.\n")
      write_note(root, "Worldbuilding/agentic review/Nested/Local Review.md", "[[Archfey Ethlenn]] must stay local.\n")

      data = TaelgarWorldbuildingDiscussionIndex.build(root)
      assert_equal 2, data.fetch("schemaVersion")
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
      refute data.fetch("sources").any? { |source| source.fetch("path").downcase.include?("/agentic review/") }
      assert_equal TaelgarWorldbuildingDiscussionIndex.identity_sha256(
        TaelgarNoteLint::ParsedNote.new("People/Archfey Ethlenn.md", File.read(root.join("People/Archfey Ethlenn.md")))
      ), data.fetch("identityIndex").fetch("People/Archfey Ethlenn.md")
    end
  end

  def test_query_builds_missing_cache_and_refreshes_changed_target_identity
    Dir.mktmpdir("worldbuilding-discussion-sidecar-test.") do |directory|
      root = Pathname.new(directory)
      target = "People/Archfey Ethlenn.md"
      write_note(root, target, canonical_note("Archfey Ethlenn"))
      write_note(root, "Worldbuilding/Talk/One.md", "# One\n\n[[Archfey Ethlenn|Ethlenn]] appears here.\n")
      write_note(root, "Worldbuilding/Talk/Two.md", "# Two\n\nArchfey Ethlenn appears here.\n")
      write_note(root, "Worldbuilding/Talk/Three.md", "# Three\n\nMist Queen appears here.\n")

      note = TaelgarNoteLint::ParsedNote.new(target, File.read(root.join(target)))
      result = TaelgarWorldbuildingDiscussionIndex::Sidecar.new(root).for(note)
      assert_equal true, result.fetch("significant")
      assert_equal 2, result.fetch("sourceCount")
      assert root.join(TaelgarWorldbuildingDiscussionIndex::OUTPUT_PATH).file?

      write_note(root, target, canonical_note("Archfey Ethlenn", aliases: ["Mist Queen"]))
      changed = TaelgarNoteLint::ParsedNote.new(target, File.read(root.join(target)))
      result = TaelgarWorldbuildingDiscussionIndex::Sidecar.new(root).for(changed)
      assert_equal 3, result.fetch("sourceCount")
    end
  end

  def test_content_changes_refresh_even_when_source_timestamp_is_preserved
    with_query_fixture do |root, target, source|
      assert_equal 1, query(root, target).fetch("sourceCount")
      stamp = root.join(source).mtime
      write_note(root, source, "# Unrelated discussion\n")
      File.utime(stamp, stamp, root.join(source))

      assert_equal 0, query(root, target).fetch("sourceCount")
      write_note(root, "Worldbuilding/Talk/New.md", "[[Archfey Ethlenn]]\n")
      assert_equal 1, query(root, target).fetch("sourceCount")
      root.join("Worldbuilding/Talk/New.md").unlink
      assert_equal 0, query(root, target).fetch("sourceCount")
    end
  end

  def test_timestamps_body_edits_and_excluded_sources_do_not_refresh_cache
    with_query_fixture do |root, target, source|
      expected = query(root, target)
      output = root.join(TaelgarWorldbuildingDiscussionIndex::OUTPUT_PATH)
      text = output.binread
      stamp = Time.at(1_000_000)
      File.utime(stamp, stamp, output)
      future = Time.now + 3600
      File.utime(future, future, root.join(source))
      write_note(root, target, root.join(target).read + "\nChanged biography without changing identity.\n")
      write_note(root, "Worldbuilding/Agentic Review/New.md", "[[Archfey Ethlenn]]\n")
      write_note(root, "Worldbuilding/Staging/New.md", "[[Archfey Ethlenn]]\n")

      assert_equal expected, query(root, target)
      assert_equal text, output.binread
      assert_equal stamp, output.mtime
    end
  end

  def test_new_and_removed_identity_collisions_refresh_other_subjects
    with_query_fixture do |root, target, source|
      write_note(root, source, "The Mist Queen appears here.\n")
      write_note(root, target, canonical_note("Archfey Ethlenn", aliases: ["Mist Queen"]))
      assert_equal 1, query(root, target).fetch("sourceCount")

      other = "People/Other Queen.md"
      write_note(root, other, canonical_note("Other Queen", aliases: ["Mist Queen"]))
      assert_equal 0, query(root, target).fetch("sourceCount")
      root.join(other).unlink
      assert_equal 1, query(root, target).fetch("sourceCount")
    end
  end

  def test_primary_name_changes_refresh_even_when_identity_set_is_unchanged
    with_query_fixture do |root, target, _source|
      write_note(root, target, canonical_note("Archfey Ethlenn", aliases: ["Mist Queen"]))
      assert_equal "Archfey Ethlenn", query(root, target).fetch("name")
      write_note(root, target, canonical_note("Mist Queen", aliases: ["Archfey Ethlenn"]))
      assert_equal "Mist Queen", query(root, target).fetch("name")
    end
  end

  def test_missing_stale_and_malformed_cache_can_be_queried_without_writing
    with_query_fixture do |root, target, source|
      output = root.join(TaelgarWorldbuildingDiscussionIndex::OUTPUT_PATH)
      assert_equal 1, query(root, target, persist: false).fetch("sourceCount")
      refute output.exist?

      query(root, target)
      original = output.binread
      write_note(root, source, "# No mention\n")
      assert_equal 0, query(root, target, persist: false).fetch("sourceCount")
      assert_equal original, output.binread

      output.write("{invalid JSON")
      assert_equal 0, query(root, target, persist: false).fetch("sourceCount")
      assert_equal "{invalid JSON", output.read
      assert_equal 0, query(root, target).fetch("sourceCount")
      assert_equal 2, JSON.parse(output.read).fetch("schemaVersion")
    end
  end

  def test_unsupported_schema_and_changed_implementation_rebuild_automatically
    with_query_fixture do |root, target, _source|
      query(root, target)
      output = root.join(TaelgarWorldbuildingDiscussionIndex::OUTPUT_PATH)
      ["schemaVersion", "implementationSha256"].each do |key|
        data = JSON.parse(output.read)
        data[key] = "outdated"
        output.write(JSON.generate(data))
        assert_equal 1, query(root, target).fetch("sourceCount")
        refute_equal "outdated", JSON.parse(output.read).fetch(key)
      end
    end
  end

  def test_cli_query_refreshes_cache_but_check_and_no_cache_are_read_only
    with_query_fixture do |root, target, source|
      output = root.join(TaelgarWorldbuildingDiscussionIndex::OUTPUT_PATH)
      stdout, = capture_io do
        assert_equal 0, TaelgarWorldbuildingDiscussionIndex::CLI.new(["--root", root.to_s, "--query", target, "--no-cache"]).run
      end
      assert_equal 1, JSON.parse(stdout).fetch("sourceCount")
      refute output.exist?
      capture_io do
        assert_equal 2, TaelgarWorldbuildingDiscussionIndex::CLI.new(["--root", root.to_s, "--write", "--no-cache"]).run
      end
      refute output.exist?
      capture_io do
        assert_equal 0, TaelgarWorldbuildingDiscussionIndex::CLI.new(["--root", root.to_s, "--query", target]).run
      end
      original = output.binread
      write_note(root, source, "# No mention\n")
      _, stderr = capture_io do
        assert_equal 2, TaelgarWorldbuildingDiscussionIndex::CLI.new(["--root", root.to_s, "--check"]).run
      end
      assert_includes stderr, "stale"
      assert_equal original, output.binread
    end
  end

  private

  def with_query_fixture
    Dir.mktmpdir("worldbuilding-discussion-cache-test.") do |directory|
      root = Pathname.new(directory)
      target = "People/Archfey Ethlenn.md"
      source = "Worldbuilding/Talk/One.md"
      write_note(root, target, canonical_note("Archfey Ethlenn"))
      write_note(root, source, "[[Archfey Ethlenn]] appears here.\n")
      yield root, target, source
    end
  end

  def query(root, target, persist: true)
    note = TaelgarNoteLint::ParsedNote.new(target, root.join(target).read)
    TaelgarWorldbuildingDiscussionIndex::Sidecar.new(root, persist: persist).for(note)
  end

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
end
