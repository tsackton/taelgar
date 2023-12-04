class EventManager {

    getPartyMeeting(file, campaign) {

        const { TokenParser } = customJS
        const { NameManager } = customJS
        const { DateManager } = customJS
        const { WhereaboutsManager } = customJS

        let results = []

        let metadata = file.frontmatter
        let displayData = NameManager.getDisplayData(metadata)
        let pageType = NameManager.getPageType(metadata)

        let format = displayData?.wParty

        if (metadata.campaignInfo) {
            metadata.campaignInfo.filter(e => e.campaign && e.date).forEach(element => {

                let displayDate = DateManager.normalizeDate(element.date)
                let locForThisDate = WhereaboutsManager.getWhereabouts(metadata, element.date).current;

                let formatStr = element.wParty ?? element.format ?? format

                if (locForThisDate && (element.campaign == campaign || !campaign)) {
                    let person = element.person ?? element.campaign                    
                    if (person) {
                        let type = element.type ?? "seen"
                        let text = TokenParser.parseDisplayString(formatStr, {frontmatter: metadata, file: ""}, displayDate, {met: type, person: person, sourcePageType: pageType})
                        results.push({ text: text, campaign: element.campaign, date: displayDate, location: locForThisDate.location })
                    }
                }
            });
        }

        return results
    }

}