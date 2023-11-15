async function regenerateHeader(tp) {
       
    async function updateCurrentFile(someContent, someFile) {
        someContent = someContent.join("\n");     
        await app.vault.adapter.write(someFile.path, someContent);
    }
 
    let tfile = app.vault.getAbstractFileByPath(tp.file.path(true));
    let filecontents = await app.vault.adapter.read(tfile.path);
    let currentContents = filecontents.split('\n');  

    let hasTags = tp.frontmatter.tags && tp.frontmatter.tags.length > 0;
    if (!hasTags) {
        new Notice("This file has no tags and therefore does not support header regeneration");
        return;
    }

    if (tp.frontmatter.tags.filter(f => !f.startsWith("status")).length == 0) {
        new Notice("Skipping regeneration of stub header; remove stub to process header")
        return
    }

    // the end of the yaml -- this is 0-counting, so if the file is just a yaml start and end it will be 1
    let indexOfYamlEnd = currentContents.findIndex((f, i) => i>0 && f == "---");

    // find the end of the header block -- the first newline (blank line) after the YAML block
    let indexOfHeaderBlockEnd = currentContents.findIndex((f, i) => i > indexOfYamlEnd && f.trim() == "");

    // the file is ONLY yaml
    if (indexOfHeaderBlockEnd == -1) {
        indexOfHeaderBlockEnd = currentContents.length;
    }

    // starting from the first newline, find the first non-newline
    let emptySpaceEnd = currentContents.findIndex((f, i) => i > indexOfHeaderBlockEnd && f.trim() != "");
    if (emptySpaceEnd != -1) {
        indexOfHeaderBlockEnd = emptySpaceEnd - 1
    }
    
      
    if (currentContents[indexOfYamlEnd+1] && currentContents[indexOfYamlEnd+1].startsWith("<%"))
    {
        new Notice("This file appears to have an unprocessed template. Please run the template before running this file. ALT-R is the hotkey");
        return;
    }

    if (currentContents.slice(indexOfYamlEnd, indexOfHeaderBlockEnd).filter(f => f.trim().startsWith("#")).length == 0) {
        // there is no H1 block in the "header" so it cannot have been an actual header. 
        indexOfHeaderBlockEnd = indexOfYamlEnd
    }

    // remove the header block
    currentContents.splice(indexOfYamlEnd+1, indexOfHeaderBlockEnd-indexOfYamlEnd);          
    // insert the template
    currentContents.splice(indexOfYamlEnd+1, 0, "<% tp.user.generateHeader(tp) %>");  

    // rewrite the file
    await updateCurrentFile(currentContents, tfile);            
}
module.exports = regenerateHeader;