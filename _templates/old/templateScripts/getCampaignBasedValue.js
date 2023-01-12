async function getCampaignValue(tp, frontmatterItem) {

    const configFilePath = app.vault.getRoot().path  + ".obsidian/taelgarConfig.json";

    let configFile = await app.vault.adapter.read(configFilePath);

    
    let parsed = JSON.parse(configFile);
        
    const campaignValue = parsed.campaignPrefix;
            
    let valueToUse = tp.frontmatter[frontmatterItem + "_" + campaignValue];
    if (!valueToUse) {
        valueToUse = tp.frontmatter[frontmatterItem];
    }

    return valueToUse;
}
module.exports = getCampaignValue;