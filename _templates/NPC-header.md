<%* 
const currentYear = 1748

let age;
let bornString;
let diedString;
let genderString;
let speciesString;
let pronouns;

if (!tp.frontmatter.species) {
  speciesString = "unknown species"
} else {
  speciesString = tp.frontmatter.species
}

if (!tp.frontmatter.gender) {
  genderString = "unknown gender, "
  pronouns = ""
} else if (tp.frontmatter.gender == "male") {
  genderString = "male "
  pronouns = "(he/him)"
} else if (tp.frontmatter.gender == "female") {
  genderString = "female "
  pronouns = "(she/her)"
} else if (tp.frontmatter.gender == "nonbinary") {
  genderString = "nonbinary "
  pronouns = "(they/them)"
}

yearDied = tp.frontmatter.died
yearBorn = tp.frontmatter.born

if (!yearBorn) {
 age = "unknown age"
 bornString = ""
 diedString = ""
} else {
 bornString = `b. ${yearBorn}`
 diedString = `d. ${yearDied}`
 if (!yearDied) { // if yearDied is undefined
   age = currentYear - yearBorn; // calculate age as currentYear - yearBorn
 } else if (yearDied > currentYear) { // if yearDied is defined and > currentYear
   age = currentYear - yearBorn; // calculate age as currentYear - yearBorn
 } else { // if yearDied is defined and <= currentYear
   age = "deceased"; // set age to "deceased"
 }
 if (age !== "deceased") { // if age is not "deceased" 
   age = `${age} years old in ${currentYear}`; // set age to "age years old" 
   diedString = ""
 }
} 

// location information //

let origLocString

if (!tp.frontmatter.home) {
  origLocString = "unknown"
} else {
  origLocString = tp.frontmatter.home
}

// current location information //

let curLocString

if (!tp.frontmatter.home) {
  curLocString = "unknown"
} else {
  curLocString = tp.frontmatter.location
}

// ancestry information //

let ancString

if (!tp.frontmatter.ancestry) {
  ancString = ""
} else {
  ancString = ` (${tp.frontmatter.ancestry})`
}

%> # <% tp.frontmatter.name %>
<% pronouns %>
<% genderString %><% speciesString %><% ancString %>
<% bornString %> <% diedString %>
<% age %>
Originally from: <% origLocString %>
Last known location: <% curLocString %>

---
