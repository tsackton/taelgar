function get_RegnalValue(metadata) {
    
    const { metadataUtils } = customJS

    let regnalData = metadataUtils.get_regnalData(metadata)

    if (!regnalData.isStarted) return "";

    if (!regnalData.isCurrent) {
        if (regnalData.length) {
            return "reigned " + regnalData.startDate.display + " - " + regnalData.endDate.display + " (" + regnalData.length + " years)";
        }
        else {
            return "reign ended " + regnalData.endDate.display;
        }
    }
    else if (regnalData.length) {       
        return "reigning since " + regnalData.startDate.display + " (" + regnalData.length + " years)";       
    }
    else {    
        return "";
    }  


}
return get_RegnalValue(dv.current() )