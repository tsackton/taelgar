# 2026-08-21 - Note Linter Metadata and Review

[2026-08-21 02:28 PM] rsulfuratus: i have been sick the past few days and mostly sleeping but in between i have been having codex make a lint-taelgar-note skill. i think it is basically done at this point.

    i just pushed a bunch of stuff so you can kind of see what it does. the skill is in the taelgar repo.

    invoke against a single note or a batch of notes.

    adds a name metadata block (which will eventually be wired to name explorer). see the new name stuff in MoC

    adds a POV frontmatter and a povNotes metadata block. see the POV stuff in MoC. the idea here is to specify whether a note is broadly "modern", or is written from a specific decade or year POV. povNotes gives context and temporal accuracy. you can look at notes for how this plays out (anything with version 3.4 is current)

    also does editorial, correctness, and sufficiency review. e.g. look at Edric or Juliana Westby for examples, which I'm leaving un-fixed.

    it will attempt to infer a pronunciation if one doesn't exist. it also requires map coordinates for rivers, roads, and settlements (for now - could expand this later but these are the easiest to represent)

[2026-08-21 02:30 PM] rsulfuratus: anything that is linted and has human-review findings gets a status/check/lint

    it does not add tags if all it does is add POV and name blocks. also corrects minor spelling issues automatically, and normalizes metadata to fix any lists in long form (except lists of dicts which are always long form)

[2026-08-21 02:32 PM] rsulfuratus: the idea behind the POV stuff is that any note with a POV of modern is basically fine in any campaign in the broadly modern era, e.g. late 1600s through 1750s. i didn't try to be more precise. if anyone wants to run a game in the historical past i think it is obvious that any note requires assessment
