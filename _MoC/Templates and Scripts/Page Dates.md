Most pages support some dates, which are used both for other processing of the page (i.e. to see if it exists or not) as well as for outputting details in the header line.

All dates are (currently) able to be specified in one of three formats:
* YYYY
* YYYY-MM
* YYYY-MM-DD

Note that in frontmatter, specifying YYYY-MM and YYYY-MM-01 are identical. If you want to indicate that the day is unknown, set the date as YYYY-MMx
YYYY compares as YYYY-01-01 for start and YYYY-12-31 for end, i.e. a death of 1728 = 1728-12-31 whereas a birth of 1728 = 1728-01-01

See also [[Formatting]]

The dates supported are:

* born, created: these are used to determine at what point the page started to exist. If the page is a Ruler, PC, or NPC, born will be used. Otherwise created.
* died, destroyed: these are used to determine at what point the page ceased to exist. If the page a Ruler, PC, or NPC, died will be used. Otherwise, destroyed
* reignStart: For rulers only. When their reign started
* reignEnd: For rulers only. When their reign ended
* pageTargetDate: Used to define the "current year" for this page, mostly for debugging

Logically, we can turn these into the following outputs:

* Page Target Date: If pageTargetDate is true, use that. Otherwise use the current Fantasy Calendar date
* Page Existence Date: The born or created date, if set, undefined otherwise
* Page End Date: The died or destroyed date, if set, undefined otherwise
### get_PageDatedValue

The get_PageDatedValue output generates a single line of text to indicate information about the page. What it generates depends on various factors. Broadly it is of the form:

Page start in future:  ```(not exist text)```
Page start and page end defined, start after end: ```Time Traveler, Check your YAML```
Page start and page end defined, end in past: ```(startPrefix) (existenceDate) - (end prefix) (end date) (endStatus) at (age) years```
Page start and page end defined, end in future: ```(startPrefix) (existenceDate) ((age) years old)```
Page start defined and page end not defined: ```(startPrefix) (existenceDate) ((age) years old)```
Page start not defined page end defined, page end in future: empty
Page start not defined page end defined, page end in past: ```(end prefix) (end date) (endStatus)```
Page start not defined, page end not defined: empty

	* age is calculated in the logical way (i.e. same as a human age)
* start prefix, end prefix, not exist text, and end status can come from YAML or have defaults. See the Javascript for details

### get_RegnalValue

This outputs the regnal information of a page. The regnal information is based on two dates: reignStart and reignEnd.

If the reignStart is not set, output nothing.
If the reignStart is after the target date, output nothing.
If the reignEnd is not set, set to page end date

If the reignEnd and in the past, is defined: ```reigned (reign start) - (reign end) ((age) years)```
If the reignEnd is not defined, or in the future: ```reigning since (reign start) ((age) years)```