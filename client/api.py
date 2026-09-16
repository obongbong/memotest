import requests

BASE_URL = "http://localhost:8000"

def get_notes():
    response = requests.get(f"{BASE_URL}/notes")
    response.raise_for_status()
    return response.json()

def get_notes(note_id):
    response = requests.get(f"{BASE_URL}/notes/{note_id}")
    response.raise_for_status()
    return response.json()

def create_note(title, content):
    response = requests.post(
        f"{BASE_URL}/notes",
        json = {
            "title": title,
            "content": content
        }
    )
    response.raise_for_status()
    return response.json()
