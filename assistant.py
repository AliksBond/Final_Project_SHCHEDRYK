from contacts import Contact
from notes import Note
from storage import Storage

class PersonalAssistant:
    def __init__(self):
        self.storage = Storage()
        self.contacts = self.storage.load_contacts()
        self.notes = self.storage.load_notes()

    def run(self):
        while True:
            print("\n--- Personal Assistant ---")
            print("1. Show contacts")
            print("2. Add contact")
            print("3. Show notes")
            print("4. Add note")
            print("5. Exit")
            choice = input("Select an option: ").strip()

            if choice == "1":
                self.show_contacts()
            elif choice == "2":
                self.add_contact()
            elif choice == "3":
                self.show_notes()
            elif choice == "4":
                self.add_note()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

    def show_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        for i, contact in enumerate(self.contacts, 1):
            print(f"{i}. {contact}")

    def add_contact(self):
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()
        if not name or not phone:
            print("Invalid input. Both name and phone required.")
            return
        contact = Contact(name, phone)
        self.contacts.append(contact)
        self.storage.save_contacts(self.contacts)
        print("Contact added successfully.")

    def show_notes(self):
        if not self.notes:
            print("No notes found.")
            return
        for i, note in enumerate(self.notes, 1):
            print(f"{i}. {note}")

    def add_note(self):
        title = input("Enter note title: ").strip()
        content = input("Enter note content: ").strip()
        if not title or not content:
            print("Invalid input. Both title and content required.")
            return
        note = Note(title, content)
        self.notes.append(note)
        self.storage.save_notes(self.notes)
        print("Note added successfully.")

