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

    let pages = undefined;
    if (input.pageFilter) pages = dv.pages(input.pageFilter.trim());
    else pages = dv.pages();

    return await dv.table(header, pages.where(pageWhere).flatMap(item => {
        let events = [];
        
        let name = metadataUtils.get_Name(item.file, true)
      
        if (item.file.frontmatter.DR != null) {
            let jsDate = metadataUtils.parse_date_to_events_date(item.file.frontmatter.DR, false)

            console.log(item.file)

            if (item.file.frontmatter.summary) {
                name = "*(" + name + ")*: " + item.file.frontmatter.summary
            }            

            events.push({ year: jsDate.year, date: jsDate.display, text: name, rawText: name, file: item.file.name, sort: jsDate.sort })
        }

        if (options.includeCreate == true || options.includeEnd == true) {
            let pageExistenceData = metadataUtils.get_pageExistenceData(item.file.frontmatter)

            if (options.includeCreate && pageExistenceData.startDate) {
                let origin = metadataUtils.get_originWhereabouts(item.file.frontmatter)
                let text = name + " " + pageExistenceData.startDescriptor
                if (origin) {
                    text += " in " + metadataUtils.get_Location(origin)
                }

                events.push({ year: pageExistenceData.startDate.year, date: pageExistenceData.startDate.display, text: text, rawText: text, file: item.file.name, sort: pageExistenceData.startDate.sort })
            }

            if (options.includeEnd && pageExistenceData.endDate) {
                let diedSpot = metadataUtils.get_lastKnownWhereabouts(item.file.frontmatter, pageExistenceData.endDate)
                let text = name + " " + pageExistenceData.endDescriptor
                if (diedSpot) {
                    text += " in " + metadataUtils.get_Location(diedSpot)
                }

                events.push({ year: pageExistenceData.endDate.year, date: pageExistenceData.endDate.display, text: text, rawText: text, file: item.file.name, sort: pageExistenceData.endDate.sort })
            }

        }

        if (options.includeRegnal == true && item.file.frontmatter.reignStart != null) {
            let regnalData = metadataUtils.get_regnalData(item.file.frontmatter)
            let pageExistData = metadataUtils.get_pageExistenceData(item.file.frontmatter)
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
        if (options.includePartyMeetings && item.file.frontmatter.lastSeenByParty && item.file.frontmatter.lastSeenByParty.length > 0) {            
            item.file.frontmatter.lastSeenByParty.filter(element => element.prefix && element.date).forEach(async element => {
                let parsedDate = metadataUtils.parse_date_to_events_date(element.date, false);
                let locForThisDate = metadataUtils.get_currentWhereabouts(item.file.frontmatter, parsedDate);

                if (locForThisDate) {
                    let partyName = await metadataUtils.get_party_name_for_party(element.prefix)
                    if (partyName) {
                        let text = name + " meet " + partyName + " at " + metadataUtils.get_Location(locForThisDate)
                        events.push({ year: parsedDate.year, date: parsedDate.display, text: text, rawText: text, file: item.file.name, sort: parsedDate.sort })
                    }
                }
            });
        }

        if (options.includeTravel && item.file.frontmatter.whereabouts && item.file.frontmatter.whereabouts.length > 0) {
            item.file.frontmatter.whereabouts.filter(e => e.start || e.end).forEach(element => {
                let parsedStart = metadataUtils.parse_date_to_events_date(element.start, false)
                let parsedEnd = metadataUtils.parse_date_to_events_date(element.end, true)
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
            let jsDate = metadataUtils.parse_date_to_events_date(t.DR, false)
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