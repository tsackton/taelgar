# 2026-09-21 - Cleenseau Sources and Climate Constraints

[2026-09-21 01:46 PM] Deciusmus: large PR that adds a huge amount of material to the Cleenseau folders.

    Mentioning it only because Codex made some changes to the shared scripts, mostly to
    (a) fix newline issues on windows
    (b) add support for a linked sourceUrl for session notes for Kiya's Dreamwidth original writeups
    (c) add support for "related writings" to session notes for my various play-by-email followups

    https://github.com/tsackton/taelgar/pull/38

    I'm going to merge it shortly. A lot of the cleenseau material is still check/ai of course but that doesn't really matter to you.

    If you had a sec to glance over the python and other changes I wouldn't mind, but mostly I did a PR because I wanted to quickly review anything OUTSIDE of Cleenseau before I dug into the Cleenseau material

[2026-09-21 01:49 PM] rsulfuratus: i didn't see anything that looks like an issue on a very brief review; fairly minimal code changes

[2026-09-21 01:49 PM] rsulfuratus: if i find anything broken can always fix later, with a "production environment" of two people i don't think it is a big deal

[2026-09-21 01:49 PM] Deciusmus: true 🙂

[2026-09-21 02:14 PM] rsulfuratus: i edited the query in pages that need review to exclude cleenseau campaign and cleenseau staging from the Needs AI Review table, for now, since there are so many. easy enough for you to make your own cleenseau review page if needed

[2026-09-21 02:18 PM] Deciusmus: I finally set up Codex remote so I mostly did this reorg from my phone. I gave Codex access to my email so have pulled I hope most of the long play by email scenes.

    Now I'm trying to better organize it all, then I need to review all the stubs

[2026-09-21 02:20 PM] rsulfuratus: yeah the remote control is pretty nice. i run the session note prep for dunmar from my phone all the time. the limitation is revising the recap/narration text which is slow

[2026-09-21 02:21 PM] Deciusmus: right, I skipped all the narration text. I am mostly focused on getting the NPCs and places pulled out into staging, and getting a well established campaign timeline (some of the dates have been a bit fuzzy lately)

[2026-09-21 02:21 PM] rsulfuratus: yeah i like your strategy of just linking to kiaya's posts for recap text

[2026-09-21 02:22 PM] rsulfuratus: i found a date error in dunmar session 2, which i was afraid was going to mess up the entire campaign timeline, but then i found a date error in the opposite direction in session 3 so it all balanced out

[2026-09-21 02:22 PM] Deciusmus: now I'm working on adding fractional sessions (13.1, 13.2 etc) to better account for play-by-email scenes in-between sessions

[2026-09-21 02:23 PM] Deciusmus: I want to end up with all the "source" material in _sessions/cleanseau.../sources rather than the "Raw Emails" folder int he Cleenseau campaign directory

[2026-09-21 02:23 PM] rsulfuratus: right that makes sense

[2026-09-21 04:47 PM] rsulfuratus: fyi i see you have `websiteSessionView: zoomable` in your cleenseau session note templates.

    right now this works by removing the markdown `## Narrative` section and replacing it with a toggled component built directly from the session-recap.md. currently requires minimally a Short and Long narrative for each recap block, plus a transcript and line ids for each recap block. note that if there is no `## Narrative` block the zoomable view does nothing, so this is inert for most of your notes

    also the python code that builds the stub note e.g. `Cleenseau - Session 22.md` should insert the sessionKey automatically (along with the template and i think tags: `[session-note]`?) so you don't need this in the template, i don't think.

[2026-09-21 08:19 PM] rsulfuratus: I am working on a few random notes that have lint comments, and am currently on the Green Sea and trying to canonicalize and finalize the climatic model. my understanding is these are the facts that need to be accounted for, anything missing?

    (1) The Sembaran monsoon, a summer system bringing wet air from the Green Sea, most likely driven by continental warming that draws cooler maritime air blowing from east to west. However, the exact extent of this is not established (e.g. do these easterlies blow all the way across the northern Green Sea, or just from approx the area NW of Irrla eastward)
    (2) A common pattern for long-distance halfling ships to be sailing east from Ursk in the autumn, established by the Wellby solo and consistent with the "circular trade" brainstorming (spring west from Medju to Cymea; summer north towards Irrla and/or Ursk; fall east towards Eastern Isles; winter southwest toward Medju).
    (3) The Great Desert and the arid south needs to have climatic reasons to be a desert, while south Cymea and the maritime trade peninsula are not a desert.
    (4) The climate of Ursk: cold, snowy winters. Wet springs, short summers. This also has to support the taiga forest stretching west of Ursk.

[2026-09-21 09:13 PM] rsulfuratus: climate discussion with codex is pretty fun, you get these great interactive graphics.
![[../_assets/discord/image-46fb86b33988f5fa.png]]

[2026-09-21 09:13 PM] Deciusmus: This was a copy and paste error

[2026-09-21 09:15 PM] Deciusmus: This looks complete to me.
