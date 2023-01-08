# NPC templates

NPC-yaml automatically inserts the following frontmatter:

```
type: NPC
name: <% tp.file.title %>
species: 
ancestry: 
gender: 
born: 
died: 
location: 
locationRegion:
home: 
homeRegion:
origin:
originRegion:
affiliations: 
aliases: []
tags: [NPC/unsorted]

```

Species and ancestry should generally follow standard conventions. These are not currently auto-linked but should be link-able if desired. Ancestry can be left blank if it doesn't make sense (e.g. for many non-human races).

Gender should be one or "male", "female", or "nonbinary". Pronouns are autocalculated from gender, and printed. The autocalculated pronouns can be overwritten by adding `pronouns` to the yaml frontmatter. The value in that field will replace the autocalculated version next time the template is inserted. 

Age is autocalulcated from the current day and date born. Generally ages should work seemlessly if one, neither, or both of born and died are set. 

Home and homeRegion are where the NPC is based. For many people will also be where they grew up, but doesn't have to be This is where in the world you would generally expect to find the NPC if not modified by game events. 

Location and locationRegion are the current location of the NPC. This will automatically be tied to a current game time, based on fantasy calendar. 

Origin and originRegion are where the NPC was born. For most NPCs, this is probably either not relevant or the same as home/homeRegion, and can be left blank. But included in case it is occasionally useful. 

Affiliations is largely for dataview queries to build org charts and the like. 