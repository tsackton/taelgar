This page documents how the last seen by party structure is generated.

Note that this is generated as static data during template processing, so does not need to be managed in Python.

The lastSeenByParty is a YAML structure with the following form:

```yaml
lastSeenByParty:
- { date: , prefix: }
```

This generates a line for each party that has seen the person, like so:

For each row, it generates "exact whereabouts location" (see  [[Whereabouts and Location Specification]]) using the date as the target date. If this generates undefined, the line is skipped. Otherwise, it outputs a line like:

```
%%^Campaign:prefix%% Last seen by [[(party page)|(party name)]] at (date): (exact location) %%^End%%
```

The prefix comes from the last seen by party structure. The party page and party name comes from the metadata.json in .obsidian:

```json
    "campaigns":[
        {
            "prefix": "clee",
            "campaignName": "Cleenseau",
            "partyName" : "The Andover Crowd",
            "partyPage" : "Some Actual Linkable File in the Vault"
        },
```

If the party page is not set, the link is not generated. If the partyName is not set, the line is skipped.