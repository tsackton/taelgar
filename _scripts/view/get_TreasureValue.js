function get_TreasureValue(treasureType,treasureRarity,treasureQuality="normal") {
    // attempt to right a dv.view function to generate treasure values from type, quality //
    // currently not working //

    // get dice roller plugin //    
    // const diceRollerPlugin = app.plugins.getPlugin("obsidian-dice-roller"); //

    let baseDice = "1d6"
    let scaleValue = 1

    if (treasureType == "trade" || treasureType == "trade good") {
        baseDice = "1d6"
        switch (treasureRarity) {
            case "common": 
                scaleValue = 1
                break;
            case "uncommon":
                scaleValue = 5
                break;
            case "rare":
                scaleValue = 10
                break;
            case "very rare":
            case "vrare":
            case "v. rare":
                scaleValue = 50
                break;
            case "legendary":
                scaleValue = 100
        }
    } else if (treasureType == "gem" || treasureType == "gemstone") {
        baseDice = "2d6"
        switch (treasureRarity) {
            case "common": 
                scaleValue = 5
                break;
            case "uncommon":
                scaleValue = 10
                break;
            case "rare":
                scaleValue = 50
                break;
            case "very rare":
            case "vrare":
            case "v. rare":
                scaleValue = 100
                break;
            case "legendary":
                scaleValue = 500
        }
    } else if (treasureType == "art" || treasureType == "art object") {
        baseDice = "3d6"
        switch (treasureRarity) {
            case "common": 
                scaleValue = 10
                break;
            case "uncommon":
                scaleValue = 50
                break;
            case "rare":
                scaleValue = 100
                break;
            case "very rare":
            case "vrare":
            case "v. rare":
                scaleValue = 500
                break;
            case "legendary":
                scaleValue = 1000
        }
    }

    switch (treasureQuality) {
        case "inferior":
        case "inf":
            scaleValue = scaleValue * 0.5
            break;
        case "exquisite":
        case "superior":
        case "exq":
            scaleValue = scaleValue * 2
    }

    diceString = baseDice + " * " + scaleValue
    return diceString

    // const treasureValue = await diceRollerPlugin.getRoller(diceString);
    // return diceRollerPlugin.roll(treasureValue)
}

result = get_TreasureValue(input.type, input.rarity, input.quality)
return result   