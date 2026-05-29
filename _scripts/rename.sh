#!/usr/bin/env bash
set -euo pipefail

find _sessions -type f -name '*.md' -print0 |
while IFS= read -r -d '' file; do
  case "$file" in
    */sources/*) ;;
    *) continue ;;
  esac

  dir=${file%/*}
  base=${file##*/}
  stem=${base%.md}

  case "$stem" in
    *" - Original") 
      echo "SKIP already renamed: $file"
      continue
      ;;
  esac

  target="$dir/$stem - Original.md"

  if [[ -e "$target" ]]; then
    echo "SKIP target exists: $target"
    continue
  fi

  mv -- "$file" "$target"
  echo "RENAMED: $file -> $target"
done