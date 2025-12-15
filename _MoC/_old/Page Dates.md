Most pages support some dates, which are used both for other processing of the page (i.e. to see if it exists or not) as well as for outputting details in the header line.

All dates are (currently) able to be specified in one of three formats:
* YYYY
* YYYY-MM
* YYYY-MM-DD

Note that in frontmatter, specifying YYYY-MM and YYYY-MM-01 are identical. If you want to indicate that the day is unknown, set the date as YYYY-MMx
YYYY compares as YYYY-01-01 for start and YYYY-12-31 for end, i.e. a death of 1728 = 1728-12-31 whereas a birth of 1728 = 1728-01-01

The dates supported are:

* born, created: these are used to determine at what point the page started to exist. 
* died, destroyed: these are used to determine at what point the page ceased to exist. 
* pageTargetDate: Used to define the "current year" for this page, mostly for debugging

Logically, we can turn these into the following outputs:

* Page Target Date: If pageTargetDate is true, use that. Otherwise use the current Fantasy Calendar date
* Page Existence Date: The born or created date, if set, 0001 otherwise
* Page End Date: The died or destroyed date, if set, 9999 otherwise

Dates are also supported in:
- whereabouts
- campaignInfo
- affiliations

0001 and 9999 dates are special dates that should never be displayed, and are used to indicate: this happened before all times or this happened after all times. 
