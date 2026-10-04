#!/usr/bin/env python3
"""Render qualitative regional SVGs from the adopted continental SVG basemap.

Usage: python3 _scripts/render_regional_climate_maps.py [spec.json ...]
The default spec lives beside this script. PNG exports can be rendered by any
SVG renderer (the checked-in exports use sharp). Coordinates in specs use the
continental map's 1780 x 1376 map area, without its surrounding title/legend.
No climatic measurements or geographic geometry are inferred by this script.
"""
import copy
import json
from pathlib import Path
import sys
import textwrap
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets/worldbuilding'
NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)
COLORS = {'ink': '#233745', 'muted': '#64747d', 'high': '#c35b50',
          'low': '#478bbc', 'wind': '#8853b6', 'water': '#00968b'}


def element(parent, tag, **attrs):
    return ET.SubElement(parent, f'{{{NS}}}{tag}',
                         {k.replace('_', '-'): str(v) for k, v in attrs.items()})


def text(parent, x, y, value, size=20, color='ink', anchor='start'):
    el = element(parent, 'text', x=x, y=y, font_size=size,
                 fill=COLORS.get(color, color), text_anchor=anchor,
                 paint_order='stroke', stroke='#ffffff', stroke_width=4,
                 stroke_linejoin='round')
    el.text = value
    return el


def arrow(parent, points, color='wind', dashed=False, width=4.2, match_dash=False):
    d = points if isinstance(points, str) else 'M' + ' L'.join(f'{x},{y}' for x, y in points)
    backing = element(parent, 'path', d=d, fill='none', stroke='white', stroke_width=width+4)
    if dashed and match_dash:
        backing.set('stroke-dasharray', '9 7')
    attrs = dict(d=d, fill='none', stroke=COLORS[color], stroke_width=width,
                 stroke_linejoin='round', stroke_linecap='round',
                 marker_end=f'url(#head-{color})')
    if dashed:
        attrs['stroke_dasharray'] = '9 7'
    return element(parent, 'path', **attrs)


def render_regional_layers(spec, source, original):
    """Compose explicit regional layers, retaining shared source geometry verbatim."""
    x, y, w, h = spec['crop']
    width, margin, top = 1400, 45, 190
    map_width = width - 2 * margin
    map_height = round(map_width * h / w)
    footer = top + map_height + 38
    inset = spec.get('episode_inset')
    height = footer + (360 if inset else 200)
    root = ET.Element(f'{{{NS}}}svg', width=str(width), height=str(height),
                      viewBox=f'0 0 {width} {height}')
    element(root, 'title').text = spec['title']
    element(root, 'desc').text = spec['subtitle']
    defs = copy.deepcopy(source.find(f'{{{NS}}}defs'))
    root.append(defs)
    for key in ('wind', 'low', 'high', 'water'):
        marker = element(defs, 'marker', id=f'head-{key}', markerWidth=13,
                         markerHeight=11, refX=11, refY=5.5,
                         orient='auto', markerUnits='userSpaceOnUse')
        element(marker, 'path', d='M0,0 L13,5.5 L0,11 Z', fill=COLORS[key])
    for i, area in enumerate(spec.get('areas', [])):
        pattern = element(defs, 'pattern', id=f'regional-hatch-{i}',
                          width=8, height=8, patternUnits='userSpaceOnUse')
        element(pattern, 'path', d='M-2,2 L2,-2 M0,8 L8,0 M6,10 L10,6',
                fill='none', stroke=area['color'], stroke_width=1, stroke_opacity='.65')
    element(root, 'rect', width=width, height=height, fill='white')
    group = element(root, 'g', font_family='Arial, Helvetica, sans-serif')
    text(group, margin, 44, spec['title'].upper(), 28)
    text(group, margin, 79, spec['subtitle'], 19, 'muted')
    text(group, margin, 119, 'H / L', 23, 'ink')
    text(group, margin + 72, 119, 'Higher / lower pressure', 17)
    arrow(group, [[365, 112], [418, 112]], width=3)
    text(group, 432, 119, 'Air flow', 17)
    arrow(group, [[575, 112], [635, 112]], 'low', True, 3, True)
    text(group, 650, 119, 'Movement of passing storms', 17)
    text(group, width - margin, 119, 'N ↑', 23, 'muted', 'end')
    if spec.get('areas'):
        arrow(group, [[margin, 153], [margin + 60, 153]], 'wind', True, 3, True)
        text(group, margin + 76, 160, 'Occasional inland inflow', 17)
        element(group, 'rect', x=400, y=141, width=28, height=23,
                fill='url(#regional-hatch-0)', stroke=spec['areas'][0]['color'])
        text(group, 445, 160, 'Elven summer moisture', 17)
    else:
        text(group, margin, 160, 'Northern cold outbreaks are shown separately in the inset.', 17, 'muted')
    viewport = element(group, 'svg', x=margin, y=top, width=map_width,
                       height=map_height, viewBox=f'{x} {y} {w} {h}', overflow='hidden')
    viewport.append(copy.deepcopy(original[0]))
    # Every retained feature names its source location and checks its identity.
    # The Nevos low, trough and Darba inflow are never redrawn from local guesses.
    for feature in spec.get('source_elements', []):
        node = original
        for index in feature['indices']:
            node = node[index]
        if 'path_prefix' in feature and not node.get('d', '').startswith(feature['path_prefix']):
            raise ValueError(f"Source path changed: {feature}")
        if 'text' in feature and ''.join(node.itertext()) != feature['text']:
            raise ValueError(f"Source label changed: {feature}")
        viewport.append(copy.deepcopy(node))
    for i, area in enumerate(spec.get('areas', [])):
        element(viewport, 'path', d=area['path'], fill=area['color'], fill_opacity='.09')
        element(viewport, 'path', d=area['path'], fill=f'url(#regional-hatch-{i})',
                stroke=area['color'], stroke_width=1.1, stroke_dasharray='5 4')
    for route in spec.get('arrows', []):
        arrow(viewport, route['points'], route.get('color', 'wind'),
              route.get('dashed', False), route.get('width', 3.2), True)
    for item in spec.get('labels', []):
        text(viewport, item[0], item[1], item[2], item[3] if len(item) > 3 else 13,
             item[4] if len(item) > 4 else 'muted', 'middle')
    element(group, 'rect', x=margin, y=top, width=map_width, height=map_height,
            fill='none', stroke='#dce3e7', stroke_width=1)
    if inset:
        ix, iy, iw, ih = inset['crop']
        inset_width, inset_height = 440, 270
        text(group, margin, footer, inset['title'], 20)
        view = element(group, 'svg', x=margin, y=footer + 15,
                       width=inset_width, height=inset_height,
                       viewBox=f'{ix} {iy} {iw} {ih}', overflow='hidden')
        view.append(copy.deepcopy(original[0]))
        for route in inset['arrows']:
            arrow(view, route['points'], 'water', width=3.2)
        for item in inset['labels']:
            text(view, item[0], item[1], item[2], item[3], 'ink', 'middle')
        element(group, 'rect', x=margin, y=footer + 15, width=inset_width,
                height=inset_height, fill='none', stroke='#dce3e7', stroke_width=1)
        note_x, wrap_width = 530, 82
    else:
        note_x, wrap_width = margin, 132
    cursor = footer
    for note in spec.get('notes', []):
        for line in textwrap.wrap(note, wrap_width):
            text(group, note_x, cursor, line, 18)
            cursor += 25
        cursor += 16
    text(group, margin, height - 24, spec['footer'], 16, 'muted')
    output = ASSETS / (spec['file'] + '.svg')
    ET.ElementTree(root).write(output, encoding='unicode', xml_declaration=False)
    return output


def render(spec):
    source = ET.parse(ASSETS / f"taelgar-continental-pressure-{spec['season']}-v2.svg").getroot()
    source_main = source.find(f'{{{NS}}}g')
    original = source_main[9]
    if spec.get('regional_layers'):
        return render_regional_layers(spec, source, original)
    x, y, w, h = spec['crop']
    width, margin, top = 1700, 55, 160
    map_width = width - margin*2
    map_height = round(map_width*h/w)
    notes = spec.get('notes', [])
    footer = top + map_height + 44
    height = footer + max(140, len(notes)*59 + 55)
    root = ET.Element(f'{{{NS}}}svg', width=str(width), height=str(height),
                      viewBox=f'0 0 {width} {height}')
    element(root, 'title').text = spec['title']
    element(root, 'desc').text = spec['subtitle'] + ' Qualitative regional interpretation; no measured pressure, speed or rainfall values.'
    defs = copy.deepcopy(source.find(f'{{{NS}}}defs'))
    root.append(defs)
    for key in ('wind', 'low', 'high', 'water'):
        marker = element(defs, 'marker', id=f'head-{key}', markerWidth=13,
                         markerHeight=11, refX=11, refY=5.5,
                         orient='auto', markerUnits='userSpaceOnUse')
        element(marker, 'path', d='M0,0 L13,5.5 L0,11 Z', fill=COLORS[key])
    areas = spec.get('areas', [])
    for i, area in enumerate(areas):
        pattern = element(defs, 'pattern', id=f'regional-hatch-{i}',
                          width=8, height=8, patternUnits='userSpaceOnUse')
        element(pattern, 'path', d='M-2,2 L2,-2 M0,8 L8,0 M6,10 L10,6',
                fill='none', stroke=area['color'], stroke_width=1,
                stroke_opacity='.65')
    element(root, 'rect', width=width, height=height, fill='white')
    group = element(root, 'g', font_family='Arial, Helvetica, sans-serif')
    text(group, margin, 47, spec['title'].upper(), 29)
    text(group, margin, 83, spec['subtitle'], 20, 'muted')
    text(group, margin, 127, 'H', 24, 'high')
    text(group, margin+32, 127, 'Higher pressure', 18)
    text(group, margin+270, 127, 'L', 24, 'low')
    text(group, margin+298, 127, 'Lower pressure', 18)
    arrow(group, [[585, 119], [650, 119]])
    text(group, 670, 127, 'Air travels this way', 18)
    if areas:
        element(group, 'rect', x=905, y=107, width=28, height=23,
                fill='url(#regional-hatch-0)', stroke=areas[0]['color'])
        text(group, 945, 127, spec.get('area_legend', 'Local influence'), 18)
    text(group, width-margin, 127, 'N ↑  ·  schematic seasonal patterns', 18, 'muted', 'end')
    viewport = element(group, 'svg', x=margin, y=top, width=map_width,
                       height=map_height, viewBox=f'{x} {y} {w} {h}', overflow='hidden')
    interior = copy.deepcopy(original)
    interior.attrib.pop('transform', None)
    if spec.get('base_only'):
        interior[:] = [interior[0]]
    else:
        # Prevent labels from being cut in half at a regional frame edge.
        for e in list(interior):
            if e.tag == f'{{{NS}}}text':
                tx, ty = float(e.get('x', 0)), float(e.get('y', 0))
                label = ''.join(e.itertext())
                half = len(label)*float(e.get('font-size', 17))*.26
                if not (x+half+8 < tx < x+w-half-8 and y+22 < ty < y+h-10):
                    interior.remove(e)
    for parent in interior.iter():
        for child in list(parent):
            if any(child.get('d', '').startswith(prefix)
                   for prefix in spec.get('omit_path_prefixes', [])):
                parent.remove(child)
    viewport.append(interior)
    # Local departures stay visually distinct from pressure contours and winds.
    area_layer = ET.Element(f'{{{NS}}}g')
    if areas:
        interior.insert(1, area_layer)
    for i, area in enumerate(areas):
        element(area_layer, 'path', d=area['path'], fill=area['color'], fill_opacity='.12')
        element(area_layer, 'path', d=area['path'], fill=f'url(#regional-hatch-{i})',
                stroke=area['color'], stroke_width=1.5, stroke_dasharray='5 4')
    # Keep geographic labels above new routes, as in the continental maps.
    routes = ET.Element(f'{{{NS}}}g')
    interior.insert(min(2, len(interior)), routes)
    for path in spec.get('arrows', []):
        arrow(routes, path['points'], path.get('color', 'wind'), path.get('dashed', False))
    for item in spec.get('labels', []):
        text(viewport, item[0], item[1], item[2], item[3] if len(item)>3 else 17, 'muted', 'middle')
    for item in spec.get('centers', []):
        cx, cy, symbol, label, rx, ry = item
        color = 'high' if symbol == 'H' else 'low'
        element(viewport, 'ellipse', cx=cx, cy=cy, rx=rx, ry=ry,
                fill='none', stroke=COLORS[color], stroke_width=1.7, opacity='.7')
        text(viewport, cx, cy, symbol, 35, color, 'middle')
        text(viewport, cx, cy+25, label, 16, 'ink', 'middle')
    for i, item in enumerate(spec.get('points', []), 1):
        cx, cy = item
        element(viewport, 'circle', cx=cx, cy=cy, r=12,
                fill='white', stroke=COLORS['ink'], stroke_width=1.3)
        text(viewport, cx, cy+5, str(i), 15, 'ink', 'middle')
    element(group, 'rect', x=margin, y=top, width=map_width, height=map_height,
            fill='none', stroke='#dce3e7', stroke_width=1)
    for i, note in enumerate(notes):
        lines = textwrap.wrap(note, 135)
        for j, line in enumerate(lines):
            text(group, margin, footer+i*59+j*25, line, 19, 'ink')
    text(group, margin, height-27,
         spec.get('footer', 'Contours show broad recurring features, not isobars. Dashed winds are episodic. Small hexes: 24 miles face to face.'),
         17, 'muted')
    output = ASSETS / (spec['file'] + '.svg')
    ET.ElementTree(root).write(output, encoding='unicode', xml_declaration=False)
    return output


if __name__ == '__main__':
    specs = [Path(p) for p in sys.argv[1:]] or [Path(__file__).with_name('regional_climate_maps.json')]
    for path in specs:
        for spec in json.loads(path.read_text()):
            print(render(spec).relative_to(ROOT))
