import importlib
w=importlib.import_module('cleanup-work');d=w.load()
C={504:[('got to stick','got the stick')],512:[('[[or offer dollar or a while we]]','or for Delwath or Wellby')],514:[("[[i'll refer lobby]]","I'll roll for Wellby")],515:[('[[or said this, I can belt all]]','[[or said this, I can]] Delwath')],540:[('will rejoin',"we'll rejoin")],568:[('with that to speak','[[which that to speak]]')],573:[('[[terroir]]','Tokra')],575:[('Can you basically','And you basically'),('20. I I','20. I')],586:[('track','trap')],613:[('avoided','avoid it')],616:[('bandits in the','bandits and the'),('taking care','taken care')],663:[('somebody Manor',"somebody's manor")],665:[('an exchange','in exchange')],668:[('innkeeper them','innkeeper, the')],704:[('know the one','No, the one')],707:[("i'm Harry Potter",'from Harry Potter')],724:[('Nobody is','Nobody has')],729:[('mud in the rain','mud and the rain')],737:[('night that','night then')],745:[("i'll see the Baxter","I'll see to Baxter")],750:[('that are','there')]}
for n,p in C.items():w.change(d,n,*p)
for n in (512,514,573):d['materialReasons'].pop(f'u{n:04d}',None)
d['materialReasons']['u0568']='Unclear ending of explanation of speaking to a named mirror prisoner.'
d['passes'].append({'pass':2,'range':'u0501-u0750','status':'every unit inspected again; repeated name drift resolved from local context'});w.save(d)
print('Second-pass checkpoint through u0750')
