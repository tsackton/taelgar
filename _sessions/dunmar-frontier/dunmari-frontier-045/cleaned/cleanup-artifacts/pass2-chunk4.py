import importlib
w=importlib.import_module('cleanup-work');d=w.load()
C={757:[('[[Why barrels]]','Why bedrolls')],779:[('I actually like if to',"I'd actually like to")],786:[('[[those analysis around]]',"there's an elf around")],796:[('[[Laurens]]','Illorians')],797:[('[[borbon]]','dwarven')],799:[('Last [[delorean]]','Less Illorian')],800:[('[[Murray in]]','Illorian')],811:[('cola','Cool')],812:[('[[tow truck so took right]]','Tokra so Tokra')],815:[('that most','at most')],828:[('Empty ness','Emptiness')],846:[('tributaries on','tributaries and')],848:[('here in Darba','here and Darba')],888:[('Now Darba','No, Darba')],896:[('and Chardon','in Chardon')],897:[('and Chardon','in Chardon')],912:[('[[I was very well be asked to be]]','That was very Wellby-esque of me')],915:[("Delwath hasn't","Delwath has it")],926:[("[[And that's too much]]", "Don't spend too much")],941:[('and water reflects',"the water reflects"),("that creature's", "[[that creature's]]")],943:[('[[Arkansas]]',"Agata's")],950:[('where the wand','were the wand')],956:[("i'm in this look", "I mean, let's look")],983:[('give out an example Tim','give that example, Tim')]}
for n,p in C.items():w.change(d,n,*p)
for n in (757,786,796,797,799,800,812,912,926,943):d['materialReasons'].pop(f'u{n:04d}',None)
d['materialReasons']['u0941']='Dream-mirror description stops after creature’s; the reflected content is not stated in this recorded unit.'
d['incidental'].pop('u0811',None)
w.incidental(d,971,'do well','Possibly missing negative in roll chatter; the final total of 10 is explicit in u0972.')
d['passes'].append({'pass':2,'range':'u0751-u1000','status':'every unit inspected again; later-session variants used to resolve earlier group-name drift'});w.save(d)
print('Second-pass checkpoint through u1000')
