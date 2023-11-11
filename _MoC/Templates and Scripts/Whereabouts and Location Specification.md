This is the new specification for whereabouts. Note that the intention here is to assume sensibility on the author of the metadata, so undefined cases (i.e. multiple events with the same dates) might have unpredictable results.

Whereabouts is YAML list with the following format:

```yaml
whereabouts:
 - { start: date or blank, end: date or blank, place: string, region: string, type: away or home }
```

* If the type is away at least the start date is expected to be specified and undefined behavior might occur (such as Javascript errors) if this is not specified.
* If the type is home, one of place or region must be specified, and undefined behavior might occur (such as Javascript errors) if this is not specified.
* Dates can be in the format YYYY, YYYY-MM, or YYYY-MM-DD

**PROPOSED**
Whereabouts is YAML list with the following format:

```yaml
whereabouts:
 - { start: date or blank, end: date or blank, location: string, type: away or home }
```
* If the type is away at least the start date is expected to be specified and undefined behavior might occur (such as Javascript errors) if this is not specified.
* If the type is home, one of place or region must be specified, and undefined behavior might occur (such as Javascript errors) if this is not specified.
* Dates can be in the format YYYY, YYYY-MM, or YYYY-MM-DD

**END**


This whereabouts YAML is then structured to generate the following logical pieces of information:

* A last known location. This is where an person "last was", based on a defined date. 
* A current location. This is where a person currently is. 
* A home location. This is where a person is based. 
* An origin location. This is where a person is from

For each of these types of locations we define the value and an output flag.

These are generated as follows:

Terms: 
* *logical end date* is the start date if the end date is undefined, otherwise the start date

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
	* If there are multiples reduce the set to all of the items with the latest start date that is before the target date. An unset start date should be treated as the earliest possible date
	* If there are still multiples (because multiple items have the same or blank start date), take the one that is lexically last in the yaml
	* If there are no items, the "home whereabouts" is undefined
* Find the "last known whereabout"
	* Candidate set = Take all of the whereabouts where type = away
		* Start is before or equal to target
	* If there are multiples, take start date that is closed to the target date
* Find the "origin whereabout"
	* Candidate set = Take all of the whereabouts where type = home and start = undefined
	* If there are multiples, select the lexically first one in the yaml

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