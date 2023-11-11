# Cleaning markdown for export

The `convert_markdown.py` script in the `_scripts` directory takes a folder and processes all markdown files in that folder (recursively). The script optionally does the following things:
- replace inline dview calls (`$=dview()`) with python functions that generate plain markdown based on the file metadata and the current date (to use this, set the `--dview` option)
- filter text flagged with comments in the form of  `%%^Campaign:<prefix> (text) %%^End`or `%%^Date:<date> (text) %%^End` based on the `--campaign` flag and either the current date in fantasy calendar json or the `--date` flag (which overrides the current date in json). to use this, set the `--filter` option 
- copy the markdown files to a new directory before processing if `-o` is set
- copy the markdown files to a new directory that is not touched if `-b` is set
  
See `convert_markdown.py -h` for full options. 

### Notes

The filter code checks for lines that start with the filter prefix and removes that line and all subsequent lines up to and including the next line that ends with the `%%^End` tag. If you have a start prefix with no end prefix or a malformed end prefix, it will remove your entire file. If you have text before the start prefix on the line, it won't work. It is probably safest to run the `--filter` option only on backups, or output to another directory. 

### To do
Not yet implemented, but planned:
- read campaign information from json if campaign flag is not set
- check for existence date on pages with a born/created date, and output a page doesn't exist yet text if current date < page date
- read yaml metadata, validate and clean against spec, and output cleaned yaml metadata
- investigate feasibiliy of impementing `dataview` or `dataviewjs` code blocks, instead of just inline code (potentially via rendering them with the obsidian engine and then replacing code block with html)