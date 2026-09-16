import json
from pathlib import Path

DATA_DIR = Path("data/notes")

def save(note_id, data):
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    path = DATA_DIR / f"{note_id}.json"

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load(note_id):
    path = DATA_DIR / f"{note_id}.json"

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

