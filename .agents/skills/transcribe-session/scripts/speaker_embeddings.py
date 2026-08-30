#!/usr/bin/env python3
"""Create resumable ECAPA speaker-embedding caches for reviews and reference banks."""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
import time
from pathlib import Path
from typing import Any, Iterable, Sequence

from speaker_review import (
    SpeakerReviewError,
    decode_to_pcm,
    load_json_object,
    normalize_text,
    resolve_input,
    resolve_pcm_decoder,
    sha256_file,
    utc_now,
)
from workspace_paths import resolve_transcription_output


SCHEMA_VERSION = 1
DEFAULT_MODEL_NAME = "speechbrain/spkrec-ecapa-voxceleb"
DEFAULT_MINIMUM_SECONDS = 1.5
DEFAULT_MINIMUM_WORDS = 4
DEFAULT_MAXIMUM_SECONDS = 8.0
DEFAULT_CONTEXT_SECONDS = 0.12
DEFAULT_BATCH_SIZE = 32
DEFAULT_CHECKPOINT_BATCHES = 5


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Create local, resumable speaker-embedding caches. Model downloads are "
            "blocked unless --allow-model-download is supplied after authorization."
        )
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    review = subparsers.add_parser(
        "review", help="Embed durable utterances from a speaker-review JSON file."
    )
    review.add_argument("review", type=Path)
    add_common_arguments(review)
    review.add_argument(
        "--minimum-duration-seconds",
        type=float,
        default=DEFAULT_MINIMUM_SECONDS,
    )
    review.add_argument(
        "--minimum-word-count", type=int, default=DEFAULT_MINIMUM_WORDS
    )
    review.add_argument(
        "--maximum-duration-seconds",
        type=float,
        default=DEFAULT_MAXIMUM_SECONDS,
        help="Maximum audio window sent to the model for one utterance (default: 8).",
    )
    review.add_argument(
        "--context-seconds",
        type=float,
        default=DEFAULT_CONTEXT_SECONDS,
        help="Audio context added around each utterance (default: 0.12).",
    )
    review.add_argument(
        "--ffmpeg", type=Path, help="Optional ffmpeg executable when absent from PATH."
    )

    bank = subparsers.add_parser(
        "reference-bank", help="Embed the verified clips in reference-bank.json."
    )
    bank.add_argument("manifest", type=Path)
    add_common_arguments(bank)
    bank.add_argument(
        "--ffmpeg", type=Path, help="Optional ffmpeg executable when absent from PATH."
    )
    return parser


def add_common_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--model-source",
        default=DEFAULT_MODEL_NAME,
        help=(
            "Local SpeechBrain model directory, or a remote model identifier when "
            "--allow-model-download has been explicitly authorized."
        ),
    )
    parser.add_argument("--model-name", default=DEFAULT_MODEL_NAME)
    parser.add_argument(
        "--model-cache",
        type=Path,
        help="Persistent SpeechBrain model cache; required for a remote model source.",
    )
    parser.add_argument("--allow-model-download", action="store_true")
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--batch-size", type=int, default=DEFAULT_BATCH_SIZE)
    parser.add_argument(
        "--checkpoint-batches", type=int, default=DEFAULT_CHECKPOINT_BATCHES
    )
    parser.add_argument(
        "--threads",
        type=int,
        default=max(1, min(8, os.cpu_count() or 4)),
        help="Torch CPU threads (default: up to 8).",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Discard an existing cache instead of resuming it.",
    )


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        validate_runtime_arguments(args)
        if args.command == "review":
            return embed_review(args)
        if args.command == "reference-bank":
            return embed_reference_bank(args)
    except SpeakerReviewError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    raise AssertionError(f"unknown command {args.command}")


def validate_runtime_arguments(args: argparse.Namespace) -> None:
    if args.batch_size < 1:
        raise SpeakerReviewError("--batch-size must be positive")
    if args.checkpoint_batches < 1:
        raise SpeakerReviewError("--checkpoint-batches must be positive")
    if args.threads < 1:
        raise SpeakerReviewError("--threads must be positive")
    if args.command == "review":
        if args.minimum_duration_seconds <= 0:
            raise SpeakerReviewError("--minimum-duration-seconds must be positive")
        if args.minimum_word_count < 1:
            raise SpeakerReviewError("--minimum-word-count must be positive")
        if args.maximum_duration_seconds < args.minimum_duration_seconds:
            raise SpeakerReviewError(
                "--maximum-duration-seconds cannot be shorter than the minimum"
            )
        if args.context_seconds < 0:
            raise SpeakerReviewError("--context-seconds cannot be negative")


def embed_review(args: argparse.Namespace) -> int:
    review_path = resolve_input(args.review, "speaker review")
    review = load_json_object(review_path, "speaker review")
    if review.get("schemaVersion") != 1:
        raise SpeakerReviewError("speaker review has an unsupported schema")
    recordings = review.get("recordings")
    utterances = review.get("utterances")
    if not isinstance(recordings, list) or not isinstance(utterances, list):
        raise SpeakerReviewError("speaker review requires recordings and utterances")
    plan = build_review_plan(
        utterances,
        minimum_duration_seconds=args.minimum_duration_seconds,
        minimum_word_count=args.minimum_word_count,
    )
    if not plan:
        raise SpeakerReviewError("speaker review has no durable utterances to embed")
    metadata = base_metadata(
        source_type="speaker-review",
        source_path=review_path,
        source_sha256=sha256_file(review_path),
        model_name=args.model_name,
        model_source=args.model_source,
        planned_count=len(plan),
    )
    metadata["selection"] = {
        "minimumDurationSeconds": args.minimum_duration_seconds,
        "minimumWordCount": args.minimum_word_count,
        "maximumDurationSeconds": args.maximum_duration_seconds,
        "contextSeconds": args.context_seconds,
    }
    output_path, cached = prepare_output(args, metadata, [item["id"] for item in plan])
    pending = [item for item in plan if item["id"] not in cached]
    if not pending:
        print(f"Embedding cache is complete: {output_path} ({len(cached)} vectors)")
        return 0

    np, torch, classifier = load_model(args)
    decoder = resolve_pcm_decoder(explicit_ffmpeg=args.ffmpeg)
    recording_by_id = {item.get("id"): item for item in recordings}
    pending_by_recording: dict[str, list[dict[str, Any]]] = {}
    for item in pending:
        pending_by_recording.setdefault(item["recordingId"], []).append(item)
    tracker = ProgressTracker(total=len(plan), completed=len(cached))
    batch_counter = 0
    with tempfile.TemporaryDirectory(prefix="speaker-embeddings-") as raw_dir:
        work_dir = Path(raw_dir)
        for recording_id, items in pending_by_recording.items():
            recording = recording_by_id.get(recording_id)
            if not isinstance(recording, dict):
                raise SpeakerReviewError(
                    f"utterance references unknown recording {recording_id}"
                )
            audio_path = resolve_input(Path(recording["audioPath"]), "review audio")
            expected_hash = normalize_text(recording.get("audioSha256"))
            if expected_hash and sha256_file(audio_path) != expected_hash:
                raise SpeakerReviewError(f"review audio hash changed: {audio_path}")
            pcm_path = work_dir / f"{recording_id}.pcm"
            _duration, sample_rate = decode_to_pcm(audio_path, pcm_path, decoder)
            samples = np.memmap(pcm_path, dtype="<i2", mode="r")
            ordered = sorted(
                items,
                key=lambda item: (
                    float(item["end"]) - float(item["start"]),
                    item["id"],
                ),
            )
            for batch in chunks(ordered, args.batch_size):
                signals = [
                    segment_signal(
                        np,
                        samples,
                        start=float(item["start"]),
                        end=float(item["end"]),
                        sample_rate=sample_rate,
                        context_seconds=args.context_seconds,
                        maximum_seconds=args.maximum_duration_seconds,
                    )
                    for item in batch
                ]
                rows = encode_signals(np, torch, classifier, signals, args.device)
                cached.update(
                    {item["id"]: rows[index] for index, item in enumerate(batch)}
                )
                batch_counter += 1
                tracker.advance(len(batch))
                tracker.print()
                if batch_counter % args.checkpoint_batches == 0:
                    write_cache(np, output_path, plan, cached, metadata, complete=False)
            del samples
            pcm_path.unlink(missing_ok=True)
    write_cache(np, output_path, plan, cached, metadata, complete=True)
    print(f"Wrote {output_path} ({len(cached)} vectors)")
    return 0


def embed_reference_bank(args: argparse.Namespace) -> int:
    manifest_path = resolve_input(args.manifest, "reference-bank manifest")
    manifest = load_json_object(manifest_path, "reference-bank manifest")
    plan = build_reference_plan(manifest)
    metadata = base_metadata(
        source_type="reference-bank",
        source_path=manifest_path,
        source_sha256=sha256_file(manifest_path),
        model_name=args.model_name,
        model_source=args.model_source,
        planned_count=len(plan),
    )
    output_path, cached = prepare_output(args, metadata, [item["id"] for item in plan])
    pending = [item for item in plan if item["id"] not in cached]
    if not pending:
        print(f"Embedding cache is complete: {output_path} ({len(cached)} vectors)")
        return 0

    np, torch, classifier = load_model(args)
    decoder = resolve_pcm_decoder(explicit_ffmpeg=args.ffmpeg)
    tracker = ProgressTracker(total=len(plan), completed=len(cached))
    batch_counter = 0
    with tempfile.TemporaryDirectory(prefix="reference-embeddings-") as raw_dir:
        work_dir = Path(raw_dir)
        for batch_number, batch in enumerate(chunks(pending, args.batch_size), start=1):
            signals = []
            for item_index, item in enumerate(batch, start=1):
                clip_path = resolve_input(Path(item["audioPath"]), "reference clip")
                if sha256_file(clip_path) != item["id"]:
                    raise SpeakerReviewError(f"reference clip hash changed: {clip_path}")
                pcm_path = work_dir / f"b{batch_number:04d}-{item_index:03d}.pcm"
                _duration, sample_rate = decode_to_pcm(clip_path, pcm_path, decoder)
                samples = np.fromfile(pcm_path, dtype="<i2")
                signals.append(
                    segment_signal(
                        np,
                        samples,
                        start=0.0,
                        end=len(samples) / sample_rate,
                        sample_rate=sample_rate,
                        context_seconds=0.0,
                        maximum_seconds=DEFAULT_MAXIMUM_SECONDS,
                    )
                )
                pcm_path.unlink(missing_ok=True)
            rows = encode_signals(np, torch, classifier, signals, args.device)
            cached.update(
                {item["id"]: rows[index] for index, item in enumerate(batch)}
            )
            batch_counter += 1
            tracker.advance(len(batch))
            tracker.print()
            if batch_counter % args.checkpoint_batches == 0:
                write_cache(np, output_path, plan, cached, metadata, complete=False)
    write_cache(np, output_path, plan, cached, metadata, complete=True)
    print(f"Wrote {output_path} ({len(cached)} vectors)")
    return 0


def build_review_plan(
    utterances: Sequence[dict[str, Any]],
    *,
    minimum_duration_seconds: float,
    minimum_word_count: int,
) -> list[dict[str, Any]]:
    plan = []
    seen = set()
    for utterance in utterances:
        utterance_id = normalize_text(utterance.get("id"))
        recording_id = normalize_text(utterance.get("recordingId"))
        duration = float(utterance.get("durationSeconds", 0.0))
        word_count = int(utterance.get("wordCount", 0))
        if duration < minimum_duration_seconds or word_count < minimum_word_count:
            continue
        if not utterance_id or not recording_id or utterance_id in seen:
            raise SpeakerReviewError("durable review utterances require unique ids")
        seen.add(utterance_id)
        plan.append(
            {
                "id": utterance_id,
                "recordingId": recording_id,
                "start": float(utterance["start"]),
                "end": float(utterance["end"]),
            }
        )
    return plan


def build_reference_plan(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    if manifest.get("schemaVersion") != 1 or not isinstance(manifest.get("clips"), list):
        raise SpeakerReviewError("reference-bank manifest has an unsupported schema")
    plan = []
    seen = set()
    for clip in manifest["clips"]:
        clip_hash = normalize_text(clip.get("clipSha256"))
        clip_path = normalize_text(clip.get("clipPath"))
        if not clip_hash or not clip_path:
            raise SpeakerReviewError("reference-bank clip requires path and SHA-256")
        if clip_hash in seen:
            raise SpeakerReviewError("reference-bank manifest contains duplicate clips")
        seen.add(clip_hash)
        plan.append({"id": clip_hash, "audioPath": clip_path})
    if not plan:
        raise SpeakerReviewError("reference-bank manifest contains no clips")
    return plan


def base_metadata(
    *,
    source_type: str,
    source_path: Path,
    source_sha256: str,
    model_name: str,
    model_source: str,
    planned_count: int,
) -> dict[str, Any]:
    source_value = Path(model_source).expanduser()
    resolved_source = str(source_value.resolve()) if source_value.exists() else model_source
    return {
        "schemaVersion": SCHEMA_VERSION,
        "sourceType": source_type,
        "sourcePath": str(source_path),
        "sourceSha256": source_sha256,
        "modelName": model_name,
        "modelSource": resolved_source,
        "plannedCount": planned_count,
        "createdAt": utc_now(),
    }


def prepare_output(
    args: argparse.Namespace,
    metadata: dict[str, Any],
    planned_ids: list[str],
) -> tuple[Path, dict[str, Any]]:
    output_path = resolve_transcription_output(
        args.output,
        error_type=SpeakerReviewError,
        label="speaker-embedding cache",
    )
    if output_path.suffix.lower() != ".npz":
        raise SpeakerReviewError("speaker embedding output must use the .npz suffix")
    if args.force or not output_path.exists():
        return output_path, {}
    np = load_numpy_for_cache()
    cached, existing_metadata = load_cache_with_metadata(np, output_path)
    compatibility_keys = (
        "schemaVersion",
        "sourceType",
        "sourceSha256",
        "modelName",
        "modelSource",
        "selection",
    )
    if any(existing_metadata.get(key) != metadata.get(key) for key in compatibility_keys):
        raise SpeakerReviewError(
            f"existing embedding cache is incompatible; inspect it or add --force: {output_path}"
        )
    unexpected = sorted(set(cached) - set(planned_ids))
    if unexpected:
        raise SpeakerReviewError(
            "existing embedding cache contains ids outside the current source"
        )
    metadata["createdAt"] = existing_metadata.get("createdAt", metadata["createdAt"])
    print(f"Resuming {output_path}: {len(cached)}/{len(planned_ids)} vectors present")
    return output_path, cached


def load_model(args: argparse.Namespace) -> tuple[Any, Any, Any]:
    try:
        import numpy as np
        import torch
        from speechbrain.inference.speaker import EncoderClassifier
    except ImportError as exc:
        raise SpeakerReviewError(
            "speaker embeddings require NumPy, Torch, and SpeechBrain in this Python "
            "environment; install them only after user authorization"
        ) from exc

    raw_source = str(args.model_source)
    local_source = Path(raw_source).expanduser()
    if local_source.exists():
        source = str(local_source.resolve())
        savedir = (
            str(args.model_cache.expanduser().resolve())
            if args.model_cache
            else source
        )
    else:
        if not args.allow_model_download:
            raise SpeakerReviewError(
                "model source is not a local path; pass a local --model-source, or obtain "
                "authorization and add --allow-model-download with --model-cache"
            )
        if args.model_cache is None:
            raise SpeakerReviewError("a remote model source requires --model-cache")
        savedir_path = args.model_cache.expanduser().resolve()
        savedir_path.mkdir(parents=True, exist_ok=True)
        source = raw_source
        savedir = str(savedir_path)
    if args.device == "cpu":
        torch.set_num_threads(args.threads)
    try:
        classifier = EncoderClassifier.from_hparams(
            source=source,
            savedir=savedir,
            run_opts={"device": args.device},
        )
        classifier.eval()
    except Exception as exc:
        raise SpeakerReviewError(f"could not load speaker model: {exc}") from exc
    return np, torch, classifier


def segment_signal(
    np: Any,
    samples: Any,
    *,
    start: float,
    end: float,
    sample_rate: int,
    context_seconds: float,
    maximum_seconds: float,
) -> Any:
    start_seconds = max(0.0, start - context_seconds)
    end_seconds = min(end + context_seconds, start_seconds + maximum_seconds)
    start_index = max(0, int(round(start_seconds * sample_rate)))
    end_index = min(len(samples), int(round(end_seconds * sample_rate)))
    if end_index <= start_index:
        raise SpeakerReviewError("speaker utterance produced an empty audio segment")
    return np.asarray(samples[start_index:end_index], dtype=np.float32) / 32768.0


def encode_signals(
    np: Any, torch: Any, classifier: Any, signals: list[Any], device: str
) -> Any:
    if not signals:
        raise SpeakerReviewError("cannot embed an empty audio batch")
    maximum_length = max(len(item) for item in signals)
    waveforms = torch.zeros((len(signals), maximum_length), dtype=torch.float32)
    lengths = torch.zeros(len(signals), dtype=torch.float32)
    for index, signal in enumerate(signals):
        waveforms[index, : len(signal)] = torch.from_numpy(signal.copy())
        lengths[index] = len(signal) / maximum_length
    try:
        with torch.no_grad():
            encoded = classifier.encode_batch(
                waveforms.to(device), lengths.to(device), normalize=True
            )
        matrix = encoded.detach().cpu().numpy().reshape(len(signals), -1)
    except Exception as exc:
        raise SpeakerReviewError(f"speaker model failed to encode a batch: {exc}") from exc
    matrix = np.asarray(matrix, dtype=np.float64)
    norms = np.linalg.norm(matrix, axis=1, keepdims=True)
    if np.any(norms <= 1e-12):
        raise SpeakerReviewError("speaker model produced a zero embedding")
    return (matrix / norms).astype(np.float32)


def chunks(items: Sequence[Any], size: int) -> Iterable[list[Any]]:
    for offset in range(0, len(items), size):
        yield list(items[offset : offset + size])


def load_numpy_for_cache() -> Any:
    try:
        import numpy as np
    except ImportError as exc:
        raise SpeakerReviewError(
            "speaker embedding caches require NumPy in this Python environment"
        ) from exc
    return np


def load_cache_with_metadata(
    np: Any, path: Path
) -> tuple[dict[str, Any], dict[str, Any]]:
    try:
        with np.load(path, allow_pickle=False) as payload:
            if not {"ids", "embeddings", "metadata_json"}.issubset(payload.files):
                raise SpeakerReviewError(
                    "resumable speaker cache requires ids, embeddings, and metadata_json"
                )
            ids = [str(item) for item in payload["ids"]]
            matrix = np.asarray(payload["embeddings"], dtype=np.float32)
            metadata = json.loads(str(payload["metadata_json"].item()))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SpeakerReviewError(f"could not resume embedding cache {path}: {exc}") from exc
    if matrix.ndim != 2 or len(ids) != matrix.shape[0] or len(ids) != len(set(ids)):
        raise SpeakerReviewError("resumable speaker cache has inconsistent dimensions")
    return {item: matrix[index] for index, item in enumerate(ids)}, metadata


def write_cache(
    np: Any,
    output_path: Path,
    plan: Sequence[dict[str, Any]],
    cached: dict[str, Any],
    metadata: dict[str, Any],
    *,
    complete: bool,
) -> None:
    ordered_ids = [item["id"] for item in plan if item["id"] in cached]
    if not ordered_ids:
        return
    matrix = np.vstack([cached[item] for item in ordered_ids]).astype(np.float32)
    payload_metadata = dict(metadata)
    payload_metadata.update(
        {
            "completedCount": len(ordered_ids),
            "complete": bool(complete and len(ordered_ids) == len(plan)),
            "updatedAt": utc_now(),
        }
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="wb", prefix=f".{output_path.name}.", dir=output_path.parent, delete=False
    ) as handle:
        temporary_path = Path(handle.name)
        np.savez_compressed(
            handle,
            ids=np.asarray(ordered_ids),
            embeddings=matrix,
            metadata_json=np.asarray(
                json.dumps(payload_metadata, sort_keys=True, separators=(",", ":"))
            ),
        )
        handle.flush()
        os.fsync(handle.fileno())
    temporary_path.replace(output_path)


class ProgressTracker:
    def __init__(self, *, total: int, completed: int) -> None:
        self.total = total
        self.completed = completed
        self.started = time.monotonic()
        self.start_completed = completed

    def advance(self, count: int) -> None:
        self.completed += count

    def print(self) -> None:
        elapsed = max(time.monotonic() - self.started, 1e-6)
        new_count = self.completed - self.start_completed
        rate = new_count / elapsed
        remaining = max(0, self.total - self.completed)
        eta = remaining / rate if rate > 0 else 0.0
        print(
            f"embedded {self.completed}/{self.total} | {rate:.2f} clips/s | "
            f"ETA {format_duration(eta)}",
            flush=True,
        )


def format_duration(seconds: float) -> str:
    rounded = max(0, int(round(seconds)))
    hours, remainder = divmod(rounded, 3600)
    minutes, whole_seconds = divmod(remainder, 60)
    if hours:
        return f"{hours:d}h {minutes:02d}m"
    if minutes:
        return f"{minutes:d}m {whole_seconds:02d}s"
    return f"{whole_seconds:d}s"


if __name__ == "__main__":
    raise SystemExit(main())
