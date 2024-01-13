async function regenerateHeader(tp, headerType) {

 
    const { OutputHandler } = customJS

    async function updateCurrentFile(someContent, someFile) {
        someContent = someContent.join("\n");     
        await app.vault.adapter.write(someFile.path, someContent);
    }
 
    let tfile = app.vault.getAbstractFileByPath(tp.file.path(true));
    let filecontents = await app.vault.adapter.read(tfile.path);
    let newContents = ""

    newContents = OutputHandler.regenerateHeader(filecontents, tp.file.title, tp.frontmatter, headerType)
    
    await updateCurrentFile(newContents, tfile)

}
module.exports = regenerateHeader;