#!/usr/bin/env python3
"""Enforce the transcription workspace boundary."""

from __future__ import annotations

from pathlib import Path


def resolve_transcription_output(
    path: Path,
    *,
    error_type: type[Exception] = ValueError,
    label: str = "output",
) -> Path:
    """Resolve an output path and reject any vault ``_sessions`` tree."""

    resolved = path.expanduser().resolve()
    if "_sessions" in resolved.parts:
        raise error_type(
            f"refusing {label} under a vault _sessions tree: {resolved}. "
            "Keep transcription work beside the original recording; "
            "prepare-session-source archives only the finalized source into the vault."
        )
    return resolved
