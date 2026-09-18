from datetime import datetime, timezone
from uuid import uuid4

from server.models.note import NoteCreate, NoteUpdate
from server.storage import file_storage


def list_notes() -> list[dict]:
	return sorted(
		file_storage.load_all(),
		key=lambda note: note["updated_at"],
		reverse=True,
	)


def get_note(note_id: str) -> dict:
	return file_storage.load(note_id)


def create_note(note: NoteCreate) -> dict:
	now = datetime.now(timezone.utc).isoformat()
	data = {
		"id": str(uuid4()),
		"title": note.title.strip() or "제목 없음",
		"content": note.content,
		"created_at": now,
		"updated_at": now,
	}
	return file_storage.save(data["id"], data)


def update_note(note_id: str, note: NoteUpdate) -> dict:
	data = file_storage.load(note_id)
	data.update(
		{
			"title": note.title.strip() or "제목 없음",
			"content": note.content,
			"updated_at": datetime.now(timezone.utc).isoformat(),
		}
	)
	return file_storage.save(note_id, data)


def delete_note(note_id: str) -> None:
	file_storage.delete(note_id)
