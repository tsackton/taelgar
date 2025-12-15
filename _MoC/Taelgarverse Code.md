# Javascript Notes
**WARNING: outdated and incomplete**

The `_scripts` directory has three kinds of Javascript code. 

#### **customJS**
This folder contains javascript code that can be imported into either a templater javascript block or a dataviewjs block by using:
```
const {FUNCTIONNAME} = customJS
```
FUNCTIONNAME is the name of a file containing a class with various methods. My understanding is the file needs to be named FUNCTIONNAME.js and the class should be the same as the filename. You'll need to set the customJS scripts folder to `_scripts/customJS`, of course. 

(to add...documentation of classes that exist and functions one might want to use for dataviewjs)

#### **view**
This folder contains dataview functions that can be used with dv.view("/path/to/function", arguments). The intention is that any code in here is needed for export and will be translated into Python for website generation. 

#### **templater**
This folder contains templater user functions. 