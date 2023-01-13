async function updateFrontmatter(tp) {
    
    function getKeyDefault(keyName, folderName, typeKeyDefaults) {
        if (!typeKeyDefaults) return "";           

        let mapForFolder = typeKeyDefaults[folderName];
        if (!mapForFolder) return "";

        return mapForFolder[keyName] ?? "";
    }

    async function updateCurrentFile(someContent, someFile) {
        someContent = someContent.join("\n");     
        await app.vault.modify(someFile, someContent);
    }

    let newFile = false;    
    let yamlInsert = false;
    let name = tp.file.title    
    let tfile = tp.file.find_tfile(name);
    let currentContents = tp.file.content.split('\n');

    if (name.startsWith("Untitled") || tp.file.content.trim() == "RERUN") {
        newFile = true;
        name = await tp.system.prompt("NPC Name") ?? "Untitled";        
        await tp.file.rename(`${name}`);
        tfile = tp.file.find_tfile(name);
        await updateCurrentFile([""], tfile);
        currentContents = ["---", "---"];
    } 

    let indexOfYamlEnd = currentContents.findIndex((f, i) => i>0 && f == "---");
    // there is no yaml -- add it, plus an empty line -- we are pushing to the top so it goes in reverse order
    if (indexOfYamlEnd == -1) {
        currentContents.unshift("");
        currentContents.unshift("---");
        currentContents.unshift("---");
        indexOfYamlEnd = 1;
        yamlInsert = true;
    }

    let fileType = tp.frontmatter.type;
    const configFilePath = app.vault.configDir  + "/taelgarConfig.json";
 
    if (await app.vault.adapter.exists(configFilePath)) {
        // this block is all about updating metadata -- we if don't have a taelgarConfig we don't bother
        let configFile = await app.vault.adapter.read(configFilePath);
        let configuration = JSON.parse(configFile);    

        let folder = tp.file.folder();
        let path = tp.file.folder(true);
        let root = path.split('/')[0];
        if (path.contains("PCs")) {
            root = "PCs";
        }
       
        let newFrontMatter = {};        

        if (!fileType) {
            // this file doesn't have a type. Do we know what type it should be?
            let typeForThisFolder = configuration.rootTypes[root];
            if (!typeForThisFolder ) {
                new Notice("Error: Unable to determine the file type. Please set type: in the yaml frontmatter");
                return;
            }

            newFrontMatter.type = typeForThisFolder;
            fileType = typeForThisFolder;
        } 
        
        if (!tp.frontmatter.name) {
            newFrontMatter.name = name;
        }

        let keysForType = configuration.typeKeys[fileType];
        if (keysForType) {
            for (const element of keysForType) {        
                if (Object.keys(tp.frontmatter).find(f => f == element) == undefined) {
                    let value = getKeyDefault(element, folder, configuration.typeKeyDefaults[fileType]);
                    if (newFile && !value)  {                        
                        if (element == "gender") {                        
                            let genders = ["male", "female", "nonbinary"];
                            value = await tp.system.suggester (genders, genders, false, "Enter a gender");                        
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
    
        for (let item in newFrontMatter)  {
            let iv = newFrontMatter[item];

            if (iv) currentContents.splice(indexOfYamlEnd, 0, `${item}: ${iv}`);
            else currentContents.splice(indexOfYamlEnd, 0, `${item}:`);                
            
            if (yamlInsert) indexOfYamlEnd++;        
        }     

    } else {
        new Notice("Unable to find a taelgarConfig.json. No metadata will be updated.")
    }
  
    // find the end of the header block -- the first newline (blank line) after the YAML block
    let indexOfHeaderBlockEnd = currentContents.findIndex((f, i) => i > indexOfYamlEnd && f.trim() == "");
    if (indexOfHeaderBlockEnd == -1) indexOfHeaderBlockEnd = currentContents.length;
  
    currentContents.splice(indexOfYamlEnd+1, indexOfHeaderBlockEnd-indexOfYamlEnd);          
    currentContents.splice(indexOfYamlEnd+1, 0, "<% tp.user.generateHeader(tp) %>");  
    await updateCurrentFile(currentContents, tfile);            
}
module.exports = updateFrontmatter;