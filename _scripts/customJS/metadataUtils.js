


class metadataUtils {

    privatehelper_getAge(older, younger) {

        if (older == undefined || younger == undefined) return undefined;

        let jsOlder = older.jsDate ?? older
        let jsYounger = younger.jsDate ?? younger
        var yearsDiff = jsOlder.getFullYear() - jsYounger.getFullYear();

        if (jsYounger.getMonth() > jsOlder.getMonth()) return yearsDiff - 1;
        else if (jsYounger.getMonth() == jsOlder.getMonth() && jsYounger.getDate() > jsOlder.getDate()) return yearsDiff - 1;

        return yearsDiff;
    }


    inLocation(targetLocation, metadata, targetDate) {


        if (!targetDate) targetDate = this.get_pageEventsDate(metadata)

        let current = this.get_currentWhereabouts(metadata, targetDate);
        if (current == undefined || current.location == undefined || current.location == "Unknown") {
            return false;
        }

        let found = this.locationSearch(current.location, targetLocation)

        return found;

    }

    homeLocation(targetLocation, metadata, targetDate, includeDead) {

        if (!targetDate) targetDate = this.get_pageEventsDate(metadata)

        if (includeDead || this.isPageAlive(metadata, targetDate)) {

            let home = this.get_homeWhereabouts(metadata, targetDate);
            if (home == undefined) return false;
            if (home.location == undefined || home.location == "Unknown") return false;

            let found = this.locationSearch(home.location, targetLocation)

            return found;
        }

        return false;
    }

    fromLocation(targetLocation, metadata, targetDate) {
        if (!targetDate) targetDate = this.get_pageEventsDate(metadata)

        let origin = this.get_originWhereabouts(metadata, targetDate);
        if (origin == undefined) return false;
        if (origin.location == undefined || origin.location == "Unknown") return false;

        let found = this.locationSearch(origin.location, targetLocation)

        return found;

    }

    locationSearch(startingLocation, targetLocation) {

        if (startingLocation.trim() === targetLocation.trim())
            return true;

        if (startingLocation.indexOf(",") == -1) {
            // we have a single string
            let file = window.app.metadataCache.getFirstLinkpathDest(startingLocation, ".");
            if (file) {
                let fm = window.app.metadataCache.getFileCache(file)
                if (fm && fm.frontmatter && fm.frontmatter.partOf) {
                    return this.locationSearch(fm.frontmatter.partOf, targetLocation)
                }

                return false;
            }

            console.log("Unable to retrieve linkpath for " + startingLocation)
            return false;
        } else {
            return startingLocation.contains(targetLocation)
        }
    }

    get_NameForFamily(input, link) {
        let file = window.app.metadataCache.getFirstLinkpathDest(input, ".");
        if (file) {

            let fm = window.app.metadataCache.getFileCache(file)
            if (!fm.frontmatter.tags || fm.frontmatter.tags.length == 0) return undefined
            if (fm.frontmatter.orgType != "family") return undefined
            if (fm.frontmatter.tags.filter(f => f.startsWith("organization")).length == 0) return undefined;
            return this.get_Name({ file: file, frontmatter: fm.frontmatter }, link)

        }

        return undefined
    }

    get_NameForPossibleLink(input, link, requiredTag) {
        let file = window.app.metadataCache.getFirstLinkpathDest(input, ".");
        if (file) {

            let fm = window.app.metadataCache.getFileCache(file)

            if (requiredTag) {
                if (!fm.frontmatter.tags || fm.frontmatter.tags.length == 0) return undefined
                if (fm.frontmatter.tags.filter(f => f.startsWith(requiredTag)).length == 0) return undefined;
            }

            return this.get_Name({ file: file, frontmatter: fm.frontmatter }, link)

        }

        return "[[" + input + "]]"
    }

    get_Name(input, link) {
        // we have three possible inputs - a templater "tp" object or a dataview "file" object or a constructed object where x.file is obsidian file and x.frontmatter is metadata

        let fileName = input.file ? (input.file.title ?? input.file.basename ?? input.file.name) : input.name;

        if (fileName == undefined) return fileName;

        let descriptiveName = fileName;

        if (input.frontmatter && input.frontmatter.name) {
            if (input.frontmatter.title) {
                descriptiveName = input.frontmatter.title + " " + input.frontmatter.name
            }
            else if (input.frontmatter.name) {
                descriptiveName = input.frontmatter.name
            }
        } else if (input.frontmatter && input.frontmatter.campaign) {
            if (input.frontmatter.sessionNumber) {
                descriptiveName = input.frontmatter.campaign + " " + input.frontmatter.sessionNumber
            }
        }

        if (descriptiveName == "Untitled") return undefined;

        if (!link) return descriptiveName;
        else if (descriptiveName == fileName) return "[[" + descriptiveName + "]]"
        else return "[[" + fileName + "|" + descriptiveName + "]]"
    }

    async get_party_name_for_party_without_metadata(prefix) {

        const metadataFilePath = app.vault.configDir + "/metadata.json";

        let metadataFile = await app.vault.adapter.read(metadataFilePath);
        metadata = JSON.parse(metadataFile);

        return this.get_party_name_for_party(metadata, prefix)

    }


    get_party_name_for_party(metadata, prefix) {

        let partyName = undefined;
        let campaignData = metadata.campaigns;
        if (campaignData) {
            let thisCampaign = campaignData.find(search => search.prefix.toUpperCase() == prefix.toUpperCase());
            if (thisCampaign) {
                partyName = thisCampaign.partyName;
                if (thisCampaign.partyFile) partyName = "[[" + thisCampaign.partyFile + "|" + partyName + "]]"
            }
        }

        return partyName;
    }

    parse_date_to_events_date(inputDate, isEnd) {
        function daysInMonth(dm, dy) {
            return new Date(dy, dm, 0).getDate();
        }

        function get_date_sort_string(jsDate) {
            return jsDate.getFullYear().toString().padStart(4, '0') + (jsDate.getMonth() + 1).toString().padStart(2, '0') + jsDate.getDate().toString().padStart(2, '0');
        }

        function get_displayDate(jsDate) {

            let currentFantasyCal = FantasyCalendarAPI.getCalendars()[0];
            let date = { year: jsDate.getFullYear(), month: jsDate.getMonth(), day: jsDate.getDate() };
            return FantasyCalendarAPI.getDay(date, currentFantasyCal).displayDate;
        }


        let jsDate = new Date(1, 0, 0, 0, 0, 0, 0);

        if (inputDate == undefined) return undefined;
        if (inputDate == "") return undefined;

        switch (typeof (inputDate)) {
            case "number":
                // this is a bare year           
                jsDate.setDate(isEnd ? 31 : 1)
                jsDate.setMonth(isEnd ? 11 : 0)
                jsDate.setFullYear(inputDate)
                return { display: "DR " + inputDate, sort: get_date_sort_string(jsDate), year: inputDate, jsDate: jsDate };

            case "string":
                // this is a string which we expect is either yyyy-mm-dd or yyyy-mm but something is wrong, most likely the actual year is not 4 digits
                let splitString = inputDate.split("-")
                if (splitString.length == 3) {
                    jsDate.setDate(parseInt(splitString[2]))
                    jsDate.setMonth(parseInt(splitString[1]) - 1)
                    jsDate.setFullYear(parseInt(splitString[0]))
                    return { display: get_displayDate(jsDate), sort: get_date_sort_string(jsDate), year: jsDate.getFullYear(), jsDate: jsDate };
                }
                else if (splitString.length == 2) {
                    let monthInt = parseInt(splitString[1]);
                    let dayInMonth = daysInMonth(monthInt, 1999)
                    if (dayInMonth == 29) dayInMonth = 28;

                    jsDate.setMonth(monthInt - 1)
                    jsDate.setDate(isEnd ? dayInMonth : 1)
                    jsDate.setFullYear(parseInt(splitString[0]))

                    let display = FantasyCalendarAPI.getCalendars()[0].static.months[monthInt - 1].name + " " + splitString[0];

                    return { display: display, sort: get_date_sort_string(jsDate), year: jsDate.getFullYear(), jsDate: jsDate };
                }

            case "object":
                if (inputDate.year == undefined) {
                    console.log("Error - unable to parse input date that is an object but doesn't have a year: " + inputDate)
                    return undefined;
                }

                if (inputDate.isLuxonDateTime) {
                    jsDate.setDate(inputDate.day ?? 1)
                    jsDate.setMonth(inputDate.month - 1 ?? 0)
                    jsDate.setFullYear(inputDate.year)
                } else {
                    // fantasy calendar, don't subtract 1
                    jsDate.setDate(inputDate.day ?? 1)
                    jsDate.setMonth(inputDate.month ?? 0)
                    jsDate.setFullYear(inputDate.year)
                }
                return { display: get_displayDate(jsDate), sort: get_date_sort_string(jsDate), year: jsDate.getFullYear(), jsDate: jsDate };
        }

        console.log("Error - unable to parse input date: " + inputDate)
        return undefined;
    }

    get_LocationFromPieces(singleLoc, depth) {

        if (singleLoc == undefined) return "Unknown"
        if (singleLoc == "") return "Unknown"
        if (typeof singleLoc === 'string' || singleLoc instanceof String) {

            if (singleLoc.indexOf(",") == -1) {
                // we have a single string
                let file = window.app.vault.getFiles().find(f => f.basename == singleLoc);
                if (file) {
                    let fm = window.app.metadataCache.getFileCache(file)
                    let name = this.get_Name({ file: file, frontmatter: fm.frontmatter }, true)
                    if (fm && fm.frontmatter && fm.frontmatter.partOf && depth < 2) {
                        let parent = this.get_LocationFromPieces(fm.frontmatter.partOf, depth + 1)
                        return name + ", " + parent
                    }

                    return name
                }

                return "[[" + singleLoc + "]]"
            }

            let locArrayValues = singleLoc.split(",").map(function (f) {
                let pieceValue = f.trim();
                let file = window.app.vault.getFiles().find(f => f.basename == pieceValue);
                if (file != undefined) {
                    return "[[" + pieceValue + "]]";
                }
                return pieceValue;
            });

            return locArrayValues.join(', ');
        }

        return "Unknown"
    }


    get_Location(place) {


        if (place == undefined) return "";
        if (place.region && !place.place) return this.get_LocationFromPieces(place.region, 0)
        if (!place.region && place.place) return this.get_LocationFromPieces(place.place, 0)
        if (place.region && place.place) return this.get_LocationFromPieces(place.place + ", " + place.region, 0)
        if (place.location) return this.get_LocationFromPieces(place.location, 0)

        return this.get_LocationFromPieces(place, 0)
    }

    get_pageEventsDate(metadata) {
        if (metadata && metadata.pageTargetDate) {
            return this.parse_date_to_events_date(metadata.pageTargetDate, false);
        }
        return this.parse_date_to_events_date(window.FantasyCalendarAPI.getCalendars()[0].current, false);
    }


    get_regnalData(metadata, targetDate) {
        if (!targetDate) targetDate = this.get_pageEventsDate(metadata)
        let status = { isStarted: undefined, isCurrent: undefined, startDate: undefined, endDate: undefined, length: undefined }

        status.endDate = this.parse_date_to_events_date(metadata.reignEnd, true) ?? this.parse_date_to_events_date(metadata.died, true);
        status.startDate = this.parse_date_to_events_date(metadata.reignStart, false)
        status.isStarted = status.startDate && status.startDate.sort <= targetDate.sort
        status.isCurrent = status.isStarted && (status.endDate == undefined || targetDate.sort < status.endDate.sort)

        if (status.startDate) {
            if (status.isCurrent) {
                status.length = this.privatehelper_getAge(targetDate, status.startDate)
            }
            else if (status.endDate) {
                status.length = this.privatehelper_getAge(status.endDate, status.startDate)
            }
        }

        return status;
    }

    isReignCurrent(metadata, targetDate) {
        return this.get_regnalData(metadata, targetDate).isCurrent
    }

    isReignStarted(metadata, targetDate) {
        return this.get_regnalData(metadata, targetDate).isStarted
    }

    isPageCreated(metadata, targetDate) {
        return this.get_pageExistenceData(metadata, targetDate).isCreated
    }

    isPageAlive(metadata, targetDate) {
        return this.get_pageExistenceData(metadata, targetDate).isAlive
    }

    get_pageExistenceData(metadata, targetDate) {
        if (!targetDate) targetDate = this.get_pageEventsDate(metadata)

        let status = {
            startDate: undefined,
            startDescriptor: undefined,
            endDate: undefined,
            endDescriptor: undefined,
            isCreated: true,
            isAlive: true,
            age: undefined
        }

        if (metadata.displayDefaults) {
            status.startDescriptor = metadata.displayDefaults.startStatus
            status.endDescriptor = metadata.displayDefaults.endStatus
            status.startPrefix = metadata.displayDefaults.startPrefix
            status.endPrefix = metadata.displayDefaults.endPrefix
        }

        if (metadata.born) {
            status.startDate = this.parse_date_to_events_date(metadata.born, false);
            if (!status.startDescriptor) status.startDescriptor = "born";
        } else if (metadata.created) {
            status.startDate = this.parse_date_to_events_date(metadata.created, false);
            if (!status.startDescriptor) status.startDescriptor = "created";
        }

        if (metadata.died) {
            status.endDate = this.parse_date_to_events_date(metadata.died, true);
            if (!status.endDescriptor) status.endDescriptor = "died";
        } else if (metadata.destroyed) {
            status.endDate = this.parse_date_to_events_date(metadata.destroyed, true);
            if (!status.endDescriptor) status.endDescriptor = "destroyed";
        }

        if (status.startDate) {
            status.isCreated = status.startDate.sort < targetDate.sort;
        }

        if (status.endDate) {
            status.isAlive = status.endDate.sort >= targetDate.sort;
        } else {
            status.isAlive = status.isCreated
        }


        if (status.startDate) {
            if (status.isAlive) {
                status.age = this.privatehelper_getAge(targetDate, status.startDate)
            }
            else if (status.endDate) {
                status.age = this.privatehelper_getAge(status.endDate, status.startDate)
            }
        }

        if (!status.startPrefix) status.startPrefix = status.startDescriptor[0] + "."
        if (!status.endPrefix && status.endDescriptor) status.endPrefix = status.endDescriptor[0] + "."

        return status;
    }

    parseWhereabouts_to_datedWhereabouts(whereaboutItem) {
        let start = this.parse_date_to_events_date(whereaboutItem.start, false);
        let end = this.parse_date_to_events_date(whereaboutItem.end, true);
        let logicalEnd = end ?? start;
        let jsDateMin = new Date('0001-01-01')

        if (!whereaboutItem.location) {
            let locToUse = undefined;
            if (whereaboutItem.place) {
                locToUse = whereaboutItem.place;
            }
            if (whereaboutItem.region) {
                if (locToUse) {
                    locToUse = locToUse + ", " + whereaboutItem.region;
                }
                else {
                    locToUse = whereaboutItem.region;
                }
            }

            whereaboutItem.location = locToUse;
        }

        return {
            item: whereaboutItem,
            normalizedStart: start ? start.jsDate : jsDateMin,
            startDate: start,
            endDate: end,
            logicalEnd: logicalEnd,
            duration: logicalEnd == undefined || start == undefined ? 0 : logicalEnd.jsDate - start.jsDate,
            type: whereaboutItem.type
        }
    }

    get_currentWhereabouts(metadata, targetDate) {

        if (!targetDate) targetDate = this.get_pageEventsDate(metadata)

        let pageExistDate = this.get_pageExistenceData(metadata, targetDate)

        if (!pageExistDate.isAlive) {
            return undefined;
        }

        let exactKnown = this.get_exactWhereabouts(metadata, targetDate)
        let home = this.get_homeWhereabouts(metadata, targetDate)
        let lastKnown = this.get_lastKnownWhereabouts(metadata, targetDate)

        if (exactKnown)
            return exactKnown;

        if (home && lastKnown) {
            let lastKnownEnd = this.parse_date_to_events_date(lastKnown.end)
            if (lastKnownEnd) {
                if (lastKnownEnd.sort < targetDate.sort) {
                    return home
                }
            }
        }
        else if (home) {
            return home;
        }

        return { location: undefined, type: "away" }
    }

    get_lastKnownWhereabouts(metadata, targetDate) {
        if (!targetDate) targetDate = this.get_pageEventsDate(metadata)

        function filter_lastKnown(f) {
            if (f.type == "away") {
                return (f.startDate != undefined && f.startDate.sort <= targetDate.sort)
            }
            else if (f.type == "home") {
                if (f.endDate) return f.endDate.sort < targetDate.sort;
            }

            return false;
        }
        if (metadata && metadata.whereabouts && metadata.whereabouts.length > 0) {
            let allowedWhereabouts = metadata.whereabouts.map(f => this.parseWhereabouts_to_datedWhereabouts(f))
                .filter(filter_lastKnown)
                .toSorted((a, b) => a.normalizedStart.jsDate - b.normalizedStart.jsDate);

            if (allowedWhereabouts.length > 0) return allowedWhereabouts.last().item;
        }
        return undefined;
    }

    get_originWhereabouts(metadata, targetDate) {

        if (metadata && metadata.whereabouts && metadata.whereabouts.length > 0) {

            if (!this.isPageCreated(metadata, targetDate)) return undefined;

            let allowedWhereabouts = metadata.whereabouts.map(f => this.parseWhereabouts_to_datedWhereabouts(f)).filter(f => f.type == "home" && f.startDate == undefined);
            if (allowedWhereabouts.length > 0) return allowedWhereabouts.first().item;
        }
        return undefined;
    }

    get_homeWhereabouts(metadata, targetDate) {
        function sort_date(a, b) {
            let indexA = a[0];
            let indexB = b[0];

            let startA = a[1].startDate;
            let startB = b[1].startDate;
            let endA = a[1].endDate;
            let endB = b[1].endDate;

            if (startA && startB)
                return startA.jsDate - startB.jsDate;

            if (startA)
                return 1;
            if (startB)
                return -1;

            if (!endA && !endB)
                return indexB - indexA;

            if (endA && endB)
                return endB.jsDate - endA.jsDate;

            if (endA)
                return -1;
            if (endB)
                return 1;

            // should be unreachable
            return 0;
        }

        if (metadata && metadata.whereabouts && metadata.whereabouts.length > 0) {
            if (!targetDate) targetDate = this.get_pageEventsDate(metadata)

            let pageExistData = this.get_pageExistenceData(metadata, targetDate)

            // if the person doesn't yet exist, they don't have a home
            if (!pageExistData.isCreated) return undefined;

            let allowedWhereabouts = metadata.whereabouts.map((f, index) => [index, this.parseWhereabouts_to_datedWhereabouts(f)]).filter(f => f[1].type == "home"
                && (f[1].startDate == undefined || f[1].startDate.sort <= targetDate.sort)
                && (f[1].endDate == undefined || (f[1].endDate && f[1].endDate.sort >= targetDate.sort)))
                .toSorted(sort_date)

            let hasOtherHomes = metadata.whereabouts.filter(f => f.type == "home").length > 1;

            if (allowedWhereabouts.length == 0) return undefined;

            let homePoss = allowedWhereabouts.first()[1];

            if (hasOtherHomes && allowedWhereabouts.length == 1 && !homePoss.startDate && !homePoss.endDate)
                return undefined;

            if (!homePoss.item.location)
                return undefined;

            return homePoss.item;
        }
        return undefined;
    }

    get_exactWhereabouts(metadata, targetDate) {
        if (metadata && metadata.whereabouts && metadata.whereabouts.length > 0) {
            if (!targetDate) targetDate = this.get_pageEventsDate(metadata)

            let allowedWhereabouts = metadata.whereabouts.map(f => this.parseWhereabouts_to_datedWhereabouts(f)).filter(f => f.type == "away"
                && f.startDate
                && f.startDate.sort <= targetDate.sort
                && f.logicalEnd.sort >= targetDate.sort).toSorted((a, b) => a.duration - b.duration);

            if (allowedWhereabouts.length > 0) return allowedWhereabouts.first().item;
        }
        return undefined;

    }
}
