# Calendar System Brainstorming: Final Text and Comments

Source: Google Drive document ID 1anb-F8574X5BJbA4o1oeSRIuNveaXB--u21Owbd9LTA
Document revision: `ANLCKQm2Hrb1iX-wxq8kEIOozB475VXM_R2A6E_ZhkC3GBPWyzpdJLK8uAmXCSjV2DbfQqAxA-ccSHsdnnGXyw`
Extracted: October 1, 2026

This is source material, not a statement of current canon. Struck-through source text is retained with its strikeout formatting removed. Literal angle-bracket source text appears as Markdown strikeout, and literal square-bracket source text appears in parentheses.
The comment archive preserves 2 open comment threads; no replies.

---
Working seriously on different calendar systems for Taelgar. Major focus is on the dwarven calendar (CY = count of years) as the “fully robust official count of days since time began” and the human Drankorian calendar as the “easiest to intuitively use human calendar as it most closely tracks real world calendar.” Some focus on elves and halflings and variant human calendars.

## Non-human calendars

### Dwarven Calendar

The dwarven calendar is fundamentally a count of hours since time began – dwarves are basically the Linux system clock.

However, practically this is not useful, so time is divided into repeating cycles.

24 hours is a day (7 days is a week but these don’t cycle precisely)

73 days is a cycle (probably needs a better name).

5 cycles is a year.

Each cycle is divided into two parts of 5 weeks each 10 weeks of 7 days, plus 3 extra days that are not part of any week

The 10 weeks of a cycle are often conventionally grouped into two subcycles of 5 weeks each, which is relatively close to human months, and then the 3 intercalary days.

Naming is probaby something like:

Cycle Name - 1 or 2 for month - week name - day

So you need names for:

5 cycles in a year

2 parts in a cycle (these repeat, so you have cycle 1 part A, cycle 2 part A, etc)

Potentially each week (5) in a part could have a unique name but this is probably unneeded

Seven days of the week

The intercalary days counting from 1 to 300, perhaps?

The 5 sets of 3 intercalary days also cycle in large units, maybe in a cycle of 300, so that every 20 years you start a new set of counting the intercalary days? That could make 20 years kind of like a decade in dwarven counting, and then perhaps a cycle of 7 “decades” = 140 years is kind of like a century, and then every 10 “centuries” is something else.

(dwarves also have units for cycles of many years, but these are less important for calculations and usually just the plain year is sufficient)

Basic calculation is:

Divide days by 365 to get years

Divide remainder by 73 to get cycles

If remainder is  70, you are part 2 week 5 + 1-3 intercalary days

If remainder is = 70, divide by 35 to get part

Remainder divide by 7 to get week

Remainder is day of the week.

===

For a 73 day cycle, some notes on prime factorizations:

1 extra day gives 72, which divides to 2 x 2 x 2 x 3 x 3

2 extra days gives 71 (prime not useful)

3 extra days gives 70, which divides to 2 x 5 x 7

4 extra days gives 69, which divides to 3 x 23

5 extra days gives 68, which divides to 2 x 2 x 17

6 extra days gives 67 (prime not useful)

7 extra days gives 66, which divides to 2 x 3 x 11

8 extra days gives 65, which divides to 5 x 13

9 extra days gives 64, which divides 2 x 2 x 2 x 2 x 2 x 2

10 extra days gives 63, which is 3 x 3 x 7

==

Some options that are symmetric and have a 7 somewhere:

Six 11 day weeks per cycle with seven extra days: d w d w d w d w d w d w d

Ten 7 day weeks with three extra days: d (w w w w w ) d ( w w w w w ) d

Three 21 day months of three 7 day weeks each, with 10 extra days: d ( w d w d w ) d ( w d w d w ) d ( w d w d w ) d

Some options that are symmetric but without a 7:

Three 23 day months per cycle with four extra days: d m d m d m d

Four 17 day months per cycle with five extra days: d m d m d m d m d

====

Six 11 day weeks per cycle with seven extra days: (d w d w) (d w d w) (d w d w) d

### Elven Calendar

Elves fundamentally simply count ka. Nothing is really super-fixed within a ka, but ka are very regular. I kind of feel there is maybe something a bit fey here? Like the elves care more about the cycles of extraplanar energy and the waxing and waning of Aldanor’s influence than the sun. Maybe even call parts of each cycle Aldanor waxing or Elmerica waning. In some sense years are probably more analogous to months for humans, seasons are weeks,and there is no real sense of anything between a day and a season as being important to track.

### Halfling Calendar

## Human Calendars

Hkar

50 weeks of 7 days, with a year running from Jan 7th - Dec 23rd (in the Drankorian months), followed by a 15 day winter in between each year.

In Drankor, the intercalary winter is dropped, but the Pyravela celebration is retained, so you get the year started on Jan 1st (which becomes Jan 1st)

Notes from Discord:

Say that the Hkar calendar was 50 weeks, running Jan 7th - Dec 23rd, which 15 day "winter" outside the calendar, of which Pyravela is the 3 day "middle"

so you have the year,  then 6 days, then pyravela, then 6 days, then the year repeats

rsulfuratus — Today at 9:08 PM

that actually has a nice symmetry to it

although on Hkar the entire 15 days would have ritual significance, only the middle part has been retained

Deciusmus — Today at 9:09 PM

right

rsulfuratus — Today at 9:09 PM

I kind of think the traveler holidays (leave taking and home coming) might date to drankor, not Hkar

Deciusmus — Today at 9:09 PM

yeah, I was thinking that as wel

rsulfuratus — Today at 9:09 PM

only problem is that Drankorian year starts on Jan 1 not Jan 7th

Deciusmus — Today at 9:10 PM

right but that makes sense

the intercalendary dates are not retained

rsulfuratus — Today at 9:10 PM

right of course

Deciusmus — Today at 9:10 PM

and it is perfectly logical, I think (or at least, not particularly weird) to -- if pyravela is what is retained -- have that be the end of the year

rsulfuratus — Today at 9:10 PM

yeah that actually works really well

Deciusmus — Today at 9:11 PM

so it isn't so much that Drankorian calendar starts on Jan 1, it is that it starts the day after Pyravela, which appens to be Jan 1

I mean, the Hkaran people wouldn't have said "our calendar starts on the 7th". It starts on the 1st, obviously 🙂

rsulfuratus — Today at 9:11 PM

sure

Deciusmus — Today at 9:12 PM

It's just that the Drankorians keep pyravela as the end of year, which is why on the "modern" calendar all the ancient holidays are 7 days later than they "should" be

## Google Docs comments

### 1. Open · AAABB4ZNtds

**Original selection:**
> practically this is not useful,

**Context in current document:** However, practically this is not useful, so time is divided into repeating cycles.

Google anchor: `kix.nca5ypkydic3`

**Mike Sackton** · 2023-12-06T16:52:29.659Z

This seems engineered to 
(a) feel different but
(b) still work pretty well with conventional human calendar

Is it worth considering what it might look like given the bare physical fact of 365 day years / 24 hour days but no attempt at connection to human weeks or months?

(That said, I just realized 73 is prime, so the only even cycles you can get are in fact 5 cycles of 73, so maybe this is best)

### 2. Open · AAABB4ZNtdg

**Original selection:**
> e dwarven calendar is fundamentally a count of hours since time began

**Context in current document:** The dwarven calendar is fundamentally a count of hours since time began – dwarves are basically the Linux system clock.

Google anchor: `kix.gvijxmszpouk`

**Mike Sackton** · 2023-12-06T16:49:12.564Z

Does this imply some dwarven city somewhere actually has a clock measured in "hours since time began"? i.e. do dwarves think in these terms?

(I sorta think they should, sometimes.)
