This file contains search results using embedded `query` blocks that contain date-like text.
# People with dates

```query
(/DR\s*\d+/ OR /\d+/s*DR/ OR /\d+\s+\w+\s+\d+:/) path:People
```
# Campaign Notes with dates

```query
(/DR\s*\d+/ OR /\d+/s*DR/ OR /\d+\s+\w+\s+\d+:/) -tag:#event-source -tag:#timeline path:Campaigns -[fc-date]
```

# Other Notes

```query
(/DR\s*\d+/ OR /\d+/s*DR/ OR /\d+\s+\w+\s+\d+:/) -tag:#event-source -tag:#timeline -path:People -path:Campaign -path:Worldbuilding -path:_DM -path:_templates -path:"Primary Sources"
```

