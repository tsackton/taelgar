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
  let species  = (p.species   ?? "").trim();
  let dm_owner = (p.dm_owner  ?? "").trim();
  let dm_notes = (p.dm_notes  ?? "").trim();

  return {
    person:   p.file.link,
    species:  species,
    dm_owner: dm_owner,
    dm_notes: dm_notes,
    status:   status
  };
});

console.log("Before sort:", data);

//------------------------------------------------------------------
// 3) Sort Data by status → species → person
//------------------------------------------------------------------

data.sort((a, b) => {
  // 1) Compare status (simple string comparison)
  if (a.status < b.status) return -1;
  if (a.status > b.status) return 1;

  // 2) Compare species
  if (a.species < b.species) return -1;
  if (a.species > b.species) return 1;
  
  return 0;
});


console.log("After sort:", data);

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


