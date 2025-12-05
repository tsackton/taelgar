# Linked Pages

This tracks pages that are in directories that imply tentative/non-public but are linked outside those directories. Generally speaking these notes should either be moved to a more appropriate place (e.g., Worldbuilding/Staging if just a marker), or should be de-linked.

### World Building - Brainstorming

```dataviewjs

// Define the target directory and directories to exclude
const targetDir = "Worldbuilding/Brainstorming";
const excludeDirs = ["Worldbuilding", "_DM_"]; 

// Function to check if a path is within the target directory 
function isInTargetDir(path) {
  return path.startsWith(`${targetDir}/`);
}

// Function to check if a path is outside the target directory and not in any excluded directories
function isOutsideTargetDir(path) {
  return !path.startsWith(`${targetDir}/`) && !excludeDirs.some(exDir => path.startsWith(`${exDir}/`));
}

// Retrieve all pages in the vault
const allPages = dv.pages();

// Filter pages to include only those in the target directory, excluding specified subdirectories
const targetPages = allPages.filter(p => isInTargetDir(p.file.path));

const results = [];

for (let page of targetPages) {
  const inlinks = page.file.inlinks;
  const externalBacklinks = inlinks.filter(link => {
    const linkedPage = dv.page(link.path);
    return linkedPage && isOutsideTargetDir(linkedPage.file.path);
  });
  if (externalBacklinks.length > 0) {
    results.push([page.file.link, externalBacklinks.map(link => dv.fileLink(link.path))]);
  }
}

dv.table(["File", "External Backlinks"], results);


```


### World Building - Tentative

```dataviewjs

// Define the target directory and directories to exclude
const targetDir = "Worldbuilding/Tentative";
const excludeDirs = ["Worldbuilding", "_DM_", "_dm_notes"]; 

// Function to check if a path is within the target directory 
function isInTargetDir(path) {
  return path.startsWith(`${targetDir}/`);
}

// Function to check if a path is outside the target directory and not in any excluded directories
function isOutsideTargetDir(path) {
  return !path.startsWith(`${targetDir}/`) && !excludeDirs.some(exDir => path.startsWith(`${exDir}/`));
}

// Retrieve all pages in the vault
const allPages = dv.pages();

// Filter pages to include only those in the target directory, excluding specified subdirectories
const targetPages = allPages.filter(p => isInTargetDir(p.file.path));

const results = [];

for (let page of targetPages) {
  const inlinks = page.file.inlinks;
  const externalBacklinks = inlinks.filter(link => {
    const linkedPage = dv.page(link.path);
    return linkedPage && isOutsideTargetDir(linkedPage.file.path);
  });
  if (externalBacklinks.length > 0) {
    results.push([page.file.link, externalBacklinks.map(link => dv.fileLink(link.path))]);
  }
}

dv.table(["File", "External Backlinks"], results);


```

##  DM Notes

```dataviewjs

// Define the target directory and directories to exclude
const targetDir = "_DM_";
const excludeDirs = ["_DM_"]; 

// Function to check if a path is within the target directory 
function isInTargetDir(path) {
  return path.startsWith(`${targetDir}/`);
}

// Function to check if a path is outside the target directory and not in any excluded directories
function isOutsideTargetDir(path) {
  return !path.startsWith(`${targetDir}/`) && !excludeDirs.some(exDir => path.startsWith(`${exDir}/`));
}

// Retrieve all pages in the vault
const allPages = dv.pages();

// Filter pages to include only those in the target directory, excluding specified subdirectories
const targetPages = allPages.filter(p => isInTargetDir(p.file.path));

const results = [];

for (let page of targetPages) {
  const inlinks = page.file.inlinks;
  const externalBacklinks = inlinks.filter(link => {
    const linkedPage = dv.page(link.path);
    return linkedPage && isOutsideTargetDir(linkedPage.file.path);
  });
  if (externalBacklinks.length > 0) {
    results.push([page.file.link, externalBacklinks.map(link => dv.fileLink(link.path))]);
  }
}

dv.table(["File", "External Backlinks"], results);

```
