# Building Taelgarverse

These are updated instructions for building the Taelgarverse webpage, current as of 11/20/2023

This depends on two Github packages:
- [Obsidian HTML](https://github.com/obsidian-html/obsidian-html)
- [taeglar-utils](https://github.com/tsackton/taelgar-utils)

The process uses the `taelgar_utils.py` script to first convert Obsidian files, and then uses `obsidianhtml` to produce clean markdown and final html.

## Step 1

Convert dynamic elements with `taelgar_utils.py`.

The `taelgar_utils.py` can do the following:
- replace inline dview calls (`$=dview()`) with python functions that generate plain markdown based on the file metadata and the current date (to use this, set the `--dview` option)
- filter text flagged with comments in the form of  `%%^Campaign:<prefix> (text) %%^End`or `%%^Date:<date> (text) %%^End` based on the `--campaign` flag and either the current date in fantasy calendar json or the `--date` flag (which overrides the current date in json). to use this, set the `--filter` option. The campaign/date filter hasn't been extensively tested. 

The `taelgar_utils.py` requires a `config.json` which specifies, at the moment, only the obsidian_path (which should be an absolute path to the root of your Taelgar obsidian folder).

The general usage would be to run:
`taelgar_utils.py --output </path/to/target/dir> --dview <path/to/folders/to/process>`

See `taelgar_utils.py -h` for full options. 

## Step 2

Convert static markdown with `obsidianhtml`

Note that obsidianhtml needs to be set up to point to the new folder created by `taelgar_utils.py`, which also needs to be an obsidian vault (with a .obsidian directory). 

## Notes

Not yet implemented, but planned:
- check for existence date on pages with a born/created date, and output a page doesn't exist yet text if current date < page date
- investigate feasibility of implementing `dataview` or `dataviewjs` code blocks, instead of just inline code (potentially via rendering them with the obsidian engine and then replacing code block with html)

## Planned Functions

**Metadata Cleanup**:
The `taelgar_utils.py` script has some preliminary functionality for cleaning yaml frontmatter, but it is currently quite out of date with respect to the current frontmatter spec and shouldn't be used. The goal is to allow a fast way to reformat yaml, remove non-required blank lines, update frontmatter, and other tools; mostly a check for if we change anything going forward. 

**Mass Replace**:
Tools to do find a specific phrase in all notes and replace with a different phrase. Designed for things like cleaning up broken links.

**Doc Import/Export**:
Using pandocs or other functionality, export specific pages as word documents for e.g. posting on Google Drive, or even directly posting on Google Drive. Ideally would also implement an import function, to generate a diff for updating markdown with external changes. 

**Incorporate HTML generation**:
Ultimately, would be ideal to incorporate html generation directly, or at least incorporate markdown cleanup directly. That is a bigger project. 