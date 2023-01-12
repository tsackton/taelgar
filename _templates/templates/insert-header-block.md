<%* 
const configFilePath = app.vault.getRoot().path + ".obsidian/taelgarConfig.json";
let configFile = await app.vault.adapter.read(configFilePath);
let config = JSON.parse(configFile);
let output = tp.user.generateHeader(tp,config) 
%><% output %>