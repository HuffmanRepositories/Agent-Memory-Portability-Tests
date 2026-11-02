#!/usr/bin/env python3
"""Validate fixture structure and uniqueness; not semantic conformance."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE_DIR = ROOT / "fixtures" / "cases"
REQUIRED = {"fixture_id", "title", "status", "category", "description", "source_memory", "migration", "expected", "loss_classification", "notes"}
VALID_STATUS = {"draft", "reviewed", "observed", "retired"}
VALID_LOSS = {"preserved", "transformed", "dropped", "unsupported", "ambiguous", "unsafe_widening"}

def validate():
    errors = []
    seen = set()
    files = sorted(FIXTURE_DIR.glob("*.json"))
    if not files:
        errors.append("No fixture JSON files found")
    for path in files:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path.name}: invalid JSON: {exc}")
            continue
        if not isinstance(data, dict):
            errors.append(f"{path.name}: top-level JSON must be an object")
            continue
        missing = REQUIRED - data.keys()
        if missing:
            errors.append(f"{path.name}: missing fields: {', '.join(sorted(missing))}")
        fid = data.get("fixture_id")
        if not isinstance(fid, str) or not fid.strip():
            errors.append(f"{path.name}: fixture_id must be non-empty string")
        elif fid in seen:
            errors.append(f"{path.name}: duplicate fixture_id {fid}")
        else:
            seen.add(fid)
        status = data.get("status")
        if not isinstance(status, str) or status not in VALID_STATUS:
            errors.append(f"{path.name}: invalid status")
        losses = data.get("loss_classification")
        if not isinstance(losses, list) or not losses or any(not isinstance(x, str) or x not in VALID_LOSS for x in losses):
            errors.append(f"{path.name}: invalid loss_classification")
        if not isinstance(data.get("expected"), list) or not data.get("expected"):
            errors.append(f"{path.name}: expected must be non-empty list")
        if not isinstance(data.get("source_memory"), dict):
            errors.append(f"{path.name}: source_memory must be an object")
        if not isinstance(data.get("migration"), dict):
            errors.append(f"{path.name}: migration must be an object")
    return files, errors

def main():
    files, errors = validate()
    if errors:
        print("\n".join("ERROR: " + e for e in errors))
        return 1
    print(f"Validated {len(files)} fixture(s); structural checks only.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
