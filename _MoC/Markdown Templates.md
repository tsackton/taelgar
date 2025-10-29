prompt:
```
please examine the directory "People/Addermanians". for each note, choose one of the four templates in _templates/markdown/people-* and reformat the note to fit the chosen template.

use detail from the note itself as well as linked pages, backlinks, and other mentions of the person in session notes, _dm_notes, DM, or other places in the repository to fill in details.

extremely important (his is the most important instruction you have. be extremeley careful to make sure you do exactly this even if other prompt instructions conflict): if there is text in the note itself, you can reformat it, but NEVER DELETE DETAILS and NEVER CHANGE THE MEANING OF TEXT if it is already written in the note itself. if this information conflicts with other information in the vault, summarize the conflict in the %% comments section.

do not invent details that are not present in notes.

do not include optional headers, metadata, or DM notes unless there is relevant information to include.

all non-DM content should be written from an in-world perspective, using a Wikipedia-style tone. do not refer to "the advventures" or "the party" - this is a meta-game concept. you can use a party name or character names if necessary, but most notes should be written to be agnostic to specific campaigns. events should not refer directly to session notes. if you link to session notes, use a linking alias (e.g. [[link target|display text]]).

do not edit a note if it is already matches the appropriate template.

add tag "status/check/ai" to all notes that are edited.

if there are relevant campaign interactions, make sure to include them, with links, in the %% comments section. only use the campaignInfo line particularly important interactions (always include first met; include last seen if relevant and obvious; include significant other interactions where they are important)
```


Another prompt:
```
please do another pass to address the following:

(1) promote major recurring figures to the high detail template  
(2) rewrite text where needed to generalize notes, removing meta-game language and references to "the party" or "the adventurers", and replacing with character names or the party name (Addermarch Mercanaries) as appropriate; and to push towards a consistent "in world wikipedia" style. be careful not to change meaning while you do this, or remove detail. only change style.  
(3) reformat front matter, adding missing fields where possible to align with templates  
(4) make sure that all event sections are properly formatted as timeline-style notes  
(5) expand DM notes / comment sections to capture as much as possible about PC interactions, even for minimal or standard notes. you may link directly to DM notes or session notes, without aliases, in the comment section.
```

another prompt:
```
vplease check Addermarch - Session 11 and Addermarch - Session 12 notes and update notes in Addermarch staging based on information there

please also check all Addermarch stagig notes, and move any metagame information or DM information to comments (wrapped with %% tags)
```

another prompt, slight modification of prompt 1:

```
please examine the directory "People/Addermanians". for each note, choose one of the four templates in _templates/markdown/people-* and reformat the note to fit the chosen template.

use detail from the note itself as well as linked pages, backlinks, and other mentions of the person in session notes, _dm_notes, DM, or other places in the repository to fill in details.

extremely important (his is the most important instruction you have. be extremeley careful to make sure you do exactly this even if other prompt instructions conflict): if there is text in the note itself, you can reformat it, but NEVER DELETE DETAILS and NEVER CHANGE THE MEANING OF TEXT if it is already written in the note itself. if this information conflicts with other information in the vault, summarize the conflict in the %% comments section. however, you can rewrite text where needed to generalize notes, removing meta-game language and references to "the party" or "the adventurers", and replacing with character names or the party name as appropriate; and to push towards a consistent "in world wikipedia" style. be careful not to change meaning while you do this, or remove detail. only change style.

do not invent details that are not present in notes.

do not include optional headers, metadata, or DM notes unless there is relevant information to include.

all non-DM content should be written from an in-world perspective, using a Wikipedia-style tone. do not refer to "the advventures" or "the party" - this is a meta-game concept. you can use a party name or character names if necessary, but most notes should be written to be agnostic to specific campaigns. events should not refer directly to session notes. if you link to session notes, use a linking alias (e.g. [[link target|display text]]).

do not edit a note if it is already matches the appropriate template.

add tag "status/check/ai" to all notes that are edited.

if there are relevant campaign interactions, make sure to include them, with links, in the %% comments section. only use the campaignInfo line particularly important interactions (always include first met; include last seen if relevant and obvious; include significant other interactions where they are important)
```