<%*
// need to reformat dates nicely //

// calculate session start string

sessionStartString = tp.frontmatter.sessionStartDate + ", " + tp.frontmatter.sessionStartTime
sessionEndString = tp.frontmatter.sessionEndDate + ", " + tp.frontmatter.sessionEndTime

%># Session <% tp.frontmatter.sessionNumber %>
(<% tp.frontmatter.realWorldDate %>)

## Summary

## Meta Information

Start: <% sessionStartString %>
End:  <% sessionEndString %>

## Timeline


## Narrative
