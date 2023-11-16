async function get_table(input) {

    let pageWhere = input.where ?? (f => true)
    let map = input.map ?? (f => [f.name, dv.fileLink(f.file)])
    let header = input.header ?? ["Name", "File"]

    const { NameManager } = customJS
    const { WhereaboutsManager } = customJS
    const { DateManager } = customJS

    let pages = undefined;
    if (input.pageFilter) pages = dv.pages(input.pageFilter.trim());
    else pages = dv.pages();

    return await dv.table(header, pages.where(pageWhere).flatMap(item => {
        let people = [];

        let name = NameManager.getName(item.file.basename, NameManager.NoLink, NameManager.TitleCase)

        let whereabouts = WhereaboutsManager.getWhereabouts(item.file.frontmatter)

        let existData = DateManager.getPageDates(item.file.frontmatter)
        let currentLoc = whereabouts.current
        let home = whereabouts.home
        let origin =  whereabouts.origin

        people.push({ name: name, file: item.file.name, life: existData, currentLocation: currentLoc?.location ?? "Unknown", homeLocation: home?.location ?? "Unknown", origin: origin?.location ?? "Unknown", debug_whereabouts: { c : currentLoc, h: home, o: origin} })

        return people;
    }).map(map))
}

return await get_table(input);