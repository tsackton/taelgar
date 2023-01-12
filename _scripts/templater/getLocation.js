function getLocation (tp, frontmatterItem) {
    
    // construct variables //
    loc = tp.frontmatter[frontmatterItem];
    locRegion = tp.frontmatter[frontmatterItem + "Region"];

    if (loc) {
        if (locRegion) {
            locArray = loc.split(',')
            locArray.push(locRegion)
        } else {
            locArray = loc.split(',')
        }
    } else {
        if (locRegion) {
            locArray = loc.split(',')
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