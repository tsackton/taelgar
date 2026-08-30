#!/usr/bin/env python3
"""Transcribe one RPG session recording with ElevenLabs Scribe v2."""

from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Sequence

from media_tools import (
    MediaBackend,
    MediaToolError,
    extract_audio_clip,
    prepare_clip_source,
    resolve_clip_backend,
)
from workspace_paths import resolve_transcription_output

try:
    import yaml
except ImportError as exc:  # pragma: no cover - dependency guard
    raise SystemExit("transcribe-session requires PyYAML: python3 -m pip install PyYAML") from exc


API_URL = "https://api.elevenlabs.io/v1/speech-to-text"
MODEL_ID = "scribe_v2"
STANDARD_KEY_NAME = "ELEVENLABS_API_KEY"
LEGACY_KEY_NAME = "ELEVEN_LABS_API"
MAX_KEYTERMS = 1000
MAX_KEYTERM_CHARACTERS = 49
MAX_KEYTERM_WORDS = 5
TURN_GAP_SECONDS = 2.0
SPEAKER_SAMPLES_PER_ID = 3
MIN_SAMPLE_SECONDS = 4.0
MAX_SAMPLE_SECONDS = 12.0
SAMPLE_PADDING_SECONDS = 0.25
MIN_SAMPLE_SEPARATION_SECONDS = 30.0

MIME_TYPES = {
    ".aac": "audio/aac",
    ".flac": "audio/flac",
    ".m4a": "audio/mp4",
    ".mp3": "audio/mpeg",
    ".mp4": "video/mp4",
    ".mov": "video/quicktime",
    ".ogg": "audio/ogg",
    ".wav": "audio/wav",
    ".webm": "audio/webm",
}


class TranscriptionError(RuntimeError):
    """A user-facing transcription failure."""


@dataclass(frozen=True)
class OutputPaths:
    raw_json: Path
    vtt: Path
    manifest: Path
    speaker_preview: Path
    speaker_samples_dir: Path

    def values(self) -> tuple[Path, ...]:
        return (
            self.raw_json,
            self.vtt,
            self.manifest,
            self.speaker_preview,
            self.speaker_samples_dir,
        )


@dataclass
class Turn:
    speaker: str
    start: float
    end: float
    text: str


@dataclass(frozen=True)
class SpeakerSamplePlan:
    speaker: str
    sample_index: int
    start: float
    end: float
    text: str


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Transcribe one RPG session recording with ElevenLabs Scribe v2 and "
            "produce raw JSON, VTT, provenance, and speaker-review artifacts."
        )
    )
    parser.add_argument("audio", type=Path, help="Local audio or video recording to upload.")
    parser.add_argument(
        "--participants",
        type=Path,
        required=True,
        help="Campaign participant roster YAML; player and game-role names become keyterms.",
    )
    parser.add_argument(
        "--keyterms",
        type=Path,
        help="Optional UTF-8 file containing one campaign/world keyterm per line.",
    )
    parser.add_argument(
        "--keyterm",
        action="append",
        default=[],
        help="Additional keyterm; may be supplied more than once.",
    )
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--language-code", default="eng")
    speaker_group = parser.add_mutually_exclusive_group()
    speaker_group.add_argument(
        "--num-speakers",
        type=int,
        help="Expected speakers; defaults to the number of roster participants.",
    )
    speaker_group.add_argument(
        "--auto-speakers",
        action="store_true",
        help="Omit num_speakers and let Scribe v2 detect the speaker count.",
    )
    parser.add_argument(
        "--env-file",
        type=Path,
        help="Optional secrets file outside the vault containing the API key.",
    )
    parser.add_argument(
        "--confirm-upload",
        action="store_true",
        help="Confirm that this exact recording is authorized for upload to ElevenLabs.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate and print the resolved plan without uploading or writing outputs.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace existing output artifacts after a fresh successful response.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        return run(args)
    except TranscriptionError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


def run(args: argparse.Namespace) -> int:
    audio_path = resolve_input_file(args.audio, "audio")
    participants_path = resolve_input_file(args.participants, "participant roster")
    keyterms_path = (
        resolve_input_file(args.keyterms, "keyterm file") if args.keyterms else None
    )
    output_dir = resolve_transcription_output(
        args.output_dir,
        error_type=TranscriptionError,
        label="transcription output directory",
    )

    participant_terms, participant_count = load_participant_terms(participants_path)
    file_terms = load_keyterm_file(keyterms_path) if keyterms_path else []
    keyterms = validate_keyterms([*participant_terms, *file_terms, *args.keyterm])

    num_speakers = (
        None
        if args.auto_speakers
        else participant_count if args.num_speakers is None else args.num_speakers
    )
    if num_speakers is not None and num_speakers < 1:
        raise TranscriptionError("--num-speakers must be a positive integer")
    language_code = str(args.language_code).strip()
    if not language_code:
        raise TranscriptionError("--language-code cannot be blank")
    try:
        clip_backend = resolve_clip_backend()
    except MediaToolError as exc:
        raise TranscriptionError(str(exc)) from exc

    outputs = build_output_paths(audio_path, output_dir)
    plan = build_plan(
        audio_path=audio_path,
        participants_path=participants_path,
        keyterms_path=keyterms_path,
        output_dir=output_dir,
        outputs=outputs,
        language_code=language_code,
        num_speakers=num_speakers,
        keyterms=keyterms,
        clip_backend=clip_backend,
        include_audio_hash=args.dry_run,
    )

    if args.dry_run:
        api_key_source = resolve_api_key(args.env_file, required=False)[1]
        plan["apiKeySource"] = api_key_source or "not configured (not required for dry-run)"
        print(json.dumps(plan, indent=2, ensure_ascii=False))
        return 0

    if not args.confirm_upload:
        raise TranscriptionError(
            "refusing external upload without --confirm-upload; run --dry-run and obtain explicit authorization first"
        )

    api_key, api_key_source = resolve_api_key(args.env_file, required=True)
    assert api_key is not None
    ensure_outputs_available(outputs, force=args.force)
    output_dir.mkdir(parents=True, exist_ok=True)

    audio_sha256 = sha256_file(audio_path)
    request_fingerprint = build_request_fingerprint(
        audio_sha256=audio_sha256,
        language_code=language_code,
        num_speakers=num_speakers,
        keyterms=keyterms,
    )

    response_temp = make_temp_path(output_dir, f".{audio_path.stem}.", ".response.json")
    media_temp_dir = Path(
        tempfile.mkdtemp(dir=output_dir, prefix=f".{audio_path.stem}.speaker-media.")
    )
    samples_temp_dir: Path | None = None
    try:
        prepared_audio_path, prepared_clip_backend = preflight_speaker_samples(
            audio_path=audio_path,
            backend=clip_backend,
            temporary_dir=media_temp_dir,
        )
        status_code = invoke_curl(
            api_key=api_key,
            audio_path=audio_path,
            response_path=response_temp,
            language_code=language_code,
            num_speakers=num_speakers,
            keyterms=keyterms,
        )
        if not 200 <= status_code < 300:
            raise TranscriptionError(format_api_error(status_code, response_temp))

        payload = load_and_validate_response(response_temp)
        turns = build_turns(payload["words"])
        if not turns:
            raise TranscriptionError("ElevenLabs returned no timed transcript turns")

        vtt_text = render_vtt(turns)
        sample_plans = select_speaker_sample_plans(turns)
        samples_temp_dir = Path(
            tempfile.mkdtemp(dir=output_dir, prefix=f".{audio_path.stem}.speaker-samples.")
        )
        sample_metadata = extract_speaker_samples(
            audio_path=prepared_audio_path,
            plans=sample_plans,
            temporary_dir=samples_temp_dir,
            final_dir=outputs.speaker_samples_dir,
            backend=prepared_clip_backend,
        )
        preview_text = render_speaker_preview(
            turns,
            audio_path.name,
            sample_metadata=sample_metadata,
            samples_dir_name=outputs.speaker_samples_dir.name,
        )
        response_summary = summarize_response(payload, turns, num_speakers)
        response_summary["speakerSampleCount"] = len(sample_metadata)
        manifest_payload = build_manifest(
            audio_path=audio_path,
            audio_sha256=audio_sha256,
            participants_path=participants_path,
            keyterms_path=keyterms_path,
            keyterms=keyterms,
            language_code=language_code,
            num_speakers=num_speakers,
            request_fingerprint=request_fingerprint,
            outputs=outputs,
            response_temp=response_temp,
            vtt_text=vtt_text,
            preview_text=preview_text,
            sample_metadata=sample_metadata,
            response_summary=response_summary,
        )

        os.replace(response_temp, outputs.raw_json)
        atomic_write_text(outputs.vtt, vtt_text)
        replace_directory(
            samples_temp_dir,
            outputs.speaker_samples_dir,
            force=args.force,
        )
        samples_temp_dir = None
        atomic_write_text(outputs.speaker_preview, preview_text)
        atomic_write_text(
            outputs.manifest,
            json.dumps(manifest_payload, indent=2, ensure_ascii=False) + "\n",
        )
    finally:
        response_temp.unlink(missing_ok=True)
        shutil.rmtree(media_temp_dir, ignore_errors=True)
        if samples_temp_dir is not None:
            shutil.rmtree(samples_temp_dir, ignore_errors=True)

    print(f"API key source: {api_key_source}")
    print(f"Wrote {outputs.raw_json}")
    print(f"Wrote {outputs.vtt}")
    print(f"Wrote {outputs.manifest}")
    print(f"Wrote {outputs.speaker_preview}")
    print(
        f"Wrote {outputs.speaker_samples_dir} "
        f"({response_summary['speakerSampleCount']} clips)"
    )
    print(
        "Response: "
        f"language={response_summary['languageCode']} "
        f"probability={response_summary['languageProbability']} "
        f"speakers={len(response_summary['speakerIds'])} "
        f"cues={response_summary['cueCount']}"
    )
    for warning in response_summary["warnings"]:
        print(f"warning: {warning}", file=sys.stderr)
    return 0


def resolve_input_file(path: Path, label: str) -> Path:
    resolved = path.expanduser().resolve()
    if not resolved.is_file():
        raise TranscriptionError(f"{label} file not found: {resolved}")
    if resolved.stat().st_size == 0:
        raise TranscriptionError(f"{label} file is empty: {resolved}")
    return resolved


def build_output_paths(audio_path: Path, output_dir: Path) -> OutputPaths:
    stem = audio_path.stem
    return OutputPaths(
        raw_json=output_dir / f"{stem}.scribe-v2.json",
        vtt=output_dir / f"{stem}.transcript.vtt",
        manifest=output_dir / f"{stem}.transcription.json",
        speaker_preview=output_dir / f"{stem}.speaker-preview.md",
        speaker_samples_dir=output_dir / f"{stem}.speaker-samples",
    )


def load_participant_terms(path: Path) -> tuple[list[str], int]:
    try:
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        raise TranscriptionError(f"could not read participant roster {path}: {exc}") from exc

    participants = payload.get("participants") if isinstance(payload, dict) else None
    if not isinstance(participants, list) or not participants:
        raise TranscriptionError(
            f"participant roster must contain a non-empty 'participants' list: {path}"
        )

    terms: list[str] = []
    for index, participant in enumerate(participants, start=1):
        if not isinstance(participant, dict):
            raise TranscriptionError(f"participant {index} is not a mapping in {path}")
        name = normalize_term(participant.get("name"))
        game_role = normalize_term(participant.get("gameRole"))
        if not name or not game_role:
            raise TranscriptionError(
                f"participant {index} requires non-empty name and gameRole in {path}"
            )
        terms.append(name)
        terms.extend(participant_name_parts(name))
        terms.append(game_role)
    return terms, len(participants)


def participant_name_parts(name: str) -> list[str]:
    parts = [part.strip(".,;:()[]{}") for part in name.split()]
    return [part for part in parts if len(part) >= 3]


def load_keyterm_file(path: Path) -> list[str]:
    try:
        lines = path.read_text(encoding="utf-8-sig").splitlines()
    except (OSError, UnicodeError) as exc:
        raise TranscriptionError(f"could not read keyterm file {path}: {exc}") from exc
    return [line.strip() for line in lines if line.strip() and not line.lstrip().startswith("#")]


def normalize_term(value: Any) -> str:
    if value is None:
        return ""
    return re.sub(r"\s+", " ", str(value)).strip()


def validate_keyterms(raw_terms: Iterable[Any]) -> list[str]:
    terms: list[str] = []
    seen: set[str] = set()
    for raw in raw_terms:
        term = normalize_term(raw)
        if not term:
            continue
        if any(ord(char) < 32 for char in term):
            raise TranscriptionError(f"keyterm contains a control character: {term!r}")
        if len(term) > MAX_KEYTERM_CHARACTERS:
            raise TranscriptionError(
                f"keyterm must contain fewer than 50 characters: {term!r}"
            )
        if len(term.split()) > MAX_KEYTERM_WORDS:
            raise TranscriptionError(f"keyterm must contain at most five words: {term!r}")
        folded = term.casefold()
        if folded in seen:
            continue
        seen.add(folded)
        terms.append(term)
    if len(terms) > MAX_KEYTERMS:
        raise TranscriptionError(
            f"resolved {len(terms)} keyterms; ElevenLabs accepts at most {MAX_KEYTERMS}"
        )
    return terms


def build_plan(
    *,
    audio_path: Path,
    participants_path: Path,
    keyterms_path: Path | None,
    output_dir: Path,
    outputs: OutputPaths,
    language_code: str,
    num_speakers: int | None,
    keyterms: list[str],
    clip_backend: MediaBackend,
    include_audio_hash: bool,
) -> dict[str, Any]:
    plan: dict[str, Any] = {
        "operation": "dry-run" if include_audio_hash else "transcribe",
        "service": "ElevenLabs",
        "endpoint": API_URL,
        "model": MODEL_ID,
        "audio": {
            "path": str(audio_path),
            "bytes": audio_path.stat().st_size,
        },
        "participantsPath": str(participants_path),
        "keytermsPath": str(keyterms_path) if keyterms_path else None,
        "languageCode": language_code,
        "numSpeakers": num_speakers,
        "speakerDetection": "automatic" if num_speakers is None else "expected-count",
        "keytermCount": len(keyterms),
        "keyterms": keyterms,
        "speakerSampleBackend": clip_backend.name,
        "speakerSamplesPerId": SPEAKER_SAMPLES_PER_ID,
        "outputDirectory": str(output_dir),
        "outputs": [str(path) for path in outputs.values()],
    }
    if include_audio_hash:
        plan["audio"]["sha256"] = sha256_file(audio_path)
    return plan


def parse_env_file(path: Path) -> dict[str, str]:
    resolved = resolve_input_file(path, "env")
    mode = stat.S_IMODE(resolved.stat().st_mode)
    if mode & 0o077:
        print(
            f"warning: env file is readable by group or others ({oct(mode)}): {resolved}",
            file=sys.stderr,
        )

    values: dict[str, str] = {}
    try:
        lines = resolved.read_text(encoding="utf-8-sig").splitlines()
    except (OSError, UnicodeError) as exc:
        raise TranscriptionError(f"could not read env file {resolved}: {exc}") from exc

    for line_number, raw_line in enumerate(lines, start=1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:].lstrip()
        if "=" not in line:
            continue
        name, raw_value = line.split("=", 1)
        name = name.strip()
        if name not in {STANDARD_KEY_NAME, LEGACY_KEY_NAME}:
            continue
        value = raw_value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
            value = value[1:-1]
        if "\n" in value or "\r" in value:
            raise TranscriptionError(
                f"invalid {name} value at {resolved}:{line_number}"
            )
        values[name] = value
    return values


def resolve_api_key(
    env_file: Path | None, *, required: bool
) -> tuple[str | None, str | None]:
    for name in (STANDARD_KEY_NAME, LEGACY_KEY_NAME):
        value = os.environ.get(name, "").strip()
        if value:
            validate_api_key(value, name)
            return value, f"environment:{name}"

    if env_file is not None:
        values = parse_env_file(env_file)
        for name in (STANDARD_KEY_NAME, LEGACY_KEY_NAME):
            value = values.get(name, "").strip()
            if value:
                validate_api_key(value, name)
                return value, f"env-file:{env_file.expanduser().resolve()}:{name}"

    if required:
        raise TranscriptionError(
            f"no ElevenLabs API key found; set {STANDARD_KEY_NAME} or pass --env-file"
        )
    return None, None


def validate_api_key(value: str, name: str) -> None:
    if any(char in value for char in ('\n', '\r', '"', "\\")):
        raise TranscriptionError(
            f"{name} contains unsupported control, quote, or escape characters"
        )


def ensure_outputs_available(outputs: OutputPaths, *, force: bool) -> None:
    existing = [path for path in outputs.values() if path.exists()]
    if existing and not force:
        formatted = "\n".join(f"- {path}" for path in existing)
        raise TranscriptionError(
            "refusing to replace existing outputs without --force:\n" + formatted
        )


def invoke_curl(
    *,
    api_key: str,
    audio_path: Path,
    response_path: Path,
    language_code: str,
    num_speakers: int | None,
    keyterms: list[str],
) -> int:
    curl = shutil.which("curl")
    if curl is None:
        raise TranscriptionError("curl is required but was not found in PATH")

    mime_type = MIME_TYPES.get(
        audio_path.suffix.lower(),
        mimetypes.guess_type(audio_path.name)[0] or "application/octet-stream",
    )
    command = [
        curl,
        "-q",
        "--config",
        "-",
        "--silent",
        "--show-error",
        "--request",
        "POST",
        API_URL,
        "--connect-timeout",
        "30",
        "--output",
        str(response_path),
        "--write-out",
        "%{http_code}",
        "--form",
        f"file=@{audio_path};type={mime_type}",
        "--form-string",
        f"model_id={MODEL_ID}",
        "--form-string",
        f"language_code={language_code}",
        "--form-string",
        "tag_audio_events=true",
        "--form-string",
        "diarize=true",
        "--form-string",
        "timestamps_granularity=word",
    ]
    if num_speakers is not None:
        command.extend(["--form-string", f"num_speakers={num_speakers}"])
    for term in keyterms:
        command.extend(["--form-string", f"keyterms={term}"])

    curl_config = f'header = "xi-api-key: {api_key}"\n'
    completed = subprocess.run(
        command,
        input=curl_config,
        text=True,
        capture_output=True,
        check=False,
    )
    if completed.returncode != 0:
        detail = completed.stderr.strip() or f"curl exited {completed.returncode}"
        raise TranscriptionError(f"ElevenLabs request failed before an HTTP response: {detail}")
    status_text = completed.stdout.strip()
    if not status_text.isdigit():
        raise TranscriptionError(f"could not determine ElevenLabs HTTP status: {status_text!r}")
    return int(status_text)


def format_api_error(status_code: int, response_path: Path) -> str:
    detail = ""
    try:
        payload = json.loads(response_path.read_text(encoding="utf-8"))
        candidate: Any = payload.get("detail") if isinstance(payload, dict) else None
        if isinstance(candidate, dict):
            candidate = candidate.get("message") or candidate.get("detail")
        if candidate is not None:
            detail = normalize_term(candidate)
    except (OSError, UnicodeError, json.JSONDecodeError):
        pass
    suffix = f": {detail[:500]}" if detail else ""
    return f"ElevenLabs returned HTTP {status_code}{suffix}"


def load_and_validate_response(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise TranscriptionError(f"ElevenLabs response was not valid UTF-8 JSON: {exc}") from exc
    if not isinstance(payload, dict):
        raise TranscriptionError("ElevenLabs response must be a JSON object")
    words = payload.get("words")
    if not isinstance(words, list):
        raise TranscriptionError("ElevenLabs response is missing the words list")

    previous_start = -1.0
    timed_items = 0
    for index, item in enumerate(words):
        if not isinstance(item, dict):
            raise TranscriptionError(f"response words[{index}] is not an object")
        start = item.get("start")
        end = item.get("end")
        if start is None and end is None:
            continue
        if not isinstance(start, (int, float)) or not isinstance(end, (int, float)):
            raise TranscriptionError(f"response words[{index}] has invalid timestamps")
        start_value = float(start)
        end_value = float(end)
        if start_value < 0 or end_value < start_value:
            raise TranscriptionError(f"response words[{index}] has an invalid time range")
        if start_value + 0.001 < previous_start:
            raise TranscriptionError("response word timestamps are not ordered")
        previous_start = start_value
        timed_items += 1
    if timed_items == 0:
        raise TranscriptionError("ElevenLabs response contains no timed word items")
    return payload


def build_turns(items: Sequence[dict[str, Any]]) -> list[Turn]:
    turns: list[Turn] = []
    current: Turn | None = None
    for item in items:
        start = item.get("start")
        end = item.get("end")
        text = item.get("text")
        if not isinstance(start, (int, float)) or not isinstance(end, (int, float)):
            continue
        if not isinstance(text, str) or not text:
            continue
        speaker_value = item.get("speaker_id")
        speaker = normalize_term(speaker_value) or (current.speaker if current else "unknown")
        start_value = float(start)
        end_value = float(end)
        starts_new_turn = (
            current is None
            or speaker != current.speaker
            or start_value - current.end > TURN_GAP_SECONDS
        )
        if starts_new_turn:
            if current is not None:
                turns.append(clean_turn(current))
            current = Turn(speaker=speaker, start=start_value, end=end_value, text=text)
        else:
            current.text += text
            current.end = max(current.end, end_value)
    if current is not None:
        turns.append(clean_turn(current))
    return [turn for turn in turns if turn.text]


def clean_turn(turn: Turn) -> Turn:
    turn.text = re.sub(r"[ \t]+", " ", turn.text.replace("\r", " ").replace("\n", " ")).strip()
    return turn


def render_vtt(turns: Sequence[Turn]) -> str:
    lines = ["WEBVTT", ""]
    for turn in turns:
        start_milliseconds = max(0, round(turn.start * 1000))
        end_milliseconds = max(start_milliseconds + 1, round(turn.end * 1000))
        lines.append(
            f"{format_vtt_milliseconds(start_milliseconds)} --> "
            f"{format_vtt_milliseconds(end_milliseconds)}"
        )
        lines.append(f"{turn.speaker}: {turn.text}")
        lines.append("")
    return "\n".join(lines)


def format_vtt_time(seconds: float) -> str:
    return format_vtt_milliseconds(max(0, round(seconds * 1000)))


def format_vtt_milliseconds(milliseconds: int) -> str:
    hours, remainder = divmod(milliseconds, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    whole_seconds, millis = divmod(remainder, 1000)
    return f"{hours:02d}:{minutes:02d}:{whole_seconds:02d}.{millis:03d}"


def select_speaker_sample_plans(
    turns: Sequence[Turn], *, samples_per_speaker: int = SPEAKER_SAMPLES_PER_ID
) -> list[SpeakerSamplePlan]:
    by_speaker: dict[str, list[Turn]] = {}
    for turn in turns:
        if turn.text:
            by_speaker.setdefault(turn.speaker, []).append(turn)

    plans: list[SpeakerSamplePlan] = []
    for speaker in sorted(by_speaker):
        turns_for_speaker = by_speaker[speaker]
        eligible = [
            turn
            for turn in turns_for_speaker
            if turn.end - turn.start >= MIN_SAMPLE_SECONDS
            and len(turn.text.split()) >= 6
        ]
        candidates = eligible or turns_for_speaker
        ranked = sorted(candidates, key=sample_candidate_score, reverse=True)
        selected: list[Turn] = []
        for turn in ranked:
            if all(
                abs(turn.start - existing.start) >= MIN_SAMPLE_SEPARATION_SECONDS
                for existing in selected
            ):
                selected.append(turn)
                if len(selected) == samples_per_speaker:
                    break
        if len(selected) < samples_per_speaker:
            for turn in ranked:
                if turn not in selected:
                    selected.append(turn)
                    if len(selected) == samples_per_speaker:
                        break

        for sample_index, turn in enumerate(sorted(selected, key=lambda item: item.start), start=1):
            start = max(0.0, turn.start - SAMPLE_PADDING_SECONDS)
            end = min(turn.end + SAMPLE_PADDING_SECONDS, start + MAX_SAMPLE_SECONDS)
            if end <= start:
                continue
            plans.append(
                SpeakerSamplePlan(
                    speaker=speaker,
                    sample_index=sample_index,
                    start=start,
                    end=end,
                    text=turn.text,
                )
            )
    return plans


def sample_candidate_score(turn: Turn) -> float:
    duration = min(MAX_SAMPLE_SECONDS, max(0.0, turn.end - turn.start))
    word_count = min(40, len(turn.text.split()))
    audio_event_count = len(re.findall(r"\[[^\]]+\]", turn.text))
    return duration * 3.0 + word_count - audio_event_count * 6.0


def preflight_speaker_samples(
    *, audio_path: Path, backend: MediaBackend, temporary_dir: Path
) -> tuple[Path, MediaBackend]:
    try:
        prepared_source, prepared_backend = prepare_clip_source(
            audio_path,
            backend=backend,
            work_dir=temporary_dir,
        )
        probe_path = temporary_dir / ".speaker-sample-probe.m4a"
        extract_audio_clip(
            prepared_source,
            probe_path,
            start_seconds=0.0,
            end_seconds=1.0,
            backend=prepared_backend,
        )
        probe_path.unlink(missing_ok=True)
        return prepared_source, prepared_backend
    except MediaToolError as exc:
        raise TranscriptionError(
            f"speaker-sample preflight failed before upload: {exc}"
        ) from exc


def extract_speaker_samples(
    *,
    audio_path: Path,
    plans: Sequence[SpeakerSamplePlan],
    temporary_dir: Path,
    final_dir: Path,
    backend: MediaBackend,
) -> list[dict[str, Any]]:
    metadata: list[dict[str, Any]] = []
    used_names: set[str] = set()
    try:
        prepared_source, prepared_backend = prepare_clip_source(
            audio_path, backend=backend, work_dir=temporary_dir
        )
        for plan in plans:
            safe_speaker = safe_filename_component(plan.speaker)
            filename = f"{safe_speaker}-{plan.sample_index:02d}.m4a"
            if filename.casefold() in used_names:
                suffix = hashlib.sha256(plan.speaker.encode("utf-8")).hexdigest()[:8]
                filename = f"{safe_speaker}-{suffix}-{plan.sample_index:02d}.m4a"
            used_names.add(filename.casefold())
            temporary_path = temporary_dir / filename
            extract_audio_clip(
                prepared_source,
                temporary_path,
                start_seconds=plan.start,
                end_seconds=plan.end,
                backend=prepared_backend,
            )
            metadata.append(
                {
                    "speakerId": plan.speaker,
                    "sampleIndex": plan.sample_index,
                    "startSeconds": round(plan.start, 3),
                    "endSeconds": round(plan.end, 3),
                    "text": plan.text,
                    "path": str(final_dir / filename),
                    "sha256": sha256_file(temporary_path),
                }
            )
    except MediaToolError as exc:
        raise TranscriptionError(str(exc)) from exc
    finally:
        (temporary_dir / ".extract-audio-clip").unlink(missing_ok=True)
        shutil.rmtree(temporary_dir / ".swift-module-cache", ignore_errors=True)
    return metadata


def safe_filename_component(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "-", value).strip("-._")
    return cleaned or "speaker"


def render_speaker_preview(
    turns: Sequence[Turn],
    audio_name: str,
    *,
    sample_metadata: Sequence[dict[str, Any]] = (),
    samples_dir_name: str = "speaker-samples",
) -> str:
    by_speaker: dict[str, list[Turn]] = {}
    for turn in turns:
        by_speaker.setdefault(turn.speaker, []).append(turn)

    lines = [
        "# Speaker Preview",
        "",
        f"Source: `{audio_name}`",
        "",
        "Use these excerpts to identify the per-file speaker IDs. Do not assume IDs remain stable across recordings.",
        "",
    ]
    for speaker in sorted(by_speaker):
        lines.extend([f"## {speaker}", ""])
        speaker_samples = [
            sample for sample in sample_metadata if sample["speakerId"] == speaker
        ]
        if speaker_samples:
            for sample in speaker_samples:
                excerpt = shorten_excerpt(str(sample["text"]))
                filename = Path(str(sample["path"])).name
                lines.append(
                    f"- [{format_vtt_time(float(sample['startSeconds']))}] "
                    f"[Audio sample {sample['sampleIndex']}](<{samples_dir_name}/{filename}>) — "
                    f"{excerpt}"
                )
        else:
            candidates = [
                turn for turn in by_speaker[speaker] if len(turn.text.split()) >= 4
            ]
            if not candidates:
                candidates = by_speaker[speaker]
            for turn in candidates[:3]:
                lines.append(
                    f"- [{format_vtt_time(turn.start)}] {shorten_excerpt(turn.text)}"
                )
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def shorten_excerpt(text: str, limit: int = 240) -> str:
    return text if len(text) <= limit else text[: limit - 3].rstrip() + "..."


def summarize_response(
    payload: dict[str, Any], turns: Sequence[Turn], expected_speakers: int | None
) -> dict[str, Any]:
    speaker_ids = sorted({turn.speaker for turn in turns})
    warnings: list[str] = []
    if expected_speakers is not None and len(speaker_ids) != expected_speakers:
        warnings.append(
            f"expected {expected_speakers} speakers but response contains {len(speaker_ids)} speaker IDs"
        )
    return {
        "transcriptionId": payload.get("transcription_id"),
        "languageCode": payload.get("language_code"),
        "languageProbability": payload.get("language_probability"),
        "audioDurationSeconds": payload.get("audio_duration_secs"),
        "wordItemCount": len(payload["words"]),
        "cueCount": len(turns),
        "speakerIds": speaker_ids,
        "warnings": warnings,
    }


def build_request_fingerprint(
    *,
    audio_sha256: str,
    language_code: str,
    num_speakers: int | None,
    keyterms: list[str],
) -> str:
    payload = {
        "audioSha256": audio_sha256,
        "model": MODEL_ID,
        "languageCode": language_code,
        "diarize": True,
        "tagAudioEvents": True,
        "timestampsGranularity": "word",
        "keyterms": keyterms,
    }
    if num_speakers is not None:
        payload["numSpeakers"] = num_speakers
    encoded = json.dumps(payload, sort_keys=True, ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def build_manifest(
    *,
    audio_path: Path,
    audio_sha256: str,
    participants_path: Path,
    keyterms_path: Path | None,
    keyterms: list[str],
    language_code: str,
    num_speakers: int | None,
    request_fingerprint: str,
    outputs: OutputPaths,
    response_temp: Path,
    vtt_text: str,
    preview_text: str,
    sample_metadata: Sequence[dict[str, Any]],
    response_summary: dict[str, Any],
) -> dict[str, Any]:
    manifest: dict[str, Any] = {
        "schemaVersion": 1,
        "createdAt": datetime.now(timezone.utc).isoformat(),
        "source": {
            "path": str(audio_path),
            "bytes": audio_path.stat().st_size,
            "sha256": audio_sha256,
        },
        "request": {
            "service": "ElevenLabs",
            "endpoint": API_URL,
            "model": MODEL_ID,
            "languageCode": language_code,
            "diarize": True,
            "tagAudioEvents": True,
            "timestampsGranularity": "word",
            "participantsPath": str(participants_path),
            "keytermsPath": str(keyterms_path) if keyterms_path else None,
            "keyterms": keyterms,
            "keytermsSha256": sha256_json(keyterms),
            "fingerprint": request_fingerprint,
        },
        "response": response_summary,
        "outputs": {
            "rawJson": str(outputs.raw_json),
            "rawJsonSha256": sha256_file(response_temp),
            "transcriptVtt": str(outputs.vtt),
            "transcriptVttSha256": sha256_text(vtt_text),
            "speakerPreview": str(outputs.speaker_preview),
            "speakerPreviewSha256": sha256_text(preview_text),
            "speakerSamplesDirectory": str(outputs.speaker_samples_dir),
            "speakerSamples": list(sample_metadata),
        },
    }
    if num_speakers is not None:
        manifest["request"]["numSpeakers"] = num_speakers
    else:
        manifest["request"]["speakerDetection"] = "automatic"
    return manifest


def sha256_json(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def make_temp_path(directory: Path, prefix: str, suffix: str) -> Path:
    descriptor, raw_path = tempfile.mkstemp(dir=directory, prefix=prefix, suffix=suffix)
    os.close(descriptor)
    return Path(raw_path)


def atomic_write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = make_temp_path(path.parent, f".{path.name}.", ".tmp")
    try:
        temp_path.write_text(content, encoding="utf-8")
        os.replace(temp_path, path)
    finally:
        temp_path.unlink(missing_ok=True)


def replace_directory(source: Path, destination: Path, *, force: bool) -> None:
    if destination.exists() or destination.is_symlink():
        if not force:
            raise TranscriptionError(
                f"refusing to replace existing speaker sample directory without --force: {destination}"
            )
        if destination.is_symlink() or destination.is_file():
            destination.unlink()
        else:
            shutil.rmtree(destination)
    os.replace(source, destination)


if __name__ == "__main__":
    raise SystemExit(main())
