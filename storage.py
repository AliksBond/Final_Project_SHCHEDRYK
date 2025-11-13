import json
from contacts import Contact
from notes import Note
import os

class Storage:
    CONTACTS_FILE = "contacts.json"
    NOTES_FILE = "notes.json"

    def load_contacts(self):
        if not os.path.exists(self.CONTACTS_FILE):
            return []
        with open(self.CONTACTS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Contact(d['name'], d['phone']) for d in data]

    def save_contacts(self, contacts):
        data = [{"name": c.name, "phone": c.phone} for c in contacts]
        with open(self.CONTACTS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def load_notes(self):
        if not os.path.exists(self.NOTES_FILE):
            return []
        with open(self.NOTES_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Note(d['title'], d['content']) for d in data]

    def save_notes(self, notes):
        data = [{"title": n.title, "content": n.content} for n in notes]
        with open(self.NOTES_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

