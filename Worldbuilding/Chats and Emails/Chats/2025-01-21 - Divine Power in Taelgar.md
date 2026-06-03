# 2025-01-21 - Divine Power in Taelgar

[2025-01-21 09:48 AM] Deciusmus: I'm fairly busy today but I do have an afternoon meeting that is mostly other people talking but that I have to attend in case someone has a question for me, during which I might do Taelgar instead of work...
    
    My goal was to try to produce a couple of maps that outlined, for the "post Downfall", "height of Drankor" and  "pre Great War":
    (a) where canonically various human and non-humans were
    (b) where the "intentional blank spots" are
    
    I've recently been playing around with Lightroom Classic, so I have temporarily switched my Adobe plan to the one that has Photoshop...
    
    So I was wondering if this would be easier if I just had the raw map Photoshop file?
[2025-01-21 09:49 AM] Deciusmus: My assumption is there are no critical secrets in there and it might be worth putting in the git repo?
[2025-01-21 09:49 AM] rsulfuratus: it is about 300 Mb, so can't go in git repo
[2025-01-21 09:50 AM] rsulfuratus: i can probably share it with you though
[2025-01-21 09:50 AM] rsulfuratus: (via Adobe)
[2025-01-21 09:52 AM] Deciusmus: you could just use Git LFS
[2025-01-21 09:54 AM] Deciusmus: might be more of a pain that it is worth though;  anywaydon't have more time right now
[2025-01-21 09:54 AM] Deciusmus: https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage
[2025-01-21 09:59 AM] rsulfuratus: https://photoshop.adobe.com/id/urn:aaid:sc:US:1a0f772b-9a25-4c61-83b1-c1d0e1013cb1
[2025-01-21 09:59 AM] Deciusmus: yeah that worked, it just popped up in my creative cloud notifications
[2025-01-21 10:00 AM] rsulfuratus: measurement scale is 84 pixels = 50 miles
[2025-01-21 10:01 AM] rsulfuratus: not sure if that is shared or you have to set yourself
[2025-01-21 11:50 AM] rsulfuratus: i added a continent scale hex layer (24 miles edge to edge). there are probably too many hexes for it to be straightforward to label them on this scale. however, each degree latitude is ~3.5 hexes, which is a useful scale, and it makes translating from smaller hex-scale maps to the main map a lot easier
[2025-01-21 11:52 AM] rsulfuratus: now that I have the basic illustrator/photoshop interactions figured out I could add thicker lines to make a regular grid that could be labeled. the whole world is 14400 pixels square. each existing grid is 210 pixels long, 161 pixels tall
[2025-01-21 11:54 AM] rsulfuratus: if I made 3x3 grids, we'd have 23 squares across and 30 squares tall, so could label top with letters and side with numbers to have a bunch of well-defined quadrants
[2025-01-21 12:33 PM] rsulfuratus: okay, updated with labels:
    each hex is 24 miles. 
    each group of 24 miles is in a rectangle (~125 miles wide, ~96 miles high) 
    each 3x3 arrangement of rectangles is labeled.
    
    if within each 3x3 grid we label the inner rectangles 1-9 (from top left to bottom right, so 1|2|3 (next row) 4|5|6 etc, 
    
    then you can uniquely pinpoint each rectangle, e.g. Chardon is H13.1 and Drankor is L18.8
[2025-01-21 12:35 PM] rsulfuratus: pinpointing the exact hex is trickier on this scale, because each rectangle of 24 hexes actually splits several because of the hex ->` rectangle conversion. but each rectangle has a regular pattern of 6 columns of 4 hexes, it is just the 2nd, 4th, and 6th columns are 0.5 hex - hex - hex - hex - 0.5 hex
[2025-01-21 12:35 PM] rsulfuratus: still you could label each column A-F, and then label the hexes 1-4 or 1-6, counting half-hexes as full
[2025-01-21 12:37 PM] rsulfuratus: then if you have:
    bigGrid.littleGrid.column-row
    
    you get:
    Chardon ->` H13.1.B-5
    Karawa ->` J15.3.E-4
[2025-01-21 12:37 PM] rsulfuratus: etc
[2025-01-21 01:51 PM] Deciusmus: It would be really nice to have the text layers be Major Geographic | Minor Geographic | Major Settlement | Minor Settlement rather tha each text on its own layer
[2025-01-21 01:52 PM] rsulfuratus: you can't really do that in photoshop
[2025-01-21 01:55 PM] rsulfuratus: it is possible that a photoshop expert might have a solution using some advanced tools but if you just merge the layers they are converted to a raster image and you can no longer edit the text
[2025-01-21 01:55 PM] rsulfuratus: however it is theoretically possible - if a huge pain - to create multiple text groups for different categories
[2025-01-21 03:19 PM] Deciusmus: I sadly had to actually mostly answer questions at my previous meeting, but now have a bit of dead time before my next thing, might try to muck around a bit with maps for real.
    
    What I'm trying to do is create a new version of https://drive.google.com/file/d/1J33KjvXeFYKkMonDmhBhv7rbleEsGksv/view but without the spectualive stuff
[2025-01-21 03:19 PM] Deciusmus: and with a bit less arrows and a bit more "here's where people and non-humans were", and with the map truncated to just the "known world"
[2025-01-21 03:20 PM] Deciusmus: is that worth trying to do in photoshop, in a new layer, or should I just export a base map and do it in a separate file?
[2025-01-21 03:21 PM] rsulfuratus: either - it is easy enough to reimport if desired but i don't think photoshop layers are the right format for storing a bunch of these history maps
[2025-01-21 03:22 PM] rsulfuratus: i would just make sure we have the hexes in any export which makes it easy to realign with the main map or any future canonical hexmap
[2025-01-21 05:08 PM] rsulfuratus: I pushed an "open questions - campaigns" doc as if we are trying to get all the info into Obsidian it seems worthwhile to priotize canonical information over stuff that is probably or definitely not canonical (especially an issue for me as a good fraction of my stuff from 2019-2023 is in OneNote)
[2025-01-21 06:07 PM] Deciusmus: I pushed an update
[2025-01-21 06:28 PM] Deciusmus: also pushed a few soulstuff/land of dead thoughts
[2025-01-21 07:28 PM] rsulfuratus: looking at your comments on divine power in taelgar, perhaps easier to move to discord. i think the point about classification of magic into arcane/divine/primal is not so much about specific D&D classes, but about where on this spectrum things fall:
    (a) fey have clerics and divine magic works for fey similarly to humans; someone making a "fey cleric" character could reasonably be expected to think a little bit about what divine entity grants them power
    (b) fey have clerics that metaphysically / in-world access magic from the Plane of Creation, but not necessarily via the Material-Plane-Centric "divine powers grant miracles", suggesting an alternate route for diivine magic to manifest
    (c) fey don't have clerics. any player that wants to play a fey cleric would be assumed to be using the cleric mechanics to represent some other kind of in-world magic, and would be expected NOT to have a connection to a particular god
    
    or, put another way, do fey, in-world, pray to gods; pray in some strange fey way; or don't pray at all in any sense
[2025-01-21 07:34 PM] Deciusmus: (About to eat dinner but will be around for taelgar stuff a bit later)
[2025-01-21 07:54 PM] Deciusmus: I think it’s b or c
[2025-01-21 07:54 PM] Deciusmus: Although I’m not sure that it is impossible for fey to pray to a god
[2025-01-21 07:55 PM] rsulfuratus: right, i mean i think we've established pretty clearly that all kinds of things are possible and that at least some gods are not picky about who they get prayers from and grant prayers to
[2025-01-21 07:56 PM] rsulfuratus: but i guess that is different from "there is fey religion"
[2025-01-21 07:56 PM] Deciusmus: Right. I think the vibe of any inner plane creature praying to a god seems … non standard
[2025-01-21 07:57 PM] rsulfuratus: the original "children of the divine" logic actually got around this nicely by making fey/elementals/giants/dragons have a direct connection to the divine presence.
[2025-01-21 07:59 PM] Deciusmus: Right. Why does that have to be wrong though?
[2025-01-21 08:00 PM] Deciusmus: I mean I’m not sure if elementals have a soul on the plane of souls necessarily but if they don’t they should have some  equivalent
[2025-01-21 08:01 PM] rsulfuratus: i kind of like the vibe that none of the speculation about the plane of souls in the in-world note is correct, but the hint from the fey idea of the dreamworld being the "real" plane of souls and the plane of souls being the echo ties into your suggestion as well
[2025-01-21 08:02 PM] Deciusmus: I also like the vibe that none of them are precisely correct
[2025-01-21 08:02 PM] Deciusmus: I also like the idea of preserving unique possibilities and contingencies rather than having a complete typology or everything is exactly in a neat box
[2025-01-21 08:03 PM] Deciusmus: But one question that seems relevant - did the riving create the plane of souls and the land of the dead? What was cosmology like before the riving?
[2025-01-21 08:05 PM] rsulfuratus: it isn't clear to me at the moment
[2025-01-21 08:06 PM] rsulfuratus: the original concept of the riving pre-dates the invention of the plane of creation as a nexus for the Divine Presence
[2025-01-21 08:06 PM] rsulfuratus: so in that pre-Plane of Creation cosmology, the riving was effectively all the inner planes mixed together
[2025-01-21 08:06 PM] rsulfuratus: and dominated by arcane magical energy
[2025-01-21 08:08 PM] rsulfuratus: the riving creates the Firstborn, pulls apart the inner planes, but it was never really resolved how the land of the dead / plane of souls / spiritual realms come into existence
[2025-01-21 08:09 PM] rsulfuratus: i think i'm coming around to the idea that the plane of souls possibly always existed, and maybe the riving stretches the plane of souls into the astral plane and perhaps even creates the plane of creation as a home/embodiment of the divine presence, behind the wall of the land of the dead
[2025-01-21 08:09 PM] rsulfuratus: so that would imply the riving creates the land of the dead, but not the plane of souls which predates it
[2025-01-21 08:12 PM] rsulfuratus: (more in a bit if you are around, have to get Nathaniel to finish his homework)
[2025-01-21 08:20 PM] Deciusmus: (Was cleaning but done)
[2025-01-21 08:20 PM] Deciusmus: (So back)
[2025-01-21 08:23 PM] Deciusmus: I think the metaphysics might work better if we assume that at least the plane of souls existed forever.
[2025-01-21 08:29 PM] Deciusmus: That sets up this idea that whatever creation process existed during the riving the great wyrms and whatnot existed on the plane of souls. How that fragmented during the riving is canonically unclear but ultimately it means a fundamental divide between children of the riving - who get soul stuff “directly” - and  after the riving - who get it from gods
[2025-01-21 08:34 PM] rsulfuratus: Yeah I think that makes sense. Want to let it sit a little but am going to update land of the dead tonight and will copy this discussion and update the open questions
[2025-01-21 08:36 PM] Deciusmus: There is a whole idea that could be explored about how the actual source of divine magic is _soulstuff_ not anything else
[2025-01-21 08:36 PM] Deciusmus: So the only creatures that don't have access to divine magic are those that do not have soulstuff
[2025-01-21 08:37 PM] Deciusmus: for most "normal" species, their own "personal" soul stuff is not strong enough to generate magical effects
[2025-01-21 08:37 PM] Deciusmus: but of course, what is _ki_ powers except kenzo using the power of his soul on the plane of souls to generate magical effects?
[2025-01-21 08:42 PM] rsulfuratus: Yeah. Actually this could tie back into hkar - maybe part of the magic of hkar was kind of an upwelling of soulstuff somehow, so that personal soulstuff was enough for magic. At least in the early days
[2025-01-21 08:43 PM] rsulfuratus: Maybe the whole thing with the void mind is it cannot create soulstuff, it can only try to shape soulstuff that escapes from the divine presence
[2025-01-21 08:43 PM] rsulfuratus: Hence the desire to conquer Hkar, and the need to destroy it
[2025-01-21 08:44 PM] rsulfuratus: Could also tie into undead, and why turn undead works, and why you cant have undead clerics but you can have undead mages

