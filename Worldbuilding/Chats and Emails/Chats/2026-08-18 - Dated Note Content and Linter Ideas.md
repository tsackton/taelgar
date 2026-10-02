# 2026-08-18 - Dated Note Content and Linter Ideas

[2026-08-18 08:15 AM] rsulfuratus: doing some work on my planned restart of the Great Library campaign, and wondering about something.

    right now we have an easy way to adjust metadata to the "campaign time" but not an easy way to adjust text.

    this is particularly relevant to the Great Library as it has a time skip to 1752, but will also be relevant to Campaign 3 which is likely to be set in a similar time, maybe between 1751-1754 or so.

    some significant things have changed: the breakup of Dunmar, the independence of Voltara/Northern Provinces, Darba as a Chardonian protectorate and major chalyte port, reopening of (parts of) the Plaguelands. and of course many more minor things.

    the POV tags are useful for recording the dated POV of a page but don't really help manage any kind of time-based text changes.

[2026-08-18 08:15 AM] rsulfuratus: there are a few strategies here, and it is kind of a fun intellectual exercise and AI-programming-challenge.

[2026-08-18 08:16 AM] rsulfuratus: i think in general a pretty low priority except for fun. but if i am going to do something for fun it is worth at least also making it useful, so the question would be what you'd actually want for a time-adjusted text

[2026-08-18 08:20 AM] rsulfuratus: in any case, i might mess around a little before i do a big west coast rewrite to update to 1752. but before i do would be interested to know what would matter to you, in terms of e.g. Taelgarverse 1720 or anything else relevant for your game.

    and also how much you care about obsidian readable vs website. that is, for things like the zoomable session notes, i have a frontmatter tag that creates the zoomable note when you build taelgarverse, and the obsidian session note is flat (with just the "long" narrative). this reduces text duplication in obsidian at the cost of extra (AI-managed) code and ancillary files.

    for time-dated gazetteer pages, for example, you could imagine having different opening paragraphs for different times which would then cause some obsidian clutter. alternatively obsidian could always be latest and you could have sidecar files that replace certain text when you build taelgarverse with a specific target date.

[2026-08-18 09:32 AM] Deciusmus: I am much less concerned about taelgarverse than about being able to  easily tell context in obsidian

[2026-08-18 09:32 AM] Deciusmus: And secondarily, to be able to easily invent dated or date-anchored content, and to be able to preserve or maintain older date-anchored content

[2026-08-18 09:35 AM] rsulfuratus: so probably sidecar files and auto-constructed note text during the taelgarverse build would not be great for those purposes since it hides the details in obsidian

[2026-08-18 09:40 AM] Deciusmus: right

[2026-08-18 09:41 AM] rsulfuratus: so i'm looking at for example Chardonian Empire.

    here is the intro paragraph:
    ```
    The Chardonian Empire is a large and powerful realm ruled from the city of [[Chardon]]. Its power rests on the legions, the city’s institutions of learning and magic, and the wealth of the [[Chalyte|chalyte]] trade. The Chardonian Empire grew from the city of Chardon in the years after the Great War, expanding in fits and starts until it stretched across the entire western coast from [[Voltara]] in the north to [[Illoria]] in the south. Today, the Chardonian Empire is vast and powerful, the dominant cultural, academic, and military force in the west, a place of learning and magic and innovation, that sees itself as the defender of civilization against the forces of evil and the heir to the [[Drankorian Empire]]
    ```

[2026-08-18 09:43 AM] rsulfuratus: that is obviously out of date. while it remains vast and powerful and a dominant cultural/academic power, it does not reach to Voltara, the lost of the northern provinces definitely affected its self-image a bit, the Chataans and the Darba Protectorate are much more important, and the defender of civilization is much more explicit against the remnants of the Cleansed and other "evil chaltyte abusers"

[2026-08-18 09:44 AM] rsulfuratus: the simplest would just be to have two intro paragraphs but that leads to duplicated text in obsidian, not sure how annoying that is.

[2026-08-18 09:44 AM] rsulfuratus: it would probably be possible to write some CSS to customize the obsidian view, of course

[2026-08-18 09:58 AM] Deciusmus: To me, the ideal paragraph would just read something like.

    >` The Chardonian Empire is a large and powerful realm ruled from the city of [[Chardon]]. Its power rests on the legions, the city’s institutions of learning and magic, and the wealth of the [[Chalyte|chalyte]] trade. The Chardonian Empire grew from the city of Chardon in the years after the Great War, expanding in fits and starts until it stretched across the entire western coast from [[Voltara]] in the north to [[Illoria]] in the south. By 1745, the chalyte trade had come to dominate the economy, and the "chaylte houses" of Voltarra were a significant force in Chardonian politics. That all changed in 1748 with the collapse of the chaylte houses and the discovery of chatlye in the Chataan Mountains, under the direct control of the Magistros. By 1750, Voltarra has broken free and is an independent province, and the vibe in Chardon has shifted. The chalyte factories that were once since as the birthright of the Empire are now treated more cautiously, as a powerful but dangerous tool.

[2026-08-18 09:58 AM] Deciusmus: I mean, ignore the exact specific text, I didn't try very hard to get the details right

[2026-08-18 09:59 AM] Deciusmus: But to me, that is a more useful paragraph than something like:

    `%%`^POV:1745`%%`
    ...
    `%%`
    `%%`^POV:1752`%%`
    ....
    `%%`^END`%%`

[2026-08-18 09:59 AM] Deciusmus: it does change the character of the intro though and almost enforce some narrative history, which isn't always desireable

[2026-08-18 10:06 AM] rsulfuratus: hmm. have to think a bit

[2026-08-18 10:13 AM] rsulfuratus: ultimately i'm not sure the date blocks and campaign blocks are working the way i want, and especially for campaign blocks it is a little silly because it is really about *players* not *campaigns* - e.g. the Cleenseau group, our group, or none. i don't have a separate taelgarverse for, e.g. Great Library or Addermarch and am never planning on it. i think Schwartz and Eric and maybe some of your players are the only people who read taelgarverse (though one of Isaac's friends also said he read a lot of stuff)

[2026-08-18 10:14 AM] rsulfuratus: it is tempting to move the campaign/block parsing to the display not the exporter, so that you could have a site-wide or per-page toggle to show "campaign X" text

[2026-08-18 10:16 AM] rsulfuratus: I have no idea how Codex build the zoomable session note toggle but it seems to work well so in principle wouldn't be too hard

[2026-08-18 01:31 PM] Deciusmus: I've been busy at work, but kinda not sure the value of having "Taelgarverse" really do that much hiding of info.

[2026-08-18 01:31 PM] Deciusmus: I think as the set of campaigns gets more complicated (i.e. Campaign 3, Great Library, plus historical Dunmar, plus Cleenseau, etc) it is a lot harder to try to narrowly tailor `*`what information each Taelgarverse sees*

[2026-08-18 01:33 PM] Deciusmus: realistically, a lot of the players are mostly the same and very little is spoiled by having someone in my game know that in 1748 Chardon has a chaylte revolution or even who Apolloyon is.

    There are a very small number of exceptions, mostly around Cloudspinner and the feywild, but even then, I'm not sure how much it really would matter for info to leak.

[2026-08-18 01:34 PM] Deciusmus: To me, it is a lot more important to think about

    (a) the distinction between player-facing info, me/you info, and you-only info (which I think is well captured with campaign none/your secret tagging, body text)

    (b) how to structure the actual obsidian data so it is clear what is relevant WHEN

[2026-08-18 01:42 PM] Deciusmus: That is, what is more important to me is (in approximate order)

    1. Being able to clearly understand from reading the note what parts of the note are most likely relevant in 1720s. This is fine if it requires me to read all of the note. (This is about avoiding inaccuracies, i.e. I dont want to introduce a plotline about the Dyer's Guild if you were thinking they are new on the scene in the 1730s)

    2. Being able to invent stuff for the 1720s without being forced to invent 1750s variant

    3. Being able to reuse your stuff. This is about trying to preserve older invention and make it easy to flag stuff that is definitely valid in 1720

%% Off-topic messages omitted. %%

[2026-08-18 04:06 PM] rsulfuratus: so, i think i've been thinking along two lines.

    (1) is a usability point for taelgarverse. it isn't that it is useful to hide information in taelgarverse necessarily, but it might be very helpful to be able to see a tailored version that is for the campaign of interest. the best way to do this would be to dynamically hide pages based on a set of standard date/campaign combos. this is really more of a fun exploring what Codex can do project than anything else, but the idea would be some kind of checkbox to see the world from the point of view of a specific campaign. in particular this might be nice for Campaign 3 to declutter people a bit. this is also potentially useful for Great Library stuff which I'm restarting in a few weeks with Isaac's friends. but I think this is a side point. there is a proposal in `_MoC/Proposals` for how this might be implemented but i'm not actively working on it.

    (2) separately, for the Great Library work, i've been trying to think of a broader/better way to track a POV date for a note, which I think gets at your second point. there are some specific complications in that particular campaign, but right now i've been overloading the gameupdate tag which is not quite right I don't think .

    i'm not sure this gets at the general point though. i think really what you want in some ideal world is a date range that basically says "this note invents detail from X to Y"

    it is totally plausible to invent something for a game without making any decision about its history, which means its existence prior to X is undetermined and could go either way.

[2026-08-18 04:11 PM] rsulfuratus: i wonder how hard this would be to agentically classify for all current notes

[2026-08-18 05:24 PM] Deciusmus: I think there are really two aspects to this...

    (a) a churn aspect. This is something like... if a note `*`was written* from the perspective of 1730 or 1720 or 1745, and it is being *updated* for 1755, it makes sense to add rather than remove content.

    Darba is a good motivating example here. The current Darba note reflects a particular vibe that is not accurate in 1752 or whatever.

    This is minor until we are both realistically trying to produce notes in similar places for different games. Biggest impacts likely to be in Tollen/Western Gulf, unless Campaign 3 drifts into Tyrwingha/Enst.

    Having Addermarch set close to Cleenseau in time massively reduces this issue for the most common overlaps, but i.e. could come up if I start updating some of the Enst river place notes for post-time-skip Cleenseau (so 1725ish).

    (b) an accuracy aspect. A simple tag that indicates "accuracy dates" for a note and an update in the dynamic info block to show something like: "This note does not cover the current period" (based on the current loaded fantasy calendar) would be beneficial in a lot of ways I think.

[2026-08-18 05:25 PM] Deciusmus: There is a simple version of (b) which is that the note is accurate for all POVs before the POV date, but I think that is actually kinda misleading. Most notes are often accurate for an odd discontinuous period that includes the far past as well as the recent dates around the POV, but not the "recent past"

[2026-08-18 05:29 PM] Deciusmus: but I am actually not sure how much any of this is anything other than some authoring conventions

[2026-08-18 05:37 PM] rsulfuratus: right i don't necessarily want to build another half-used system to classify notes.

    we already have dm notes / dm owner that is a bit stale; status tags that are okay but not perfect and are stale in places; inconsistently used campaign and date blocks, plus a few scattered excludePublish notes; and a range of half-finished reformating projects

[2026-08-18 05:38 PM] rsulfuratus: plus my start on the POV comment which, again, is pretty half-formed

[2026-08-18 05:45 PM] rsulfuratus: About to bike home but I guess overall what I keep circling around is some way to report what a meta information a perfectly complete note should have. Putting aside implementation details for now

[2026-08-18 05:47 PM] rsulfuratus: Then my idea would be to build some kind of classifier that says what meta information a note is missing. My new session pipeline makes it really easy to identify notes that need to be created or updated from a session but there are ~2000 notes in taelgarverse that predate this

[2026-08-18 06:05 PM] rsulfuratus: Basically I want something like a linter that checks a note both deterministically and with a judgement agent and reports what’s missing, some editorial quality and writes a time stamped metadata so that one check can be “do more recent sessions / dm notes link to this”

[2026-08-18 08:16 PM] rsulfuratus: do you have an opinion where agent skills relevant to taelgar live? currently this is all in taelgar-utils but i wonder if a _skills directory in taelgar is better

[2026-08-18 08:42 PM] Deciusmus: I don't

[2026-08-18 08:42 PM] Deciusmus: _skills might be more accessible
