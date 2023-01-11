---
built: 1599
destroyed: 1742
yearOverride: 1743
reignStart: 1741
died: 1742
location: abc
location_clee: 123
---


_<%+ tp.user.getAgeBasedValue(tp, { startPrefix: "built", preExistError: "(not yet build)", endPrefix: "burned down in"}) %>_
<%+ tp.user.getRegnalValue(tp) %>

Location: <%+ tp.user.getCampaignBasedValue(tp, "location") %>



