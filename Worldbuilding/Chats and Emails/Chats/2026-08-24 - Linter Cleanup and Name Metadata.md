# 2026-08-24 - Linter Cleanup and Name Metadata

[2026-08-24 01:04 PM] rsulfuratus: don't know if you've paid any attention to the large number of recent commits in taelgar. i had the flu and was basically out of commission for four days, ended up watching movies and ordered codex around from my phone, mostly.

    i am very happy with the lint-taelgar-note skill and it pulls up tons of issues with existing notes. so far i've run it on ~300 notes, and about ~3/4 come back clean or with only pronunciation and/or map metadata to specify.

    the POV stuff is not ~100% accurate but it is good enough imo.

    i'm also trying to reduce secrets and info that is only in my dm notes.

    it is probably a bit ridiculous to actually do this for all notes but it is a fairly chill background task since the skill tells you exactly what needs to be fixed, and there are only a small number of notes that have serious issues that require thought to fix. so it has been nice to do for 10 minutes when i have energy.

    as part of this i'm also trying to reduce AI writing in the vault; currently there are a fraction of notes that are obviously nearly 100% written by AI. the lint skill has a prose quality flag and i've also been adding status/check/ai to notes that read as strong AI to me

[2026-08-24 02:47 PM] Deciusmus: i have not been paying a ton of attention

[2026-08-24 02:47 PM] Deciusmus: I've been working on a replacement for D&D Beyond 🙂

%% Off-topic messages omitted. %%

[2026-08-24 04:51 PM] Deciusmus: that's kinda fun to just clean stuff up...

    is the intention to delete the `%%` lint `%%` and `%%`metadata:name`%%` blocks once cleaned? I assume I leave the `%%`pov`%%` block

[2026-08-24 05:03 PM] rsulfuratus: just the lint

[2026-08-24 05:04 PM] rsulfuratus: my plan is to rewrite the name explorer to use the metadata name block, although this could maybe be moved to frontmatter instead of a block

[2026-08-24 05:04 PM] rsulfuratus: the taelgarverse exporter now strips all of them properly though

[2026-08-24 05:16 PM] rsulfuratus: i've been leaving name blocks liks this:

    ```
    `%%`^Metadata:names:v1`%%`
    - {name: Guluppa-Sog, role: primary, language: Bullywug, pronunciation: goo-LUP-pa sog, meaning: "the settlement by the southern still-water", status: documented}
    `%%`^End`%%`
    ```

[2026-08-24 05:17 PM] rsulfuratus: or if no meaning/notes:

    ```

    `%%`^Metadata:names:v1`%%`
    - {name: Asqara River, role: primary, language: Mawaran, pronunciation: AHS-kah-rah, status: documented }
    `%%`^End`%%`
    ```

[2026-08-24 05:17 PM] rsulfuratus: or if a pronunciation is not needed:

    ```
    `%%`^Metadata:names:v1`%%`
    - {name: Thomas Hawke, role: primary name, language: Tollish, status: documented}
    `%%`^End`%%`
    ```

[2026-08-24 05:18 PM] rsulfuratus: or for something complex:

    ```

    `%%`^Metadata:names:v1`%%`
    - {name: Istaros, role: primary, language: Common, pronunciation: ISS-tah-rohs, derivedFrom: Aistanë, status: documented, notes: Likely corruption of the Elvish form.}
    - {name: Aistanë, language: Elvish, pronunciation: EYE-stah-neh, meaning: blessed water, status: documented}
    - {name: Drogar, language: Orcish, pronunciation: droh-GAHR, status: documented}
    - {name: Mahar, language: Dunmari, pronunciation: mah-HAHR, status: documented}
    `%%`^End`%%`
    ```
