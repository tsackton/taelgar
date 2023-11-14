## Whereabouts Handling, Take 2

A whereabouts entry consists of four parts:
- a type, which can be home or away
- a start, which is any date, an empty string, or a null/None value
- an end, which is any date, an empty string, or a null/None value
- a location, which is any string, which can be empty, or a null/None
  
A whereabouts entry must have a type.
A whereabouts entry with a type of away must have a start that is a valid date.

Given a whereabouts and a target date two additional values are calculated - imputed start, imputed end. We also assume that born and died may exist or may be undefined. 

We assume unless otherwise specified that all dates are passed to a clean_date function, with an end parameter. When dates are passed with end=False, the earliest valid date consistent with a partial representation is returned. When dates are passed with end=True, the latest valid date consistent with a partial representation is returned.

born and died are computed as: 

Imputed_start:
- for type home, the imputed start is equal to the earliest possible date derived from born, or a generic earliest possible date if born is undefined, and the imputed end is equal to the target date, or the died date if it exists
- for type away, imputed start is always equal to start, which must be provided. if start is YYYY or YYYY-MM, imputed start should be the earliest valid month/day
- for type away, imputed end is always equal to imputed_start

1. An origin whereabouts is defined as the earliest 'home' location, where earliest is defined as the smallest imputed start.
	- if multiple home locations have the same imputed start, the lexicographically first home is considered the origin whereabouts.
	- if born is defined and imputed_start > born, origin whereabouts is "unknown"
	- if born is not defined but imputed_start > target date, origin whereabouts is "unknown" (if born is defined and born > target_date, preExistError should trigger so whereabouts does not need to handle this)

2. A home whereabouts is defined as the valid home location with the shortest duration between imputed start and target date.
	- A valid home location is a home location where imputed end >= target date
	- If there are multiple valid home locations with equal duration between imputed start and target date, the lexicographically last home is considered the home whereabouts.
	- If there are no valid home locations, home is unknown. Note if you want a defined origin and an unknown home, you must have only home locations with real end dates < target date in the whereabouts. 

Examples:

```yaml
born: 1450
{ type: home, start: , end: , location: origin}
{ type: home, start: 1500, end: , location: home}
```
```yaml
born: 1450
{ type: home, start: , end: , location: origin}
{ type: home, start: 1500, end: , location: home}
```
After 1500, this should generate "origin" / "home"
Before 1500, this should generate "origin" / "origin"

```yaml
born: 1450
{ type: home, start: 1475, end: 1499, location: first home}
{ type: home, start: 1500, end: , location: home}
```
After 1500, this should generate "unknown" / "home"
Between 1475-1500 , this should generate "unknown" / "first home"
Before 1475, this should generate "unknown/unknown"

```yaml
born: 
{ type: home, start: 1475, end: 1499, location: first home}
{ type: home, start: 1500, end: , location: home}
```
After 1500, this should generate "first home" / "home"
Between 1475-1500 , this should generate "first home" / "first home"
Before 1475, this should generate "unknown/unknown"

```yaml
born: 1450
{ type: home, start: 1475, end: , location: home}
{ type: home, start: , end: , location: origin}
```
Before 1475 this should generate "origin/origin" 
After 1475 this should generate "origin/home"

```yaml
born: 1450
{ type: home, start: , end: , location: origin}
{ type: home, start: , end: , location: home}
```
This should generate "origin/home" for all valid dates (>1450)


1. A current whereabouts is defined as the valid current location with the shortest duration. A valid current location is determined by the following algorithm:
	- if there are no away lines in the whereabouts, the only valid current location is the home location, which might be unknown
	- if there are away lines, the list of valid current locations is the set of away locations where imputed start <= target_date <= imputed_end
	- if the list of valid current locations is empty, then the current whereabouts is set to unknown if real end is undefined, and home otherwise
	- if the list of valid current locations is not empty, then the current whereabouts is set to the valid location with the shortest duration (imputed_end - imputed_start)

2. A last know whereabouts is defined as the valid current location with the shortest duration, defined as imputed_end - target_date. A known location cannot be unknown. A known location is determined by the following algorithm:
	- if the current whereabouts is not unknown, the last known whereabouts is the current whereabouts, and the last known date is the target date
	- if the current whereabouts is unknown, determine the last known location as follows if there is at least one away line:
		- the last known location is the away lines where imputed_start <= target_date and with the shortest duration between imputed_end and target_date
		- if there are multiple valid last known locations, the one with the shortest duration (imputed_end - imputed_start) is preferred
		- if there are multiple valid last known locations with the same duration, the one lexigraphically last in the file is preferred
		- the last known date is defined as the imputed_end of the last known location
	- if there are no away lines, for example because home is unknown (e.g. there is an origin, but no known home), the last known location is the origin, and the last known location date is the origin end date

**For discussion:**

If there is a died date in the metadata, this will also override the target date. Or is there a better way to handle dead people?


## Whereabouts Handling, Take 1



This is the new specification for whereabouts. Note that the intention here is to assume sensibility on the author of the metadata, so undefined cases (i.e. multiple events with the same dates) might have unpredictable results.

Whereabouts is YAML list with the following format:

```yaml
whereabouts:
 - { type: away or home, start: date or blank, end: date or blank, location: string }
```
* If the type is away at least the start date is expected to be specified and undefined behavior might occur (such as Javascript errors) if this is not specified.
* If the type is home, one of place or region must be specified, and undefined behavior might occur (such as Javascript errors) if this is not specified.
* Dates can be in the format YYYY, YYYY-MM, or YYYY-MM-DD

This whereabouts YAML is then structured to generate the following logical pieces of information:

* A last known location. This is where an person "last was", based on a defined date. 
* A current location. This is where a person currently is. 
* A home location. This is where a person is based. 
* An origin location. This is where a person is from

For each of these types of locations we define the value and an output flag.

These are generated as follows:

Terms: 
* *logical end date* is the start date if the end date is undefined, otherwise the start date
* *home count* is the number of "home" lines in the whereabouts section ignoring dates

Algorithm:
* Find the "exact known whereabouts". 
	* Candidate set = Take all of the whereabouts with type = away 
		* Start is defined and before or equal to target date
		* Logical end is after or equal to target date
	* If there are multiple items in the candidate set, select the one with the smallest duration between the logic end date and the start date
	* If there are no items, the "exact known whereabouts" is undefined
* Find the "home whereabouts". 
	* Candidate set = Take all of the whereabouts with type = home
		* Start is unset or before or equal to target date and end (not logical end) is after or equal to target date
		* Start is unset or before or equal to target date and end is unset
	* If there is a single value, and the home count is greater than one, and the single value has an undefined start and end date, the "home whereabout" is undefined
		* This spec line is to handle the situation where you have a home with no dates (for the origin) and another home with an end date that is in the past
	* If there is a single value and the home count is one, use it as the home origin
	* If there are multiples sort by start date, then order in the yaml file, and take the last one
	* If the set is empty, "home whereabouts" is undefined
	* Regardless of the rules above, a home whereabouts with a blank location should be considered undefined
* Find the "last known whereabout"
	* Candidate set = Take all of the whereabouts where type = away
		* Start is before or equal to target
	* If there are multiples, take start date that is closed to the target date
* Find the "origin whereabout"
	* Candidate set = Take all of the whereabouts where type = home and start = undefined
	* If there are multiples, select the first one in the yaml

We can then define our 4 location types:

**An origin location** is defined as
	Value: the origin whereabout
	Output: origin whereabout is defined and home is defined but not equal, or the origin whereabout is defined and there is no home whereabout

A **current location** is defined as
	Value: 
		If there is an exact known whereabouts, use that and set the output flag to true
		Otherwise, if there is both a home and last known whereabouts where
		* The last known whereabouts has a defined end and
		* The last known whereabouts end date is in the past compared to the target date
		Then use the home whereabout as the current location and set the output flag to false
		Otherwise, the current location is Unknown and set the output flag to true
	Output: See algorithm above

A **home location** is defined as
	Value: the home whereabouts
	Output: the home whereabouts is defined

A **last known location** is defined as
	Value: the last known whereabouts
	Output: the last known whereabouts is defined and the current location is Unknown


### get_Homewhereabouts

1. Gets the Page Existence Date and the Target Date (see [[Page Dates]])
* If the Page Existence Date  is defined Target Date is before the Page Existence Date, it exits with no output.
2. Calculates the four values above using the Target Date 
3. Sets the "page exists" flag to true if the Page End Date is defined Page End Date is before the Target Date
4. It outputs between 1 and 2 lines.

Line 1: If the origin output flag is true: "Originally from: (origin)"
Line 2: If the home output flag is true, and the page exists flag is true: "Based in: (home)"
Line 2: If the home output flag is true, and the page exists flag is false: "Lived in: (home)"

### get_CurrentWhereabouts
1. Gets the Page Existence Date and the Target Date (see [[Page Dates]])
* If the Page Existence Date is defined and the Target Date is before the Page Existence Date, it exits with no output.
2. Calculates the four values above using the Target Date 
3. Sets the "page exists" flag to true if the Page End Date is defined Page End Date is before the Target Date
4. It outputs between 1 and 2 lines.

Line 1: If the last known location output flag is true, "Last known Location (as of lastknown.date): (lastknown)"
Line 2: If the current location output flag is true, and the page exists flag is true: "Current location (as of target date): (current)"

See [[Formatting]],  [[Whereabouts and Last Seen By Party]] and [[Page Dates]] for more information.