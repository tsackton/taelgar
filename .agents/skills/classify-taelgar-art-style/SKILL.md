---
name: classify-taelgar-art-style
description: Visually review Taelgar and RPGs images in batches, discover and revise style treatments, and retrieve illustrated examples from the private art catalog. Use for style discovery and reference lookup. Image generation and vault asset placement have their own workflows.
---

# Classify Taelgar art style

The catalog is at `~/Documents/RPGs/taelgar-art-catalog/`. Open `index.html` to browse, or use the script below for lookup. The catalog holds observations about art already in the collection. The user chooses any future art direction separately.

**Would the reason for grouping two images still hold if they depicted completely different things?** Look for the way an edge is made, how two colors meet, or how marks turn a flat shape into a volume. An inn and a castle can have very little in common visually. A tree and a face may share the same treatment.

## Review an image

Check the format first. Exclude framed tokens and battlemaps from the finished style gallery. A framed token uses an enclosing ring or square frame as a playing piece. A square portrait, circular vignette, or painted picture frame alone is insufficient. A battlemap depicts a space for tactical play at encounter scale, with or without a grid. Regional maps and settlement overviews can enter style discovery. When a token has an unframed source, review that source independently.

1. View the pixels. Use a labeled sheet to orient yourself, then open individual previews or originals wherever marks, outlines, a border or lettering are hard to resolve. A prompt in a filename is evidence about naming, never evidence of what the finished image looks like. Allow uncertainty about physical media and provenance.
2. Write a short, specific paragraph before assigning a group. Follow the most diagnostic features through two or three visible parts of the image. Consider line weight, lost or found edges, stroke direction, exposed ground, modeling, surface, palette, light, scale of detail and depth. Describe relationships. “Pale paper shows between the irregular brown lines of the ribs and through the amber wash” locates a technique; “warm, detailed fantasy illustration” could fit dozens of treatments.
3. Record broad subjects independently. Include a named person or place where a filename, caption, labeled map or unambiguous note identifies the depiction. Give the evidence. An embedding note can use a generic illustration or depict someone other than its title character.
4. Compare the image with actual members of the nearest treatments. Describe what they share and where they diverge. Use an existing treatment, propose a new candidate (a single example is sufficient), or record an uncertain match with alternatives in the basis. Name the treatment by the rendering. Use the families in the catalog’s style definitions. The five illustration families are Photographic realism, Painterly illustration, Drawn illustration, Stylized 3D illustration, and Sketches, prints and decorative art. Maps and Documents and diagrams have their own treatments. Use Unassigned for open illustration-family decisions. Each treatment belongs to one family. When a treatment appears to span families, compare the images with treatments in their assigned family and reapply the fitting treatment. Preserve detailed observations and choose the broad family by the overall look. Proposed review-sheet groups become treatments only after human review. Keep quality opinions, guessed generator versions and preferred future styles out of the discovery record.

## Finished catalog

Read `catalog.json` for the styles, corrected image descriptions, subjects, related image IDs, examples and source provenance. Full-size images and thumbnails have catalog-relative paths. A review ID can share its kept original with another review. Treat the source collection and former filenames as provenance. Use the copy under `originals/` to open or cite the artwork.

Use `scripts/catalog.py build` to render the finished index from the JSON. Use `verify` to check the gallery, archived originals and thumbnails. On this Mac use `~/.local/miniforge3/envs/taelgar/bin/python`. Batch discovery and temporary review materials belong in a separate working directory.

## Look up existing examples

Run `lookup 'Ink and watercolor illustration'` or search by subject or name in the gallery. Return the diagnostic description, a few representative originals across subjects where available, and the nearest alternative with its visual distinction. Open the originals before using them in a new brief. The bank records styles encountered and user corrections; approval to restyle an image is a separate task.
