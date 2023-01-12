The NPC template does the following:

* Prompts for name and uses it for the file
* Calculate the species and ancestry from the folder 
	* TODO: Use taelgarConfig.json to make folders to defaults
	* Prompts otherwise
	* When prompting for species, it uses the Species\ MD files as the input for the dropdown
	* Select Other to get free text
* Prompt for origin and home regions
	* The form is "City, State, Country"
	* The template will separate these into blocks, determine if they are linkable, and link them if they are linkable
	* It will add the last piece to a homeRegion/originRegion tag intended for use in dataview queries
* Prompt for party status (met/unmet/unaware)
	* If met, will set a last met date of the current campaign date. This might not be accurate, but is often good enough
	* This also provides the format
* Set the whereabouts YAML to set the person to be in there home region at all dates