* (DR:: 1510) : Thing 510
* (DR:: 1520) : Thing 520
* (DR:: 1530-01-01) : Thing with date
* (DR:: 20) : Thing with short
* (DR:: 1) : Founding of Drankor
* (DR:: 0003-02-02) Early Drankor
* (DR:: 3-01-20) Early Drankor


```dataviewjs
await dv.view("_scripts/view/get_EventsTable", {   yearStart: 1,   yearEnd: 2000,   pageFilter: "\"People/Chardonians\"",  includeAll : true })
 ```