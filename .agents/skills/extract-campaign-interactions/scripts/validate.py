#!/usr/bin/env python3
"""Validate v6 session bundles; retain read-only v5/v3 pilot compatibility."""
import argparse
import json
from pathlib import Path
import legacy_v3
from session_model import validate as validate_v5, render as render_v5

def validate(data, vault, processing=None):
    if data.get('schema_version') == 3:
        return legacy_v3.validate(data, vault)
    if 'schema_version' in data:
        raise ValueError('Unsupported schema version')
    return validate_v5(data, vault, processing=processing)

def render(data, vault, *args, **kwargs):
    if data.get('schemaVersion') in {5, 6}:
        return render_v5(data, vault, *args, **kwargs)
    return legacy_v3.render(data, vault, *args, **kwargs)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--vault', type=Path, required=True)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--preview', type=Path)
    parser.add_argument('--excerpts', type=Path)
    parser.add_argument('--processing', type=Path)
    args = parser.parse_args()
    data = json.loads(args.input.read_text())
    processing = None
    if data.get('schemaVersion') == 6:
        path = args.processing or args.input.parent / 'session-processing-data.json'
        processing = json.loads(path.read_text())
    result = validate(data, args.vault, processing)
    if data.get('schemaVersion') in {5, 6}:
        if args.preview:args.preview.write_text(render_v5(data,args.vault,args.preview,processing=processing))
        print(json.dumps({k:v for k,v in result.items() if k!='catalog'}))
    else:
        if args.preview:args.preview.write_text(legacy_v3.render(data,args.vault,*result))
        if args.excerpts:args.excerpts.write_text(legacy_v3.render(data,args.vault,*result,excerpts=True))
        print('Validated historical v3 extraction')
