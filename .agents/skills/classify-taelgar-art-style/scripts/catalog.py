#!/usr/bin/env python3
"""Maintain the private Taelgar style catalog. A single coordinator owns writes."""
import argparse
from collections import defaultdict, deque
import hashlib
import json
import os
from pathlib import Path
import random
import tempfile

DEFAULT = Path.home() / "Documents/RPGs/taelgar-art-catalog"


def read(path):
    return json.loads(path.read_text())


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode="w", dir=path.parent, delete=False) as tmp:
        tmp.write(content)
    os.replace(tmp.name, path)


def save(path, data):
    write(path, json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def source(config, row):
    root = Path(config["roots"][row["collection"]])
    path = (root / row["relativePath"]).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError(f"Path escapes source: {path}")
    return path


STYLE_FIELDS = ("family", "treatment", "fit", "statement", "basis")


def set_aside(row):
    return row["battlemap"] or row["framedToken"]


def apply_format(row):
    if set_aside(row):
        for field in STYLE_FIELDS:
            row.pop(field, None)
    return row


def records(catalog):
    corrections = read(catalog / "corrections.json")
    rows = []
    for file in sorted((catalog / "batches").glob("*.json")):
        for raw in read(file):
            patch = corrections.get(str(raw["id"]), {})
            forbidden = patch.keys() - {"title","subjects","depicts","battlemap","framedToken","family","treatment","fit","statement","basis","format","relatedIds"}
            if forbidden:
                raise ValueError(f"Unknown correction fields: {forbidden}")
            rows.append(apply_format({**raw, **patch, "batch": file.stem}))
    if set(corrections) - {str(r["id"]) for r in rows}:
        raise ValueError("Correction for unknown image")
    return rows


def scan(config):
    for collection, root in config["roots"].items():
        for directory, dirs, files in os.walk(root):
            dirs[:] = sorted(d for d in dirs if not d.startswith(".") and d != "node_modules"
                             and not (collection == "RPGs" and directory == root and d in config["excludedRPGsFolders"]))
            for name in sorted(files):
                f = Path(directory) / name
                if name.startswith(".") or f.suffix.lower() not in config["extensions"]:
                    continue
                stat = f.stat()
                yield dict(collection=collection, relativePath=str(f.relative_to(root)),
                           bytes=stat.st_size, modifiedNs=stat.st_mtime_ns)


def inventory(catalog, config, rows, match_copies=False):
    # A path's review survives a rename once its content has been identified.
    old_path = catalog / "inventory.json"
    old = {(v["collection"],v["relativePath"]):v for v in read(old_path)} if old_path.exists() else {}
    known_hashes = {r["sha256"]:r["id"] for r in rows}
    by_path = {(r["collection"],r["relativePath"]):r for r in rows}
    reviewed_sizes = {source(config,r).stat().st_size for r in rows} if match_copies else set()
    result = []
    for item in scan(config):
        key = item["collection"], item["relativePath"]
        prev, review = old.get(key, {}), by_path.get(key)
        if (prev.get("bytes"),prev.get("modifiedNs")) == (item["bytes"],item["modifiedNs"]):
            digest = prev.get("sha256")
        elif review:
            digest = hashlib.sha256(source(config,item).read_bytes()).hexdigest()
        else:
            digest = None
        if not digest and item["bytes"] in reviewed_sizes:
            digest = hashlib.sha256(source(config,item).read_bytes()).hexdigest()
        if digest:
            item["sha256"] = digest
        item["reviewId"] = known_hashes.get(digest)
        result.append(item)
    save(old_path, result)
    return result


def balanced(rows, seed):
    rng = random.Random(seed)
    groups = defaultdict(lambda: defaultdict(list))
    for r in rows:
        groups[r["collection"]][str(Path(r["relativePath"]).parent)].append(r)
    queues = {}
    for collection, folders in groups.items():
        bins = list(folders.values())
        rng.shuffle(bins)
        for items in bins:
            rng.shuffle(items)
        pending = deque(bins)
        queue = deque()
        while pending:
            group = pending.popleft()
            queue.append(group.pop())
            if group:
                pending.append(group)
        queues[collection] = queue
    while any(queues.values()):
        for q in queues.values():
            if q:
                yield q.popleft()


def plan(catalog, config, rows, args):
    if args.output.exists():
        raise ValueError("Manifest already exists. Resume it or choose a new destination.")
    if args.count < 1:
        raise ValueError("Choose a positive number of images.")
    paths = inventory(catalog, config, rows)
    taken = {r["sha256"]:r["id"] for r in rows}
    next_id = max(taken.values(), default=0) + 1
    result = []
    for item in balanced([v for v in paths if v["reviewId"] is None], args.seed):
        path = source(config,item)
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        item["sha256"] = digest
        if digest in taken:
            # An unpublished reservation is not yet a completed review.
            if taken[digest] < next_id:
                item["reviewId"] = taken[digest]
            continue
        uid = next_id + len(result)
        taken[digest] = uid
        result.append(dict(id=uid, collection=item["collection"],relativePath=item["relativePath"],
                           sha256=digest,path=str(path)))
        if len(result) == args.count:
            break
    save(catalog / "inventory.json", paths)
    save(args.output, result)
    print(f"Assigned {len(result)} of {args.count} requested images to {args.output}")


def checked(catalog, config, rows):
    styles = read(catalog / "styles.json")
    families = set(config.get("families", [s["family"] for s in styles]))
    by_id = {r["id"]:r for r in rows}
    labels = {s["treatment"]:s for s in styles}
    if len(by_id) != len(rows) or len({r["sha256"] for r in rows}) != len(rows):
        raise ValueError("Duplicate ID or byte-identical review")
    if len(labels) != len(styles):
        raise ValueError("Duplicate style label")
    for r in rows:
        assert all(type(r[k]) is bool for k in ("battlemap","framedToken")), r["id"]
        assert all(isinstance(r[k],str) and r[k].strip() for k in ("title","format")), r["id"]
        if not set_aside(r):
            style = labels[r["treatment"]]
            assert r["family"] == style["family"] and r["fit"] in {"existing","candidate","uncertain"}, r["id"]
            assert all(isinstance(r[k],str) and r[k].strip() for k in ("statement","basis")), r["id"]
            assert isinstance(r["subjects"],list) and all(isinstance(subject,str) for subject in r["subjects"]), r["id"]
            assert all(d.get("name") and d.get("role") and d.get("evidence") for d in r["depicts"]), r["id"]
        assert set(r.get("relatedIds",[])) <= by_id.keys(), r["id"]
        assert source(config,r).is_file(), r["id"]
        if r["collection"] == "RPGs" and Path(r["relativePath"]).parts[0] in config["excludedRPGsFolders"]:
            raise ValueError("Excluded image " + r["relativePath"])
    for s in styles:
        assert s["family"] in families, s["treatment"]
        assert s["description"] and s["status"] and (not s["neighbor"] or s["neighbor"] in labels), s["treatment"]
        assert s["examples"] and all(by_id[i].get("treatment") == s["treatment"] for i in s["examples"]), s["treatment"]
    return styles


def thumbnail(catalog, config, row):
    from PIL import Image, ImageOps
    dest = catalog / "thumbnails" / (row["sha256"] + ".jpg")
    if dest.exists():
        return
    with Image.open(source(config,row)) as raw:
        im = ImageOps.exif_transpose(raw).convert("RGBA")
        im.thumbnail((800,800),Image.Resampling.LANCZOS)
        bg = Image.new("RGB", im.size, (216,215,211))
        bg.paste(im, mask=im.getchannel("A"))
        dest.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(dir=dest.parent, delete=False) as f:
            bg.save(f, format="JPEG", quality=88)
        os.replace(f.name, dest)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog",type=Path,default=DEFAULT)
    commands = parser.add_subparsers(dest="command", required=True)
    cmd = commands.add_parser("inventory",help="Refresh path-level coverage")
    cmd.add_argument("--match-copies",action="store_true",help="Hash unreviewed files matching a reviewed file size to identify exact copies")
    cmd = commands.add_parser("plan",help="Prepare one disjoint batch manifest")
    cmd.add_argument("--count",type=int,default=100)
    cmd.add_argument("--seed",type=int,default=7313)
    cmd.add_argument("--output",type=Path,required=True)
    cmd = commands.add_parser("assemble",help="Join reconciled worker rows to the selected originals in a staging directory")
    cmd.add_argument("--manifest",type=Path,required=True)
    cmd.add_argument("--reviews",type=Path,nargs="+",required=True)
    cmd.add_argument("--output",type=Path,required=True)
    commands.add_parser("build",help="Validate records, cache previews and rebuild gallery and inventory")
    commands.add_parser("verify",help="Verify catalog links, source hashes and cached images")
    cmd = commands.add_parser("lookup",help="Find treatments and retrieve diagnostic details and example originals")
    cmd.add_argument("query")
    args = parser.parse_args()
    catalog = args.catalog.expanduser()
    config,rows = read(catalog/"config.json"), records(catalog)
    if args.command == "assemble":
        from PIL import Image
        records_by_id = {}
        for file in args.reviews:
            for r in read(file):
                if r["id"] in records_by_id:
                    raise ValueError(f'Duplicate review #{r["id"]}')
                records_by_id[r["id"]] = r
        manifest = read(args.manifest)
        ids = [r["id"] for r in manifest]
        if len(set(ids)) != len(ids) or set(ids) != set(records_by_id):
            raise ValueError("Manifest and completed reviews must cover the same unique IDs")
        batch = []
        for m in manifest:
            path = source(config,m)
            if hashlib.sha256(path.read_bytes()).hexdigest() != m["sha256"]:
                raise ValueError(f"Original changed: {path}")
            r = dict(records_by_id[m["id"]])
            r.update({k:m[k] for k in ("id","sha256","collection","relativePath")})
            if path.suffix.lower() == ".svg":
                if not r.get("width") or not r.get("height"):
                    raise ValueError(f"Supply the viewed SVG dimensions on row {r['id']}")
            else:
                with Image.open(path) as im:
                    r["width"],r["height"] = im.size
            r.setdefault("format","battlemap" if r["battlemap"] else "framed token" if r["framedToken"] else "illustration")
            batch.append(apply_format(r))
        if args.output.exists() and read(args.output) != batch:
            raise ValueError("Output already holds different records")
        if len({r["sha256"] for r in batch}) != len(batch):
            raise ValueError("Duplicate image content in manifest")
        save(args.output,batch)
        return
    if args.command == "plan":
        return plan(catalog,config,rows,args)
    if args.command == "inventory":
        print(f"{len(inventory(catalog,config,rows,args.match_copies))} source paths")
        return
    styles = checked(catalog,config,rows)
    if args.command == "lookup":
        by_id = {r["id"]:r for r in rows}
        for s in styles:
            if args.query.casefold() in (s["treatment"]+" "+s["family"]).casefold():
                print(s["treatment"],s["description"],sep="\n")
                if s["neighbor"]:
                    print(f'Nearby: {s["neighbor"]}. {s["distinction"]}')
                for uid in s["examples"]:
                    r = by_id[uid]
                    print(f'  #{uid} {r["title"]} — {source(config,r)}\n    {r["statement"]}')
        return
    if args.command == "build":
        from gallery import render
        for r in rows:
            thumbnail(catalog,config,r)
        paths = inventory(catalog,config,rows)
        write(catalog/"index.html",render(config,rows,styles,len(paths),catalog))
    else:
        from PIL import Image
        from html.parser import HTMLParser
        class Images(HTMLParser):
            def __init__(self):
                super().__init__()
                self.links = set()
            def handle_starttag(self,tag,attrs):
                if tag == "img":
                    self.links.add(dict(attrs)["src"])
        page = Images()
        page.feed((catalog/"index.html").read_text())
        parked = Images()
        parked.feed((catalog/"set-aside.html").read_text())
        assert not page.links.intersection(parked.links), "A set-aside image appears in the style gallery"
        for r in rows:
            path = f'thumbnails/{r["sha256"]}.jpg'
            assert path in (parked.links if set_aside(r) else page.links) and hashlib.sha256(source(config,r).read_bytes()).hexdigest()==r["sha256"],r["id"]
            with Image.open(catalog/path) as im:
                im.verify()
    print(f'{args.command}: {len(rows)} unique image records, {len(styles)} treatments')


if __name__ == "__main__":
    main()
