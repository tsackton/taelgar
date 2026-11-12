"""Offline HTML views. The JSON catalog remains the source of truth."""
from collections import defaultdict
from html import escape
import json
from pathlib import Path
from urllib.parse import quote


def e(value):
    return escape(str(value),quote=True)


def thumb(r):
    return 'thumbnails/' + r['sha256'] + '.jpg'


CSS = """
*{box-sizing:border-box}html{font-family:"Helvetica Neue",Arial,sans-serif;background:#f7f5ef;color:#292d2c}
body{margin:auto;max-width:1620px;padding:34px clamp(18px,4vw,70px) 72px}
h1,h2,h3{font-family:Georgia,serif;font-weight:normal;text-wrap:balance}h1{font-size:clamp(2.4rem,6vw,4.5rem);line-height:1;margin:0 0 12px}
h2{font-size:clamp(1.55rem,3vw,2.25rem);margin:0 0 5px}p{line-height:1.5}a{color:#31574c;text-underline-offset:.16em}
.controls{display:flex;gap:12px;flex-wrap:wrap;padding:20px 0;border-block:1px solid #c9ccc2;margin:24px 0}
label{display:grid;gap:4px;font-size:.84rem}input,select{font:inherit;color:inherit;padding:9px;border:1px solid #9daba1;border-radius:3px;background:#fff}
section{padding:24px 0 30px;border-top:1px solid #bdc4b8}.groupdesc{max-width:80ch;margin:8px 0}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,260px),1fr));gap:22px 18px;margin-top:16px}
article{min-width:0;background:#fffef9;border:1px solid #dadbd2;border-radius:5px;overflow:hidden}
img{display:block;width:100%;height:240px;object-fit:contain;background:#e8e6de}
.copy{padding:12px 14px 16px}.copy p{margin:.45em 0}h3{font-size:1.3rem;margin:.2em 0}.meta,small{font-size:.82rem;color:#4f6057}
summary{cursor:pointer;padding:6px 0;color:#31574c}.path{overflow-wrap:anywhere}article:target{outline:3px solid #9e6c40} [hidden]{display:none!important}
.skip{margin:4px 0 18px}.chip{display:inline-block;border:1px solid #a7b5aa;border-radius:2px;padding:2px 5px;font-size:.78rem}
"""


VIEWER_CSS = """body:has(#viewer[open]){overflow:hidden}
#viewer{position:fixed;inset:0;width:100vw;height:100%;height:100dvh;max-width:none;max-height:none;box-sizing:border-box;margin:0;padding:0;border:0;background:#141615;color:#f4f4ef}
#viewer[open]{display:grid;grid-template-rows:auto minmax(0,1fr)}
#viewer::backdrop{background:#141615}
.viewer-bar{display:flex;align-items:center;flex-wrap:wrap;gap:8px 16px;padding:9px clamp(12px,2vw,32px);background:#202320}
.viewer-bar button{background:#2b302d;border-color:#626b65;color:#f4f4ef;min-height:38px}
.viewer-bar .viewer-buttons{display:flex;gap:6px;align-items:center;flex-wrap:wrap}
#viewer-caption{flex:1 1 210px;overflow-wrap:anywhere}
#viewer-area{overflow:auto;overscroll-behavior:contain;min-height:0;position:relative}
.viewer-canvas{display:grid;place-items:center;width:100%;height:100%}
#viewer-image{display:block;max-width:100%;max-height:100%;width:auto;height:auto;min-width:0;min-height:0;cursor:zoom-in}
#viewer-area.actual .viewer-canvas{width:max-content;height:max-content;min-width:100%;min-height:100%}
#viewer-area.actual #viewer-image{max-width:none;max-height:none;cursor:zoom-out}
#viewer-error{position:absolute;top:40%;width:100%;text-align:center}#viewer-error a{color:inherit}

.viewer-bar button{cursor:pointer;font:inherit;border:1px solid #626b65;border-radius:4px;padding:6px 10px}.viewer-bar button:disabled{cursor:default;opacity:.45}#viewer-image{background:transparent}
"""

VIEWER = """<dialog id="viewer" aria-label="Full-size image viewer">
 <div class="viewer-bar">
  <span id="viewer-caption" aria-live="polite"></span>
  <div class="viewer-buttons">
   <button type="button" id="viewer-prev" aria-label="Previous image" title="Previous image (←)">←</button>
   <button type="button" id="viewer-next" aria-label="Next image" title="Next image (→)">→</button>
   <button type="button" id="viewer-zoom" aria-pressed="false">Actual size</button>
   <button type="button" id="viewer-close" autofocus title="Close (Esc)">Close</button>
  </div>
 </div>
 <div id="viewer-area"><div class="viewer-canvas"></div>
  <p id="viewer-error" hidden>The original could not be displayed. <a id="viewer-original" target="_blank" rel="noopener">Open original file</a></p>
 </div>
</dialog>
<script>
'use strict';
const $ = id => document.getElementById(id);
let thumbs = [];
const viewer = $('viewer');
const viewerArea = $('viewer-area');
const viewerImage = document.createElement('img');
viewerImage.id = 'viewer-image';
viewer.querySelector('.viewer-canvas').append(viewerImage);
let imagePosition = 0;
let openingThumbnail;

function setActualSize(actual) {
  viewerArea.classList.toggle('actual', actual);
  $('viewer-zoom').setAttribute('aria-pressed', String(actual));
  $('viewer-zoom').textContent = actual ? 'Fit to screen' : 'Actual size';
  viewerArea.scrollLeft = actual ? (viewerArea.scrollWidth - viewerArea.clientWidth) / 2 : 0;
  viewerArea.scrollTop = actual ? (viewerArea.scrollHeight - viewerArea.clientHeight) / 2 : 0;
}
function showOriginal(position) {
  imagePosition = (position + thumbs.length) % thumbs.length;
  const thumb = thumbs[imagePosition];
  const title = thumb.querySelector('img').alt;
  const id = thumb.closest('article').id.replace('image-', '');
  const treatment = thumb.closest('section').dataset.treatment;
  $('viewer-caption').textContent = treatment + ' · ' + (imagePosition + 1) + ' of ' + thumbs.length + ' · #' + id + ' ' + title;
  $('viewer-original').href = thumb.href;
  $('viewer-error').hidden = true;
  viewerImage.hidden = false;
  viewerImage.alt = title;
  viewerImage.src = thumb.href;
  $('viewer-zoom').disabled = false;
  setActualSize(false);
}
function openViewer(event) {
  if (event.ctrlKey || event.metaKey || event.altKey || event.shiftKey) return;
  event.preventDefault();
  openingThumbnail = event.currentTarget;
  const group = openingThumbnail.closest('section');
  thumbs = Array.from(group.querySelectorAll('article:not([hidden]) > a.original'));
  const single = thumbs.length === 1;
  $('viewer-prev').disabled = single;
  $('viewer-next').disabled = single;
  viewer.showModal();
  showOriginal(thumbs.indexOf(openingThumbnail));
}
viewerImage.addEventListener('error', () => {
  if (!viewer.open || viewerImage.naturalWidth || !viewerImage.complete) return;
  viewerImage.hidden = true;
  $('viewer-error').hidden = false;
  $('viewer-zoom').disabled = true;
});
$('viewer-prev').onclick = () => showOriginal(imagePosition - 1);
$('viewer-next').onclick = () => showOriginal(imagePosition + 1);
$('viewer-close').onclick = () => viewer.close();
$('viewer-zoom').onclick = viewerImage.onclick = () => setActualSize(!viewerArea.classList.contains('actual'));
viewer.addEventListener('keydown', event => {
  if (event.altKey || event.ctrlKey || event.metaKey || event.shiftKey) return;
  if (event.key !== 'ArrowLeft' && event.key !== 'ArrowRight') return;
  event.preventDefault();
  showOriginal(imagePosition + (event.key === 'ArrowRight' ? 1 : -1));
});
viewer.addEventListener('close', () => {
  viewerImage.removeAttribute('src');
  if (openingThumbnail?.isConnected) openingThumbnail.focus({preventScroll:true});
});



document.querySelectorAll('a.original').forEach(thumb => thumb.addEventListener('click', openViewer));
</script>"""


def card(config,r,parked_ids):
    path=Path(config["roots"][r["collection"]])/r["relativePath"]
    names = ", ".join(d['name'] for d in r.get("depicts",[]))
    evidence="".join(f'<p>{e(d["name"])} · {e(d["evidence"])}</p>' for d in r.get("depicts",[]))
    aliases=r.get("aliases",[])
    copies="".join(f'<p class="path">Copy · <a href="{e((Path(config["roots"][a["collection"]])/a["relativePath"]).as_uri())}">{e(a["relativePath"])}</a></p>' for a in aliases)
    variants = []
    for i in r.get("relatedIds", []):
        page = ""
        if (i in parked_ids) != (r["id"] in parked_ids):
            page = "set-aside.html" if i in parked_ids else "index.html"
        variants.append(f'<a href="{page}#image-{i}">#{i}</a>')
    variants = ", ".join(variants)
    if variants:
        variants="<p>Related images · "+variants+"</p>"
    flags=[name for k,name in [('battlemap','Battlemap'),('framedToken','Framed token')] if r[k]]
    form=" · ".join(flags) if flags else r["format"]
    if r["id"] in parked_ids:
        return f'''<article id="image-{r["id"]}"><a href="{e(path.as_uri())}"><img loading="lazy" src="{thumb(r)}" alt="{e(r["title"])}"></a>
        <div class="copy"><span class="meta">#{r["id"]} · {e(r["collection"])} · {e(form)}</span><h3>{e(r["title"])}</h3>
        <a class="path" href="{e(path.as_uri())}">{e(r["relativePath"])}</a>{copies}{variants}</div></article>'''
    search=" ".join([r["title"],str(r["id"]),r["relativePath"],r["treatment"],r["family"],
                     r["statement"],names,*r["subjects"],*(a["relativePath"] for a in aliases)]).casefold()
    lane="illustration" if r["format"]=="illustration" else "other"
    return f'''<article id="image-{r["id"]}" data-search="{e(search)}" data-lane="{lane}" data-source="{e(r["collection"])}" data-fit="{e(r["fit"])}">
    <a class="original" aria-haspopup="dialog" href="{e(path.as_uri())}"><img loading="lazy" src="{thumb(r)}" alt="{e(r["title"])}"></a>
    <div class="copy"><span class="meta">#{r["id"]} · {e(r["collection"])} · {e(form)}</span>
    <h3>{e(r["title"])}</h3><p>{e(r["statement"])}</p>
    <details><summary>Classification and source</summary><p>{e(r["treatment"])} · {e(r["fit"])}</p><p>{e(r["basis"])}</p>
    <p>{e(", ".join(r["subjects"]))}</p>{evidence}<a class="path" href="{e(path.as_uri())}">{e(r["relativePath"])}</a>{copies}{variants}</details></div></article>'''


def document(title,body,extra_css=""):
    return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+e(title)+'</title><style>'+CSS+extra_css+'</style></head><body>'+body+'</body></html>'


def render(config, rows, styles, npaths, catalog):
    from catalog import write, set_aside
    by_id={r['id']:r for r in rows}
    for item in json.loads((catalog/"inventory.json").read_text()):
        r=by_id.get(item.get("reviewId"))
        if r and (r["collection"],r["relativePath"]) != (item["collection"],item["relativePath"]):
            r.setdefault("aliases",[]).append(item)
    parked = [r for r in rows if set_aside(r)]
    parked_ids = {r["id"] for r in parked}
    rows = [r for r in rows if r["id"] not in parked_ids]
    inventory_parts = ['<nav><a href="index.html">Style gallery</a></nav><h1>Set-aside assets</h1>']
    for flag, title in (("framedToken", "Framed tokens"), ("battlemap", "Battlemaps")):
        members = [r for r in parked if r[flag]]
        inventory_parts.append(f'<section><h2>{title} ({len(members)})</h2><div class="grid">')
        inventory_parts.extend(card(config,r,parked_ids) for r in members)
        inventory_parts.append('</div></section>')
    write(catalog/"set-aside.html",document("Set-aside assets","".join(inventory_parts)))
    reports=[]
    for file in sorted((catalog/'reviews').glob('*.json'),reverse=True):
        report=json.loads(file.read_text())
        parts=[f'<p><a href="../index.html">All treatments</a></p><h1>{e(report["title"])}</h1><p>{e(report["intro"])}</p>']
        for block in report["sets"]:
            ids = [i for i in block["ids"] if i not in parked_ids]
            if not ids:
                continue
            parts.append(f'<section><h2>{e(block["title"])}</h2><p class="groupdesc">{e(block["text"])}</p><div class="grid">')
            for i in ids:
                r=by_id[i]
                parts.append(f'<article><a href="../index.html#image-{i}"><img src="../{thumb(r)}" alt="{e(r["title"])}"></a><div class="copy"><span class="meta">#{i} · {e(r["treatment"])}</span><h3><a href="../index.html#image-{i}">{e(r["title"])}</a></h3><p>{e(r["statement"])}</p></div></article>')
            parts.append('</div></section>')
        write(file.with_suffix('.html'),document(report['title'],''.join(parts)))
        reports.append(f'<a href="reviews/{quote(file.stem)}.html">{e(report["title"])}</a>')
    def options(vals):
        return ''.join(f'<option value="{e(k)}">{e(v)}</option>' for k,v in vals)
    reports.append(f'<a href="set-aside.html">Set-aside assets ({len(parked)})</a>')
    for sheet in reversed(config.get("reviewSheets", [])):
        reports.insert(0, f'<a href="{e(quote(sheet["path"]))}">{e(sheet["title"])}</a>')
    families=sorted({s['family'] for s in styles})
    groups=defaultdict(list)
    for r in rows:
        groups[r['treatment']].append(r)
    parts=[f'<header><h1>Taelgar art catalog</h1><p>{len(rows)} style-reviewed images · {len(styles)} working treatments · {npaths:,} source paths inventoried</p></header>',
           '<nav class="skip">'+ ' · '.join(reports)+'</nav>',
           f'''<div class="controls"><label>Search<input id="search" type="search" placeholder="Name, subject or brushwork"></label>
           <label>Family<select id="family"><option value="">All families</option>{options((f,f) for f in families)}</select></label>
           <label>Treatment<select id="treatment"><option value="">All treatments</option>{options((s['treatment'],s['treatment']) for s in sorted(styles,key=lambda s:s['treatment']))}</select></label>
           <label>Format<select id="lane"><option value="">All formats</option>{options([('illustration','Illustrations'),('other','Other formats')])}</select></label>
           <label>Discovery<select id="status"><option value="">All treatments</option><option value="candidate">New candidates</option><option value="pilot">Pilot treatments</option></select></label>
           <label>Assignment<select id="fit"><option value="">All assignments</option><option value="uncertain">Uncertain matches</option></select></label>
           <label>Source<select id="source"><option value="">Both collections</option>{options((k,k) for k in config['roots'])}</select></label><button type="button" id="reset">Clear filters</button></div><p id="count" aria-live="polite"></p>''']
    current_family = None
    for s in sorted(styles,key=lambda s:(s['family'],s['treatment'])):
        if current_family != s['family']:
            current_family = s['family']
            parts.append(f'<h2 class="family-heading" data-heading="{e(current_family)}">{e(current_family)}</h2>')
        members=groups[s['treatment']]
        examples=s['examples']
        members.sort(key=lambda r:examples.index(r['id']) if r['id'] in examples else len(examples)+r['id'])
        parts.append(f'<section data-status="{e(s["status"])}" data-family="{e(s["family"])}" data-treatment="{e(s["treatment"])}"><small>{e(s["family"])} · {e(s["status"])} · {len(members)} images</small><h3 class="treatment-heading">{e(s["treatment"])}</h3><p class="groupdesc">{e(s["description"])}</p>')
        if s['neighbor']:
            parts.append(f'<p class="groupdesc"><small>Compare with {e(s["neighbor"])}</small><br>{e(s["distinction"])}</p>')
        parts.append('<div class="grid">'+''.join(card(config,r,parked_ids) for r in members)+'</div></section>')
    parts.append('''<script>
    const controls = document.querySelector(".controls");
    const selects = Array.from(controls.querySelectorAll("select"));
    const choices = new Map(selects.map(select => [select.id, Array.from(select.options, o => [o.value, o.text])]));
    const groups = Array.from(document.querySelectorAll("section[data-family]"));
    const familyHeadings = Array.from(document.querySelectorAll(".family-heading"));
    const entries = groups.flatMap(group => Array.from(group.querySelectorAll("article"), card => ({
      card, group, values: {...group.dataset, ...card.dataset}
    })));
    const search = document.getElementById("search");

    function filter(event){
      const values = Object.fromEntries(selects.map(s => [s.id, s.value]));
      if (event?.target.id === "family" && values.family && values.treatment &&
          !entries.some(e => e.values.family === values.family && e.values.treatment === values.treatment)) {
        values.treatment = "";
      }
      const text = search.value.trim().toLowerCase();
      const searched = entries.filter(e => e.values.search.includes(text));
      function matches(entry, omit){
        return selects.every(({id}) => id === omit || (omit === "family" && id === "treatment") ||
          !values[id] || entry.values[id] === values[id]);
      }
      for (const select of selects){
        const available = new Set(searched.filter(e => matches(e, select.id)).map(e => e.values[select.id]));
        // Keep an explicit selection clearable during an empty text search.
        const options = choices.get(select.id).filter(([v]) => !v || available.has(v) || v === values[select.id]);
        select.replaceChildren(...options.map(([v, label]) => new Option(label, v)));
        select.value = values[select.id];
      }
      const visible = new Set(searched.filter(e => matches(e)).map(e => e.card));
      const shownGroups = new Set();
      for (const {group,card} of entries){
        card.hidden = !visible.has(card);
        if (!card.hidden) shownGroups.add(group);
      }
      for (const group of groups) group.hidden = !shownGroups.has(group);
      const visibleFamilies = new Set(Array.from(shownGroups, group => group.dataset.family));
      for (const heading of familyHeadings) heading.hidden = !visibleFamilies.has(heading.dataset.heading);
      document.getElementById("count").textContent = visible.size + " matching images";
    }
    function reset(){
      search.value = "";
      for (const select of selects) select.value = "";
      filter();
    }
    controls.addEventListener("input",filter);
    document.getElementById("reset").addEventListener("click",reset);
    const parkedIds = new Set(PARKED_IDS);
    function revealTarget(){
      const id = location.hash.slice(1);
      if (parkedIds.has(id)) {
        location.replace("set-aside.html#" + id);
        return;
      }
      const target = document.getElementById(id);
      if(target?.hidden){
        reset();
        target.scrollIntoView();
      }
    }
    window.addEventListener("hashchange", revealTarget);
    filter();
    revealTarget();
    </script>'''.replace('PARKED_IDS',json.dumps([f'image-{i}' for i in sorted(parked_ids)])))
    family_css = """.family-heading{font-size:clamp(2rem,4vw,3rem);margin:42px 0 10px}.treatment-heading{font-size:clamp(1.55rem,3vw,2.25rem);margin:.15em 0}"""
    parts.append(VIEWER)
    return document("Taelgar art catalog",''.join(parts),family_css + VIEWER_CSS)
