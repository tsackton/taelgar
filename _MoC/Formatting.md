This documents some expectations around formatting to align Javascript and Python.

Most text is output as plain text. There are two areas where we have a bit more complexity.

### Whereabouts Location.
A whereabouts location is a two-part element with a place and a region. Either one or both are set. The expected format for a whereabouts location is to split the place by comma, and rejoin the place and region as:
```
each, piece, of, the, split, region
```

Where any part of each, piece, of, the, split, region that represents a file under Gazetteer should be linked.

### Dates
Dates are in one of 3 forms: YYYY, YYYY-MM or YYYY-MM-DD. Ideally they would be formatted as:
* YYYY: YYYY DR (in the future, we plan to support CY format as well)
* YYYY-MM: MonthName YYYY
* YYYY-MM-DD: MonthName Day, YYYY

MonthName should ideally be the month from Fantasy Calendar, in case we rename them. But at the moment it could be the English month