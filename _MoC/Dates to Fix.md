This file contains search results using embedded `query` blocks that contain date-like text but that aren't marked as #event-source or #timeline 

# People with dates

```query
(/DR\s*\d+/ OR /\d+/s*DR/ OR /\d+\s+\w+\s+\d+:/) -tag:#event-source -tag:#timeline ([type:NPC] OR [type:PC] OR [type:Organization] OR [type:Ruler])
```
# Campaign Notes with dates

```query
(/DR\s*\d+/ OR /\d+/s*DR/ OR /\d+\s+\w+\s+\d+:/) -tag:#event-source -tag:#timeline path:Campaigns
```

# Other Notes

```query
(/DR\s*\d+/ OR /\d+/s*DR/ OR /\d+\s+\w+\s+\d+:/) -tag:#event-source -tag:#timeline -[type:NPC] -path:Campaign -path:Worldbuilding -path:_DM -[type:PC] -[type:Organization] -[type:Ruler] -path:_templates -path:"Primary Sources"
```

