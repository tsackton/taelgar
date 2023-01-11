### getRegnalValue(tp)

**FrontMatter used**
* `reignEnd` (optional)
* `died` (optional, used in place of `reignEnd` if `reignEnd` is not specified)
* `reignStart` (required)
* `yearOverride` (used for testing, to set the current year)

This returns the reigning years for a monarch. It requires reignStart and returns empty if missing. reignEnd is optional, and if not specified, died will be used instead.

If currently reigning (because the reignEnd is in the future or not specifed) will return a string like: `"reigning since " + yearStart + " (" + reignLength + " years)"`

If the reign ended in the past (because reignEnd is in the past or died is in the past), it will return a string like: `"reigned " + yearStart + " - " + yearEnd + " (" + (yearEnd-yearStart) + " years)"`

If the reign start is in the future, it will return an empty string.

Usage (without the spaces)
```
< % + tp.user.getRegnalValue(tp) % >
```

### getAgeBasedValue(tp, strings)
**FrontMatter used**
* `born` 
* `died` 
* `built`
* `destroyed`
* `created`
* `yearOverride` (used for testing, to set the current year)

At least one of `born`, `died`, `created`, `built`, `destroyed` must be provided.

This calculates a "page status" that takes into account the starting and ending date of the page.  

If the born, built, or created date is after the destroyed or died date it fails.

It generates one of the following strings:
* A lifetime string, returned when there is a
	* born, built, or created date before the current date
	* died or destroyed date before the current date
	* Format: `startPrefix yearStart - endPrefix yearEnd at age age`
* A not-yet-existing string, returned when there is a
	* born, built, or created date after the current date
	* Any or no died or destroyed date
	* Format: `preExistError`
* A dead string, returned when there is
	* No born, built, or created date
	* died or destroyed date before the current date
	* format: `endPrefix yearEnd`
* An alive string, returned when there is
	* A born, built, or created date before the current date
	* No died or destroyed date OR a died or destroyed date after the current date
	* Format: `startPrefix yearStart (age years old)`

The string formats can be controlled via a strings parameter, which is JSON object with three properties:
* `preExistError` default `(not yet born)`
* `startPrefix` default `b.`
* `endPrefix` default `d.`

Usage (with defaults)
```
< % + tp.user.getAgeBasedValue(tp) % >
```

Usage (with overrides)
```
< % + tp.user.getAgeBasedValue(tp, {endPrefix: "petrified"}) % >

< % + tp.user.getAgeBasedValue(tp, {preExistError: "(not yet created)", startPrefix: "created", endPrefix: "destroyed"}) % >
```

### getCampaignBasedValue(tp. name)
This returns the value of the named frontmatter item, but if there is a campaign specific override it uses it.

For example if you wanted to have a population for a town, it could be done like:

```yaml
population: 1230
population_dufr: 1600
```

Usage 
```
population: < % + tp.user.getCampaignBasedValue(tp, "population") % >
```

This will return 1230 for my campaign and 1600 for yours.

To set the campaign value create a file in your .obsidian folder called taelgarConfig.json with the following contents:

```json
{
  "campaignPrefix": "clee"
}
```