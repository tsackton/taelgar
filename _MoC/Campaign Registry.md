# Campaign Registry

linterAudienceSpecialValues:: "all", "none"

The field above records the reserved non-campaign `audience` values recognized by the validator. It does not settle the positive campaign-audience design discussed below.

The authoritative machine-readable campaign registry is `_scripts/session_note_campaigns.json`. It supplies both campaign metadata conventions and session-note pipeline configuration. Other files may retain compatibility copies temporarily, but linters and new tools must validate against this registry rather than infer codes from folder names or legacy metadata.

## Canonical names and codes

| Campaign name          | Campaign code |
| ---------------------- | ------------- |
| Addermarch             | `adma`        |
| Dunmar Frontier        | `dufr`        |
| Cleenseau              | `clee`        |
| Great Library          | `grli`        |
| Mawar Adventures       | `mawar`       |
| Into the Chasm         | `itc`         |
| Labyrinths of the Lost | `lablost`     |
| Lost in the Feywild    | `feywild`     |

Campaign codes are always lowercase. Aliases in the registry exist only to recognize older spellings, mixed-case codes, folder terminology, and command-line input; they are not canonical authored values.

## Authored metadata rules

- `campaign` identifies campaign-owned documents such as session notes, campaign meta pages, and campaign source material. It uses the canonical long campaign name: `campaign: Dunmar Frontier`.
- `knownTo` uses canonical short codes: `knownTo: [dufr, grli]`.
- The `campaign` key inside each `campaignInfo` dictionary uses a canonical short code: `{campaign: dufr, date: 1748-05-05, type: met}`.
- Campaign content blocks use canonical short codes: `%%^Campaign:dufr%%`.
- `%%^Campaign:none%%` is the reserved marker for shared DM material that is not associated with a player campaign.

This registry does not settle the still-underdeveloped semantics of positive `audience` values. If that field is retained, its representation should be specified separately rather than inferred from the three short-code uses above.

A linter may accept a configured alias long enough to identify the intended campaign, but it must report the noncanonical representation and offer the correct long name or lowercase short code as appropriate to the field.

## Registry fields

Every campaign entry requires:

- `name`: canonical long name used in `campaign` frontmatter;
- `code`: canonical lowercase short code used in campaign-scoped metadata and blocks;
- `aliases`: recognized noncanonical names or codes;
- `sessionRoot`: corresponding directory under `_sessions`;
- `campaignRoot`: campaign directory in the vault;
- `notePattern`: session-note path pattern relative to `campaignRoot`; and
- `defaultTemplate`: session-note template used by the component builder.

`partyPage` is optional and identifies the party page when one exists. Registry validation should reject missing names or codes, non-lowercase codes, duplicate codes, and aliases that resolve to more than one campaign.

## Compatibility

The older campaign list in `.obsidian/metadata.json` remains a compatibility input for older header and export code. It is not authoritative for linting and must not override the names or codes in `_scripts/session_note_campaigns.json`. Consumers should migrate to the authoritative registry or to generated compatibility data derived from it.
