Trying to brainstorm some ideas about metadata, independent of questions about header formatting.

My basic thought is there are three super-fundamental bits of metadata that are valuable to query:

(a) where a page is in space - whereabouts
(b) things that happened involving a page in time - events
(c) things that are associated with a page - associations

Location and associations are page-dated, that is they can vary with time, but things that happen aren't -- they are time-based already so are fixed in time (it is just display decisions that might depend on page date)

**Events** include things like:
- a person was born
- a city was destroyed
- a battle happened
- an inn burnt down
- a person met another person
- a sword was forged

An event, normally, would have a date and a description; possibly it would have a span (start/end). The date could, theoretically be unknown or approximate, or could be a pointer to another date. For example, a person who died in the Great War but for whom a specific date of death is not known could have something like:

- {date: Great War, event: died } 

This can work even if the "date" page doesn't have dates, although I think properly a date must be either a date string or a page with the event type. But, for example, a person who died during the "Sundering of the Dwarves" could have a date for that event pointing to a page that doesn't itself have known dates. Dates can inherit: if a battle is part of a war, and the battle has no dates, you can inherit the start/end from the war.

**Whereabouts** are *just locations*, always in the form of { start, end, location }. Locations can inherit from other locations, so you get location chains. A location must be a physical place, although a page can be "with" another page (that is an item, person, etc) implying it inherits its location from that page. Locations always have a start and an end, at least implicitly, which are dates. These (probably) have to be explicit date strings, not event pages, although whereabouts should allow both concepts of "indefinite" and "unknown". 

**Associations** include things like:
- the species a person is
- the political unit a city belongs to
- the army a garrison is part of
- the secret society a person is
- the ancestry a person is
- the war a battle is part of

Associations are any relationship like: "X is part of Y", "X is a type of Y", "X is a member of Y", "X is the leader of Y". Could also include things like "X is the father of Y", "X is the friend of Y". Any page can be associated with any other page. 

***Implicit Metadata***
I think one key is this creates a lot of implicit metadata. E.g., if you are born at a location - you specify an event "born" at date X in location Y, that implicitly sets a location for your date of birth to location Y, to the precision with which it is known. If X is the father of Y, then Y is the child of X. 

A key piece of code would likely be to check for inconsistencies in implicit metadata. You'd like to run a templater command that would report an error if there is conflicting implicit metadata, or have some other way to check this, and possibly a way to make it explicit (could lead to long frontmatter). 


***Shorthands***
Another key would be that while internally you might think of a list of associations, whereabouts, and events, you wouldn't, I think, want just three massive lists to set frontmatter (maybe you would). You'd like things like born to be a shorthand, be able to set ancestry and other common associations as a shorthand, etc. 

Need to think about this a bit. 
