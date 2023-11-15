class init {
    async invoke() {
        const metadataFilePath = app.vault.configDir + "/metadata.json";
        let metadataFile = await app.vault.adapter.read(metadataFilePath);        
        customJS.state.coreMeta = JSON.parse(metadataFile)
    }
}