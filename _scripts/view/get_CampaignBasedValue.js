let metadata = dv.current()
let frontmatterItem  = input.key
const configFilePath = app.vault.getRoot().path  + ".obsidian/taelgarConfig.json";
let configFile = await app.vault.adapter.read(configFilePath);
let parsed = JSON.parse(configFile);
const campaignValue = parsed.campaignPrefix;

let valueToUse = metadata[frontmatterItem + "_" + campaignValue];
if (!valueToUse) {
    valueToUse = metadata[frontmatterItem];
}
return valueToUse