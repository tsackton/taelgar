async function regenerateHeader(tp) {
       
    async function updateCurrentFile(someContent, someFile) {
        someContent = someContent.join("\n");     
        await app.vault.modify(someFile, someContent);
    }

    let newFile = false;    
    let yamlInsert = false;
    let name = tp.file.title    
    let tfile = tp.file.find_tfile(name);
    let currentContents = tp.file.content.split('\n');   

    let fileType = tp.frontmatter.type;
    if (!fileType) {
            new Notice("This file has no filetype and therefore does not support header regeneration");
            return;
    }

    // the end of the yaml -- this is 0-counting, so if the file is just a yaml start and end it will be 1
    let indexOfYamlEnd = currentContents.findIndex((f, i) => i>0 && f == "---");

    // find the end of the header block -- the first newline (blank line) after the YAML block
    let indexOfHeaderBlockEnd = currentContents.findIndex((f, i) => i > indexOfYamlEnd && f.trim() == "");
    
    // the file is ONLY yaml
    if (indexOfHeaderBlockEnd == -1) indexOfHeaderBlockEnd = currentContents.length;
  
    // remove the header block
    currentContents.splice(indexOfYamlEnd+1, indexOfHeaderBlockEnd-indexOfYamlEnd);          
    
    // insert the template
    currentContents.splice(indexOfYamlEnd+1, 0, "<% tp.user.generateHeader(tp) %>");  
    
    // rewrite the file
    await updateCurrentFile(currentContents, tfile);            
}
module.exports = regenerateHeader;