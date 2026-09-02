# Image Callouts

Taelgar images use three semantic roles. Choose the role first, use the standard size unless there is a clear reason not to, and place the callout where the image becomes relevant.

| Role | Use | Default display |
| --- | --- | --- |
| `aside` | NPC portraits, heraldry, small objects, and other supporting images | Floats right beside the text; standard width `20rem` |
| `figure` | Scene illustrations, maps, and images that deserve their own visual beat | Centered in the text; standard width `36rem` |
| `hero` | The strongest wide or establishing image | Full narrative width |

Named sizes are `small`, `standard`, and `large`.

| Size | Aside | Figure |
| --- | ---: | ---: |
| `small` | `12.5rem` | `24rem` |
| `standard` | `20rem` | `36rem` |
| `large` | `26rem` | `48rem` |

Images shrink to fit narrow displays. Semantic asides stop floating on narrow displays, while older image markup retains its existing behavior.

## Aside images

Use a right aside for the usual NPC portrait or supporting image:

```markdown
> [!image|right standard]
> ![[portrait.jpg]]
> *NPC name or a short contextual caption.*
```

Use `small` for compact heraldry, symbols, or objects:

```markdown
> [!image|right small]
> ![[duval-shield.png]]
> *The shield of House Duval.*
```

Use `left` only when it makes the surrounding composition work better:

```markdown
> [!image|left large]
> ![[important-npc.jpg]]
> *A larger portrait floated to the left.*
```

The callout floats from the point where it is written. Put it immediately before the paragraph it illustrates.

## Figure images

Figures interrupt the text flow and center the image:

```markdown
> [!image|figure standard]
> ![[ruined-fort.jpg]]
> *The ruined fort seen from the causeway.*
```

Use `figure large` for a detailed map or a particularly important scene:

```markdown
> [!image|figure large]
> ![[regional-map.png]]
> *The eastern frontier and its major routes.*
```

Place a figure after the paragraph or short passage that introduces what it depicts.

## Hero images

A hero fills the available narrative width:

```markdown
> [!image|hero]
> ![[festival-at-karawa.jpg]]
> *Karawa during the Festival of Rebirth.*
```

Use heroes sparingly. A note does not need one, and the hero does not need to be the first image or illustrate the first section.

## Galleries

Use a gallery when two or more related images should be read as one visual group:

```markdown
> [!gallery]
> - ![[temple-exterior.jpg]]
>   *The temple exterior.*
> - ![[temple-interior.jpg]]
>   *The central sanctuary.*
> - ![[temple-detail.jpg]]
>   *Carving above the inner door.*
```

The gallery chooses the number of columns that fit the available width and collapses naturally on narrow displays. Do not use a gallery merely because a note contains several images; use it when those images belong together at the same point in the text.

## Images without captions

A direct embed is acceptable when no caption is needed:

```markdown
![[portrait.jpg|right|small]]
```

Prefer a callout when the image needs a caption or when its role should be obvious to a future editor.

## Exact widths and older markup

Named sizes should cover most cases. An exact numeric width remains available for an unusual asset:

```markdown
> [!image|right]
> ![[unusually-shaped-object.png|180]]
> *A small object with an exceptional aspect ratio.*
```

Existing callouts such as `[!image|left]` or `[!image|right]`, and existing numeric embeds such as `![[portrait.jpg|right|400]]`, remain supported. There is no need to migrate them unless the sizing or placement is already unsatisfactory.

## Session recap images

Generated session notes take image instructions from the matching `session-recap.md`. Do not hand-edit the generated image placement when the recap is available.

The first image attached to a recap scene uses:

```markdown
- Image: scene-art.jpg
- Image Role: figure
- Image Size: standard
- Image Placement:
- Image Render:
- Image Caption: Visible caption text
- Image Alt: Concise visual description
```

Normally leave `Image Placement` and `Image Render` blank. An aside defaults to the start of its scene and the right side; a figure or hero defaults to the end of its scene. Use `Image Render: left` to put an aside on the left. A numeric render such as `right|280` remains an escape hatch.

Additional images use contiguous numbered fields:

```markdown
- Image 2: second-scene-art.jpg
- Image 2 Role: figure
- Image 2 Size: standard
- Image 2 Placement:
- Image 2 Render:
- Image 2 Caption: A second view of the same scene
- Image 2 Alt: Concise visual description
```

Consecutive figures in the same scene and at the same placement become a gallery automatically. Asides remain independent. Session images appear only in the Long zoom level on Taelgarverse.

## Lightbox

Press and hold an image to enlarge it in Obsidian Reading View or Live Preview. Release it to return to the note.
