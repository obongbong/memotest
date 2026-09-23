from fastapi import FastAPI
from server.routes.notes import router as notes_router

app = FastAPI(title="Memo")
