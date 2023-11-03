function get_date_sort_string(jsDate) {
    return jsDate.getUTCFullYear().toString().padStart(4, '0') + (jsDate.getUTCMonth()+1).toString().padStart(2,'0') + jsDate.getUTCDate().toString().padStart(2,'0');
}

function get_displayDate(jsDate) {
  
    let currentFantasyCal = window.FantasyCalendarAPI.getCalendars()[0];    
    let date = {year: jsDate.getUTCFullYear(), month: jsDate.getUTCMonth(), day: jsDate.getUTCDate()};
    console.log(date);
    return window.FantasyCalendarAPI.getDay(date, currentFantasyCal).displayDate;      
}

function parse_date_to_events_date(inputDate) {
    let jsDate = new Date(1,0,0,0,0,0,0);
 
    switch (typeof(inputDate)) {
        case "number":
            // this is a bare year           
            jsDate.setMonth(0)
            jsDate.setDate(1)
            jsDate.setFullYear(inputDate)

            return  { display : "DR " + inputDate, sort : get_date_sort_string(jsDate), year : inputDate };

        case "string":
            // this is a string which we expect is either yyyy-mm-dd or yyyy-mm but something is wrong, most likely the actual year is not 4 digits
            let splitString = inputDate.split("-")
            if (splitString.length == 3) {
                jsDate.setFullYear(parseInt(splitString[0]))
                jsDate.setMonth(parseInt(splitString[1])-1)
                jsDate.setDate(parseInt(splitString[2]))

                return  { display : get_displayDate(jsDate), sort : get_date_sort_string(jsDate), year : jsDate.getUTCFullYear() };
            }
            else if (splitString.length == 2) {
                jsDate.setFullYear(parseInt(splitString[0]))
                jsDate.setMonth(parseInt(splitString[1])-1)    
                jsDate.setDate(1)            

                return  { display : get_displayDate(jsDate), sort : get_date_sort_string(jsDate), year : jsDate.getUTCFullYear()};                
            }

        case "object":
            if (inputDate.year == undefined) {
                console.log("Error - unable to parse input date that is an object but doesn't have a year: " + inputDate)
                return undefined;            
            }

            jsDate.setFullYear(inputDate.year)
            jsDate.setMonth( inputDate.month-1 ?? 0)
            jsDate.setDate(inputDate.day ?? 1)
            return  { display : get_displayDate(jsDate), sort : get_date_sort_string(jsDate), year : jsDate.getUTCFullYear()};
    }

    console.log("Error - unable to parse input date: " + inputDate)
    return undefined;
}



function get_table(input) {

    let yearStart = input.yearStart;
    let yearEnd = input.yearEnd ?? input.yearStart;
    let pageFilter = input.pageFilter ?? "#event-source";
    let map = input.map ?? (f => [f.date, f.text, dv.fileLink(f.file)])
    let header = input.header ?? ["Date", "Event", "File"]
    let options = input.options ?? {};
   
    return dv.table(header, dv.pages(pageFilter).flatMap(item => {
        
        console.log(item.file.name);

        if (item.file.lists.length == 0) {
            console.log("no lists");

            if (item.file.frontmatter.DR != null) {
                console.log("has DR");
                let jsDate = parse_date_to_events_date(item.file.frontmatter.DR)
                return [{ year: jsDate.year, date: jsDate.display, text: item.file.name, rawText: item.file.name, file: item.file.name, sort: jsDate.sort }];
            }

            let events = [];
            /* born: 1700
reignStart: 1717
died: 1718*/

            if (options.includeBirthEvents == true && item.file.frontmatter.born != null) {
                console.log("has bday");
                let jsDate = parse_date_to_events_date(item.file.frontmatter.born)
                let text = "[[" + item.file.name + "]] was born"                
                events.push({ year: jsDate.year, date: jsDate.display, text: text, rawText: text, file: item.file.name, sort: jsDate.sort })
            }

            return events;
        } 
        else {
            console.log("lists");
            return item.file.lists.where(t => t.DR != null).map(t => {
                let textWithDate = t.text;
                let pattern = /\(\w+:: \d{4}(?:-\d{2})?(?:-\d{2})?\):?/;
                let realText = textWithDate.replace(pattern, '').trim(); // trim() is used to remove any leading or trailing whitespace that may be left after the replacement
                let jsDate = parse_date_to_events_date(t.DR)
                var obj =  { year: jsDate.year, date: jsDate.display, file: item.file.name, text: realText, rawText: t.text, sort: jsDate.sort  };
               
                return obj;
            })
        }
    }).where(f => f.year >= yearStart && f.year <= yearEnd).sort(f => f.sort).map(map))
}

return get_table(input);