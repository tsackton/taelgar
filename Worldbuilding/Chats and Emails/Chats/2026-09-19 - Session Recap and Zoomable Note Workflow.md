# 2026-09-19 - Session Recap and Zoomable Note Workflow

[2026-09-19 12:00 PM] Deciusmus: I'm spending some time trying to clean up the Cleenseau session notes, in prep for trying to get all my worldbuilding more correctly in the main vault...

    I'm using codex pretty heavily, but obviously I have a much weaker source pipeline as there are no transcripts.  Although in the first session I tried, codex did a pretty good job coorelating with my adventure dm notes for names and such.

    Remind me how the dunmari pipeline works? You have a very nice dunmari session 1-5 with images, highlights, etc

    If I understand correctly, the python script should be fully building the main session note from the _generated folder, right? And that is what powers the taeglarverse "zoomable" pieces?

[2026-09-19 02:19 PM] Deciusmus: Is the majority of your pipeline around creating the _generated folder from transcripts?

[2026-09-19 03:18 PM] rsulfuratus: whoops didn't see this earlier.

    the python script exports the session recap into structured text in _generated
    there is a templater script that builds the actual session note from the _generated components, based on a template in the frontmatter.

[2026-09-19 03:18 PM] rsulfuratus: this is all controlled by:
    ```
    sessionKey: dunmari-frontier-session-1
    session-template: dunmar-frontier-template.md
    ```

[2026-09-19 03:18 PM] rsulfuratus: the sessionKey says what _generated folder to look in
    the session-template structures the output

[2026-09-19 03:19 PM] rsulfuratus: there is not a ton of documentation of this step but codex should be able to figure out how to set up a template based on existing stuff

[2026-09-19 03:19 PM] rsulfuratus: i just pushed all my skills, so you can build off those

[2026-09-19 03:20 PM] rsulfuratus: the agentic skill pipeline is built around generating the session recap from the transcript

[2026-09-19 03:20 PM] rsulfuratus: however, it doesn't really need to be based on a transcript, for example you can look at mawar ep 1 which is one of the few i don't have recorded

[2026-09-19 03:21 PM] rsulfuratus: the key thing is the session recap is the human gated component, that is what you would need to edit. downstream of there is deterministic; upstream is agentic

[2026-09-19 03:21 PM] rsulfuratus: the zoomable stuff is separate, and is part of the website code

[2026-09-19 03:23 PM] rsulfuratus: it should be extendable to work if you just have short/medium/long and don't have a transcript view, but so far i haven't tried this

[2026-09-19 03:24 PM] rsulfuratus: note that the zoomable code rebuilds the entire narrative section from the session recap (and linked beat transcripts) directly

[2026-09-19 03:25 PM] rsulfuratus: it does attempt to backport links if you manually edit links but i don't know how well this works. i tend to add aliased links directly to the session recap text.

[2026-09-19 03:25 PM] rsulfuratus: note also that if you have notes for NPCs, locations, etc, the templater code automatically pulls information for you from frontmatter.

[2026-09-19 03:27 PM] rsulfuratus: the images come from the session recap. there is a note in MoC (Image Callouts) that gives the formatting. most of this is built into website css and obsidian css/code that should be shared

[2026-09-19 03:33 PM] rsulfuratus: changing the zoomable view (which is turned on by frontmatter) looks pretty simple

[2026-09-19 03:33 PM] rsulfuratus: if you get to that point, just make sure codex runs the tests so that the existing dunmar/feywild/chasm stuff doesn't break

[2026-09-19 03:40 PM] rsulfuratus: generally my advice would be to stick with the session recap format, but potentially you could build your own cleenseau-session-recap skill that works primarily from whatever text you have. but then you can reuse all the deterministic parts
