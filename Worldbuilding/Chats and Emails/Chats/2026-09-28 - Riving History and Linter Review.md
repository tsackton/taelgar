# 2026-09-28 - Riving History and Linter Review

[2026-09-28 09:28 AM] rsulfuratus: so in the climate work i've been doing, i've found it easier to develop a separate climate model, and then ask codex to identify notes that need review/have conflicts, and then manually update them. i found it useful to have one place to review overall details instead of trying to track a bunch of scattered notes.

    but that workflow is not necessarily the most optimal or best for every task.

    for history it does help to centralize open questions because this probably involves more invention and decision-making than the climate stuff (which is mostly about having a model for future work - my ultimate goal is to make a generate-taelgar-weather skill that gives you the weekly forecast for any place and time, and tracks weather in a history log so that upcoming weather is sensible with past weather)

[2026-09-28 09:29 AM] rsulfuratus: i have about 20 minutes so i'm taking a quick look at the mythic history of taelgar in your branch - not sure the best way to address open questions? just put in the doc?

[2026-09-28 09:52 AM] rsulfuratus: one thing that doesn't quite come through that i'm not sure where to put is a sense that the Riving is like a second phase of the pre-time mythic history, not precisely a single event or transition.

    the exact metaphysical details are a little unclear but in my mind it was always somehow both extended and instantaneous, but more in a sense of operating in a separate time stream than the pre-Riving sense of cause and effect don't make sense

    that is, you could order events in the Riving in sequence, but it wouldn't make sense to speak of the passing of years, particularly. so it is kind of a transition point.

    but there is an idea of cause/effect, before/after. the firstborn are created first, and then they walk around and reshape the world and then they create the species originating from them. so a sequence of events but with no precise way to state how much time each took

[2026-09-28 09:53 AM] rsulfuratus: i would also clearly place Aerin and the kenku here, not in the primordial chaos

[2026-09-28 02:44 PM] Deciusmus: been swamped.  for open questions, yeah just add to doc or put here

[2026-09-28 02:49 PM] Deciusmus: my thinking is something like...

    (a) for Mythic History at least, the initial collection into a document is useful, but it feels like the wrong long-term home as the interrelationships between Cosmology and Species origins etc are blurry, so I'd rather have something like a bunch of more-fleshed out pages with more details on the subbits and then a very light "Mythic History Overview" that provides some meta-commentary and is very link dense

    (b) I think actual history might work better that way long term -- i.e. have codex build the summary page from notes -- but to get there probably requires some roundabout initial creation of summary pages with dense open questions to then answer + throw  away (or move to Talk or whatever)

[2026-09-28 07:48 PM] Deciusmus: why does linting require ruby?

[2026-09-28 07:48 PM] rsulfuratus: i don't know, that's a good question

[2026-09-28 07:48 PM] Deciusmus: iwas trying to run lint on my new and improved riving note and I got...

    The initial validation is blocked only because Ruby is not on this shell’s command path. I’m locating the vault’s available Ruby runtime now; this does not affect the note or broaden the lint scope.

[2026-09-28 07:48 PM] Deciusmus: I don't know if I have ruby installed..

[2026-09-28 07:49 PM] rsulfuratus: i think maybe codex decided to write some of the skill scripts in ruby for some reason

[2026-09-28 07:49 PM] Deciusmus: although codex seems to have gotten past that so i  guess i do..

[2026-09-28 07:49 PM] Deciusmus: no, it is trying to install ruby itself... haha

[2026-09-28 07:50 PM] rsulfuratus: yeah the generate taelgar lint values is in ruby for some reason

[2026-09-28 07:50 PM] rsulfuratus: must have been feeling like ruby that day

[2026-09-28 07:50 PM] rsulfuratus: i doubt there is a good reason to do it in ruby instead of python

[2026-09-28 07:52 PM] rsulfuratus: it should be trivial to install, don't think there is much reason to rewrite in something else honestly

[2026-09-28 07:54 PM] rsulfuratus: ah. i didn't have a yaml parser in my system python but ruby has it native. the linting stuff does a lot of yaml parsing so i guess it decided to just go straight to ruby instead of installing a pyyaml

[2026-09-28 08:34 PM] Deciusmus: it worked fine

[2026-09-28 08:34 PM] Deciusmus: the linter doesn't like invented canon very much though

[2026-09-28 08:36 PM] rsulfuratus: what do you mean?

[2026-09-28 08:37 PM] Deciusmus: i'lll push in a sec so you can see. I invented some specifies in the RIving -- which we might not keep, I don't know what you will think -- and the linter complained pretty heavily that this was unsupported by vault sources.

[2026-09-28 08:38 PM] Deciusmus: pushed

[2026-09-28 08:38 PM] Deciusmus: curious what you think esp of the riving invention around scholarly debate and how that fits into cosmology

[2026-09-28 08:44 PM] rsulfuratus: the linter really doesn't like vault inconsistencies, which is intentional and i think worth keeping

[2026-09-28 08:47 PM] Deciusmus: yeah agreed

[2026-09-28 08:47 PM] Deciusmus: definitely not a complaint about the linter

[2026-09-28 08:47 PM] Deciusmus: just a comment

[2026-09-28 08:47 PM] Deciusmus: its good to flag it

[2026-09-28 09:06 PM] rsulfuratus: trying to finish session notes from games this weekend so didn't have energy for a deep read but on quick glance i think i like the general riving vibes. the think i'd want to think about is how much it should really be a source of study, as opposed to speculation and philosophy in-world. the vibe is a little more "arcane geographer" than "metaphysical theology" if that makes sense

[2026-09-28 09:06 PM] rsulfuratus: but i haven't yet read all the supporting notes carefully; this is mostly just first impressions

[2026-09-28 09:09 PM] rsulfuratus: i guess mostly this could be summarized as the riving seems like a place where everyone has their own opinion instead of a place where the standard multiverse model is a dominant force and there are some counter-thoughts.

    i would tentatively keep Gaius Devarro's opinions, but maybe tune down the idea that is the standard multiversal model. there is some text that points in this direction e.g. not really a subject of study but then the note drifts a bit into maybe a touch more codification than the riving should have

[2026-09-28 09:10 PM] rsulfuratus: it might for example be a useful place to invent some dunmari or skaer or zimkovan or other perspectives that are not commonly captured by the "university cosmology" instead of just relying on elves and lizardfolk

[2026-09-28 09:19 PM] Deciusmus: I'm going to pull the Riving page and some of the related other pages, but not the main "Mythic History" page, into a new commit on main, with status/check/tim set on all of them.

    My plan is to take a step back from mythic history and use the gathered source material to create proper pages for the RIving (as above) and also the Primoridal Cosmos (which probably draws more heavily on fey and giant legends than human scholarship?)

    Having done that, I plan to review the various "historical framework" and "background of history" docs to try to move or eliminate via reference to the Riving and Primordial Cosmos various duplicative or redudnant info

[2026-09-28 09:19 PM] rsulfuratus: sounds good
