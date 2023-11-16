async function get_table(input) {

    let yearStart = input.yearStart;
    let yearEnd = input.yearEnd ?? input.yearStart;    
    let pageWhere = input.where ?? (f => true)
    let map = input.map ?? (f => [f.date, f.text, dv.fileLink(f.file)])
    let header = input.header ?? ["Date", "Event", "File"]
    let options = {
        includeCreate: input.includeCreate ?? input.includeAll ?? false,
        includeEnd: input.includeEnd ?? input.includeAll ?? false,
        includeRegnal: input.includeRegnal ?? input.includeAll ?? false,
        includeTravel: input.includeTravel ?? input.includeAll ?? false,
        includePartyMeetings: input.includePartyMeetings ?? input.includeAll ?? false
    };

    const { metadataUtils } = customJS
    const { DateManager } = customJS
    const { WhereaboutsManager } = customJS

    let pages = undefined;
    if (input.pageFilter) pages = dv.pages(input.pageFilter.trim());
    else pages = dv.pages();

    return await dv.table(header, pages.where(pageWhere).flatMap(item => {
        let events = [];
        
        let name = metadataUtils.get_Name(item.file, true)
      
        if (item.file.frontmatter.DR != null) {
            let jsDate = DateManager.normalizeDate(item.file.frontmatter.DR, false)
            
            if (item.file.frontmatter.summary) {
                name = "*(" + name + ")*: " + item.file.frontmatter.summary
            }            

            events.push({ year: jsDate.year, date: jsDate.display, text: name, rawText: name, file: item.file.name, sort: jsDate.sort })
        }

        if (options.includeCreate == true || options.includeEnd == true) {
            let pageExistenceData = DateManager.getPageDates(item.file.frontmatter)

            if (options.includeCreate && pageExistenceData.startDate) {
                let origin = WhereaboutsManager.getWhereabouts(item.file.frontmatter).origin
                let text = name + " " + pageExistenceData.startDescriptor
                if (origin) {
                    text += " in " + metadataUtils.get_Location(origin)
                }

                events.push({ year: pageExistenceData.startDate.year, date: pageExistenceData.startDate.display, text: text, rawText: text, file: item.file.name, sort: pageExistenceData.startDate.sort })
            }

            if (options.includeEnd && pageExistenceData.endDate) {
                let diedSpot = WhereaboutsManager.getWhereabouts(item.file.frontmatter, pageExistenceData.endDate).lastKnown
                let text = name + " " + pageExistenceData.endDescriptor
                if (diedSpot) {
                    text += " in " + metadataUtils.get_Location(diedSpot)
                }

                events.push({ year: pageExistenceData.endDate.year, date: pageExistenceData.endDate.display, text: text, rawText: text, file: item.file.name, sort: pageExistenceData.endDate.sort })
            }

        }

        if (options.includeRegnal == true && item.file.frontmatter.reignStart != null) {
            let regnalData = DateManager.getRegnalDates(item.file.frontmatter)
            let pageExistData = DateManager.getPageDates(item.file.frontmatter)
            if (regnalData.startDate) {
                let text = name + " was crowned"
                events.push({ year: regnalData.startDate.year, date: regnalData.startDate.display, text: text, rawText: text, file: item.file.name, sort: regnalData.startDate.sort })
            }
            // only include end dates if (a) they don't match the death date or (b) we didn't include death dates
            if (regnalData.endDate && (regnalData.endDate != pageExistData.endDate || !options.includeEnd)) {
                let text = name + " reign ended"
                events.push({ year: regnalData.startDate.year, date: regnalData.startDate.display, text: text, rawText: text, file: item.file.name, sort: regnalData.startDate.sort })
            }
        }
        if (options.includePartyMeetings) {            
            WhereaboutsManager.getPartyMeeting(item.file.frontmatter, undefined).forEach(element => {        
                let name = metadataUtils.get_Name(item.file, true, false)
                let uncap = element.text.charAt(0).toLowerCase() + element.text.slice(1)

                let processedText = name + " " + uncap
                
                events.push({ year: element.date.year, date: element.date.display, text: processedText, rawText: element.text, file: item.file.name, sort: element.date.sort })
            });
        }

        if (options.includeTravel && item.file.frontmatter.whereabouts && item.file.frontmatter.whereabouts.length > 0) {
            item.file.frontmatter.whereabouts.filter(e => e.start || e.end).forEach(element => {
                let parsedStart = DateManager.normalizeDate(element.start, false)
                let parsedEnd = DateManager.normalizeDate(element.end, true)
                let location = metadataUtils.get_Location(element)

                let arriveVerb = "was at"
                let departVerb = "left"

                if (parsedEnd || element.type == "home") {
                    // we have a start and an end, or a start for a home -- show as a range 
                    arriveVerb = "arrived at"
                    if (element.type == "home") {
                        arriveVerb = "moved to"
                    }
                }

                if (parsedEnd) {
                    let departText = name + " " + departVerb + " " + location
                    events.push({ year: parsedEnd.year, date: parsedEnd.display, text: departText, rawText: departText, file: item.file.name, sort: parsedEnd.sort })
                }

                if (parsedStart) {
                    let atText = name + " " + arriveVerb + " " + location
                    events.push({ year: parsedStart.year, date: parsedStart.display, text: atText, rawText: atText, file: item.file.name, sort: parsedStart.sort })
                }
            });
        }

        item.file.lists.where(t => t.DR != null).forEach(t => {            
            let jsDate = DateManager.normalizeDate(t.DR, false)
            if (jsDate != undefined) {
        
                let textWithDate = t.text;
                let pattern = /\(\w+:: -?\d{1,4}(?:-\d{1,2})?(?:-\d{1,2})?\):?/;
                let realText = textWithDate.replace(pattern, '').trim(); // trim() is used to remove any leading or trailing whitespace that may be left after the replacement

                let descriptor = item.file.frontmatter.timelineDescriptor ?? item.file.frontmatter.name

                if (item.file.frontmatter.type == "SessionNote") descriptor = item.file.frontmatter.campaign

                if (descriptor) {
                    realText = "*(" + descriptor + ")*: " + realText
                }            

                var obj = { year: jsDate.year, date: jsDate.display, file: item.file.name, text: realText, rawText: t.text, sort: jsDate.sort };                
                
                events.push(obj)
            }

        })        

        return events;
    }
    ).where(f => f.year >= yearStart && f.year <= yearEnd).sort(f => f.sort).map(map))
}

return await get_table(input);