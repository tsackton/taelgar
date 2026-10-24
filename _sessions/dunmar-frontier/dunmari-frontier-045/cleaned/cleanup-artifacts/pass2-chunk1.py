import importlib
w=importlib.import_module('cleanup-work');d=w.load()
C={21:[('that far','that fire')],35:[('troll legged','troll-like')],54:[('want a','want to')],68:[("it's emotional","its emotional")],102:[('I stopped',"I'll stop"),("by it's striking",'by striking')],103:[('to have someone','at someone')],107:[('are just gonna get [[a chance]]','[[or just get a chance]]')],108:[('peacefully and its','peacefully in its')],109:[('park','[[park]]')],110:[('such poison','[[suction poison]]')],115:[("[[it doesn't work here you're asking me to, I think, at least people]]","[[it doesn't work here you're asking me to]], I think it eats people")],124:[('This places','this place is')],132:[('do you felt','you felt'),('family have','family of')],141:[("it's soul",'its soul')],144:[("it's wyvern",'its wyvern')],146:[('wyvern','[[winner and]]')],180:[('Here is married to go in and','[[Here is married to go in and]]')],191:[("Where they're 12",'Were there 12')],198:[('hobgoblin in the wizard','hobgoblin and the wizard')],204:[('Already within','[[are ready]] within')],206:[('standing next to fly','standing next to you, fly')],211:[('So, Wellby','So, Wellby')],224:[("in Delwath's pocket",'[[and have the pocket]]')],245:[('like stops','it stops')]}
for n,p in C.items():w.change(d,n,*p)
# u0211's name substitution was not warranted by the source: the next clause addresses everybody losing invisibility.
w.change(d,211,('So, Wellby', 'So, [[while the]]'))
# u0099: entire lead-in is unclear, not just two words.
w.change(d,99,('throwing up for like [[here was]]','[[throwing up for like here was]]'))
for n,r in {109:'Unclear description of the creature’s heart/soul and poison.',110:'Unclear exact poison description; the creature’s poison association is clear.',146:'Unclear statement about a possible wyvern/mirror prisoner.',180:'Unclear interruption about the proposed mirror plan.',204:'Unclear lead-in to the 30-foot mirror range.',211:'Unclear lead-in; warning about losing invisibility when fly is cast is intact.',224:'Unclear storage/owner reference for the mirror.'}.items():d['materialReasons'][f'u{n:04d}']=r
for n in (180,191):d['incidental'].pop(f'u{n:04d}',None)
w.incidental(d,25,'72 I','Unclear numerical false start; the amount is explicitly settled at 140 gold in u0033.')
w.incidental(d,100,'you have a lot','Broken conversational aside; apology/relationship banter is clear from surrounding speech.')
w.incidental(d,156,'I seem to be a great moment')
w.incidental(d,162,'What did that mean')
d['passes'].append({'pass':2,'range':'u0001-u0250','status':'every unit inspected again; missed errors corrected and speculative first-pass substitutions retracted'});w.save(d)
print('Second-pass checkpoint through u0250')
