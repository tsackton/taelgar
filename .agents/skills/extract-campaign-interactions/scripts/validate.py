#!/usr/bin/env python3
"""Validate canonical v5 sessions; retain read-only compatibility with v3 pilots."""
import argparse
import json
from pathlib import Path
import legacy_v3
from session_model import validate as validate_v5, render as render_v5

def validate(data, vault):
    if data.get('schema_version') == 3:
        return legacy_v3.validate(data, vault)
    if 'schema_version' in data:
        raise ValueError('Unsupported schema version')
    return validate_v5(data, vault)

def render(data, vault, *args, **kwargs):
    if data.get('schemaVersion') == 5:
        return render_v5(data, vault, *args, **kwargs)
    return legacy_v3.render(data, vault, *args, **kwargs)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--vault', type=Path, required=True)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--preview', type=Path)
    parser.add_argument('--excerpts', type=Path)
    args = parser.parse_args()
    data = json.loads(args.input.read_text())
    result = validate(data, args.vault)
    if data.get('schemaVersion') == 5:
        if args.preview:args.preview.write_text(render_v5(data,args.vault,args.preview))
        print(json.dumps({k:v for k,v in result.items() if k!='catalog'}))
    else:
        if args.preview:args.preview.write_text(legacy_v3.render(data,args.vault,*result))
        if args.excerpts:args.excerpts.write_text(legacy_v3.render(data,args.vault,*result,excerpts=True))
        print('Validated historical v3 extraction')
