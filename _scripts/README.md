# Scripts notes

I've copied all javascript and python code that interact with obsidian or markdown to the `_scripts` directory (my filter_sercrets.py script for git smudge/clean lives elsewhere, in the .scripts directory).

There are currently three things in here:

#### **convert_markdown.py**
This is the python script that takes the obsdiantohtml md output and cleans it by replacing dv.view() code with Python replacements, and removing Date blocks. This needs to be fixed to work with the new javascript so it won't do anything yet. I will update this readme with run instructions once it is functional.

#### **customJS**
This folder contains javascript code that can be imported into either a templater javascript block or a dataviewjs block by using:
```
const {FUNCTIONNAME} = customJS
```
FUNCTIONNAME is the name of a file containing a class with various methods. My understanding is the file needs to be named FUNCTIONNAME.js and the class should be the same as the filename. You'll need to set the customJS scripts folder to `_scripts/customJS`, of course. 

Right now, the only class that exists here is metadataUtils. All the metadataUtils functions take the metadata object as their first argument, with optional additional arguments depending on the function. 

#### **view**
This folder contains dataview functions that can be used with dv.view("/path/to/function", arguments). 

#### **templater**
This folder contains templater user functions. The generateHeader function will create a header depending on the type frontmatter. Currently only the NPC type works. 