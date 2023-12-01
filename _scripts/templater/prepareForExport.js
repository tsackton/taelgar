async function prepareForExport(tp) {

    const { DateManager } = customJS
    const { OutputHandler } = customJS

    let date = await tp.system.prompt("Enter new fantasy calendar date override: (YYYY, YYYY-MM, or YYYY-MM-DD, or blank to clear)")

    let normalized = DateManager.normalizeDate(date)

    if (normalized) {
        customJS.state.overrideDate = normalized
    } else {
        customJS.state.overrideDate = undefined
    }


    const files = app.vault.getMarkdownFiles()

    for (let i = 0; i < files.length; i++) {        
        await app.vault.process(files[i], (data) => {            
            let md = app.metadataCache.getFileCache(files[i])                        
            if (md && md.frontmatter && md.frontmatter.tags && md.frontmatter.headerVersion == "2023.11.25") { 
                new Notice("Processing file " + files[i].basename)                
                let newC = OutputHandler.regenerateHeader(data, files[i].name, md.frontmatter, false)            
                return newC.join("\n");     
            }
            return data
        })
    }

}
module.exports = prepareForExport;