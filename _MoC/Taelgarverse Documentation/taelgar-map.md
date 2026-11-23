# `taelgar-map`

Use a `taelgar-map` block to embed an interactive map in Obsidian and on the Taelgarverse website. Use a version 2 manifest for artwork registered to the Taelgar world map, or an image-and-bounds block for a standalone map with its own coordinate scale.

## Version 2 maps

A version 2 fence references a vault `.map.json` manifest. Use a vault path or a quoted wikilink such as `"[[assets/campaign/green-sea-labeled.map.json]]"`. Give the block a stable `id` that is unique within its note, especially when editing a note with multiple maps.

````markdown
```taelgar-map
version: 2
id: green-sea-campaign-intro
source: assets/campaign/green-sea-labeled.map.json
height: 520px
fitBounds: false
minZoom: -2.75
maxZoom: 2
```
````

See [[Green Sea Campaign Intro#Welcome to the Green Sea|the Green Sea campaign map]] for a working example. Its manifest contains the following fields.

```json
{
  "version": 2,
  "image": "green-sea-labeled.png",
  "sourceOffset": [6290, 3745]
}
```

`image` is a PNG path relative to the manifest. `sourceOffset` is the position of the exported image’s top-left corner in the original Photoshop canvas, in `[x, y]` pixels. Use `[0, 0]` for a whole-canvas export. Version 2 maps use the shared world scale of 0.6 miles per native canvas pixel. Use the actual export offset and preserve the image’s native resolution so the grid, town markers, and measurements line up.

### Set the view

| Block option | Behavior |
| --- | --- |
| `crop` | Restricts the portion visible in this embed, including panning and **Fit map**. Omit it to show the full exported image. |
| `height`, `width` | Set the embedded size. The defaults are `650px` and `100%`. |
| `minZoom`, `maxZoom` | Bound zoom. The defaults are `-4` and `6`. |
| `fitBounds` | Fits the view to the available image or crop on load by default. Set `false` to start at the configured minimum zoom. |
| `grid` | Set `grid: {visible: true}` to show the adaptive block and hex grid on load. Use `showCoordinates: false` inside `grid` to hide coordinate readouts. |

Set a crop with a rectangle in original Photoshop pixels. X increases to the right and Y increases downward. The viewer intersects that rectangle with the exported image. A crop completely outside the export produces an error.

```yaml
crop: {x: 5000, y: 7000, width: 1200, height: 900}
```

You can also use inclusive hex references. Quote both values and use the same depth for slash references. In dotted notation, `16.10` starts at `16.10.A.01`, and `16.10.I.24` is the last hex in that block.

```yaml
crop:
  topLeft: "16.10"
  bottomRight: "17.12.I.24"
```

### Add layers and edit in Obsidian

- **Shared layers.** List `.map-layers.json` files under `layers` in the manifest, using paths relative to the manifest. To give readers a checkbox for a layer, use `toggleableLayers: [realms]` in the block. If more than one layer has that ID, use a vault path and ID such as `assets/maps/borders.map-layers.json#realms`. Each layer’s configured `visible` value supplies its initial visibility.
- **Regional artwork.** List exact vault-root-relative `.map-detail.json` paths under `details` in the block. The viewer displays those images automatically at the appropriate zoom.
- **Map editor.** Choose **Open map editor** below a version 2 map, or put the cursor in the block and run **Taelgarverse: Open current map in editor**. The editor opens the full export. **Place town** saves a position to the chosen settlement note’s `mapLocation` when you confirm the placement. The editor also supports shared region borders.
- **Create a map.** Run **Taelgarverse: Create map from image** to select or import a registered PNG, enter its world offset, and create a manifest and map note. To export directly from the source Photoshop file, use **Taelgarverse: Create map from Photoshop file**.

## Standalone image maps

Use `image` and `bounds` for a map with its own scale. Bounds are two increasing Leaflet coordinate pairs in `[y, x]` order. When using a local frame with one map unit per image pixel, use `[[0, 0], [imageHeight, imageWidth]]`, replacing the placeholders with numbers. `lat` and `long` optionally set the initial center in those same coordinates. `minZoom`, `maxZoom`, and `defaultZoom` control zoom.

````markdown
```taelgar-map
image: "[[My Map.png]]"
bounds: [[0, 0], [100, 200]]
height: 600px
```
````

For a calibrated standalone map, provide `calibration.hexMiles` and `calibration.hexPixels` for the same distance across opposite hex sides. `hexPixels` uses original image pixels. Set `calibration.imageSize` to the image’s original `[width, height]`, and optionally set `calibration.imageSha256` to verify the source image. If the supplied size or hash fails verification, the map still displays and measurement is disabled. An explicit calibration reports miles and takes precedence over the legacy `scale` and `unit` fields. A block with no calibration, scale, or unit reports map units. See [[World of Taelgar|Map of Taelgar]] for a calibrated example.

## Measure and sketch

Choose **Measure → Straight line** for a single segment or **Measure → Trace** to follow a route. A trace that closes can show perimeter and area. Measurements use flat map coordinates and are independent of zoom. Sketches and measurements in an embedded map are temporary.
