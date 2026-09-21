# Regression tests and vault diagnostics

Any working vault note, template, campaign registry, or generated index can be
edited, rewritten, renamed, or deleted. Those changes must not change whether
the code's regression tests pass. Tests may read implementation files and
explicit test fixtures; they must never seed a temporary vault from working data.

Use inline synthetic inputs or files under `tests/fixtures` or `tests/data`.
The linter suites share `lint_fixture_vault.rb`, which copies the small
test-owned governance declarations and generates their catalog in each temporary
vault. These declarations are not synchronized with the working `_MoC` notes.
The six-note trial JSON is also an independent fixture, not a live note lookup.
Name Explorer's `test-vault.js` creates its own miniature vault, decision store,
and partial evidence index, including rename, rewrite, and deletion cases.

Run all vault regression tests without copying any working notes, templates,
registries, generated indexes, or skill prose:

```sh
python3 _scripts/tests/run_isolated.py
```

This runner discovers the Python, Ruby, and JavaScript tests in the first-party
code directories and runs them in a temporary code-and-fixture-only tree. It
does not move or hide anything in the working vault. Python needs PyYAML and
Pillow; Ruby and Node.js must be available. Use `--python`, `--ruby`, or `--node`
to select runtimes. The caller's environment is inherited, so Python packages
can also be supplied through `PYTHONPATH`. This is data isolation for regression
testing, not an operating-system sandbox against arbitrary file access.

Test behaviors such as stale indexes, missing inputs, invalid declarations,
and unresolved references by changing fixtures inside the temporary vault.
Do not lock tests to current note counts, campaign lists, prose, model choices,
or template section order. The session-component suite tests generated slot
content; the Dunmar template's layout is freely editable.

## Optional live diagnostics

These existing read-only commands check the current vault. Their results can
legitimately change after an edit, and they are not regression tests:

```sh
ruby _scripts/generate_taelgar_lint_values.rb --check --root .
ruby _scripts/generate_language_pronunciation_analogues.rb --check --root .
ruby _scripts/generate_language_pronunciation_analogues.rb --audit --root .
ruby _scripts/generate_worldbuilding_discussion_index.rb --check --root .
```

Use a diagnostic when its generated data is needed, and review its report in
that context. A stale index is maintenance work, not evidence that a regression
test should enforce the current contents of an editable note.
