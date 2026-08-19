---
headerVersion: 2023.11.25
lintedAt: "2026-08-19T16:23:04-04:00"
lintVersion: "2.3"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Istaros
aliases: [Aistanë, Drogar, Mahar]
whereabouts: Istaros Watershed
dm_owner: joint
dm_notes: important
POV: post-Great-War
---
# Istaros
>[!info]+ Information
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Istaros is a major river that flows several thousand miles from its source in the [[Mostreve Hills]] to the [[Sea of Storms]]. The [[Istaros Watershed]] has been central to many rich realms, including the [[Drankorian Empire]] and later the [[Istabor Alliance]], but since the [[Great War]] it has been largely cursed and deserted, as nearly the entire river system flows through the [[Desolation of Cha'mutte]]. 
## Upper Istaros

The source of the Istaros is [[Lake Aeulian]], which in turn is fed by the [[Andonne]] and the [[Valmont]], which flow from the Sentinels and the Mostreve Hills, respectively. Here, the Istaros once flowed through riparian forests and scenic river valleys dotted with productive agricultural villages and minor tributaries. Now, this land is cursed, and few dare venture through the now-haunted, ash-choked landscape. 

Near [[Isingue]], the Istaros is joined by the [[Thalurien|Thalúrien]], a major tributary from the east. The waters at this confluence were long known to be magically blessed, giving exceptional fertility to the soils of this land, which was the culturally and mystical center of the [[Istabor Alliance]]. Now, the city of Isingue is ruined, consumed by the [[Cha'mutte's Plague]], and the fate of the life-giving magic of the land is unknown. 

The upper Istaros ends a hundred miles or so south of Isingue, at the confluence with the [[Kezhur]], where the river enters a rocky, broken landscape, where the land was shattered by Cha'mutte's magic.

## Middle Istaros

The Middle Istaros, known as the Drogar to the orcs of Xurkhaz, starts just south of the confluence with the [[Kezhur]], among the rocky hills of the southern Plaguelands. The river flows through a series of gorges cut into the uplifted land, with several dramatic waterfalls created during the cataclysm after the Great War. 

Here, the Istaros forms the eastern border of the [[Xurkhaz]], as it enters a rocky desert for a hundred miles before spilling onto the flat arid landscape of the eastern Garamjala. Here, the river makes a wide bend around the Garamjala Plateau, before turning southwest and joining the [[Yandare]]. This is the section of the Istaros known as the Mahar to the Dunmari. 
## Lower Istaros

Once, the Istaros joined the Hara, forming a broad river that flowed past the famous city of Drankor, the center of the Drankorian Empire. Now, none know what remains of the lower Istaros, or if the Hara even still reaches the Istaros. 
## Names

The Istaros has many names. To the original Drankorians, the refugees from [[Hkar]] after [[the Downfall]], it was known by its elvish name, Aistanë (EYE-stah-neh), meaning 'blessed water'. To the [[Orcs]] of [[Xurkhaz]], it is known as the Drogar. To the Dunmari, it is known as the Mahar. The name Istaros is likely a corruption of the Elvish, in the years after the [[First Plague]] and the fall of Drankor.

%%^Metadata:names:v1%%
- {name: Istaros, role: primary, language: unknown, pronunciation: ISS-tah-rohs, derivedFrom: Aistanë, status: proposed, notes: likely corruption of the Elvish form; source language and exact sound change are unresolved}
- {name: Aistanë, role: historical, language: Elvish, pronunciation: EYE-stah-neh, meaning: blessed water, status: documented}
- {name: Drogar, role: regional, language: Orcish, status: documented}
- {name: Mahar, role: regional, language: Dunmari, status: documented}
%%^End%%

%%^Metadata:map:v1%%
locations:
- {role: source, feature: , map: world, locator: }
- {role: outlet, feature: , map: world, locator: }
%%^End%%

%%^Metadata:article:v1%%
mode: geographic reference
povNotes: "Accuracy range: post-Great-War. The article contrasts the present cursed watershed with earlier river landscapes and deliberately leaves the lower Istaros and the fate of Isingue's life-giving water uncertain."
%%^End%%

%%^Lint%%
## Taelgar note lint

### Open findings

- [ ] **warning — `name.pronunciation_missing`:** `ISS-tah-rohs` is a low-confidence spelling-based proposal. The note says Istaros is probably a corruption of Aistanë, but the sound change and present form’s source language are unresolved. If accepted, copy:
  ```yaml
  pronunciation: ISS-tah-rohs
  ```
  and update the primary name entry’s status.
- [ ] **warning — `metadata.map_location_missing`:** A major waterway requires map metadata. Replace the explicit `status: missing` block with supported route, source, mouth, and confluence data when available; do not invent coordinates.
- [ ] **suggestion — `coverage.newer_heartroot_evidence`:** Later DuFr source material identifies the ancient fertility around Isingue more specifically with the Heartroot and its wounding. Decide whether that belongs here or only in linked campaign material. Copy-ready campaign-scoped candidate: `%%^Campaign:dufr%% The [[Dunmar Fellowship]] learned that the ancient fertility along the upper Istaros was bound to the [[Heartroot]], a vast symbiotic magic wounded during the [[Great War]]; an untainted fragment survived on the [[Aurbez Plateau]]. %%^End%%`

### Applied changes

- Added `POV: post-Great-War`, current article metadata, an explicit missing-map block, and v1 name metadata preserving the documented regional names and unresolved primary form.

### Validated

- Local hidden material supports `dm_notes: important`. The article honestly leaves the lower river and the fate of Isingue’s life-giving water uncertain.
%%^End%%
