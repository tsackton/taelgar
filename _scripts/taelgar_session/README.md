# Shared session Python library

This package supplies common mechanics to transcript processing, scene mapping,
and entity mapping. It does not choose entities, divide scenes, or change review
status. Existing skill helpers remain the command-line entry points.

| Module | Responsibility |
| --- | --- |
| `storage` | Bundle-relative safe paths, byte SHA-256, no-follow file creation, atomic writes, and one cross-platform session lock. |
| `units` | Read prepared/cleaned UID lines and validate their timing and uncertainty syntax. |
| `transcript` | Read YAML-registered polished speech; verify byte hashes and complete original UID/offset coverage. |
| `sources` | Load source bundles, group indivisible UIDs/turns, validate evidence ranges, render reading windows/links, and recheck inputs. |
| `validation` | Shared map errors, fields, strings, confidence/status vocabulary, map JSON encoding, and canonical metadata digests. |
| `passages` | Check exact retained wording around marked inline omissions, without judging relevance or completeness. |

## Imports and policy

Repository scripts add the repository's `_scripts` directory to `sys.path`, then
import `taelgar_session`. This works from any working directory and in the
code-and-fixture-only regression tree. PyYAML is the only external dependency.
The package never imports skill scripts.

```python
from taelgar_session import sources

bundle = sources.load(session_yaml, vault_root)
text = sources.window(bundle, start_uid, end_uid)
```

`load` requires known session dates by default. Entity mapping explicitly uses
`allow_unknown_dates=True` and `allow_source_changes=True` to inspect stale inputs;
its guarded confirmation/save workflow still rejects silent source acceptance.
Neither option changes the sources or invents dates. Prepared narrative loading
and its occurrence references remain in the entity helper.

`transcript.load` is the lower-level registered transcript reader.
`sources.load` adds vault context, source fingerprints, whole-UID groups, and
mapping input digests. Reading windows always use polished speech and expand to
complete groups; source bounds
reject endpoints that divide a combined turn or shared UID.

`transcript_core` re-exports shared storage and UID functions for existing
processing/correction callers. `entity_map.scenes` and `entity_review.scenes`
remain compatibility aliases to the shared source API; they do not import the
scene mapper. New consumers should import this package directly.

Storage locks are shared by all consumers, including Windows kernel mutexes;
callers hold the lock while rechecking inputs and writing. Processing transaction
and editorial logic remain in `transcript_core`. Its JSON encoder deliberately
retains its existing sorted/default-string representation; map JSON encoding in
`validation` retains its own existing bytes. Do not unify them casually: hashes
and recovery records depend on those representations.

Run the library regressions without live session data:

```sh
python -B -m unittest discover -s _scripts/taelgar_session/tests
```

Also run the affected skill suites; see [test setup](../tests/README.md).
