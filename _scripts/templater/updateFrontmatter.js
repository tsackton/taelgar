async function updateFrontmatter(tp, allowPrompting, typeToUse) {

    function fixupLocation(locString) { return locString.replace("[[", "").replace("]]", "");}

    function processReplacementsInString(stringItem, config) {
        let campaign = "";
        let campaignPrefix = "";
        if (config) {
            campaign = config.campaign??"";
            campaignPrefix = config.campaignPrefix??"";
        }
        if (stringItem == undefined) return "";
        return stringItem.replace("{campaign}", campaign).replace("{campaignPrefix}", campaignPrefix);
    }


    function getKeyDefault(keyName, folderName, config, filetype) {
        if (!config || !config.typeKeyDefaults) return "";
        let typeKeyDefaults = config.typeKeyDefaults[filetype];
        if (!typeKeyDefaults) return "";

        let mapForFolder = typeKeyDefaults[folderName];
        if (!mapForFolder) return "";

        return processReplacementsInString(mapForFolder[keyName], config);
    }

    async function updateCurrentFile(someContent, someFile) {
        someContent = someContent.join("\n");
        await app.vault.adapter.write(someFile.path, someContent);
    }

    let newFile = false;
    let yamlInsert = false;
    let name = tp.file.title

    let tfile = app.vault.getAbstractFileByPath(tp.file.path(true));
    let filecontent = await app.vault.adapter.read(tfile.path);
    let currentContents = filecontent.split('\n');

    let indexOfYamlEnd = currentContents.findIndex((f, i) => i > 0 && f == "---");
    // there is no yaml -- add it, plus an empty line -- we are pushing to the top so it goes in reverse order
    if (indexOfYamlEnd == -1) {
        currentContents.unshift("");
        currentContents.unshift("---");
        currentContents.unshift("---");
        indexOfYamlEnd = 1;
        yamlInsert = true;
    }
    else if (!tp.frontmatter.name) {
        // there is no name -- this means that we have not processed the data but we do have YAML
        // insert a blank line to preserve the contents of the file -- it is very unlikely to be a
        // header block
        currentContents.splice(indexOfYamlEnd + 1, 0, "");
    }

    let fileType = tp.frontmatter.type ?? typeToUse;
    const configFilePath = app.vault.configDir + "/taelgarConfig.json";
    const metadataFilePath = app.vault.configDir + "/metadata.json";

    let metadata = undefined;
    let config = undefined;

    if (await app.vault.adapter.exists(configFilePath)) {
        let configFile = await app.vault.adapter.read(configFilePath);
        config = JSON.parse(configFile);
    }

    if (await app.vault.adapter.exists(metadataFilePath)) {
        let metadataFile = await app.vault.adapter.read(metadataFilePath);
        metadata = JSON.parse(metadataFile);
    }

    if (metadata == undefined || metadata.types == undefined || metadata.types.length == 0) {
        new Notice("Missing metadata.json file. Cannot define frontmatter.")
        return;
    }

    let folder = tp.file.folder();
    let path = tp.file.folder(true);
    let root = path.split('/')[0];
    if (path.contains("PCs")) {
        root = "PCs";
    }

    let filetypeMetadata = undefined;
    let newFrontMatter = {};
    if (!fileType) {
        // this file doesn't have a type. Do we know what type it should be?
        for (const typeMetadata of metadata.types) {
            if (typeMetadata.typeFolderNames && typeMetadata.typeFolderNames.some(f => path.match(new RegExp(f)))) {
                fileType = typeMetadata.typeName;
                filetypeMetadata = typeMetadata;
                newFrontMatter.type = fileType;
                break;
            }
        }
    }

    if (!fileType) {
        let validTypes = metadata.types.map(s => s.typeName).concat("unlisted");
        fileType = await tp.system.suggester(validTypes, validTypes, false, "No type could be found in the file. Select a type");
        if (fileType == undefined || fileType == "unlisted") {
            new Notice("File type could not be automatically determined or is not known. Cancelling further processing");
            return;
        }
        newFrontMatter.type = fileType;
    }

    if (name.startsWith("Untitled")) {        
        newFile = true;
        name = await tp.system.prompt("Enter a name for " + fileType );
        let checkDp = tp.file.find_tfile(name);
        fname = name;
        while (checkDp != undefined) {
            fname = await tp.system.prompt("Another file already named " + fname + ". Enter a new filename: ");
            if (fname == undefined) {
                new Notice("No name provided, cancelling further processing");
                return;
            }
            checkDp = tp.file.find_tfile(fname);
        }
    }

    if (!filetypeMetadata) {
        filetypeMetadata = metadata.types.find(f => f.typeName == fileType);
        if (!filetypeMetadata) {
            new Notice("No metadata provided for type " + fileType + ". Minimal metadata processing will occur");
        }
    }

    if (filetypeMetadata) {
        let infoLine = currentContents.find((f) => (f.contains("b.") || f.contains("she")|| f.contains("he")||f.contains("they")));

        for (const element of filetypeMetadata.frontmatter) {            
            if (Object.keys(tp.frontmatter).find(f => f == element) == undefined) {
               
                let value = getKeyDefault(element, folder, config, fileType);
                if (infoLine != undefined) {
                    if (element == "gender") {
                        if (infoLine.contains("she")) value = "female";
                        else if (infoLine.contains("they")) value = "nonbinary";
                        else if (infoLine.contains("he")) value= "male";
                    } 
                    else if (element == "born") {
                        let bIndex = infoLine.search("b.");
                        if (bIndex > 0)     {
                            value = infoLine.substr(bIndex+3, 4);
                        }                        
                    }
                    else if (element == "died") {
                        let dIndex = infoLine.search("d.");
                        if (dIndex > 0)     {
                            value = infoLine.substr(dIndex+3, 4);
                        }                        
                    }
                }

                if (newFile && !value && allowPrompting) {
                    if (element == "gender") {
                        let genders = ["male", "female", "nonbinary"];
                        value = await tp.system.suggester(genders, genders, false, "Enter a gender");
                    }

                    if (element == "born") {
                        let age = await tp.system.prompt("Enter an age (0 to skip)");
                        if (age != 0) {
                            value = (window.FantasyCalendarAPI.getCalendars()[0].current.year - age);
                        }
                    }
                }

                newFrontMatter[element] = value;
            }
        }
    }

    if (!tp.frontmatter.name) {
        newFrontMatter.name = name;
    }

    if (!tp.frontmatter.tags) {
        newFrontMatter.tags = "[" + filetypeMetadata.initialTags.map(t => processReplacementsInString(t,config)).join(", ") + "]";
    }    

    if (filetypeMetadata.supportsWhereabouts) {
        console.log("Filetype supports whereabouts. Starting whereabouts processing.");
        if (!tp.frontmatter.whereabouts || tp.frontmatter.whereabouts.length == 0) {           
            var indexOfWhereabouts = currentContents.findIndex(s => s.startsWith("whereabouts:"));
            if (indexOfWhereabouts > 0) {
                currentContents.splice(indexOfWhereabouts, 1);      
                indexOfYamlEnd--;  
            }

            let insertedWhereabouts = false;
            let whereaboutsInsertIndex = indexOfYamlEnd;

            if (tp.frontmatter.origin || tp.frontmatter.originRegion) {
                let initialDate = "0001-01-01";
                if (!tp.frontmatter.origin) { tp.frontmatter.origin = "unknown"}
                if (!tp.frontmatter.originRegion) { tp.frontmatter.originRegion = "unknown"}
                if (tp.frontmatter.born || newFrontMatter.born) {
                    initialDate = (tp.frontmatter.born??newFrontMatter.born) + "-01-01" 
                }

                if (!insertedWhereabouts) { 
                    currentContents.splice(whereaboutsInsertIndex++, 0, "whereabouts:");
                    insertedWhereabouts = true;
                }
         
                currentContents.splice(whereaboutsInsertIndex++, 0, `     - { date: ${initialDate}, place: "${fixupLocation(tp.frontmatter.origin)}", region: ${fixupLocation(tp.frontmatter.originRegion)}}`);
         
                // we need to keep the insert elements in the right spot, so we change where the "yaml end" is
                indexOfYamlEnd--;
            }       

            if (tp.frontmatter.home || tp.frontmatter.homeRegion) {             
                let initialDate = "0001-01-02";
                if (!tp.frontmatter.home) { tp.frontmatter.home = "unknown"}
                if (!tp.frontmatter.homeRegion) { tp.frontmatter.homeRegion = "unknown"}
                if (tp.frontmatter.born || newFrontMatter.born) {
                    initialDate = (tp.frontmatter.born??newFrontMatter.born) + "-01-02" 
                }
         
                if (!insertedWhereabouts) { 
                    currentContents.splice(whereaboutsInsertIndex++, 0, "whereabouts:");
                    insertedWhereabouts = true;
                }
                currentContents.splice(whereaboutsInsertIndex++, 0, `     - { date: ${initialDate}, place: "${fixupLocation(tp.frontmatter.home)}", region: ${fixupLocation(tp.frontmatter.homeRegion)}}`);
         
                // we need to keep the insert elements in the right spot, so we change where the "yaml end" is
                indexOfYamlEnd--;                
            }        

            if (tp.frontmatter.location || tp.frontmatter.locationRegion) {
                let currentYear = String(window.FantasyCalendarAPI.getCalendars()[0].current.year).padStart(4, '0');
                let currentMonth = String(window.FantasyCalendarAPI.getCalendars()[0].current.month+1).padStart(2, '0');
                let currentDay = String(window.FantasyCalendarAPI.getCalendars()[0].current.day).padStart(2, '0');
            
                let initialDate = `${currentYear}-${currentMonth}-${currentDay}`;
                if (!tp.frontmatter.location) { tp.frontmatter.location = "unknown"}
                if (!tp.frontmatter.locationRegion) { tp.frontmatter.locationRegion = "unknown"}
                if (!insertedWhereabouts) { 
                    currentContents.splice(whereaboutsInsertIndex++, 0, "whereabouts:");
                    insertedWhereabouts = true;
                }
                currentContents.splice(whereaboutsInsertIndex, 0, `     - { date: ${initialDate}, place: "${fixupLocation(tp.frontmatter.location)}", region: ${fixupLocation(tp.frontmatter.locationRegion)}, excursion: true }`);
        
                // we need to keep the insert elements in the right spot, so we change where the "yaml end" is
                indexOfYamlEnd--;
            }   

            if (insertedWhereabouts) indexOfYamlEnd--;
        } else {
            console.log("Filetype already has whereabouts present. No processing required.");
        }

        if (tp.frontmatter.born || newFrontMatter.born) {
            var originDateWhereabouts = currentContents.findIndex((f,i) => i<indexOfYamlEnd && f.startsWith("     - { date: 0001-01"));
            while (originDateWhereabouts > 0) {
                console.log(`Found non-born whereabouts data`);
                currentContents[originDateWhereabouts] = currentContents[originDateWhereabouts].replace("0001", tp.frontmatter.born??newFrontMatter.born);        
                originDateWhereabouts = currentContents.findIndex((f,i) => i<indexOfYamlEnd && f.startsWith("     - { date: 0001-01"));        
            }   
        }

        ["home", "homeRegion", "location", "locationRegion", "origin", "originRegion"].forEach(element => {
            var index = currentContents.findIndex(s => s.startsWith(element + ":"));            
            if (index > 0) {
                console.log(`Found ${element}: element to remove at index ${index}`);
                currentContents.splice(index, 1);      
                indexOfYamlEnd--;  
            }            
        });
    }


    for (let item in newFrontMatter) {
        let iv = newFrontMatter[item];

        if (iv) currentContents.splice(indexOfYamlEnd, 0, `${item}: ${iv}`);
        else currentContents.splice(indexOfYamlEnd, 0, `${item}:`);

        if (yamlInsert) indexOfYamlEnd++;
    }

    let headerType = tp.frontmatter.type ?? fileType;


    if (newFile) {
        let newFileName = tfile.path.replace("Untitled", fname);
        await app.vault.rename(tfile, newFileName);
        tfile = app.vault.getAbstractFileByPath(newFileName);
    }



    await updateCurrentFile(currentContents, tfile);
    await tp.user.regenerateHeader(tp, headerType);


}
module.exports = updateFrontmatter