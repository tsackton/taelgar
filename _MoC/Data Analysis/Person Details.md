# People Details

This gives various ways of breaking down species and ancestry, as well as finding pages with missing frontmatter

## Species, Subspecies, Ancestry

- Species is species
- Subspecies is a subtype of a species that is not connected to a place or culture, e.g. salt lizardfolk may exist outside of Mawar; peronar may exist outside of Drankor, etc
- Ancestry is a culture or origin; ancestries should always refer back to locations in the Gazetteer

### Counts
```dataview
TABLE WITHOUT ID
  split(Combo, "\\|")[0] AS "Species",
  split(Combo, "\\|")[1] AS "Subspecies",
  split(Combo, "\\|")[2] AS "Ancestry",
  length(rows) AS "Count"
FROM #person
GROUP BY (default(species, "missing") + "|" + 
   default(subspecies, "none") + "|" + 
   default(ancestry, "none")) AS Combo

SORT split(Combo, "\\|")[0], length(rows) DESC

```

### Missing Species, With Status, Excluding Stubs

```dataview
TABLE WITHOUT ID
  file.link AS "Page",
  Status AS "Status"
FROM #person AND !#status/stub
WHERE !species
FLATTEN choice(
    length(filter(file.etags, (t) => startswith(t, "#status/stub"))) > 0,
    "stub",
    choice(
      length(filter(file.etags, (t) => startswith(t, "#status/needswork"))) > 0,
      "needs work",
      choice(
        length(filter(file.etags, (t) => startswith(t, "#status/check"))) > 0,
        "check",
        choice(
          length(filter(file.etags, (t) => startswith(t, "#status/active"))) > 0,
          "active",
          "complete"
        )
      )
    )
  ) AS "Status"
SORT Status ASC
```

## Possibly Incomplete People

### Humans

Humans Missing Ancestry

```dataview
TABLE WITHOUT ID
  file.link AS "Page",
  Status AS "Status"
FROM #person
WHERE species = "human" and !ancestry
FLATTEN choice(
    length(filter(file.etags, (t) => startswith(t, "#status/stub"))) > 0,
    "stub",
    choice(
      length(filter(file.etags, (t) => startswith(t, "#status/needswork"))) > 0,
      "needs work",
      choice(
        length(filter(file.etags, (t) => startswith(t, "#status/check"))) > 0,
        "check",
        choice(
          length(filter(file.etags, (t) => startswith(t, "#status/active"))) > 0,
          "active",
          "complete"
        )
      )
    )
  ) AS "Status"
SORT Status ASC
```

### Halflings and Dwarves

No affiliation. Note this doesn't capture dwarves without a thuhr, for example, as a dwarf with a clan affiliation will not be included here. Including family to catch those using the old frontmatter.

```dataview
table species, ancestry, family, Status as "status"
from #person
where !affiliations and (species = "dwarf" or species = "halfling") 
FLATTEN choice(
    length(filter(file.etags, (t) => startswith(t, "#status/stub"))) > 0,
    "stub",
    choice(
      length(filter(file.etags, (t) => startswith(t, "#status/needswork"))) > 0,
      "needs work",
      choice(
        length(filter(file.etags, (t) => startswith(t, "#status/check"))) > 0,
        "check",
        choice(
          length(filter(file.etags, (t) => startswith(t, "#status/active"))) > 0,
          "active",
          "complete"
        )
      )
    )
  ) AS "Status"
sort species, subspecies, ancestry
```

### Elves

Not clear what makes an elf complete. For now, showing ka, subspecies, and ancestry. 

```dataview
table species, ancestry, subspecies, ka, Status as "status"
from #person
where species = "elf" 
FLATTEN choice(
    length(filter(file.etags, (t) => startswith(t, "#status/stub"))) > 0,
    "stub",
    choice(
      length(filter(file.etags, (t) => startswith(t, "#status/needswork"))) > 0,
      "needs work",
      choice(
        length(filter(file.etags, (t) => startswith(t, "#status/check"))) > 0,
        "check",
        choice(
          length(filter(file.etags, (t) => startswith(t, "#status/active"))) > 0,
          "active",
          "complete"
        )
      )
    )
  ) AS "Status"
sort species, ka
```

### Fey, Dragon, Elemental, Giant, Undead

For these, we have used 'subspecies' instead of 'ancestry'. Plotting the pages without subspecies here. Including ancestry to catch places where we accidentally use "ancestry" instead of subspecies. 

```dataview
TABLE WITHOUT ID
  file.link AS "Page",
  species,
  ancestry,
  Status AS "Status"
FROM #person AND !#status/stub
WHERE (species = "fey" or species = "elemental" or species = "dragon" or species = "giant" or species = "undead") and !subspecies
FLATTEN choice(
    length(filter(file.etags, (t) => startswith(t, "#status/stub"))) > 0,
    "stub",
    choice(
      length(filter(file.etags, (t) => startswith(t, "#status/needswork"))) > 0,
      "needs work",
      choice(
        length(filter(file.etags, (t) => startswith(t, "#status/check"))) > 0,
        "check",
        choice(
          length(filter(file.etags, (t) => startswith(t, "#status/active"))) > 0,
          "active",
          "complete"
        )
      )
    )
  ) AS "Status"
SORT species, Status
```

### Other Species

Centaur, hobgoblin, kenku, lizardfolk, orc, stoneborn currently have nothing obvious to include besides species, so nothing to display. 

### Freeform Species

List of species that are not one of:
human, dwarf, elf, halfling, stoneborn, lizardfolk, orc, hobgoblin, kenku, centaur, fey, giant, dragon, undead, elemental. 

```dataview
TABLE WITHOUT ID
  file.link AS "Page",
  species,
  ancestry,
  subspecies,
  Status AS "Status"
FROM #person AND !#status/stub
WHERE species != "fey" and species != "elemental" and species != "dragon" and species != "giant" and species != "undead" and species != "human" and species != "elf" and species != "dwarf" and species != "lizardfolk" and species != "centaur" and species != "halfling" and species != "hobgoblin" and species != "kenku" and species != "orc" and species != "stoneborn"
FLATTEN choice(
    length(filter(file.etags, (t) => startswith(t, "#status/stub"))) > 0,
    "stub",
    choice(
      length(filter(file.etags, (t) => startswith(t, "#status/needswork"))) > 0,
      "needs work",
      choice(
        length(filter(file.etags, (t) => startswith(t, "#status/check"))) > 0,
        "check",
        choice(
          length(filter(file.etags, (t) => startswith(t, "#status/active"))) > 0,
          "active",
          "complete"
        )
      )
    )
  ) AS "Status"
SORT species, Status
```

## People Without Origins

People that lack ancestry and don't have an origin whereabouts. 

```dataviewjs
//------------------------------------------------------------------
// 1) Gather & Filter Pages
//------------------------------------------------------------------
const { util } = customJS;
let pages = dv.pages("#person");

// Keep only those missing both ancestry & origin
let missingBoth = pages.filter(p => {
    let hasAncestry = !!p.ancestry;
    let hasOrigin   = util.originExists(p.file.frontmatter);
    return (!hasAncestry && !hasOrigin);
});

//------------------------------------------------------------------
// 2) Build an Array of Data
//------------------------------------------------------------------
let data = missingBoth.map(p => {
  // Compute status from tags
  let tags = p.file.etags ?? [];
  let status = "complete";  // default if none match

  if (tags.some(t => t.startsWith("#status/stub"))) {
    status = "stub";
  } else if (tags.some(t => t.startsWith("#status/needswork"))) {
    status = "needs work";
  } else if (tags.some(t => t.startsWith("#status/check"))) {
    status = "check";
  } else if (tags.some(t => t.startsWith("#status/active"))) {
    status = "active";
  }

  // Gather species, dm_owner, dm_notes
  let species  = (p.species   ?? "missing").trim();
  let dm_owner = (p.dm_owner  ?? "missing").trim();
  let dm_notes = (p.dm_notes  ?? "missing").trim();

  return {
    person:   p.file.link,
    species:  species,
    dm_owner: dm_owner,
    dm_notes: dm_notes,
    status:   status
  };
});


//------------------------------------------------------------------
// 4) Render the Table
//------------------------------------------------------------------
dv.table(
  ["Person", "species", "dm_owner", "dm_notes", "status"],
  data.map(row => [
    row.person,
    row.species,
    row.dm_owner,
    row.dm_notes,
    row.status
  ])
);

```


