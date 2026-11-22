"""Preview or apply the installed Taelgarverse saved-header writer."""
import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile


def apply_preview(source: bytes, plan: dict) -> bytes:
    # The native writer reports JavaScript string offsets in UTF-16 code units.
    text = source.decode("utf-8").encode("utf-16-le")
    start, end = plan["start"] * 2, plan["end"] * 2
    if not 0 <= start <= end <= len(text) or text[start:end] != plan["before"].encode("utf-16-le"):
        raise ValueError("The native header preview does not match the candidate")
    replacement = plan["replacement"].encode("utf-16-le")
    return (text[:start] + replacement + text[end:]).decode("utf-16-le").encode("utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("note", type=Path)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[4])
    parser.add_argument("--add", action="store_true", help="Add a header to an eligible candidate without one")
    parser.add_argument("--write", action="store_true", help="Apply the native writer after page approval")
    args = parser.parse_args()
    root, note = args.root.resolve(), args.note.resolve()
    try:
        relative = note.relative_to(root)
        if args.note.is_symlink():
            raise ValueError("Use a regular vault note rather than a symlink")
        tool = root / ".obsidian" / "plugins" / "taelgarverse" / "header-tool.cjs"
        if not tool.is_file():
            raise ValueError("Install or reload Taelgarverse to make its header tool available")
        source = note.read_bytes()
        with tempfile.TemporaryDirectory(prefix="taelgar-header-preview-") as folder:
            report = Path(folder) / "result.json"
            command = ["node", str(tool), "--vault", str(root), "--file", relative.as_posix(),
                       "--report", str(report)]
            if args.add:
                command.append("--add")
            if args.write:
                command.append("--write")
            result = subprocess.run(command, capture_output=True, encoding="utf-8", check=False)
            if not report.is_file():
                raise ValueError(result.stderr.strip() or result.stdout.strip() or "No native header report")
            plan, = json.loads(report.read_text(encoding="utf-8"))["files"]
        if result.returncode or plan["status"] not in {"changed", "unchanged"}:
            raise ValueError(plan.get("reason") or result.stderr.strip() or result.stdout.strip())
        if args.write:
            if plan["status"] == "changed" and not plan.get("written"):
                raise ValueError("The native writer did not save this header")
            sys.stdout.write(result.stdout)
        else:
            if note.read_bytes() != source:
                raise ValueError("The candidate changed during preview")
            sys.stdout.buffer.write(apply_preview(source, plan))
    except (OSError, ValueError, KeyError) as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()
