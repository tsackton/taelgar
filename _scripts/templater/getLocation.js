function getLocation (tp, place, region) {
    
    // construct variables //
    loc = place;
    locRegion = region;

    if (loc) {
        if (locRegion) {
            locArray = loc.split(',')
            locArray.push(locRegion)
        } else {
            locArray = loc.split(',')
        }
    } else {
        if (locRegion) {
            locArray = locRegion.split(',')
        } else {
            // no values
            return ""
        }
    }

    let locArrayValues = locArray.map(function(f) {
        pieceValue = f.trim();
        file = tp.file.find_tfile(pieceValue);
        if (file != undefined) { return "[[" + pieceValue + "]]";  }
        return pieceValue;
    });
    
    return locArrayValues.join(', ');
}
module.exports = getLocation