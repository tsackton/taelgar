# WhereaboutsManager

This class handles whereabouts data. 

**Normalized whereabouts**
A normalized whereabouts is an object constructed from a whereabouts line, where a whereabouts line is generally understood to be a dict with at least a type, almost always a location, and potentially a start, end, or format, as well as date/excursion from previous versions. 

Backwards compatibility - type:
- whereabouts with type: origin are treated as type: home
- whereabouts with type: excursion are treated as type: away
- whereabouts with excursion: true are treated as type: away

Backwards compatibility - location:
- whereabouts with place: string and/or region: string are treated as location: place, region, location: place, or location: region

*Comment: as far as I can find there are no files for which any of these conditions are true, so I don't think we need to maintain backwards compatibility here.*

A normalized whereabouts always has the following properties: 
- start: a normalized date, defined as start, otherwise date, otherwise undefined
- type: a string, either home or away
- end: a normalized date, defined as end, otherwise undefined
- location: a string, defined as location, otherwise "place, region", otherwise place or region, otherwise undefined
- logicalEnd: a normalized date, defined as end, otherwise maximum possible date
- logicalStart: a normalized date, defined as start, otherwise minimum possible date
- awayEnd: a normalized date, defined as logicalEnd for type home, and end, otherwise start, otherwise maximum possible date for type away
- format: a string, defined as a format string if one exists for this whereabout, otherwise undefined

**Normalized whereabout list**
Any function that works on whereabouts is expected to first generate a normalized whereabouts list using `whereaboutsManager.getWhereaboutsList(metadata)`.

This function takes a metadata object and returns a list of normalized metadata, with the following convenience and backwards compatibility checks:
- if whereabouts exists and is a string, assumes this means { type: home, location: string}
- if the page is a place, and whereabouts does not exist, but partOf does, assume this means {type: home, location: partOf}

*Any other helper/convenience functions for whereabouts processing should presumably go here*

**whereabouts object**

A whereabouts object is created by `whereaboutsManager.getWhereabouts(metadata, targetDate)` and consists of an object with four properties: `current`, `lastKnown`, `origin`, and `home`, each of which define the current, lastKnown, origin, and home whereabouts as of targetDate. Each property is itself a **normalized whereabout** if it contains a known location, or `undefined` if that location is unknown at `targetDate`, except for `lastKnown`, where `undefined` can also mean "identical to current".
- `origin` is defined as the lexically first home whereabout that is valid as of originDate (born/created or dateMin), otherwise undefined
- `home` is defined as the lexically last home whereabout that is valid as of targetDate, otherwise undefined
- `current` is defined as the valid whereabout as of targetDate that is closest to targetDate, with the lexically last selected if multiple whereabouts have equal closeness. 
- `lastKnown` is defined as the current whereabouts, otherwise the last certain location

*It would be more generalizable IMO if undefined always mean "unknown", so lastKnown could never be undefined unless there are no valid whereabouts. For example for a metadata table that displays last known location, it would be a lot easier to just display last known, rather than always have to check last known and get current otherwise. I think it is better to handle the case of "you don't want to show lastknown + current if they are the same" in the header code. *