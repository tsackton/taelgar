#!/usr/bin/env python3
"""Export an approved static image without resizing or overwriting any file."""

import argparse
import hashlib
import io
import json
import os
from pathlib import Path
import re
import tempfile

from PIL import Image, ImageOps


FORMATS = {
    "webp": ("WEBP", {".webp"}, {"quality": 90, "method": 6}),
    "webp-lossless": ("WEBP", {".webp"}, {"lossless": True, "exact": True, "method": 6}),
    "jpg": ("JPEG", {".jpg", ".jpeg"}, {"quality": 90, "subsampling": 0}),
    "png": ("PNG", {".png"}, {}),
}


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def export_image(source, destination, format_name="webp", background=None):
    source = Path(source).expanduser().resolve(strict=True)
    # Do not resolve a destination symlink: even a dangling link is a collision.
    destination = Path(destination).expanduser().absolute()
    if os.path.lexists(destination):
        raise FileExistsError(f"Destination already exists: {destination}")
    encoding, suffixes, settings = FORMATS[format_name]
    if destination.suffix.lower() not in suffixes:
        raise ValueError(f"{format_name} requires extension {', '.join(sorted(suffixes))}")
    if background is not None:
        if format_name != "jpg" or not re.fullmatch(r"#[0-9a-fA-F]{6}", background):
            raise ValueError("--background requires JPEG and a color such as '#ffffff'")

    original = source.read_bytes()
    with Image.open(io.BytesIO(original)) as opened:
        if getattr(opened, "n_frames", 1) != 1:
            raise ValueError("Animated or multi-frame inputs are not supported")
        source_format = opened.format
        icc_profile = opened.info.get("icc_profile")
        # Preserve displayed orientation while avoiding stale EXIF orientation.
        oriented = ImageOps.exif_transpose(opened)
        rgba = oriented.convert("RGBA")
        has_transparency = rgba.getchannel("A").getextrema()[0] < 255
        if encoding == "JPEG":
            if has_transparency and background is None:
                raise ValueError("Transparent JPEG input needs an explicitly chosen --background")
            if has_transparency:
                rgb = tuple(int(background[i:i + 2], 16) for i in (1, 3, 5))
                canvas = Image.new("RGBA", rgba.size, rgb + (255,))
                canvas.alpha_composite(rgba)
                prepared = canvas.convert("RGB")
            else:
                prepared = rgba.convert("RGB")
        else:
            prepared = rgba if has_transparency else rgba.convert("RGB")

    buffer = io.BytesIO()
    save_settings = dict(settings)
    if icc_profile:
        save_settings["icc_profile"] = icc_profile
    prepared.save(buffer, format=encoding, **save_settings)
    encoded = buffer.getvalue()
    with Image.open(io.BytesIO(encoded)) as check:
        check.load()
        if check.format != encoding or check.size != prepared.size:
            raise ValueError("Encoded image format or dimensions differ from the requested output")
        decoded = check.convert("RGBA")
        if encoding != "JPEG" and decoded.getchannel("A").tobytes() != rgba.getchannel("A").tobytes():
            raise ValueError("Export changed transparency")
        if format_name in {"png", "webp-lossless"} and decoded.tobytes() != rgba.tobytes():
            raise ValueError("Lossless export changed pixels")
        alpha = decoded.getchannel("A").getextrema()[0] < 255

    # Publish a fully encoded file atomically, without replacing a concurrent file.
    destination.parent.mkdir(parents=True, exist_ok=True)
    temp_path = None
    try:
        with tempfile.NamedTemporaryFile(dir=destination.parent, prefix=".image-export-", delete=False) as temporary:
            temp_path = Path(temporary.name)
            temporary.write(encoded)
            temporary.flush()
            os.fsync(temporary.fileno())
        os.link(temp_path, destination)
    finally:
        if temp_path is not None:
            temp_path.unlink(missing_ok=True)

    if destination.read_bytes() != encoded:
        raise OSError(f"Export readback mismatch: {destination}")
    return {
        "source": str(source),
        "source_format": source_format,
        "source_sha256": sha256(original),
        "destination": str(destination),
        "format": encoding,
        "export_choice": format_name,
        "settings": settings,
        "background": background,
        "width": prepared.width,
        "height": prepared.height,
        "has_transparency": alpha,
        "bytes": len(encoded),
        "sha256": sha256(encoded),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--format", choices=FORMATS, default="webp")
    parser.add_argument("--background", help="User-selected JPEG background as #RRGGBB")
    args = parser.parse_args()
    try:
        result = export_image(args.source, args.destination, args.format, args.background)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Export failed: {error}\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
