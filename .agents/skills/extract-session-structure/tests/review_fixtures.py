"""Registered bundles for isolated review renderer tests."""
from pathlib import Path


def registered_manifest(vault: Path, bundle: str, filename: str) -> Path:
    campaign_root = vault / '_sessions' / 'dunmar-frontier'
    cleaned = campaign_root / bundle / 'cleaned'
    cleaned.mkdir(parents=True)
    (campaign_root.parent / 'campaign-registry.json').write_text('{"dufr":"Index.md"}')
    (vault / 'Index.md').write_text(
        '---\nname: Dunmari Frontier\nsessionBundleDirectory: _sessions/dunmar-frontier\n---\n')
    manifest = cleaned / filename
    manifest.write_text('campaign: Regression\nsessionNumber: 999\n')
    return manifest
