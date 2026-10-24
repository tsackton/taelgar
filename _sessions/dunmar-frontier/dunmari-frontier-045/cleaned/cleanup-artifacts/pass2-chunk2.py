import importlib
w=importlib.import_module('cleanup-work');d=w.load()
C={251:[('Were 30',"We're 30")],280:[("isn't a","isn't it")],284:[('his actions','his action')],291:[('make it its','make its')],293:[("it's like point","[[it's like point]]")],302:[('in in fact','in fact')],304:[('it failed its save','it [[felt safe]]')],328:[('rolled high enough','[[rolled high enough]]')],334:[('advantage to though','advantage too though')],342:[('For that\'s what I would roll',"Or that's what I would rule")],356:[('issue in the mirror','issue, the mirror')],385:[("[[it doesn't carry something your character it]]","it doesn't count as something you're carrying")],405:[('50 feet','15 feet')],406:[('stick as','stick has')],407:[('stick me','stick at me')],447:[('roaring outrage','roar in outrage')],448:[('[[versus a nice quiet blow the side of the heart of style Jabbar somebody]]','[[versus a nice quiet blow the side of the]] Horn of Silent Alarm [[somebody]]')],452:[('[[wow is not]]','[[wow]] is not')],457:[('There were', 'They were')],477:[('well reverse',"we'll reverse")]}
for n,p in C.items():w.change(d,n,*p)
# Preserve an unrecoverable middle of the DM’s response rather than inventing a complete sentence.
w.change(d,353,('Well Kenzo— Wellby is complete— Wellby can do whatever he wants. Wellby certainly gets a surprise round','Well Kenzo [[welby is complete to lb can do it every once]] Wellby certainly gets a surprise round'))
for n,r in {293:'Unclear objection about when the group would react to the creature approaching.',304:'Unclear save result wording, which conflicts with the stated excitement about fighting.',328:'Possible missing negation in explanation of Delwath’s failed stealth; source says high enough while nearby lines say the creature hears him.',353:'Unclear middle of ruling about Wellby’s available actions; surprise round is explicit.'}.items():d['materialReasons'][f'u{n:04d}']=r
d['materialReasons'].pop('u0385',None)
w.incidental(d,296,'is to have them','Broken lead-in to an otherwise clear statement of the escape plan.')
w.incidental(d,430,'I live','Interrupted lead-in about damage calculation, not a separate game action.')
d['passes'].append({'pass':2,'range':'u0251-u0500','status':'every unit inspected again; missed errors corrected and uncertain rules passages retained'});w.save(d)
print('Second-pass checkpoint through u0500')
