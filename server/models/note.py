from datetime import datetime

from pydantic import BaseModel, Field


class NoteCreate(BaseModel):
	title: str = Field(default="제목 없음", max_length=200)
	content: str = ""


class NoteUpdate(NoteCreate):
	pass


class Note(NoteCreate):
	id: str
	created_at: datetime
	updated_at: datetime
