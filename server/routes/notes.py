from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from server.models.note import NoteCreate, NoteUpdate
from server.services import note_service

router = APIRouter()

@router.get("/notes")
async def list_notes():
    notes = note_service.list_notes()
    return JSONResponse(content=notes)

@router.get("/notes/{note_id}")
async def get_note(note_id: str) -> JSONResponse:
    try:
        note = note_service.get_note(note_id)
        return JSONResponse(content=note)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Note not found")

@router.post("/notes")
async def create_note(note: NoteCreate) -> JSONResponse:
    created_note = note_service.create_note(note)
    return JSONResponse(content=created_note, status_code=201)

@router.put("/notes/{note_id}")
async def update_note(note_id: str, note: NoteUpdate) -> JSONResponse:
    try:
        updated_note = note_service.update_note(note_id, note)
        return JSONResponse(content=updated_note)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Note not found")

@router.delete("/notes/{note_id}")
async def delete_note(note_id: str) -> JSONResponse:
    try:
        note_service.delete_note(note_id)
        return JSONResponse(content=({"message": "Note deleted successfully"}))
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Note not Found")

@router.get("/health")
async def health_check() -> JSONResponse:
    return JSONResponse(content={"status": "ok"})