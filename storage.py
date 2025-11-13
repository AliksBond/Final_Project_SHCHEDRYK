"""
Модуль storage.py відповідає за збереження та завантаження контактів і нотаток у JSON-файли.
"""

import json
import os
from contacts import Contact
from notes import Note


class Storage:
    """
    Клас Storage реалізує збереження та завантаження контактів і нотаток.
    Використовуються два файли: contacts.json та notes.json
    """
    CONTACTS_FILE = "contacts.json"
    NOTES_FILE = "notes.json"

    def load_contacts(self):
        if not os.path.exists(self.CONTACTS_FILE):
            return []
        try:
            with open(self.CONTACTS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Contact(d['name'], d['phone']) for d in data]
        except json.JSONDecodeError:
            print("Помилка при завантаженні контактів. Використовується порожній список.")
            return []

    def save_contacts(self, contacts):
        data = [{"name": c.name, "phone": c.phone} for c in contacts]
        with open(self.CONTACTS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def load_notes(self):
        if not os.path.exists(self.NOTES_FILE):
            return []
        try:
            with open(self.NOTES_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Note(d['title'], d['content'], d.get('tags', [])) for d in data]
        except json.JSONDecodeError:
            print("Помилка при завантаженні нотаток. Використовується порожній список.")
            return []

    def save_notes(self, notes):
        data = [{"title": n.title, "content": n.content, "tags": n.tags} for n in notes]
        with open(self.NOTES_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)


