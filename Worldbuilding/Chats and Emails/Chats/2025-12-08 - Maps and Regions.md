# 2025-12-08 - Maps and Regions

[2025-12-08 09:37 AM] rsulfuratus: pretty busy day today but am poking around with a bit of data cleaning. two questions:
    
    (1) is it worth thinking about standardizing typeOf vocabulary, and using typeOfAlias and subtypeOf for display control? i have noticed you started to do this with waterway, but we aren't that consistent. the obvious ones would be: 
    - waterway (including river, brook, canal, etc); 
    - bay (including gulf and other related terms like cove or bight); 
    - lake (though currently we have no ponds or other enclosed freshwater bodies)
    - settlement (for town, village, city, etc)
    
    but it is hard to have a strictly controlled vocabulary as there are sometimes weird things (like the Prismwell). 
    
    waterway and settlement are both kind of half-done, fwiw
    
    (2) is it worth thinking about how / if to incorporate the hex grid information into frontmatter? doing it on the watershed page is nice for quickly adding it, but in some ways it would be more useful to identify locations directly in the page itself. 
    
    at least for waterways, you could image have source, source-hex, outlet, outlet-hex as frontmatter. it would also be useful to specify hex location for settlements, which presumably are never bigger than 1 hex (though could span hex boundaries i guess, though in that case i'd just list the hex that has more of the settlement).
[2025-12-08 10:19 AM] Deciusmus: my basic opinion:
    
    a "well defined" type of is useful mostly for cases where you want do to something like:
    
    Settlements in Barony of Cleenseau
    
    or 
    
    Rivers in the Teft Watershed
    
    that auto-populate
[2025-12-08 10:20 AM] Deciusmus: outside of those cases, I'm not 100% sure if there is a lot of value?
[2025-12-08 10:23 AM] Deciusmus: I guess it might be useful to distinguish between, i.e.
    
    magical place
    built place
    geographic place
    
    so one option would be something like
    
    typeof = magical place | building | settlement | waterway | geographic feature
    
    and everything else is a typeofAlias
[2025-12-08 10:24 AM] Deciusmus: another option would be 
    
    typeOf = waterway | settlement | `<anything else>`
[2025-12-08 10:24 AM] Deciusmus: but I can kinda see it could be nice to have a 
    
    Geographic Features of Blah blah
[2025-12-08 10:33 AM] rsulfuratus: right, this is largely useful for this kind of automation, though i think there is some tension between the desire to do things like get all settlements in place X, and the desire to e.g. get all cities across the world (though "city" isn't necessarily well defined
[2025-12-08 10:34 AM] rsulfuratus: i deal with controlled vocabularies at work a lot and there are some big pluses but also it can be hard to get them right
[2025-12-08 10:34 AM] Deciusmus: I do as well
[2025-12-08 10:35 AM] Deciusmus: but in this case, we have pretty easy ways to fix/update if we dislike the controlled vocab
[2025-12-08 10:35 AM] rsulfuratus: right, that's true
[2025-12-08 10:35 AM] rsulfuratus: i'm looking at existing controlled vocabularies for geographic terms now to see if useful
[2025-12-08 10:36 AM] rsulfuratus: i guess the othe question is if we want to deal with hierarchies
[2025-12-08 10:41 AM] rsulfuratus: here's getty thesaurus of geographic names system:
![[Worldbuilding/Chats and Emails/_assets/discord/image-92E62.png]]
[2025-12-08 10:41 AM] rsulfuratus: (too complicated but the basic idea might be useful)
[2025-12-08 11:06 AM] Deciusmus: So I don't think we should overthink it...
    
    I think there is a lot of value to some level of standardized vocab.
    
    To me the only question is whether we do
    
    1. waterway | settlement | `<uncontrolled>`
    2. waterway | settlement | (some other controlled words) | `<uncontrolled>`
    3. waterway | settlement | (some other controlled words)
[2025-12-08 01:33 PM] rsulfuratus: so poking around a little about how we have actually used things (with obsidian base views, which makes this really easy). 
    
    (1) subtypeOf is only very lightly used; the main use is subtypeOf = magic / magical for items, with a secondary use for abandoned/ruined/lost 
    
    (2) subtypeOf and typeOfAlias (and the related subspecies / speciesAlias) are inconsistently used, e.g. subtypeOf = market, typeOf = town vs typeOfAlias = market town; subspecies = archfey vs speciesAlias = archfey
    
    (3) typeOfAlias is often used really as a subtype, e.g. in settlement and waterway. indeed both typeOfAlias and speciesAlias are, as far as I can tell, nearly exclusively used for subtype, not for an actual alias. 
    
    (4) typeOf is used for every place, organization, item, and person (as species); it is occasionally used for events. it is rarely and not usefully used for culture. it is not used elsewhere. 
    
    (5) subtags are used inconsistently to sub for subtypeOf: inconsistently for items, more consistently for pc, religion. 
    
    i do think this inconsistency makes it harder to organize and find information, but there is a danger of just organizing for organization's sake (not that big a deal if someone wants to for fun, but annoying if it makes updating/adding notes harder or more tedious later)
    
    there is also the concern about any significant changes requiring updating the javascript code, and/or the displayDefaults, which may be more or less annoying depending on what it involves. 
    
    in any case - i might not actually have time to do anything today it has taken >`2 hours to just type this between meetings and emails. 
    
    but if i were to do something, i think the basic framework would involve:
    - controlled vocab for typeOf
    - consistent use of subtypeOf for more specific subtypes of the larger typeOf
    - potential implementation of some kind of "descriptor" field for haunted, ruined, etc, anything that is not hierarchical
[2025-12-08 02:18 PM] rsulfuratus: okay, i have ~20 minutes while i'm eating lunch. i'm not sure any of what follows is worth doing (and i have like 4+ other half-finished taelgar-related projects). but just kind of geeking out on organization.
    
    one could imagine restructuring descriptive tags, typeOf, and subtypeOf into a more controlled hierarchical system, where (nearly) every note should have at least tag (to define basic category) and typeOf, and usually subtypeOf as well. 
    
    typeOf would be fairly broad, and strictly controlled based on the descriptive tag. subtypeOf would be loosely controlled, so there suggested terms that have some consistent meaning, but which can be added to relatively freely. 
    
    so you get a basic hierarchy from descriptive tag >` typeOf >` subtypeOf. 
    
    on top of that you have two generic adjectival keys: ancestry and descriptor. these, crucially, are not part of the hierarchy, so can be applied anywhere. ancestry is used pretty consistently already and serves as the cultural marker of (person, place, thing, etc). descriptor could have some consistent terms, like ruined and magical, but would generally be uncontrolled. conceivably there are edge cases, like a ruined market town, where you might want two or more descriptors, but this can potentially just be handled with aliases or text (do you really need to tag a ruined town as a ruined market town?).
[2025-12-08 02:18 PM] rsulfuratus: this would require some code rewrites but probably nothing that codex/copilot couldn't handle in a few minutes
[2025-12-08 02:18 PM] rsulfuratus: might also require some displayDefault updates
[2025-12-08 02:18 PM] rsulfuratus: in any case not sure i actually plan to do this, just kind of idle thinking
[2025-12-08 02:19 PM] rsulfuratus: the complication is getting the units right
[2025-12-08 02:22 PM] Deciusmus: So the complexity here is actually that I think you sometimes want
    
    Subtype typeof
    
    And other times not
[2025-12-08 02:23 PM] rsulfuratus: for display you mean?
[2025-12-08 02:23 PM] Deciusmus: That is—-
    
    If you envision settlement as a type and city as a subtype you want to say just “a city in place” in the header
[2025-12-08 02:23 PM] Deciusmus: But for some other scenarios you might want both
[2025-12-08 02:24 PM] Deciusmus: Although maybe not?
[2025-12-08 02:24 PM] Deciusmus: Conceptually the alias stuff could all go away if the display was just
    
    Subtype ?? Typeof
[2025-12-08 02:24 PM] rsulfuratus: yeah that is likely what you'd want
[2025-12-08 02:26 PM] rsulfuratus: the display defaults would not be that hard imo to clean up. from an organizational point of view, i'm more thinking about where to draw the lines in the levels of hierarchy
[2025-12-08 02:27 PM] rsulfuratus: e.g., is a deity: 
    - descriptive tag: person, species: power, subspecies: embodied god, ancestry: elven
    - descriptive tag: power, typeOf: deity, subtypeOf: embodied god, ancestry: elven
[2025-12-08 02:27 PM] rsulfuratus: anyway i have another meeting now
[2025-12-08 02:33 PM] Deciusmus: I am eating lunch so a few thoughts,..
    
    1. the largest motivating feature for organizing in this way is dataview tables
    
    2. The tables id be most likely to want are things like
    — all the settlements in the Barony of Avril
    — all the rivers in the Semb watershed
    — all the inns in sembara
    — all the religious sites to the wanderer in taelgar
[2025-12-08 02:35 PM] Deciusmus: But also other things like:
    
    — all the magic items made of dragon hide 
    — all the books we’ve made up
    — the defined buildings and streets in a ward of Tollen
    — the bridges that cross the Semb
[2025-12-08 02:39 PM] Deciusmus: Separately from the search features there is the idea of building the 
    
    “A (something) in (somewhere)”
    
    Header line
[2025-12-08 02:42 PM] Deciusmus: I wonder what the actual use of subtype is, honestly.
[2025-12-08 02:44 PM] Deciusmus: I wonder about a spec like:
    
    - all pages should have a typeOf and that’s controlled vocab 
    - ancestry, material are special tags valid for (all, items) to describe the culture or material
    - any page that wants the display text to vary can use typeOfAlias
[2025-12-08 03:09 PM] Deciusmus: Looking some more at places only, it really seems to me like "subType" is solving a problem we don't have.
    
    I think that just typeOf and typeOfAlias would be sufficient for places.
    
    It needs a little bit of thought as to the right controlled vocabulary, but I'm not convinced having a subtype gets anything.
    
    TypeOf = search/filter options, well-defined, agreed set
    TypeOfAlias = what shows up in the "A (something) in (somewhere)" line
    
    The data has a lot of half-hearted attempts to categorize places via subtype (i.e. "ruined", "fortified",  "haunted", "abandoned", "underwater")  but not much else.
    
    I'm not sure the advantage of a descriptor over typeOfAlias...
    
    When I am authoring a page, it seems easier to just do:
    
    typeOfAlias: haunted underwater ruin
    typeOf: building
    
    then
    
    descriptor: haunted underwater
    subTypeOf: ruin
    typeOf: building
[2025-12-08 04:15 PM] Deciusmus: I have to focus on work for a bit, but I was playing around a little.
    
    Without deciding about subtype or whatever, what do you think of this as an initial set of controlled vocab for place typeOf:
    
    * settlement:  replaces city, town, market town, village, hamlet, camp
    * waterway: replaces river, brook, stream
    * subdivision: replaces ward, neighborhood, urban area, duchy, barony, province, march, shire, manor (in the sense of sembaran manorial estate)
    * building: replaces house, manor (in the sense of manor hall), hall
    * road: replaces street
    * inn: replaces tavern
[2025-12-08 04:15 PM] Deciusmus: Plus watershed, region, island, plane, holy site
[2025-12-08 04:34 PM] rsulfuratus: been busy. but coming out of meetings now. 
    
    my original reason to think about subtypes is actually having to do with the map and generally thinking about biomes and map features. 
    
    for example:
    i was thinking about how to handle roads and settlements. right now for the map, we just use a totally arbitrary set of icons and randomly drawn rivers. but it would be feasible to set up layer styles, to have city/town/village for example with different icons
[2025-12-08 04:34 PM] rsulfuratus: was also thinking about like your "roads of sembara"
[2025-12-08 04:35 PM] rsulfuratus: but it is a lot of mental effort to categorize these as part of the mapping effort
[2025-12-08 04:35 PM] Deciusmus: ah, I see, so it provides guidance to what icon to use in mapping?
[2025-12-08 04:35 PM] rsulfuratus: much easier to have something like a data view of "cities" and then pull up photoshop and drag all the "city" layers to the right layer group and then hit apply style and your are done
[2025-12-08 04:36 PM] rsulfuratus: works for labels too - to style text based on city/town/village
[2025-12-08 04:36 PM] Deciusmus: that's a good use case, but it requires some controlled definition of what it means to be a "city"
[2025-12-08 04:36 PM] Deciusmus: or a "town"
[2025-12-08 04:36 PM] rsulfuratus: well, i'm fine with a somewhat arbitrary line here i just don't want to decide if rinburg counts as a city or a town in your mind for example
[2025-12-08 04:37 PM] rsulfuratus: and it is more about separation of effort. if i'm fiddling with photoshop i don't want to worry about definitions
[2025-12-08 04:37 PM] rsulfuratus: but the idea would be that each settlement (for example) is its own named shape layer so it is trivial to drag them to different style groups
[2025-12-08 04:38 PM] rsulfuratus: (i mean this is a long term project but i have been very into learning how to actually use photoshop which is about 1000x more poweful than what i have done with it to date)
[2025-12-08 04:39 PM] rsulfuratus: but for mapping purposes, the only things that really matter are settlement, road, and river
[2025-12-08 04:39 PM] rsulfuratus: well the only things where subtype would affect graphics
[2025-12-08 04:39 PM] rsulfuratus: plus ruined/abandoned etc
[2025-12-08 04:40 PM] rsulfuratus: (but that could be a subtype, actually)
[2025-12-08 04:40 PM] rsulfuratus: (though might want Drankor and some podunk ruined village in the hills to look different....)
[2025-12-08 04:41 PM] rsulfuratus: although actually the potential is large. could do this with borders (which could just be shape layers, too); with fort/tower/keep kind of things; maybe with other things as well
[2025-12-08 04:42 PM] Deciusmus: but honestly is subttype really the right way to do this
[2025-12-08 04:42 PM] Deciusmus: ?
[2025-12-08 04:42 PM] rsulfuratus: i'm not sure
[2025-12-08 04:43 PM] rsulfuratus: this is why i started thinking about it but from the beginning was not sure if this was useful or just idle over-organizing
[2025-12-08 04:43 PM] rsulfuratus: (thought the current state of several different half-implemented systems does kind of bother me)
[2025-12-08 04:44 PM] Deciusmus: You could imagine, for settlements, having the basic idea that says the icon is determined by two axes:
    
    importance = "city" or "town" or "village"
    type = "transient" or "ruined" or "permanent"
    
    then you can have an 9 icons
[2025-12-08 04:44 PM] Deciusmus: or maybe slightly fewer, say using the same icon for all transient settlements, and only having 2 icons or ruins
[2025-12-08 04:45 PM] Deciusmus: but I'm not sure it is obvious how that maps to subtype
[2025-12-08 04:45 PM] rsulfuratus: yeah it might be easier to just define "icon", which would be one of ruined big, ruined small, transient, city, town, village
[2025-12-08 04:45 PM] rsulfuratus: at which point it is not obvious that it needs to be recorded in frontmatter
[2025-12-08 04:45 PM] Deciusmus: Although the idea of "importance" might be usefully cross-cutting
[2025-12-08 04:46 PM] Deciusmus: i.e. roads, rivers, settlements and perhaps other things all have the idea of "importance" which could be very useful from a mapping project
[2025-12-08 04:46 PM] Deciusmus: prominence might be a better word
[2025-12-08 04:46 PM] rsulfuratus: for rivers too you actually usually want different styles for important/main stem; important/tributaries; minor
[2025-12-08 04:47 PM] rsulfuratus: but that actually maps well to city/town/village
[2025-12-08 04:47 PM] rsulfuratus: but i'm not actually convinenced now this is useful to track in obsidian
[2025-12-08 04:47 PM] Deciusmus: Well... I was thinking that prominence is actually pretty useful for mimimally invented places
[2025-12-08 04:47 PM] rsulfuratus: yeah maybe
[2025-12-08 04:47 PM] Deciusmus: it is a good shorthand to encapsulate the perceived importance of a place
[2025-12-08 04:49 PM] Deciusmus: i.e. Gowerbourne is a settlement I made up for an NPC backstory. But I dropped it a few other times, and it has kinda evolved in my head into one of the more important market towns along the Wistel, similar to say Ainwick (but not as large or important as Wisford itself)
[2025-12-08 04:49 PM] Deciusmus: It is true that the first sentence in the obsidian page is "A large market town "
[2025-12-08 04:49 PM] Deciusmus: but I can see it being useful to have the concept of promienence in frontmatter
[2025-12-08 04:50 PM] Deciusmus: which I think, from a "don't want to think about it" perspective, is kinda useful.
    
    Is Rinburg = Wisford = Embry = Fellburn?
    
    or is it more like
    
    Rinburg = Fellburn = Gowerbourne
    Wisford = Embry
    
    that's the kind of categorization that could be useful in frontmatter
[2025-12-08 04:52 PM] Deciusmus: Road is very similar....  it is not always clear what the "most important" roads are just from the descriptive text
[2025-12-08 04:55 PM] rsulfuratus: maybe. i kind of feel like there is a bit more nuance than is easy to capture with frontmatter though. 
    
    to be honest, my main issue is that i have i already have:
    - two big creative cleanup projects (creature directory rewrite; history of X project)
    - three big gap-filling project (status tags; ai assisted filling in of stubs/staging; old secret/DM note/ dm_notes cleanup)
    - a big programming project (session note pipeline)
    - my mapping project
    
    it is sometimes nice to have a pure reorg project, which is what appeals about the typeOf stuff (I've also been working on dangling links and few other little cleanups like that). 
    
    but prominence feels too much like another half finished invention project for me right now
[2025-12-08 04:55 PM] Deciusmus: that's fair
[2025-12-08 04:56 PM] Deciusmus: But as far as typeOf cleanup, to me the key thing is deciding what the vocab for the main typeOf tag should be
[2025-12-08 04:57 PM] rsulfuratus: yeah. i think it is a little hard to decide without looking at things. and actually part of this could be rethinking descriptive tags - for example i think that deity either needs to be collapsed with person (with species = deity) or more likely replaced with "power" to fold in things like archfey, cha'mutte, etc.
[2025-12-08 04:57 PM] rsulfuratus: i guess though there is no reason we need to decide on a typeOf system in one go
[2025-12-08 04:57 PM] Deciusmus: Well, I spend a bit of time this afternoon looking at place typeOf
[2025-12-08 04:58 PM] Deciusmus: I don't think it makes sense to worry about everything at all once
[2025-12-08 04:59 PM] Deciusmus: What I did was:
    
    * convert all of (town|city|etc) to settlement (keeping old value as typeOfAlias)
    * convert all of (duchy|barony|province|ward|neighborhood) to subdivision (keeping old value as typeOfAlias)
    * convert all of (river|stream) to waterway ..
[2025-12-08 04:59 PM] Deciusmus: then made a new view in your typeof base that filters out:
    
    "subdivision", "settlement", "realm", "inn", "building", "waterway", "watershed", "road", "holy site", "island", "plane", "region
[2025-12-08 04:59 PM] Deciusmus: which leaves 161 pages that have a typeOf not in the list above
[2025-12-08 05:00 PM] Deciusmus: it is really easy to do because you can bulk edit in the base directly
[2025-12-08 05:00 PM] rsulfuratus: yeah the other reason i was thinking about all this is playing around with base, which seems very powerful
[2025-12-08 05:02 PM] Deciusmus: it's a bit hard to know what to do with the remaining ~150 items though, which are scattered, i.e. 
    
    abbey, battlefield, bridge, canal, canyon, cave, castle, desert, fen, forest, ...
[2025-12-08 05:02 PM] Deciusmus: forge, fort, gap, gate, ...
[2025-12-08 05:03 PM] Deciusmus: my thinking was to just push this and we can each look and propose further simplifications until we get to a good place, but wanted to make sure you were ok with the simplifications I laready did first
[2025-12-08 05:06 PM] rsulfuratus: so it is easy enough to go back and forth. there are maybe some details i'd change (for example, i like to track tavern and inn separately as i think the vibe is often very different, though in play that doesn't always come across)
[2025-12-08 05:07 PM] rsulfuratus: i think as long as the old value of typeOf is in typeOfAlias there is no reason not to just push
[2025-12-08 05:07 PM] Deciusmus: I also collapsed a few subType=haunted, typeOf = city to move the subType to the typeOfAlias
[2025-12-08 05:07 PM] rsulfuratus: yeah that's fine
[2025-12-08 05:08 PM] Deciusmus: the only annoying thing is that editing in the base changes:
    
    tags `[ab, cd]`
    
    to 
    tags
    - ab
    - cd
    
    which is totally the same but annoys me. BUt I'm ot going to fix that
[2025-12-08 05:11 PM] rsulfuratus: my general feeling is that we ultimately need:
    - waterway
    - settlement
    - realm
    - plane
    
    then:
    - building, possibly split into a few major types (buliding, holy site, inn)
    - road, possibly split into intercity and intracity
    - subdivision, possibly split into "urban area" and "subdivision" or something similar
    - geographic feature (possibly split between landmark and topological feature)
    - some kind of biome categories (forest, wetlands, grasslands, etc)
    - bodies of water (split at least into lake / ocean / gulf)
[2025-12-08 05:11 PM] rsulfuratus: yeah any time you use obsidian to edit frontmatter it expands arrays into lists
[2025-12-08 05:13 PM] Deciusmus: yeah, I think that is generally about correct
[2025-12-08 05:14 PM] Deciusmus: there a few odd ones like
    university, fort, castle, keep, abbey =>` are these all buildings or do we need something like "building complex" to represent larger things?
[2025-12-08 05:14 PM] rsulfuratus: abbey can just be holy site
[2025-12-08 05:15 PM] rsulfuratus: i would start with those all being buildings
[2025-12-08 05:15 PM] Deciusmus: similarly, there is potentially a difference between "lair" and other "dungeon-like" places and other buildings
[2025-12-08 05:15 PM] Deciusmus: similarly things like "gate", "bridge"
[2025-12-08 05:15 PM] rsulfuratus: right, i think the tricky bit here is always the level of detail. i guess i would tend to start by overclumping, and then resplit
[2025-12-08 05:15 PM] Deciusmus: right that makes sense
[2025-12-08 05:16 PM] Deciusmus: I pushed what i've done so far but am now back to working so if you want to do any more changes go ahead
[2025-12-08 05:16 PM] rsulfuratus: so i might start by lumping gate, bridge, road, street into ->` "travel features" or something (not a good name)
[2025-12-08 05:16 PM] Deciusmus: we should add a page for "Places Type Of Vocabulary" and then update the base so that anything not in the vocab is shown as "non-standard" and can get fixed
[2025-12-08 05:20 PM] rsulfuratus: i am going to start by ruthlessly lumping to as few categories as possible, and then see what needs to be split
[2025-12-08 05:25 PM] rsulfuratus: got it under 100 nonstandard; added forest, wetlands, lake to standard; pushed. gotta head home and get nathaniel but will probably do a bit more in 20 minutes
[2025-12-08 06:30 PM] rsulfuratus: with:
    - subdivision
    - settlement
    - realm
    - inn
    - building
    - waterway
    - watershed
    - road
    - holy site
    - island
    - plane
    - region
    - lake
    - wetlands
    - forest
    - plain
    - desert
    - topographical feature
    - marine feature
    - subterranean feature
    - infrastructure
    
    have only 5 things left
[2025-12-08 06:30 PM] rsulfuratus: 
![[Worldbuilding/Chats and Emails/_assets/discord/image-668F8.png]]
[2025-12-08 06:30 PM] rsulfuratus: all a bit tricky
[2025-12-08 06:31 PM] rsulfuratus: though Sulmana and Oracle's Pyre are either not invented yet except as a name (Sulmana) or intentionally left unclear for secret reasons (Oracle's Pyre)
[2025-12-08 06:32 PM] rsulfuratus: Gomat probably could be a transient settlement
[2025-12-08 06:32 PM] Deciusmus: what is "infrastructure"
[2025-12-08 06:32 PM] rsulfuratus: roads, bridges, walls
[2025-12-08 06:32 PM] rsulfuratus: sorry not road
[2025-12-08 06:32 PM] rsulfuratus: bridges, walls, gates
[2025-12-08 06:32 PM] rsulfuratus: any structure that is not a building and not a road basically
[2025-12-08 06:32 PM] Deciusmus: would "structure" be clearer?
[2025-12-08 06:33 PM] rsulfuratus: maybe but bulidings are structures are they not?
[2025-12-08 06:33 PM] Deciusmus: yeah but also inns are buildings
[2025-12-08 06:33 PM] Deciusmus: as are holy sites (usually)
[2025-12-08 06:34 PM] rsulfuratus: to me structure and buliding sound like synonyms while infrastructure clearly feels different
[2025-12-08 06:34 PM] Deciusmus: I'm not picky
[2025-12-08 06:34 PM] Deciusmus: infrastructure to me sounds very "meta"
[2025-12-08 06:34 PM] rsulfuratus: but these categories may all change anyway so i'm not too focused on names just yet
[2025-12-08 06:35 PM] rsulfuratus: e.g. right now fey portals and the prismwell are in infrastructure which is probably not right
[2025-12-08 06:35 PM] rsulfuratus: as are markets, fairgrounds, plazas
[2025-12-08 06:35 PM] Deciusmus: for Gomat, I think it is either a "lake" or a "settlement"
[2025-12-08 06:36 PM] Deciusmus: for sunset gate, it is a topographical feature I think
[2025-12-08 06:36 PM] Deciusmus: just of the feywild
[2025-12-08 06:38 PM] Deciusmus: for Oracle's Pyre and Sulmana I think leaving blank is strictly correct, but if that is going to annoy us, maybe allow for secret or unknown - they both seem like literally named places that could be any of (holy site, settlement, building, infrastructure, topographical feature)
[2025-12-08 06:38 PM] Deciusmus: scar of shadowfire is tricky
[2025-12-08 06:38 PM] rsulfuratus: for now i just put scar of shadowfire in infrastructure and both oracle's pyre and sulmana as typeOf: place
[2025-12-08 06:54 PM] rsulfuratus: pushed
[2025-12-08 07:01 PM] rsulfuratus: Generally my sense:
    - buildings / structures / infrastructure probably needs a bit more work
    - realm / subdivison / region might need some thought as well
    - waterways and settlements are clean, not surprisingly
    - forest / plain / desert / wetlands seems to work pretty well to capture biome type things with maybe a bit of refinement 
    - topographical feature, marine feature, subterranean feature are close
[2025-12-08 08:19 PM] Deciusmus: Re: realm -
    
    To me the key things are:
    
    - a way to capture political entities that are largely their own thing and have independent history,
    - a way to capture a subdivision of a political entity, mostly to this “parts of” 
    - a way to capture geographic scale features
[2025-12-08 08:20 PM] Deciusmus: What I’m not sure about is whether it’s worth splitting “subdivision” into marco and micro (duchy vs ward, for example)
[2025-12-08 08:20 PM] Deciusmus: Are there motivating examples of whether the existing region / realm / subdivision is a bit unclear ?
[2025-12-08 08:25 PM] rsulfuratus: right now "realm" includes:
    - fey realms
    - shadowfolds / domains of dread
    - groups of related kingdoms (dwarven kingoms as a note)
    - vostok (more a region)
    - Skaer and Skaerhem 
    - Zimkova
    
    so it is being used for a variety of general ideas
[2025-12-08 08:25 PM] rsulfuratus: part of this could be just reclassifying, e.g. Zimkova and Vostok might be region, not realm
[2025-12-08 08:26 PM] rsulfuratus: Skaer and Skaerhem might just need a little disentanglement (Skaer is really a culture page mostly; Skaerhem is the page for the islands; neither actually describes the political realm of the Skaer kingdom or whatever)
[2025-12-08 08:27 PM] rsulfuratus: region is also fairly unclear - it includes all the big regions, but also things like Borderlands and Heartlands in Sembara
[2025-12-08 08:27 PM] Deciusmus: Zimkova should be a region I think.
[2025-12-08 08:27 PM] Deciusmus: Vostok probably as well
[2025-12-08 08:28 PM] Deciusmus: Fey and shadowfolds might be worth having something else for though
[2025-12-08 08:29 PM] rsulfuratus: subdivision is a little better i think, though it is sometimes a little complicated because things change. e.g. i think it is useful to keep the "Dunmar" page even though this is really now two, or maybe three, separate political entities
[2025-12-08 08:29 PM] rsulfuratus: so what is the subdivision and what is the realm?
[2025-12-08 08:33 PM] rsulfuratus: from an abstract conceptual framework, i'd prefer something like (names placeholders):
    - region (strictly geographic)
    - political unit (realm/subdivision)
    - extraplanar domain (fey, shadowfolds, etc)
    - neighborhood (parts of settlements)
[2025-12-08 08:34 PM] rsulfuratus: basically eject extraplanar weirdness; make the settlement the fundamental unit, and have (a) a type for basically "groups of settlements" and (b) a type for basically "parts of settlements"
[2025-12-08 08:34 PM] rsulfuratus: but from a use-case point of view i don't know if that is right
[2025-12-08 08:35 PM] Deciusmus: I think extraplanar domain is clearly correct
[2025-12-08 08:36 PM] Deciusmus: And I think neighborhood makes sense — I was a little unsure if lumping wards and baronies together really makes sense
[2025-12-08 08:38 PM] rsulfuratus: so thinking a little more, i think for me the real issue with subdivision vs realm is that that is what whereabouts is for, and whereabouts is much more flexible and powerful
[2025-12-08 08:39 PM] rsulfuratus: typeOf should just tell me this is a page about a political unit of some kind
[2025-12-08 08:39 PM] rsulfuratus: and then the alias can tell me what it is called
[2025-12-08 08:40 PM] rsulfuratus: so i'm not sure there is a use case for kingdoms vs baronies - they could all just be realms imo
[2025-12-08 08:40 PM] Deciusmus: Yeah I can see that actually
[2025-12-08 08:42 PM] rsulfuratus: i think this actually gets back to old conversations about what is the "illoria" page, it is about the island or the realm? 
    
    while it is never going to be strictly perfect, the typeOf should tell you what the note largely focuses on. 
    
    e.g., in Dunmar, where i've written a lot, we have the "Dunmar" page, and the "Hara Basin" page. clearly realm vs region. and typeOf is useful for that
[2025-12-08 08:43 PM] rsulfuratus: or refounded alliance of aurbez vs aurbez plateau
[2025-12-08 08:45 PM] rsulfuratus: probably something like the "Cleanseau region" note is the most complicated here but even then the cleanseau region note leans more towards landscape/geography, while the manor of X pages are more political
[2025-12-08 08:49 PM] Deciusmus: Yeah I think that makes sense. I think if a few pages have unclear region/realm division that’s probably ok. I’d probably lean towards region for anything that doesn’t have a leader of some sort
[2025-12-08 08:49 PM] Deciusmus: But that doesn’t have to be a hard rule
[2025-12-08 08:50 PM] rsulfuratus: right. i'd also use realm for collections of related realms, like the "dwarven kingdoms" page or the "dunmar" page (now); possibly also something like the Borderlands which is really a collection of baronies
[2025-12-08 08:54 PM] Deciusmus: There are also some pages that maybe shouldn’t exist. Borderlands might be better as a section on the sembara page for example. Although maybe not. I think there’s good flexibility here
[2025-12-08 08:57 PM] rsulfuratus: without commiting to typeOf names yet, i think these are solid basic categories:
    
    People:
    
    typeOf categories that relate to settlements and people
    
    - settlement (a place where people live, from a farmstead to a major city)
    - neighborhood (a part of a settlement)
    - realm (a collection of settlements; can be e.g. a shire/barony; a kingdom; or a page about a group of kingdoms that share a history/information)
    
    Geographic regions:
    
    typeOf categories that relate to collections of geographic features
    
    - region (a collection of geographic features)
    - watershed (river systems)
    
    Extraplanar
    
    typeOf categories that relate to extraplanar features
    
    - plane (a page about a plane)
    - extraplanar domain (a page about a specific subregion of a page)
    - portal (a page about portal, extraplanar weak point, extraplanar vortex, or other kind of planar connection)
[2025-12-08 08:58 PM] rsulfuratus: still leaves: biomes, structures, water features, and landforms
[2025-12-08 08:58 PM] rsulfuratus: biomes are actually basically fine with just forest, plain, desert, and wetlands, although "plain" should probably be more like "open space"
[2025-12-08 09:07 PM] rsulfuratus: water features are also basically find with waterway, lake, and probably a handful of marine features (embayment, seaway, and something for sea/ocean).
[2025-12-08 09:07 PM] Deciusmus: Looks good to me so far
[2025-12-08 09:09 PM] rsulfuratus: landforms might require a bit of thought, and structures definitely requires a bit of thought
[2025-12-08 09:10 PM] Deciusmus: Yeah agreed. Might be worth moving ahead with the above and coming back to landforms and structures
[2025-12-08 09:11 PM] rsulfuratus: yeah. i was going to try to type up a note categorization document with this so far tonight but probably won't futher
[2025-12-08 09:12 PM] rsulfuratus: actually i might generally clean up MoC a bit. i'm searching for the displayDefaults and substitution tokens and can never find them
[2025-12-08 09:15 PM] rsulfuratus: `*`always searching
