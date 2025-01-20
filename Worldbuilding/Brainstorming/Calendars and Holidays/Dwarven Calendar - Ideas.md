The dwarven calendar is fundamentally a count of hours since time began – dwarves are basically the Linux system clock.

%% Comment from Mike: 
Does this imply some dwarven city somewhere actually has a clock measured in "hours since time began"? i.e. do dwarves think in these terms?  (I sorta think they should, sometimes.)
%%

However, practically this is not useful, so time is divided into repeating cycles.

%% Comment from Mike
This seems engineered to   
(a) feel different but  
(b) still work pretty well with conventional human calendar  
  
Is it worth considering what it might look like given the bare physical fact of 365 day years / 24 hour days but no attempt at connection to human weeks or months?  
  
(That said, I just realized 73 is prime, so the only even cycles you can get are in fact 5 cycles of 73, so maybe this is best)
%%

24 hours is a day (7 days is a week but these don’t cycle precisely)
73 days is a cycle (probably needs a better name).
5 cycles is a year.

Each cycle is divided into two parts of 5 weeks each 10 weeks of 7 days, plus 3 extra days that are not part of any week
The 10 weeks of a cycle are often conventionally grouped into two subcycles of 5 weeks each, which is relatively close to human months, and then the 3 intercalary days.

Naming is probaby something like:

Cycle Name - 1 or 2 for month - week name - day

So you need names for:
* 5 cycles in a year
* 2 parts in a cycle (these repeat, so you have cycle 1 part A, cycle 2 part A, etc)
* Potentially each week (5) in a part could have a unique name but this is probably unneeded
* Seven days of the week

The intercalary days counting from 1 to 300, perhaps?

The 5 sets of 3 intercalary days also cycle in large units, maybe in a cycle of 300, so that every 20 years you start a new set of counting the intercalary days? That could make 20 years kind of like a decade in dwarven counting, and then perhaps a cycle of 7 “decades” = 140 years is kind of like a century, and then every 10 “centuries” is something else. 

(dwarves also have units for cycles of many years, but these are less important for calculations and usually just the plain year is sufficient)

Basic calculation is: 

Divide days by 365 to get years
Divide remainder by 73 to get cycles
If remainder is > 70, you are part 2 week 5 + 1-3 intercalary days
If remainder is <= 70, divide by 35 to get part
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