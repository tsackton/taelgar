# NPCs

## Templates

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

NPC-header inserts a brief summary table with basic information calculated from yaml frontmatter.

## Tags

Currently working with four main importance tags:
- Key: an extensively recurring NPC with highly significant plot relevance
- Major: a recurring NPC or one with plot relevance
- Minor: an NPC with minor plot relevance, or significant screen time in a single session
- Background: an NPC with a non-plot-relevant role in a single session, or otherwise  a color/background character

Plus two info tags on top:
- Unmet: the party has not yet met the NPC, although they have heard of them
- Unknown: the party does not yet know of this NPC

Plus the special historical tag:
- Historical: an NPC who is deceased and can't be met.

An NPC cannot have more than one importance tag, and generally all except historical NPCs should have an importance tag. Historical NPCs can have one, but don't need it. 