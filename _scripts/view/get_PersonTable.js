async function get_table(input) {

    let pageWhere = input.where ?? (f => true)
    let map = input.map ?? (f => [f.name, dv.fileLink(f.file)])
    let header = input.header ?? ["Name", "File"]

    const { metadataUtils } = customJS

    let pages = undefined;
    if (input.pageFilter) pages = dv.pages(input.pageFilter.trim());
    else pages = dv.pages();

    return await dv.table(header, pages.where(pageWhere).flatMap(item => {
        let people = [];

        let name = metadataUtils.get_Name(item.file, true)
        let existData = metadataUtils.get_pageExistenceData(item.file.frontmatter)
        let currentLoc = metadataUtils.get_currentWhereabouts(item.file.frontmatter)
        let home = metadataUtils.get_homeWhereabouts(item.file.frontmatter)
        let origin = metadataUtils.get_originWhereabouts(item.file.frontmatter)

        people.push({ name: name, file: item.file.name, life: existData, currentLocation: currentLoc?.location ?? "Unknown", homeLocation: home?.location ?? "Unknown", origin: origin?.location ?? "Unknown", debug_whereabouts: { c : currentLoc, h: home, o: origin} })

        return people;
    }).map(map))
}

return await get_table(input);