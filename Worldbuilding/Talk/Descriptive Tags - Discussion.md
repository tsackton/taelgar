## Proposed Tag Rework Dec 2025
(Tim)

As part of typeOf cleanup and generally working through some organizational stuff, there are some potential issues with our current descriptive tag setup that might be worth exploring. 

### Living Beings

Right now, we have: person, species, and deity that capture specific individuals, pages about types of creatures, and pages about specific deities, respectively. Person is obviously fine as a category, but is currently used for things that blur the line with deity (e.g, Ethlenn or Cha'mutte; see [[Divinities and Powers - Discussion]]). 

A potential reorganization might be:

- **person**: a page about specific individual
- **creature**: a page about a type of creature, which could be a species (e.g. humans or elves), a broad creature type (e.g. undead or lycanthropes), or a specific kind of creature (e.g. duskhounds or axebeaks)
- **power**: a page about a power or divinity per [[Divinities and Powers - Discussion]]. 

The typeOf (species) of a person doesn't have a strict controlled vocabulary but should generally be something with a creature tag. 

Creatures could gain typeOf vocabulary if desired (e.g. following [[Metaphysics of Creatures]]); it could be useful to have an explicit species typeOf, but it is less obvious if a "transformation" or "creature of the inner plane" typeOf is useful. 

Powers have a natural typeOf here: embodied god, incorporeal god, small god, archfey, elder wyrm, possibly a few others (demigod? whatever gazankoa is?). Alternatively could use typeOf for pantheon but I think affiliations is a more natural fit there, most likely; see below on secondary tags. 

Transition:
- person would remain
- species is optionally renamed creature, but generally keeps the same notes
- deity is renamed power, and some notes from person are moved to power

### Places

Right now, we have place for a specific geographic place, and there does not seem to be a need to revise this. So we keep:

* **place**: a specific geographical place

Place typeOf has extensive discussion elsewhere. 

Transition: not needed, place remains place. 

### Things

Right now, we have item, a single tag for all material objects of any kind, including things as diverse as vehicles, classes of magic items, named books, specific artifacts, and general materials. Functionally, this works pretty well, and probably doesn't need to be revised. The biggest general issue with things is more about campaign vs general. Optionally, we could rename this to object to be a little more generic. 

* **object**: a specific unique material object (e.g., the Crown of Purity, the Wave Dancer, Vindristjarna), a class of objects (e.g., Drankorian Message Stones, books), or a kind of material (chalyte, mithril). 

Object typeOf is slightly complicated and likely requires a bit of thought to make useful; this is a place where things like subtypeOf and something like "descriptor" might be useful; we currently have the rarity frontmatter item which is inconsistently used but is included in header generation when available. 

Items are also one place where subtags have been widely, if inconsistently, used. These have potential value, but as they are not consistently applied, their value is limited. Subtags should either be required for items (e.g., vehicle, book, artifact, equipment, material), or be removed. The main advantage of tags over things like typeOf is the tags sidebar menu which makes click-to-search easy, but I'm not sure that is really an advantage (e.g., `["typeOf":vehicle]` works fine in search too). And subtags are much more annoying for dataview and base queries. 

Transition: rename item to object, if desired, but no retagging is needed, excepting subtag cleanup (to add or remove). 

### Groups




* **organization**: a specific group of people or other type of organization, including things like pantheons or families or clans.
* **culture**: a page describing a specific culture

### Events

Currently, we have three time-related tags: event, for specific events of a particular duration; holiday, for well holidays but potentially could be used for recurring events generally; and timeline, which is inconsistently used for chronologies. 

I think the easiest approach is to move timeline to meta or background, holiday to background, and focus just on events. So we would have just:

* **event**: a page about a specific event

Transition plan would be to move timeline to meta or background, depending on whether there is significant text on the page, and to move holiday to background. 

### Conceptual and Meta

Various pages that are either conceptual, or meta, are captured by the "background" and "meta" tags. These work fine, though see the discussion above in Groups. Keep:

* **background**: a conceptual page that describes world background. This is still canonical information (or at least, potentially canonical, depending on the status tags) but it doesn't refer to an individually identifiable in-game thing (i.e. Land Owning in Sembara or Climate Background). A good catch-all for otherwise unclear pages.
* **meta**: a page about pages, for example this page. Does not contain world information, but may contain information about world information. Can also be used for map of content-style pages that are outside the \_MoC folder, for example indexes of NPCs or indexes of events, and for rules-focused pages (Playing a X; Creature Types; etc). 

More discussion is in Events and Groups, above. These pages don't clearly need typeOf categories at the moment. 

Transition plane: none needed.

### Source Material 

Right now, we have two general descriptive tags for source material: session-note, for session notes, and source, for primary sources. These are find and shouldn't change, although session-note is a little weird because we don't enforce tags in Campaigns where these are most useful. So we keep:

* **session-note**: a page about a specific session
* **source**: a page containing the actual text or a paraphrase of actual in-world information, typically intended to be given to players as is. 

There are, however, some revisions that may be useful around these categories. In particular, auto-generating session note headers would be useful; this is currently done either via AI or as part of the session note pipeline, but it is a pain when changing titles or taglines, or other little cleanup like that. This would also open up the possibility of using campaign as a typeOf synonym for session-note, to autogenerate a "Session X of the typeOf" kind of line (with "Session" being changeable in displayDefaults for situations where Episode is preferred, for example). 

Additionally, it may be worthwhile to remove the "notes in campaign don't need tags" rule. 

Transition plan: none involving tag categories directly. 

### Secondary Tags

We have inconsistently used four "secondary" tags: pc, religion, historical, and testcase. These have, I think, generally not turned out to be useful. I think a large issue is that the vault grows by repeated passes of note creation, tagging/cleanup, rewrite, tagging/cleanup, etc. If there is no automated way to generate a list of notes that should be tagged with a secondary tag, but aren't, then many notes slip through the cracks; if there is an automated way, it isn't obvious what use the secondary tag has. 

Religion and historical are potentially very useful, but are not routinely used, which in some ways makes them worse than useless. That is, in principle religion/mosnumena should pull up all pages related to Mos Numena, but it doesn't currently, and it is really hard to find the missing pages since we have no other signal to say "this page is about religion". Same with historical - it is not used sufficiently cleanly enough to reliably filter things.

PC is more or less reliably tagged, but it isn't obvious what the use case is. 

testcase feels more like a status tag than anything else. 

I would propose:
- move testcase to status/testcase, or leave as is, depending on whether having some notes with permanent status tags is more or less annoying than having a random top-level meta tag. 
- delete PC; `["dm_owner":player] tag:#person  ` should already pull up all PCs. If we decide we need frontmatter to associate pages with specific campaigns, this should be applied more broadly, not just to PCs (e.g. via a campaign: frontmatter entry).
- delete historical and religion as secondary tags; to the extent these are useful for search, etc (religion definitely is; historical I'm less certain), find a way to this with other frontmatter. 

Note though that religion is by far the most useful of the secondary tags IMO, and there is the strongest argument for keeping it despite the problems. 