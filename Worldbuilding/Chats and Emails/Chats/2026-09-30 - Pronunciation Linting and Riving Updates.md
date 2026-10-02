# 2026-09-30 - Pronunciation Linting and Riving Updates

[2026-09-30 11:39 AM] Deciusmus: is there a standard way of telling the linter that the name shouldn't have a pronounciation? i.e. it wants to add pronounciation to "the Garrison Gate (of Cleenseau)" which seems odd to me

[2026-09-30 11:46 AM] rsulfuratus: it complains about anything that has even one non-english word

[2026-09-30 11:46 AM] rsulfuratus: so in that case it wants a pronunciation for Cleenseau

[2026-09-30 11:47 AM] rsulfuratus: i do one of two things, randomly

[2026-09-30 11:47 AM] rsulfuratus: sometimes I just add the pronunciation for the non-standard-english part as a pronunciation key in yaml (e.g., just for Cleenseau)

[2026-09-30 11:47 AM] rsulfuratus: sometimes I just leave the name with no pronunciation

[2026-09-30 11:48 AM] rsulfuratus: the linter skill will not re-lint notes unless you explicitly tell it to, so if you resolve lint finding and delete the block there is nothing forcing you to fix everything

[2026-09-30 11:49 AM] rsulfuratus: i spent a while thinking about whether it was worth tracking things like resolved decisions to prevent them from reappearing but decided that in practice the vast bulk of the work the initial lint of unlinted notes so it wasn't worth my time

[2026-09-30 01:17 PM] rsulfuratus: edited riving and pushed. basically used your ideas but restructured the text a little and downweighted the idea of scholarly study of the Riving, and upweighted non-human descriptions

[2026-09-30 01:18 PM] rsulfuratus: i left the lint note until we have a chance to resolve the notes that would need updating based on this revised description

[2026-09-30 03:18 PM] Deciusmus: might be interesting to write a yendalist view of the riving

[2026-09-30 03:19 PM] Deciusmus: and does the riving belong in history? it feels like maybe it should be in Planar Concepts

[2026-09-30 06:21 PM] rsulfuratus: yeah I think probably planar concepts. i don't think it makes sense to start history until the time exists

[2026-09-30 08:22 PM] rsulfuratus: fwiw since i saw you were running a limbo thing soon i'm trying to get at least the automated recaps of the last dunmar sessions done. we'll see how good codex does. i'm actually pushing up towards my weekly limit for once...
