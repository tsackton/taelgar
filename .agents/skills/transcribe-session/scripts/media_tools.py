#!/usr/bin/env python3
"""Small, deterministic media helpers for the transcribe-session skill."""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path


class MediaToolError(RuntimeError):
    """A media probe or extraction operation failed."""


@dataclass(frozen=True)
class MediaBackend:
    name: str
    executable: str


def resolve_clip_backend() -> MediaBackend:
    ffmpeg = shutil.which("ffmpeg")
    if ffmpeg:
        return MediaBackend(name="ffmpeg", executable=ffmpeg)
    swiftc = shutil.which("swiftc")
    swift_source = Path(__file__).with_name("extract_audio_clip.swift")
    if swiftc and swift_source.is_file():
        return MediaBackend(name="swift-asset-reader-source", executable=swiftc)
    raise MediaToolError(
        "speaker audio samples require ffmpeg or macOS Swift with AVFoundation"
    )


def prepare_clip_source(
    source: Path, *, backend: MediaBackend, work_dir: Path
) -> tuple[Path, MediaBackend]:
    source = source.expanduser().resolve()
    if backend.name != "swift-asset-reader-source":
        return source, backend
    swift_source = Path(__file__).with_name("extract_audio_clip.swift")
    executable = work_dir / ".extract-audio-clip"
    module_cache = work_dir / ".swift-module-cache"
    module_cache.mkdir(parents=True, exist_ok=True)
    environment = os.environ.copy()
    environment["CLANG_MODULE_CACHE_PATH"] = str(module_cache)
    environment["SWIFT_MODULECACHE_PATH"] = str(module_cache)
    try:
        completed = subprocess.run(
            [
                backend.executable,
                str(swift_source),
                "-O",
                "-module-cache-path",
                str(module_cache),
                "-o",
                str(executable),
            ],
            text=True,
            capture_output=True,
            check=False,
            env=environment,
            timeout=180,
        )
    except subprocess.TimeoutExpired as exc:
        raise MediaToolError("timed out compiling the AVFoundation clip helper") from exc
    if completed.returncode != 0:
        detail = completed.stderr.strip() or completed.stdout.strip()
        raise MediaToolError(f"could not compile AVFoundation clip helper: {detail[:1200]}")
    if not executable.is_file():
        raise MediaToolError("Swift compiler produced no AVFoundation clip helper")
    return source, MediaBackend(name="swift-asset-reader", executable=str(executable))


def resolve_probe_backend() -> MediaBackend:
    ffprobe = shutil.which("ffprobe")
    if ffprobe:
        return MediaBackend(name="ffprobe", executable=ffprobe)
    afinfo = shutil.which("afinfo")
    if afinfo:
        return MediaBackend(name="afinfo", executable=afinfo)
    raise MediaToolError(
        "recording manifests require ffprobe or the macOS afinfo utility"
    )


def extract_audio_clip(
    source: Path,
    output: Path,
    *,
    start_seconds: float,
    end_seconds: float,
    backend: MediaBackend | None = None,
) -> None:
    if start_seconds < 0 or end_seconds <= start_seconds:
        raise MediaToolError(
            f"invalid clip range {start_seconds:.3f}-{end_seconds:.3f}"
        )
    source = source.expanduser().resolve()
    if not source.is_file():
        raise MediaToolError(f"source media file not found: {source}")
    output = output.expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    selected = backend or resolve_clip_backend()
    duration = end_seconds - start_seconds

    if selected.name == "ffmpeg":
        command = [
            selected.executable,
            "-hide_banner",
            "-loglevel",
            "error",
            "-y",
            "-i",
            str(source),
            "-ss",
            f"{start_seconds:.3f}",
            "-t",
            f"{duration:.3f}",
            "-vn",
            "-map_metadata",
            "-1",
            "-ac",
            "1",
            "-ar",
            "16000",
            "-c:a",
            "aac",
            "-b:a",
            "48k",
            str(output),
        ]
    elif selected.name == "swift-asset-reader":
        command = [
            selected.executable,
            str(source),
            str(output),
            f"{start_seconds:.3f}",
            f"{duration:.3f}",
        ]
    else:  # pragma: no cover - internal invariant
        raise MediaToolError(f"unsupported clip backend: {selected.name}")

    try:
        completed = subprocess.run(
            command,
            text=True,
            capture_output=True,
            check=False,
            timeout=120,
        )
    except subprocess.TimeoutExpired as exc:
        raise MediaToolError(
            f"{selected.name} timed out extracting {source.name}"
        ) from exc
    if completed.returncode != 0:
        detail = completed.stderr.strip() or completed.stdout.strip()
        raise MediaToolError(
            f"{selected.name} failed to extract {source.name}: {detail[:800]}"
        )
    if not output.is_file() or output.stat().st_size == 0:
        raise MediaToolError(
            f"{selected.name} reported success but produced no clip: {output}"
        )


def probe_duration(
    source: Path, *, backend: MediaBackend | None = None
) -> float:
    source = source.expanduser().resolve()
    if not source.is_file():
        raise MediaToolError(f"source media file not found: {source}")
    selected = backend or resolve_probe_backend()

    if selected.name == "ffprobe":
        command = [
            selected.executable,
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "json",
            str(source),
        ]
        try:
            completed = subprocess.run(
                command,
                text=True,
                capture_output=True,
                check=False,
                timeout=60,
            )
        except subprocess.TimeoutExpired as exc:
            raise MediaToolError(f"ffprobe timed out for {source}") from exc
        if completed.returncode != 0:
            raise MediaToolError(
                f"ffprobe failed for {source}: {completed.stderr.strip()[:800]}"
            )
        try:
            payload = json.loads(completed.stdout)
            duration = float(payload["format"]["duration"])
        except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
            raise MediaToolError(f"ffprobe returned no valid duration for {source}") from exc
    elif selected.name == "afinfo":
        command = [selected.executable, "-r", str(source)]
        try:
            completed = subprocess.run(
                command,
                text=True,
                capture_output=True,
                check=False,
                timeout=60,
            )
        except subprocess.TimeoutExpired as exc:
            raise MediaToolError(f"afinfo timed out for {source}") from exc
        if completed.returncode != 0:
            raise MediaToolError(
                f"afinfo failed for {source}: {completed.stderr.strip()[:800]}"
            )
        match = re.search(
            r"^estimated duration:\s*([0-9]+(?:\.[0-9]+)?)\s+sec\s*$",
            completed.stdout,
            flags=re.MULTILINE,
        )
        if not match:
            raise MediaToolError(f"afinfo returned no valid duration for {source}")
        duration = float(match.group(1))
    else:  # pragma: no cover - internal invariant
        raise MediaToolError(f"unsupported probe backend: {selected.name}")

    if duration <= 0:
        raise MediaToolError(f"media duration must be positive for {source}")
    return duration
