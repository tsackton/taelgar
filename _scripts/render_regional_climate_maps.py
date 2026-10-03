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


def arrow(parent, points, color='wind', dashed=False, width=4.2):
    d = points if isinstance(points, str) else 'M' + ' L'.join(f'{x},{y}' for x, y in points)
    element(parent, 'path', d=d, fill='none', stroke='white', stroke_width=width+4)
    attrs = dict(d=d, fill='none', stroke=COLORS[color], stroke_width=width,
                 stroke_linejoin='round', stroke_linecap='round',
                 marker_end=f'url(#head-{color})')
    if dashed:
        attrs['stroke_dasharray'] = '9 7'
    return element(parent, 'path', **attrs)


def render(spec):
    source = ET.parse(ASSETS / f"taelgar-continental-pressure-{spec['season']}-v2.svg").getroot()
    source_main = source.find(f'{{{NS}}}g')
    original = source_main[9]
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
