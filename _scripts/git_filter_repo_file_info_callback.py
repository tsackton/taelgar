# This file is a git-filter-repo --file-info-callback function body.
# git-filter-repo supplies: filename, mode, blob_id, and value.

if not filename.lower().endswith(b".md"):
    return (filename, mode, blob_id)

contents = value.get_contents_by_identifier(blob_id)
secret_filter_module = value.data.get("taelgar_secret_filter_module")
if secret_filter_module is None:
    import importlib.util
    import os
    import sys

    script_path = os.path.join(os.getcwd(), "_scripts", "secret_filter.py")
    spec = importlib.util.spec_from_file_location("taelgar_secret_filter", script_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load tracked Taelgar secret filter")
    secret_filter_module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = secret_filter_module
    spec.loader.exec_module(secret_filter_module)
    value.data["taelgar_secret_filter_module"] = secret_filter_module

try:
    cleaned = secret_filter_module.clean_history_bytes(contents)
except secret_filter_module.SecretFilterError as exc:
    display_path = filename.decode("utf-8", errors="replace")
    raise RuntimeError("could not clean {}: {}".format(display_path, exc))

if cleaned == contents:
    return (filename, mode, blob_id)
return (filename, mode, value.insert_file_with_contents(cleaned))
