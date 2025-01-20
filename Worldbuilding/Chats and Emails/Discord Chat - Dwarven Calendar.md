[12/5/2023 9:09 PM] rsulfuratus
I think dwarves should have 10 months of 35 days each (divided into 5 weeks of 7 days each)


[12/5/2023 9:10 PM] rsulfuratus
then, three 5-day intercalary "months"


[12/5/2023 9:11 PM] rsulfuratus
or maybe 5 3-day


[12/5/2023 9:11 PM] rsulfuratus
actually five 3-day intercalary periods is better. between every other month you have a 3-day transition


[12/5/2023 9:12 PM] .deciusmus
sounds reasonable


[12/5/2023 9:12 PM] .deciusmus
the age calculation is annoying. If you have bare years, it is one day off


[12/5/2023 9:12 PM] rsulfuratus
so the whole thing is super regular. The first day of the year is also always the same day of the week because you have exactly 35 weeks in a year

[12/6/2023 9:47 AM] rsulfuratus
working seriously on calendar eras here: https://docs.google.com/document/d/1anb-F8574X5BJbA4o1oeSRIuNveaXB--u21Owbd9LTA/edit?usp=sharing


[12/6/2023 9:48 AM] rsulfuratus
just have bits of 10-15 minute chunks throughout the day so will be pretty fragmentary for a while


[12/6/2023 12:18 PM] .deciusmus
For dwarven calendar what about no months?

Each 73 day cycle has 7 named days (one for each thuhr) and 6 11 day weeks spaced Roman style like

Ruler day - 11 days - Traveller day - 11 days - etc 

Where the 1st and last day are both named


[12/6/2023 12:18 PM] .deciusmus
Dates are cycle + counting towards next names day (like Roman kalends/nones/ides)


[12/6/2023 12:19 PM] .deciusmus
Conventionally the middle day of each week is rest/market day


[12/6/2023 12:20 PM] .deciusmus
(And maybe you name the days like:
X
1 day after X
2 day after X
3 day after X
4 day after X
5 day after X
Between X and Y
5 day until Y
…
Y


[12/6/2023 12:22 PM] rsulfuratus
That is interesting


[12/6/2023 12:22 PM] rsulfuratus
I was kind of going for a slightly Mayan system with cycles-within-cycles-within-cycles


[12/6/2023 12:24 PM] .deciusmus
Right. But the math of cycles in cycles in cycles is rough, as 73 is prime


[12/6/2023 12:27 PM] .deciusmus
So either you have a year is 5 cycles of 73, and the cycles inside 73 are messy, or you have to use something other than 365 for your big cycles


[12/6/2023 12:29 PM] .deciusmus
I think if you want cycles-in-cycles-in-cycles I'd have the intercalendary days outside of the nested cycle


[12/6/2023 12:30 PM] .deciusmus
i.e. have something like

big cycle is 360 days with 10 blocks of 36 each with 6 blocks of 6 or whatever


[12/6/2023 12:30 PM] .deciusmus
but obviously that is a lot harder to code as the inner cycles move around through the year


[12/6/2023 12:30 PM] .deciusmus
although they don't if you add "out of cycle" days


[12/6/2023 12:30 PM] .deciusmus
(which is how the mayans did it)


[12/6/2023 12:31 PM] rsulfuratus
so i had messed around with two intersecting cycles: 10 weeks per month, 5 months per year
3 extra days per month, 15 extra days per year


[12/6/2023 12:31 PM] rsulfuratus
the extra days count from 1 to 300


[12/6/2023 12:31 PM] rsulfuratus
so every time the extra days start over at 1, you have a 20 year cycle


[12/6/2023 12:32 PM] rsulfuratus
this is strongly inspired by the mayan calendar round


[12/6/2023 12:34 PM] rsulfuratus
with the mayan long count equivalent to the dwarven count of hours


[12/6/2023 12:34 PM] rsulfuratus
but you could also do it without intercalary days by not sticking with a 7 day week


[12/6/2023 12:35 PM] .deciusmus
right what is interesting about the mayan calendar is 2 different ways of counting (reading wikipedia now) that intersect


[12/6/2023 12:36 PM] rsulfuratus
i was trying to go for the same feeling, but simpler to translate


[12/6/2023 12:36 PM] .deciusmus
i.e the 260 day cycle + the 365 day cycle


[12/6/2023 12:38 PM] rsulfuratus
rather than each day having two names that cycle (one per year and one per less-than-year), you have the day/year combo be unambiguous, but the years themselves cycle based on the intercalary day names


[12/6/2023 12:39 PM] rsulfuratus
the strictly mayan style is a bit annoying for dwarves since we want CY years to exist and be equal in length to DR years (both 365 days). whereas my understanding of the mayan calendar is you don't have year numbers


[12/6/2023 12:40 PM] .deciusmus
right the mayan long count is just days in base 20


[12/6/2023 12:47 PM] .deciusmus
what about

Cycle = 73 days = 5 per year
Each cycle has 36 days / middle day / 36 days
Each 36 day period is divided into 5 7 day weeks, with another middle day in between.

So the calendar goes

Cycle 1/partA/week1 - Cycle1/partA/week2 - middle day - Cycle1/partB/week3 - Cycle1/partB/week4 - middle middle - etc

Which, I think, is exactly what you proposed


[12/6/2023 12:47 PM] .deciusmus
But I'm not sure I'd think about names for "part a" and "part b"


[12/6/2023 12:48 PM] .deciusmus
I'd create names for the 5 cycles, and names for the days of the week


[12/6/2023 12:49 PM] .deciusmus
then I'd use roman style naming:

14 days before 1st middle day
13 days...
1st middle day
14 days before middle middle
13 days before middle middle
middle middle
14 days before last middle
13 days before last middle..

etc


[12/6/2023 12:49 PM] .deciusmus
or split like to use days before / days after


[12/6/2023 12:50 PM] .deciusmus
14 days before 1st middle
...
1st middle
1 day after 1st middle
7 days after 1st middle
7 days before middle middle
...
middle middle
1 day after middle middle.
7 days before last middle
...


[12/6/2023 12:50 PM] .deciusmus
etc


[12/6/2023 12:51 PM] .deciusmus
actually if you had names for the "1 day before... 7 day before" etc


[12/6/2023 12:51 PM] .deciusmus
and had the intercalendary days repeat on a cycle


[12/6/2023 12:51 PM] .deciusmus
the day name would encode the year which might be interesting


[12/6/2023 12:53 PM] rsulfuratus
yeah I think something like this makes sense just need to work out the details


[12/6/2023 12:53 PM] rsulfuratus
the only problem is a 5 week cycle can't have an even. middle point that is between weeks


[12/6/2023 12:54 PM] rsulfuratus
might be better to do two weeks / day / three weeks / day / two weeks day


[12/6/2023 12:55 PM] rsulfuratus
instead of dividing cycle into two parts


[12/6/2023 12:55 PM] .deciusmus
I was thinking a middle week


[12/6/2023 12:55 PM] rsulfuratus
ah that works


[12/6/2023 12:55 PM] .deciusmus
messing around, one sec


[12/6/2023 12:56 PM] rsulfuratus
actually that doesn't quite work. you have 10 weeks plus 3 days in a cycle


[12/6/2023 12:56 PM] rsulfuratus
you could have (2w / 1d / 2w) (1w / 1d / 1w) (2w / 1d / 2w)


[12/6/2023 12:57 PM] rsulfuratus
or you could have (2w / 1d ) (3w / 1d / 3w) (1d / 2w)


[12/6/2023 12:58 PM] rsulfuratus
or you could just have (1 d / 5 wk / 1 d / 5wk / 1d)


[12/6/2023 12:59 PM] rsulfuratus
that is the most symmetric


[12/6/2023 12:59 PM] .deciusmus
but I think for 5 weeks to work it needs a name


[12/6/2023 1:00 PM] .deciusmus
1 d / 5 wk / 1d / 5wk etc is your original proposal


[12/6/2023 1:00 PM] rsulfuratus
a date could be:
year - cycle - (1-2) - (1-5) - (1-7)


[12/6/2023 1:00 PM] .deciusmus
I was trying to layer in some roman idea around counting towards/away from the middle days


[12/6/2023 1:01 PM] rsulfuratus
I think that is better for someone else than dwarves. i like dwarves being kind of mathematical


[12/6/2023 1:01 PM] rsulfuratus
e.g.


[12/6/2023 1:01 PM] rsulfuratus
5881.2.1.5.3 = year 5881, 2nd cycle, 1st part, 5th week, 3rd day


[12/6/2023 1:01 PM] .deciusmus
right, if you add a part it works


[12/6/2023 1:01 PM] .deciusmus
I don't think you need 5 parts


[12/6/2023 1:02 PM] rsulfuratus
sure, you just could days in each cycle/part combo from 1-35


[12/6/2023 1:02 PM] rsulfuratus
rather than counting weeks + day of week


[12/6/2023 1:03 PM] rsulfuratus
although if you have 5 parts nothing ever gets into double digits which is kind of pleasing


[12/6/2023 1:03 PM] rsulfuratus
(except year)


[12/6/2023 1:04 PM] .deciusmus
if you separate out the regularity of the week, I actually think the 36 / 1 could work fine


[12/6/2023 1:04 PM] .deciusmus
you have a sequence of numbered incalendary days from 1 - 300 or whatever


[12/6/2023 1:04 PM] .deciusmus
the date is then

CY 4133 Cycle 1 35 days since day 256


[12/6/2023 1:05 PM] .deciusmus
or 
CY 4133 Cycle 1 24 days after day 256


[12/6/2023 1:05 PM] .deciusmus
or 
CY 4133 Cycle 1 Day 256


[12/6/2023 1:07 PM] .deciusmus
but I guess the problem is that  week is, like in human calendar, not really part of the cycle of anything


[12/6/2023 1:07 PM] .deciusmus
might be nicer for dwarves to have the week be part of something


[12/6/2023 1:08 PM] .deciusmus
but you could have a 6 day week and then do

year.cycle.week.day

with one day each cycle that isn't part of a week


[12/6/2023 1:12 PM] .deciusmus
you could also do

2 weeks / 1 day / 2 weeks / 8 day middle middle week /  2 weeks / 1 day / 2 weeks

which keeps the idea of middles


[12/6/2023 1:17 PM] rsulfuratus
I like the date being year.cycle.(part).(week).day.(extra), and I don't think the dwarves should have a concept of units of time that are outside the cycle


[12/6/2023 1:17 PM] rsulfuratus
e.g. weeks either don't exist or are regular within the cycle


[12/6/2023 1:17 PM] .deciusmus
yeah, I think that makes sense


[12/6/2023 1:18 PM] rsulfuratus
but not sure exactly the correct arrangement of partts/weeks/extra days to make it work


[12/6/2023 1:18 PM] .deciusmus
if you are wedded to a 7 day week, 6 is a nice number


[12/6/2023 1:18 PM] .deciusmus
you get 6 cycles of 6 days in each cycle


[12/6/2023 1:19 PM] .deciusmus
sorry, 12 cycles of 6 days


[12/6/2023 1:19 PM] .deciusmus
or 6 x 6


[12/6/2023 1:19 PM] .deciusmus
but your numbering could be

year.cycle(5/73days).week(12/6 days).day


[12/6/2023 1:19 PM] .deciusmus
with 1 special day per cycle / 5 per year


[12/6/2023 1:20 PM] rsulfuratus
that might work, although i like have a 7 in there somewhere as it seems natural to have something in the cycle associated with gods


[12/6/2023 1:20 PM] rsulfuratus
the outer cycle has to be 5 to get 5*73


[12/6/2023 1:21 PM] rsulfuratus
so the 7 probably needs to be in the 73


[12/6/2023 1:21 PM] rsulfuratus
unless the gods are part of the extra day rotation


[12/6/2023 1:21 PM] .deciusmus
you can get 7 extra days per month if you have 11 weeks of 6 days


[12/6/2023 1:22 PM] .deciusmus
"month = 73 day cycle"


[12/6/2023 1:22 PM] .deciusmus
(or 6 weeks of 11 days)


[12/6/2023 1:23 PM] .deciusmus
you could have

year.cycle.week(11/6 days each).day(1 of 6)
or
year.cycle.thuhr N

where each god repeats once per cycle, and the N increments once per cycle


[12/6/2023 1:23 PM] .deciusmus
so each year you have 5 traveller days, 5 ruler days, etc


[12/6/2023 1:24 PM] .deciusmus
you each have some akwardness where the days get inserted, or they need to be 6 weeks of 11 not 11 weeks of 6


[12/6/2023 1:26 PM] rsulfuratus
have meetings until 4 but will think on this a bit. definitely think the right option is somewhere in here


[12/6/2023 1:26 PM] .deciusmus
yeah, i need to go do some work as well


[12/6/2023 1:28 PM] .deciusmus
you could have

Thurhday - 2 weeks - Thuhr day - 2 weeks - Thurh day - 2 weeks - Thurday - 2 weeks - Thurh day - 2 week  - Thurday - 1 week - Thurday


[12/6/2023 1:29 PM] .deciusmus
it gives you one week per cycle (5 per year) which is close to 2 thuhr days


[12/6/2023 1:29 PM] .deciusmus
it gives lots of cycles of 5, which could be interesting, i.e. 5 cycles per year, 5 days to each thuhr per year, 5 "special weeks" per year, etc


[12/6/2023 3:54 PM] rsulfuratus
Here are the various prime factorizations for a 73 day cycle with X extra days:
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


[12/6/2023 3:55 PM] rsulfuratus
The only options I've found that fit a 73-day cycle and also have some kind of 7 somewhere are:
Six 11 day weeks per cycle with seven extra days: d w d w d w d w d w d w d
Ten 7 day weeks with three extra days: d (w w w w w ) d ( w w w w w ) d
Three 21 day months of three 7 day weeks each, with 10 extra days: d ( w d w d w ) d ( w d w d w ) d ( w d w d w ) d


[12/6/2023 3:58 PM] .deciusmus
Yeah I did the same think basically, just slightly more informally


[12/6/2023 3:59 PM] .deciusmus
7 10 day weeks or 11 6 day weeks also work if you are willing to mess about with the symmetry


[12/6/2023 4:00 PM] rsulfuratus
I like either six 11 day weeks with the 7 "thuhr days" inserted between each week, or ten 7 day weeks (each day named after a thuhr/god)


[12/6/2023 4:01 PM] .deciusmus
I personally like the 7 thuhr days


[12/6/2023 4:01 PM] rsulfuratus
yeah I do to


[12/6/2023 4:01 PM] rsulfuratus
*too


[12/6/2023 4:01 PM] rsulfuratus
the only slight hesitation is it is almost too perfect


[12/6/2023 4:02 PM] .deciusmus
Well, you could have 6 day weeks, gives you the odd pattern


[12/6/2023 4:02 PM] rsulfuratus
i like the symmetry in a cycle, I just want an "outer cycle" as well


[12/6/2023 4:02 PM] .deciusmus
oh, you mean the 5x5


[12/6/2023 4:02 PM] rsulfuratus
yeah


[12/6/2023 4:02 PM] rsulfuratus
but you could do 7x7 with the thuhr days


[12/6/2023 4:03 PM] .deciusmus
well, you intersincally have 5 of them per year, right?


[12/6/2023 4:04 PM] .deciusmus
but you mean make the repeating cycle every 35 days


[12/6/2023 4:04 PM] .deciusmus
i.e. Ruler 35 -> Ruler 1


[12/6/2023 4:04 PM] .deciusmus
so you have a 7 year cycle of thuhr days layered on top of the year


[12/6/2023 4:04 PM] rsulfuratus
right


[12/6/2023 4:05 PM] rsulfuratus
well, something like that


[12/6/2023 4:06 PM] rsulfuratus
can tune the repeat unit of the outer cycle to get something longer or shorter


[12/6/2023 4:06 PM] .deciusmus
so would dates be: year.cycle.day? Or year.cycle.week.day


[12/6/2023 4:06 PM] rsulfuratus
I'd do the latter


[12/6/2023 4:07 PM] rsulfuratus
with day 0 being the intercalary day


[12/6/2023 4:07 PM] rsulfuratus
athought that doesn't quite work because there is one more intercalary day than weeks


[12/6/2023 4:07 PM] .deciusmus
so either year.(name of cycle).(number of week).(number of day) or year.(name of cycle).ruler 35


[12/6/2023 4:07 PM] rsulfuratus
right yeah that works


[12/6/2023 4:08 PM] rsulfuratus
can tweak the exact representation but something like that


[12/6/2023 4:08 PM] .deciusmus
Which basically means for names just need to make up the names of the 5 cycles


[12/6/2023 4:09 PM] rsulfuratus
might just call them dwarven word for first, second, third


[12/6/2023 4:09 PM] rsulfuratus
etc


[12/6/2023 4:09 PM] .deciusmus
It seems like 

year 5122, 2nd month, 3rd week, 11th day is a little short on names?


[12/6/2023 4:09 PM] .deciusmus
but maybe its ok


[12/6/2023 4:10 PM] rsulfuratus
I mean like november, december except in fake dwarvish


[12/6/2023 4:10 PM] rsulfuratus
so they'd have names, the names just mean first month, second month, etc when translated


[12/6/2023 4:10 PM] .deciusmus
right, I'm projecting into dwarvish


[12/6/2023 4:11 PM] .deciusmus
I guess you could have weekday names on top of the cycle


[12/6/2023 4:11 PM] .deciusmus
i.e. what does a dwarf say to his friend, let's meet next Thirdday?


[12/6/2023 4:11 PM] .deciusmus
that works for me, but then I wonder if you want names for months


[12/6/2023 4:12 PM] rsulfuratus
you probably need names of the week because next eleventhday sounds weird


[12/6/2023 4:12 PM] rsulfuratus
or maybe it is just "1 after ruler, 2 after ruler" etc


[12/6/2023 4:12 PM] rsulfuratus
e.g. roman style


[12/6/2023 4:12 PM] .deciusmus
right, actually that works


[12/6/2023 4:16 PM] rsulfuratus
maybe this:
Ruler
1 after ruler
2 after ruler
3 after ruler
4 after ruler
5 after ruler
Ruler midweek
5 before priest
4 before priest
3 before priest
2 before priest
1 before priest
Priest


[12/6/2023 4:18 PM] rsulfuratus
the only slighty asymettric bit is that there are two thuhr days in a row between one cycle and the next, so there is one thuhr, which ever is last, that never gets the "after" days


[12/6/2023 4:18 PM] .deciusmus
the other point I guess is that the romans used these instead of day #, not instead of names for days of the week


[12/6/2023 4:19 PM] .deciusmus
ie. Friday the 6th kalends


[12/6/2023 4:19 PM] rsulfuratus
yeah


[12/6/2023 4:20 PM] rsulfuratus
but probably no need to actually make up dwarven weekday names


[12/6/2023 4:22 PM] rsulfuratus
on the other hand I could see no real need for days of the week names in dwarven. maybe within each cycle you'd just say 2.6 or 3.4


[12/6/2023 4:23 PM] rsulfuratus
maybe the middle day of the week has a special name and conventionally the thuhr days and the middle days are rest days


[12/6/2023 4:24 PM] .deciusmus
I mean, for the purposes of calendars and dates, I think it doesn't matter. 

A CY date is

Year.(Month, named, maybe "Firstember style").number.number OR
Year.(Month, named, maybe "Firstember style").thuhr number


[12/6/2023 4:24 PM] rsulfuratus
if you wanted to invent dwarven day names they could be dervied from something like 5 before, 4 before, on, 1 after, 2 after


[12/6/2023 4:24 PM] .deciusmus
where the dots are not intended to be necessarly the separator


[12/6/2023 4:25 PM] rsulfuratus
right although the number after the thuhr is not needed to uniquely specify a day w/i a year


[12/6/2023 4:25 PM] rsulfuratus
it just specifies a year within a 7 year cycle


[12/6/2023 4:26 PM] .deciusmus
yeah


[12/6/2023 4:26 PM] .deciusmus
I guess whether the style is

year.named month.thuhr
year.named month.thuhr number
or just
year.thuhr number

is up for grabs. They all uniquely specify a date


[12/6/2023 4:27 PM] rsulfuratus
still going to think on this a bit, but I think this is the basic framework. not 100% sure about the thuhr number yet. feels like with thuhr days you kind of already have a nice concept that doesn't need the extra cycle tacked on


[12/6/2023 4:28 PM] .deciusmus
sure, year.named month.thuhr could be were it lands


[12/6/2023 4:30 PM] .deciusmus
Zekaf
Nunaf
Gemaf
Ramekaf
Gamekaf

strawman month names based on this https://thedwarrowscholar.tumblr.com/post/171797132184/hi-im-just-wondering-how-you-say-numbers1-10-in and this https://annwn-dnd.fandom.com/wiki/Dwarrow_Calendar

{Embed}
The Dwarrow Scholar
https://thedwarrowscholar.tumblr.com/post/171797132184/hi-im-just-wondering-how-you-say-numbers1-10-in
The Dwarrow Scholar
Hi I'm just wondering how you say numbers(1-10) in khuzdul?
Well met!
Here’s a handy little overview of the cardinal numbers from zero till ten.
And some extra information on the matter concerning...
https://images-ext-1.discordapp.net/external/sBGjmnT2cCfZNlYIgki3gJrteGeVUftAZB4Yn9ufbkQ/https/64.media.tumblr.com/4b09dc085aa95a2df0a773c4979f7292/tumblr_inline_p5hga9ODGs1tcuw0n_500.png

{Embed}
https://annwn-dnd.fandom.com/wiki/Dwarrow_Calendar
Dwarrow Calendar
The calendar of the Kingdom of Rhoane, as laid out by the dwarven founders. Month 1 “‘âfdohyar” Holidays: 1) Ghiluz Durin (Durin’s Day) – 1st of ‘âfdohyar —- 2) gwivashazdînmerag (Treasures of the...
https://images-ext-1.discordapp.net/external/8Pt7vDBFlQwZCcDQg05P2MjnDvfnlVoGWfDAiUjVlIs/%3Fcb%3D20210713142711/https/static.wikia.nocookie.net/ucp-internal-test-starter-commons/images/a/aa/FandomFireLogo.png/revision/latest


[12/6/2023 8:55 PM] .deciusmus
are you messing around with code at all?


[12/6/2023 8:55 PM] rsulfuratus
no


[12/6/2023 8:55 PM] .deciusmus
i was making a stab at error bars for dates


[12/6/2023 8:55 PM] .deciusmus
But was piggybacking on your dwarf stuff


[12/6/2023 8:56 PM] rsulfuratus
i'm not likely to do any coding work until after my game on Sunday, so go wild


[12/6/2023 9:00 PM] .deciusmus
DR 1/1/1 is supposed to be March 16, 4133 right? Which would be 75th day?


[12/6/2023 9:00 PM] rsulfuratus
March 17th


[12/6/2023 9:00 PM] rsulfuratus
well, actually, no


[12/6/2023 9:00 PM] .deciusmus
so the 76th day of 4133?


[12/6/2023 9:00 PM] rsulfuratus
that's backwards


[12/6/2023 9:01 PM] rsulfuratus
1/1/4133 is march 17, dR 1


[12/6/2023 9:01 PM] .deciusmus
right so 1/1 DR is a late date in 4132


[12/6/2023 9:01 PM] rsulfuratus
yes


[12/6/2023 9:02 PM] rsulfuratus
the code i pushed last night gets the conversion correct from years since creation


[12/6/2023 9:03 PM] rsulfuratus
3-17-1749 should be 1-1-5882


[12/6/2023 9:03 PM] rsulfuratus
3-17-1748 should be 1-1-5881


[12/6/2023 9:04 PM] rsulfuratus
Etc


[12/6/2023 9:06 PM] .deciusmus
but it seems to be reporting CY 4133-08-35.2 for DR 1 / 1/ 1


[12/6/2023 9:06 PM] rsulfuratus
Hmm


[12/6/2023 9:06 PM] rsulfuratus
Maybe I messed something up


[12/6/2023 9:06 PM] rsulfuratus
I was testing with jsfiddle and it was correct


[12/6/2023 9:07 PM] rsulfuratus
What does report for DR 1748-3-17


[12/6/2023 9:07 PM] .deciusmus
5881.1.1


[12/6/2023 9:07 PM] .deciusmus
it gets that right


[12/6/2023 9:08 PM] rsulfuratus
So yes I think I got the year drankor was founded wrong then


[12/6/2023 9:08 PM] .deciusmus
are you sure the year isn't just off by 1


[12/6/2023 9:09 PM] rsulfuratus
Well the year for 1748 is correct


[12/6/2023 9:09 PM] rsulfuratus
Don’t know how it could get one year wrong and another right


[12/6/2023 9:09 PM] .deciusmus
because year 1 doesn't count


[12/6/2023 9:10 PM] .deciusmus
there is no year zero


[12/6/2023 9:10 PM] rsulfuratus
Ah hmm maybe


[12/6/2023 9:10 PM] .deciusmus
so the dates of 4133 and 5881 can't both be correct


[12/6/2023 9:10 PM] .deciusmus
there is 1 too many years in between them


[12/6/2023 9:11 PM] .deciusmus
because the years are counted inclusive of 1, i.e. year 2 is actually only 1 year old, so to speak


[12/6/2023 9:11 PM] .deciusmus
yeah, there are 1748 years between 4133 and 5881 but only 1747 years between 1 and 1748


[12/6/2023 9:15 PM] .deciusmus
easiest to just say Drankor was founded in late 4133 instead of late 4132


[12/6/2023 9:16 PM] rsulfuratus
That is what I meant


[12/6/2023 9:16 PM] rsulfuratus
When I said I got the date wrong


[12/6/2023 9:17 PM] .deciusmus
right
