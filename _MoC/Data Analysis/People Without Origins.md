```dataviewjs
//------------------------------------------------------------------
// 1) Gather & Filter Pages (convert to real array)
//------------------------------------------------------------------
const api = globalThis.Taelgarverse;
if (api?.apiVersion !== 1) {
    dv.paragraph("This query requires a Taelgarverse build with the note query API.");
    return;
}
const queries = await api.getNoteQueries();
let pages = dv.pages("#person").array(); // .array() converts Dataview's DataArray to a normal JS array

// Keep only those missing both ancestry & origin
let missingBoth = pages.filter(p => {
  let hasAncestry = !!p.ancestry;
  let hasOrigin = queries.getRecordedOrigin(p.file.path) !== null;
  return (!hasAncestry && !hasOrigin);
});

//------------------------------------------------------------------
// 2) Build a plain JS array of data
//------------------------------------------------------------------
let data = missingBoth.map(p => {
  let tags   = p.file.etags ?? [];
  let status = "complete";
  if (tags.some(t => t.startsWith("#status/stub")))         status = "stub";
  else if (tags.some(t => t.startsWith("#status/needswork"))) status = "needs work";
  else if (tags.some(t => t.startsWith("#status/check")))     status = "check";
  else if (tags.some(t => t.startsWith("#status/active")))    status = "active";

  return {
    person:   p.file.link,
    species:  p.species ?? "missing",
    status
  };
});

//------------------------------------------------------------------
// 3) Sort: (1) status in custom order, (2) species alphabetically
//------------------------------------------------------------------
let statusOrder = ["stub", "needs work", "check", "complete", "active"];
function getStatusIndex(s) {
  let idx = statusOrder.indexOf(s);
  return idx >= 0 ? idx : statusOrder.length; 
}

data.sort((a, b) => {
  // Compare status by custom order
  let sCmp = getStatusIndex(a.status) - getStatusIndex(b.status);
  if (sCmp !== 0) return sCmp;

  // Then compare species alphabetically
  return a.species.localeCompare(b.species, undefined, { sensitivity: "base" });
});

//------------------------------------------------------------------
// 4) Render the table
//------------------------------------------------------------------
dv.table(["Person", "Species", "Status"], 
  data.map(row => [row.person, row.species, row.status])
);

```



