#!/usr/bin/env python3
"""Draw two qualitative ocean figures from the reviewed v3 geographic paths.

The basin figure reuses its exact cropped basemap and existing current paths.
The Gulf figure reuses the geographic inset, then adds the adopted vertical
exchange as an explicitly unscaled section. No channel geometry is inferred.
"""
import copy
from pathlib import Path
import xml.etree.ElementTree as E

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets/worldbuilding'
NS = 'http://www.w3.org/2000/svg'
E.register_namespace('', NS)
C = {'ink':'#233745', 'muted':'#64747d', 'cold':'#478bbc',
     'warm':'#c7773f', 'water':'#00968b', 'wind':'#8853b6'}
OLD = E.parse(ASSETS / 'taelgar-green-sea-currents-v3.svg').getroot()
VIEWS = list(OLD.iter(f'{{{NS}}}svg'))


def e(parent, tag, **attrs):
    return E.SubElement(parent, f'{{{NS}}}{tag}',
                        {k.replace('_','-'):str(v) for k,v in attrs.items()})


def t(parent, x, y, value, size=20, color='ink', anchor='start', halo=4):
    node=e(parent,'text',x=x,y=y,font_size=size,fill=C.get(color,color),
           text_anchor=anchor,paint_order='stroke',stroke='white',
           stroke_width=halo,stroke_linejoin='round')
    node.text=value
    return node


def root(title, subtitle, height):
    r=E.Element(f'{{{NS}}}svg',width='1700',height=str(height),viewBox=f'0 0 1700 {height}')
    e(r,'title').text=title
    e(r,'desc').text=subtitle+' Qualitative adopted model; no measured speed, depth, or transport.'
    d=e(r,'defs')
    for name,color in C.items():
        m=e(d,'marker',id=f'arrow-{name}',markerWidth=12,markerHeight=10,
            refX=10,refY=5,orient='auto',markerUnits='userSpaceOnUse')
        e(m,'path',d='M0,0 L12,5 L0,10 Z',fill=color)
        m=e(d,'marker',id=f'map-{name}',markerWidth=3,markerHeight=2.6,
            refX=2.5,refY=1.3,orient='auto',markerUnits='userSpaceOnUse')
        e(m,'path',d='M0,0 L3,1.3 L0,2.6 Z',fill=color)
    e(r,'rect',width=1700,height=height,fill='white')
    g=e(r,'g',font_family='Arial, Helvetica, sans-serif')
    t(g,55,47,title.upper(),29)
    t(g,55,83,subtitle,20,'muted')
    return r,g


def arrow(parent, d, color, width=4, dashed=False, small=False, halo=True):
    if halo:
        e(parent,'path',d=d,fill='none',stroke='white',stroke_width=width+(1 if small else 4))
    a=e(parent,'path',d=d,fill='none',stroke=C[color],stroke_width=width,
        stroke_linejoin='round',stroke_linecap='round',
        marker_end=f'url(#{"map" if small else "arrow"}-{color})')
    if dashed: a.set('stroke-dasharray','1.3 1' if small else '9 7')
    return a


def basin():
    r,g=root('Green Sea · Ocean circulation',
             'Cold northeastern and warm southeastern inflows feed a shared offshore return toward the east.',1420)
    for x,name,label in [(55,'cold','Cold northern inflow'),(425,'warm','Warm southern inflow'),(810,'water','Shared eastward return')]:
        arrow(g,f'M{x},120 h60',name)
        t(g,x+78,128,label,18)
    t(g,1645,128,'N ↑  ·  water movement',18,'muted','end')
    vp=copy.deepcopy(VIEWS[1]); vp.set('x','55'); vp.set('y','160'); vp.set('width','1590'); vp.set('height','938')
    for n in list(vp):
        if n.tag==f'{{{NS}}}text' or n.tag==f'{{{NS}}}rect' or n.tag==f'{{{NS}}}path': vp.remove(n)
    img=vp[0]
    e(vp,'rect',x=780,y=255,width=1127,height=665,fill='white',fill_opacity='.72')
    # Put the new veil directly above the basemap and below current paths.
    veil=vp[-1];vp.remove(veil);vp.insert(1,veil)
    colors={'#2166ac':C['cold'],'#d06b25':C['warm'],'#078b81':C['water'],
            '#fcfbf8':'#ffffff','#6b7478':C['muted']}
    for n in vp.iter():
        for attr in ('fill','stroke'):
            if n.get(attr) in colors:n.set(attr,colors[n.get(attr)])
    def label(x,y,v,size=13,c='muted',anchor='middle'):
        t(vp,x,y,v,size,c,anchor,2.7)
    for x,y,v in [(835,365,'Sembara'),(910,295,'Vostok'),(1030,312,'Skaerhem'),(1260,330,'Ursk'),(950,540,'Cymea'),(1340,560,'Irrla'),(1510,865,'Medju'),(1820,570,'Eastern Isles'),(1820,615,'Outer Ocean')]:label(x,y,v)
    label(830,420,'Tollen',11,anchor='start');label(837,513,'Western Gulf',10)
    label(1280,754,'Maritime Trade',11);label(1280,770,'Peninsula',11)
    label(1510,305,'Cold northern inflow',15,'cold')
    label(1210,397,'Coastal branch',11,'cold')
    label(1450,490,'Shared offshore return',15,'water')
    label(1450,509,'Surface slows where summer easterlies oppose it',11,'water')
    label(1500,635,'Warm southern inflow',15,'warm')
    label(1500,655,'Westward, then north through the western basin',11,'warm')
    label(1060,483,'Confluence',12,'water');label(1060,500,'Mixing continues downstream',9,'water')
    label(1080,560,'Warm branch',11,'warm');label(1080,576,'turns north',11,'warm')
    label(1820,375,'Northern exchange',10,'cold');label(1820,390,'through / beneath isles',9,'cold')
    label(1770,520,'Eastern exits',10,'water');label(1785,726,'Southern exchange',10,'warm')
    label(1500,585,'GREEN SEA',19)
    g.append(vp)
    e(g,'rect',x=55,y=160,width=1590,height=938,fill='none',stroke='#dce3e7')
    rows=[('Winter and spring','Northern westerly intervals assist eastward surface flow. Winter mixing replenishes nutrients; increasing light supports spring growth.'),
          ('Summer','Northern easterlies strengthen the coastal westward branch. Offshore surface return weakens; broader or deeper export continues.'),
          ('Autumn','Returning westerlies assist offshore eastward flow. Waves against a persisting westward coastal current can become steep.'),
          ('Eastern exchange','Dashed paths cross the moving island chain at unassigned depths and passages. Gulf exchange is detailed on its separate figure.')]
    for i,(title,body) in enumerate(rows):
        y=1140+i*57;t(g,55,y,title,20);t(g,265,y,body,18)
    t(g,55,1390,'Schematic corridors, not pilotage tracks. No current speeds or sea-ice boundaries are assigned. Small hexes: 24 miles face to face.',17,'muted')
    E.ElementTree(r).write(ASSETS/'taelgar-green-sea-currents-v4.svg',encoding='unicode')


def gulf():
    r,g=root('Western Gulf · Layered exchange',
             'Freshwater surplus drives surface export through deep straits, above a cold, saltier inflow.',1390)
    arrow(g,'M55,120 h60','water');t(g,135,128,'Surface export',18)
    arrow(g,'M425,120 h60','cold',dashed=True);t(g,505,128,'Deeper inflow',18)
    arrow(g,'M805,120 h60','wind');t(g,885,128,'Summer wind',18)
    t(g,1645,128,'N ↑  ·  map plus unscaled section',18,'muted','end')
    vp=e(g,'svg',x=55,y=175,width=820,height=647,viewBox='801 420 190 150',overflow='hidden')
    vp.append(copy.deepcopy(VIEWS[2][0]))
    e(vp,'rect',x=801,y=420,width=190,height=150,fill='white',fill_opacity='.72')
    # Common plan-view corridor: the depth separation is shown in the section.
    points=[(893,472),(900,463),(908,462),(913,460),(917,459),(919,460),(922,460),(925,459),(928,456),(931,453.5),(938,454),(944,454),(950,453),(962,451),(981,452)]
    d='M'+' L'.join(f'{x},{y}' for x,y in points)
    arrow(vp,d,'water',1.25,small=True)
    reverse='M'+' L'.join(f'{x},{y}' for x,y in reversed(points))
    # Dash overlays use the same corridor rather than implying separate channels.
    arrow(vp,reverse,'cold',.65,dashed=True,small=True,halo=False)
    for x,y,v,sz,c,anchor in [(809,437,'Tollen / Volta',5.7,'ink','start'),(825,500,'Western Gulf',6.2,'muted','start'),(951,534,'Cymea',7,'muted','middle'),(939,478,'Deep Straits of Cymea',5.2,'ink','middle'),(850,544,'Summer upwelling',5.4,'cold','middle'),(846,552,'on exposed Cymean shores',4.2,'cold','middle')]:
        t(vp,x,y,v,sz,c,anchor,1)
    e(vp,'path',d='M939,471 L940,455',stroke=C['muted'],stroke_width='.45',fill='none')
    # Southward alongshore wind; rightward Ekman transport is west, offshore.
    arrow(vp,'M886,493 L885,518','wind',1,small=True)
    arrow(vp,'M879,512 L869,512','cold',.9,small=True)
    e(vp,'path',d='M850,539 L870,515',stroke=C['cold'],stroke_width='.45',fill='none')
    e(g,'rect',x=55,y=175,width=820,height=647,fill='none',stroke='#dce3e7')
    t(g,920,200,'STRAIT SECTION · NOT TO SCALE',20)
    t(g,940,241,'Western Gulf',21);t(g,1620,241,'Main Green Sea',21,anchor='end')
    e(g,'rect',x=940,y=285,width=680,height=98,fill='#e7f4f1')
    e(g,'rect',x=940,y=383,width=680,height=166,fill='#eaf2f8')
    e(g,'path',d='M940,285 H1620 M940,549 H1620',fill='none',stroke='#cbd8df',stroke_width=2)
    arrow(g,'M995,335 H1575','water',6)
    t(g,1280,315,'Fresher, less dense surface water',19,'water','middle')
    arrow(g,'M1575,447 H995','cold',6,dashed=True)
    t(g,1280,490,'Cold, saltier water enters below',19,'cold','middle')
    t(g,920,588,'Both layers use the deep passage.',20)
    t(g,920,625,'Mixing exchanges heat and salt between them.',19)
    t(g,920,662,'Net export includes the river and rain surplus.',19)
    t(g,920,699,'Wind and tides can reverse local flow temporarily.',19)
    t(g,920,736,'No depth, layer thickness or current speed is assigned.',18,'muted')
    t(g,55,874,'SUMMER COASTAL RESPONSE',21)
    t(g,55,913,'Along west-facing Cymean shores, southward winds favor offshore transport and localized upwelling.',20)
    t(g,55,948,'The opposing east-facing shores favor onshore transport and downwelling. Headlands and seabed modify the pattern.',20)
    t(g,55,1008,'SEASONAL EXPRESSION',21)
    lines=[('Winter','Cooling erodes thermal layering; freshwater can still preserve a surface-to-depth density contrast.'),
           ('Spring','Runoff and increasing light support coastal growth; river timing varies between catchments.'),
           ('Summer','Warm surface layers coexist with cool upwelling patches; the net two-layer strait exchange persists.'),
           ('Autumn','Cooling and wet spells reshape layering and plumes without assigning a permanent gulf-wide loop.')]
    for i,(season,body) in enumerate(lines):
        t(g,55,1051+i*47,season,20);t(g,185,1051+i*47,body,20)
    t(g,55,1280,'NAVIGATION  ·  Outbound ships gain current help; inbound ships need useful wind. Opposing waves steepen in the straits.',19)
    t(g,55,1348,'The plan-view arrows share one corridor; the section shows their vertical separation. Small map hexes: 24 miles face to face.',17,'muted')
    E.ElementTree(r).write(ASSETS/'taelgar-western-gulf-exchange-v1.svg',encoding='unicode')


if __name__=='__main__':
    basin();gulf()
    print('assets/worldbuilding/taelgar-green-sea-currents-v4.svg')
    print('assets/worldbuilding/taelgar-western-gulf-exchange-v1.svg')
