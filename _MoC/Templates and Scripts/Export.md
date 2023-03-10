To clean the md files generated by obsdiantohtml, you should be able to run:
```
python $OBSIDIAN_DIR/_templates/templateScripts/convert_markdown.py --date <DATE> --campaign <CAMPAIGN> --dir <directory of md output from obsidiantohtml>
```

Date must be the form of a year (for now), and campaign should be the same campaign string as in your  taelgarConfig.json. It does not read that file, so you must specify this on the command line (this is for the scenario where you might want to export the same vault for different campaigns). 

There may still be some bugs, as I haven't tested on real complex output yet. 

This code does three things:

It replaces dv.view() calls with the correct values from metadata, or with ... if the particular dv.view function is not reimplemented in Python. 

It checks if the born/created/built year is after the DATE value passed to the command line. If so, it still exports the yaml frontmatter, but replaces the text on the page with a header with name (if defined in the frontmatter) or "unnamed entity" if name is not defined, followed by a single line of text (**This entity does not yet exist!**).

It checks for comments in the form of  `%%^Date:YEAR%%` and `%%^End%%`, and removes all text in between these comments if YEAR is greater than the DATE passed on the command line. Currently, it assumes that  `%%^Date:YEAR%%` and `%%^End%%` must each occur on their own separate line, so:
```
%%^Date: 1745%%
text
%%^End%%
```
will work but:
```
%%^Date: 1745%% text %%^End%%
```
will not. 

There can be whitespace before/after the year in the Date: field, but their can't be whitespace in the `%%^End%%` block.

This could be extended to full dates or to  `%%^Campaign: CAMPAIGNKEY` at some point if it is useful. 
