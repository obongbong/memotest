import json
from pathlib import Path
from typing import Any

DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "notes"


def save(note_id: str, data: dict[str, Any]) -> dict[str, Any]:
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    path = DATA_DIR / f"{note_id}.json"

    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
    return data


def load(note_id: str) -> dict[str, Any]:
    path = DATA_DIR / f"{note_id}.json"

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_all() -> list[dict[str, Any]]:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    notes = []
    for path in DATA_DIR.glob("*.json"):
        with path.open("r", encoding="utf-8") as file:
            notes.append(json.load(file))
    return notes


def delete(note_id: str) -> None:
    path = DATA_DIR / f"{note_id}.json"
    path.unlink()

