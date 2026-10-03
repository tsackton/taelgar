---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T13:42:28-04:00"
lintVersion: "3.5"
tags: [person, status/gameupdate/gl, status/check/lint]
species: human
ancestry: "Deno'qai"
gender: female
campaignInfo:
  - {campaign: grli, type: defeated, date: 1748-10-14}
name: Yeshara
pronunciation: yeh-SHAH-rah
affiliations:
  - {type: primary, org: "Yo'nari"}
whereabouts:
  - {type: home, location: Cairn Dor}
knownTo: [grli]
dm_owner: none
dm_notes: none
POV: 1748
---
# Yeshara
*(yeh-SHAH-rah)*
>[!info]+ Biographical Info  
> A [[Deno'qai]] [[Humans|human]] (she/her), of the [[Yo'nari]]  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:grli%% Defeated by the [[Silver Tempests]] on October 14th, 1748 in [[Cairn Dor]], [[Shadowfolds]], the [[Echo Realms]] %%^End%%

Yeshara, called the Wolf-Queen and the Queen of Eternal Waking, is an ancient [[Yo'nari]] queen and the ruler of [[Cairn Dor]]. Her attempt to free her people from sleep created the shadowed domain of [[Cairn Dor]]; her repeated efforts to extend that "freedom" to other peoples resulted in a cycle of wars across [[Apporia]] lasting thousands of years.

## Origins

Though many details of her origins are shrouded in mystery, a few details are clear. Yeshara ruled the [[Yo'nari]], a tribe of early [[Northerners]] and ancestors of the modern day [[Deno'qai]], who lived in the interior mountains of Apporia before the [[Downfall Wars]]. The Yo'nari had frequent dealings with the fey and other strange inhabitants of the [[Apporia|Apporian Peninsula]], and Yeshara came to believe that dreams made mortals vulnerable. Her fear became an obsession after her brother [[Ilanar]] disappeared following a fey bargain and was later found trapped in a dreamlike torpor.

Yeshara outlawed lullabies and rites associated with sleep, imposed prolonged vigils, and punished what she called dream-taint. Her campaign culminated in a midwinter rite at the [[Cleaver-Stone]], intended to sever the Yo'nari from the [[Plane of Souls|Plane of Consciousness]] and end their need to sleep. Instead, the rite created Cairn Dor, transported Yeshara and her followers into it, and transformed the Cleaver-Stone into a portal between the new realm and the [[Material Plane]].

## Rule of Cairn Dor

Now, Yeshara rules over the domain of Cairn Dor, where she enforces her vigil against sleep. Her guardians, the [[Shemra Azem]], are magically connected to dreamers, kidnapped mortals from the [[Material Plane]]; through this connection, they never sleep, and can survive seemingly fatal wounds. 

Her subjects, the remnants of the [[Yo'nari]], now called the Nurim-Dor, live in fear of sleep. 

Yeshara cannot be killed while Cairn Dor exists, but she can be subdued. If her magic fails, she falls into a slumber that lasts for tens or hundreds of years and puts her domain into stasis while it lasts. 

%%^Campaign:none%%

## DM notes

- The folk stories gathered in [[Castrella]] describe Yeshara as afraid of the dark, while the more detailed background centers her fear on sleep and dreams. The account above treats “fear of the dark” as the later folktale form of the older doctrine.
- [[GL - Session 62 - DM Notes]] has significant background, but some details are out of date and were subsequently superseded.
- Yeshara's human species and Yo'nari ancestry describe her origin. Her nature after the creation of Cairn Dor is more like a "Domains of Dread" Darklord. Surviving traditions variously misidentify her as a folk witch, trickster fey, or other supernatural figure.
- Sources: [[Great Library Session Notes - Arc 5]], [[GL - Session 62 - DM Notes]], [[Session 63 Background]], [[Letter from Chardon for Samso on the Umbral Covenant]], [[Apporian Shadow War]], [[War of the Severed Dreams]], and [[War of the Dark Rift]].

%%^End%%

%%^Metadata:names:v1%%
- {"name": "Yeshara", "language": "unknown", "pronunciation": "yeh-SHAH-rah", "status": "documented"}
- {"name": "Wolf-Queen", "role": "title", "language": "Common", "status": "documented"}
- {"name": "Queen of Eternal Waking", "role": "title", "language": "Common", "status": "documented"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: an active-rule portrait before the October DR 1748 defeat, with ancient origins and recurring wars as backstory; the later slumber and the DR 1752 state are not incorporated into the visible account.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and the legacy Great Library campaign code, added knownTo: [grli], and recorded documented names and the pre-defeat temporal frame.
- Corrected “superceded” to “superseded” in the existing source note.

### Validated judgments
- The Campaign:none block preserves source provenance and interpretive/DM guidance; it is retained.
- The status/gameupdate/gl tag is not assessable until the human chooses whether to update the account or preserve the earlier active-rule portrait; the tag is unchanged.
- No local-only _DM_ matches were found; dm_notes: none is consistent with that evidence boundary.

### Editorial assessment
**Underdeveloped** — The account explains her origins and active rule but omits the defining defeat, resulting slumber, and her still-sleeping state when Cairn Dor emerged from stasis in DR 1752. A short dated outcome paragraph and a decision about the active-rule frame would close the central gap.

### Open findings

- [ ] **Warning — coverage.later_material_change:** [[Great Library Session Notes - Arc 5]] and [[Cairn Dor]] establish that the Silver Tempests defeated Yeshara on October 14, DR 1748, putting her and the domain to sleep; she remained asleep when the adventurers and captives woke on June 28, DR 1752. The current “Now, Yeshara rules” account omits that durable change. Choose an updated article/POV, defer with the existing game-update tag, or intentionally preserve the pre-defeat account and disposition that tag. A bounded proposed addition is:

  ```markdown
  %%^Date:1748-10-14%%
  On October 14, DR 1748, the [[Silver Tempests]] defeated Yeshara after awakening the captive dreamers. Her fall sent her and the people of [[Cairn Dor]] into sleep and put the domain into stasis.
  %%^End%%

  %%^Date:1752-06-28%%
  When Cairn Dor emerged from stasis in June DR 1752, Yeshara and the Nurim-Dor remained asleep; their later fate is unknown.
  %%^End%%
  ```

  If adopting these layers, frame the existing active-rule section as the pre-defeat state; no visibility block has been added automatically.

- [ ] **Warning — metadata.classification_review:** The person/human classification records her origin, but the visible article says she cannot be killed while her domain exists and gives her a singular supernatural origin. Under [[Note Categorization]], that warrants reviewing whether her current entity type is a power. Human choice: retain the person classification with a specific rationale, or use `tags: [power, status/gameupdate/gl]` and `typeOf: extraplanar power` (alongside any active lint status), preserving her human and Yo’nari origins in the Origins section. The exact supernatural category and person-only relationship fields need human disposition; no classification was changed.
%%^End%%
