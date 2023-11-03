function get_table(input) {

    let yearStart = input.yearStart;
    let yearEnd = input.yearEnd ?? input.yearStart;
    let pageFilter = input.pageFilter ?? "#event-source";

    return dv.table(["Date", "Event", "File"], dv.pages(pageFilter).flatMap(item => {
        if (item.file.lists.length == 0 && item.file.frontmatter.DR != null) {
            return [{ year: item.file.frontmatter.DR.year ?? item.file.frontmatter.DR, date: item.file.frontmatter.DR, text: item.file.name, file: item.file.name }];
        } else {
            return item.file.lists.where(t => t.DR != null).map(t => {
                let firstColon = t.text.lastIndexOf(':')
                let realText = firstColon > 0 ? t.text.substring(firstColon + 1) : t.text;
                return { year: t.DR.year ?? t.DR, date: t.DR, file: item.file.name, text: realText };
            })
        }
    }).where(f => (f.year >= yearStart) && (f.year <= yearEnd)).sort(f => f.date.year == null ? dv.date(f.date + "-01-01") : f.date).map(f => [f.date, f.text, dv.fileLink(f.file)]))
}

return get_table(input);