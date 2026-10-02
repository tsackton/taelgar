# elf birth rate math

## Mike Sackton — January 25, 2021 at 8:48 PM

I was playing around a bit on how the elven population would grow, assuming:

* 160 year generations
* various birth rates & starting pop sizes
* 90% of each generation dies at age ~1200
* 5% of each generation dies at age  ~1400
* the remaining 5% lives forever

How many elves do you envision in Taelgar right now? More than a million? 100,000? less than 100,000?

## Tim Sackton — January 25, 2021 at 8:52 PM

I think right now (1749 DR) it would be ~100,000, but could have been significantly more before Great War

## Tim Sackton — January 25, 2021 at 9:57 PM

Do you have an online population growth calculator or something? Kind of curious to do this for other races.

Also I don't have a good sense of human population numbers. I think of elves as like 0.1%-1% of human population, which implies a range of 10-100 million for humans. Seems to0 low for human population the whole continent, but the top half of that range seems reasonable for the northwest corner at least.

Just doing some rough calculations, the whole world map is a continent that is about the size of Eurasia in land area, and the northwestern portion (the campaign area) is about 25% of the total land area of the continent.

Asia in 1500 had 280 million people, and Europe about 70 million, so roughly 350 million total. Taelgar definitely has a lower population density than the real world in 1500, so unless there is some dense urban places out in the far east or south (possible), probably <300 million total in the world, and likely <70 million in the northwest corner. Greater Sembara could be 20 million or so, Cymea 10-15 million, and Chardon easily 20 million, but otherwise everything that is made up at least is pretty small (Dunmar can't be more than 10 million and probably notably less, Vostok <1 million, same with Skaegenland). So that works out with a ~60-80 million pop range for this area.

I could also imagine other populations of elves elsewhere, perhaps in the far south or far east, or even on different continents (I have a bit of a world geological history worked out I'll share sometime), so the ~100k wouldn't necessarily be entire race.

## Mike Sackton — January 25, 2021 at 10:16 PM

I just shared a google spreadsheet.

It takes the birth rate and calcs the new births in the next gen (which is the births in the prev gen * the growth rate) and then subtracts deaths. Deaths are basically each year:

5% elves live to 1600
10% elves live to 1440
20% elves live to 1280
50% elves live to 1120
10% elves live to 960
3% elves live to 800
2% elves live forever

(I think I got the math right on that)

Then I added an excess deaths and excess deaths of elvens who hadn't had kids, in each generation (i.e. for downfall, etc) and copied it out to 40 generations (assuming a generation is 160 years)

## Mike Sackton — January 25, 2021 at 10:26 PM

Just a warning if you are playing around with my spreadsheet, it doesn't handle the excess deaths quite right. It assumes the excess death has no impact on the people who die after the bad event. But of course, there are fewer people around to die, because so many of them already died.

## Tim Sackton — January 25, 2021 at 10:37 PM

I believe to properly account for that you need the age structure of the excess deaths. An easier option might be to just calculate the size of each generation over time, playing with this now

## Mike Sackton — January 25, 2021 at 10:47 PM

I haven't tried to find one, but here is a pop. growth simulator in R: https://github.com/ellisp/blog-source/tree/master/_working/0122-demographics (running online at https://ellisp.shinyapps.io/0122-demographics/)

Just doing some rough calculations, the whole world map is a continent that I think you are assuming way too many people. Humans have only been around for 4500 years on Taelgar (or a bit less). And there has been a *lot *of death and destruction. Some people think the Black Plague killed half of Europe.. .The fall of Hkar probably killed half the people on Taelgar. I gotta go to bed, but I wonder what the raw population of a human society would be that has a fertility rate of 2.5 people per woman, a life expectancy of 60, a starting population of 1 million, and three major disasters (Hkar, Drankor Plague, Great War) at years 1700, 2400, and 4000 that killed 50%, 15%, and 15% of the world population.

I suspect it would be a lot less than 300 million, but I have to admit I'm not sure.

Mike

## Tim Sackton — January 26, 2021 at 12:54 AM

Spent way too much time on this.

For elves, you can look in your spreadsheet on the elves-by-gen section. You can change the starting pop, the pre- and post-downfall growth rates, and tinker with the death toll of both major events (downfall and cha'mutte) by changing the multiplicative factor for each generation in the appropriate columns. My basic idea is that the first 1000 years, the population grows rapidly (inevitable without much death), then you have the 'height of empire' of steady growth up to about 1 million before the downfall, then throughout the Drankorian era you have a flat or shrinking population, partially offset by a mini post-downfall baby boom. So immediately post downfall the population shifts quite young, but then inevitably ages again, as it shrinks. After Cha'mutte, because of the age structure of death, you have a rapidly growing population -- I am thinking that perhaps in the final war against Cha'mutte the elves tried to protect Delwath's generation, and so relatively few of them fought. The numbers don't quite work because the excess death events aren't perfectly timed with generations. If I ever feel like it, could work this out in more precise detail. I'm not sure the numbers here are quite right with the births per adult and the death distribution.

For humans (sheet 3), you actually get 326 million in current day Taelgar by assuming exactly what you suggest, except using 0.20% growth per year instead of life expectancy and fertility. If you boost the Hkar growth rate a bit and reduce other growth rates, you get more like 400-500 million people, which might be reasonable for the entire world (not just the main continent). Feel free to tinker. Because it is exponential, very very sensitive to the growth rate assumptions, more so than the excess death events.

## Mike Sackton — January 26, 2021 at 9:58 AM

So I spent a while reading about population growth and demographics in the real world instead of doing math. I hadn't been thinking very clearly about the power of exponential growth. So if you have growth rates like the 1950s for 4000 years you could populate hundreds of worlds. And if you have growth rates like 500 AD (barely above 0) for 4000 years you end with just about what you started with.

In the real world, growth rates of human populations were driven by the death rate, and especially the child death rate, more than anything else. As well as natural resources -- places with famine, limited food, etc end up with lower birth rates as people naturally don't have as many kids.

So really, you can kinda tell any story you want from a population perspective.

In the real world, for most of human history, 60-75% of the world population lived in Asia (mostly in China and India), and most of the rest of the population lived in Europe. Even the large empires in central and south America really only had a few percent of the world population, as did the large central and southern African empires. And this kinda makes sense when you think about the world geography (except for the fact that large populations never developed in North America). The amount of land in the southern hemisphere is just really low compared to the north, and a lot of it is in the less fertile latitudes.

It might be worth thinking about what the northwest of Taelgar should feel like -- is it the center of the world, the biggest population, and the place of riches to the other folks? Are traders from far away coming to Chardon seeking out its magic and spices? Or is the northwest of Taelgar more like Europe? With rumors of bigger, fancier places in far off lands... Or is it more like the ancient Roman world, where there is a bit of a bimodal distribution of Rome <-> China? Or something totally else?

I personally kinda like the idea that although there might be many far off places in the mode of the Inca or the central African empires, the major trading partners out to the east are more like Europe than China....

## Tim Sackton — January 26, 2021 at 10:36 AM

Yeah, thinking about population density across the landscape is why I started playing with the more detailed human population breakdown.

My general sense is a rough history like this:

Age of Hkar: Hkar is massively dominant, starting obviously at 100% of pop but even with significant outmigration still retaining like 70% of the world's population at Downfall, with the rest very lightly settled across Elder race kingdoms.

Age of Drankor: Drankor is like China although not quite as dominant (~50% of world's population), and the south is like Europe. But certainly Drankor is the place of myth and riches, the place where people come from far and wide to learn the secrets of Hkar.

Age of Cha'mutte (post Drankor fall, pre Great War): The northwest suffers way more in the fall of Drankor than the south, so things begin to shift a little. Now you have kind of a bi-modal world, where the Sembara/Chardon/Dunmar nexus and the South are about equal in population.

Current day: Again the northwest suffers vastly more than the south, and so the balance increasingly shifts again, with the south gaining relative to the northwest.

A high fraction of the best land in the main continent is in the northwest. To the east of Dunmar, you have a vast desert, and south of that is very tropical around the equator. Obviously can have high pops like current southeast Asia. Then in the north, the Green Sea occupies the middle latitudes, and the far north is cold and dark. However, there is a southern continent, which could have lots of fertile land.

As far as trade and perspectives of the northwest: I do think there is definitely an (accurate) sense that Drankor was the center of the world, and in places like Chardon and Cymea this attitude probably persists somewhat. Trade east along the Green Sea is kind of even; pre-Great War, for sure, it was stuff from Chardon flowing east across the mountains to Cymea to be traded further east, but with a clear Chardon is China, further east is Europe vibe. But now with the western trade routes severed, probably there is a bit more bi-directional flow. But the populations out east are not really rumors of vast, distant far of fancy lands. In Chardon, you do still sometimes get ships/trade from the south, and that has a bit more of a China/far off land of wonder vibe. But because navigation through the sea of storms is basically impossible without magic, these ships are few and far between. Some goods from the south come north across the desert and then circulate around the Green Sea.

But I think it is not really analagous to real world history in any particularly clear way. Certainly, in the absence of the two plagues, you would have northwestern Taelgar feel very much like China, with an ancient, dominant empire that pulled in trade from the entire continent. But the wars of the age of Cha'mutte caused so much destruction and death in the northwest relative to the rest of the world that that dynamic is disrupted.

I'm working on high level overviews of geography and human history I will share later today that has some of this stuff.
