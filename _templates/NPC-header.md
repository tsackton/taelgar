<%* 
// get fantasy calendar dates //

const currentYear =  FantasyCalendarAPI.getCalendars()[0].current.year
const currentGameMonth = FantasyCalendarAPI.getCalendars()[0].current.month
const currentGameDay = FantasyCalendarAPI.getCalendars()[0].current.day
const currentGameMonthName = FantasyCalendarAPI.getCalendars()[0].static.months[currentGameMonth].name

let genderString;
let speciesString;
let currentGameTimeEditString;
let pronouns;

currentGameTimeEditString = currentGameMonthName + " " + currentGameDay + ", " + currentYear

// species and gender //

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
  pronouns = ", he/him"
} else if (tp.frontmatter.gender == "female") {
  genderString = "female "
  pronouns = ", she/her"
} else if (tp.frontmatter.gender == "nonbinary") {
  genderString = "nonbinary "
  pronouns = ", they/them"
}

// if pronouns are defined in metadata, overwrite default calculation

if (tp.frontmatter.pronouns) {
  pronouns = "(" + tp.frontmatter.pronouns + ")"
}

// ancestry information //

let ancString

if (!tp.frontmatter.ancestry) {
  ancString = ""
} else {
  ancString = " (" + tp.frontmatter.ancestry + ")"
}

// calculate age and create born + died string //

yearDied = tp.frontmatter.died
yearBorn = tp.frontmatter.born

let age;

// calculate age as current year - year born, or deceased year - year born if deceased year is < current year //

if (!yearBorn) {
  age = "unknown age"
} else if (yearDied && (yearDied < currentYear)) {
  age = yearDied - yearBorn
} else {
  age = currentYear - yearBorn
}

// calculate strings //

let ageString;
let bornString;
let deathString;

if (!yearBorn && !yearDied) {
// don't know birth year or death year
  ageString = age
  bornString = ""
  deathString = ""
} else if (!yearBorn && yearDied) {
// know year died, but not year born
  if (yearDied > currentYear) {
  // will die in the future //
    ageString = age
    bornString = ""
    deathString = ""
  } else {
  // has died in or before current year
    ageString = "deceased at unknown age"
    bornString = ""
    deathString = "d. " + yearDied + "\n>"
  }
} else if (yearBorn && !yearDied) {
// known birth year, no death year
  ageString = age + " years old"
  bornString = "b. " + yearBorn
  deathString = "\n>"
} else if (yearBorn && yearDied) {
// both birth and death are defined
  if (yearDied > currentYear) {
  // will die in the future //
    ageString = age + " years old"
    bornString = "b. " + yearBorn
    deathString = "\n>"
  } else if (yearDied <= currentYear) {
  // has died in or before current year
    ageString = "deceased at " + age
    bornString = "b. " + yearBorn
    deathString = ", d. " + yearDied + "\n>"
  } else {
   // shouldn't get here
   ageString = "ERROR1"
  }
} else {
 // shouldn't get here
 ageString = "ERROR2"
}

// home location //

let basedLocString

if (!tp.frontmatter.home && !tp.frontmatter.homeRegion) {
  basedLocString = "unknown"
} else if (!tp.frontmatter.home && tp.frontmatter.homeRegion) {
  basedLocString = "[[" + tp.frontmatter.homeRegion + "]]"
} else if (tp.frontmatter.home && !tp.frontmatter.homeRegion) {
  basedLocString = tp.frontmatter.home
} else {
  basedLocString = tp.frontmatter.home + ", [[" + tp.frontmatter.homeRegion + "]]"
}

// current location information //

let curLocString

if (!tp.frontmatter.location && !tp.frontmatter.locationRegion) {
  curLocString = "unknown"
} else if (!tp.frontmatter.location && tp.frontmatter.locationRegion) {
  curLocString = "[[" + tp.frontmatter.homeRegion + "]]"
} else if (tp.frontmatter.location && !tp.frontmatter.locationRegion) {
  curLocString = tp.frontmatter.location
} else {
  curLocString = tp.frontmatter.location + ", [[" + tp.frontmatter.locationRegion + "]]"
}

// current location information //

let origLocString

if (!tp.frontmatter.origin && !tp.frontmatter.originRegion) {
  origLocString = ""
} else if (!tp.frontmatter.origin && tp.frontmatter.originRegion) {
  origLocString = "Originally from: [[" + tp.frontmatter.originRegion + "]]\n>"
} else if (tp.frontmatter.origin && !tp.frontmatter.originRegion) {
  origLocString = "Originally from: " + tp.frontmatter.origin + "\n>"
} else {
  origLocString = "Originally from: " + tp.frontmatter.origin + ", [[" + tp.frontmatter.originRegion + "]]\n>"
}

%># <% tp.frontmatter.name %>
>[!info] Basic information
><% speciesString %><% ancString %><% pronouns %>
><% bornString %><% deathString %><% ageString %>
><% origLocString %>Based in: <% basedLocString %>
>Location (updated <% currentGameTimeEditString %>): <% curLocString %>

