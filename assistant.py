"""
Модуль assistant.py реалізує клас PersonalAssistant для взаємодії з користувачем
через командний рядок.
"""

from contacts import Contact, is_valid_phone
from notes import Note
from storage import Storage


class PersonalAssistant:
    """
    Клас PersonalAssistant управляє контактами та нотатками користувача.
    """
    def __init__(self):
        self.storage = Storage()
        self.contacts = self.storage.load_contacts()
        self.notes = self.storage.load_notes()

    def run(self):
        """
        Основний цикл програми з компактним меню.
        """
        print("\n--- Personal Assistant ---")
        print("Доступні команди:")
        print("show_contacts - Показати контакти")
        print("add_contact - Додати контакт")
        print("show_notes - Показати нотатки")
        print("add_note - Додати нотатку")
        print("search_notes - Пошук нотаток за тегом")
        print("exit - Вихід")

        while True:
            command = input("\nВведіть команду: ").strip().lower()
            if command == "show_contacts":
                self.show_contacts()
            elif command == "add_contact":
                self.add_contact()
            elif command == "show_notes":
                self.show_notes()
            elif command == "add_note":
                self.add_note()
            elif command == "search_notes":
                self.search_notes_by_tag()
            elif command == "exit":
                print("До побачення!")
                break
            else:
                print("Невірна команда. Спробуйте ще раз.")

    def show_contacts(self):
        """Виводить усі контакти користувача."""
        if not self.contacts:
            print("Контакти відсутні.")
            return
        for i, contact in enumerate(self.contacts, 1):
            print(f"{i}. {contact}")

    def add_contact(self):
        """Додає новий контакт після перевірки введених даних."""
        name = input("Введіть ім'я: ").strip()
        phone = input("Введіть номер телефону: ").strip()
        if not name or not phone or not is_valid_phone(phone):
            print("Невірне введення. Ім'я та дійсний номер телефону обов'язкові.")
            return
        contact = Contact(name, phone)
        self.contacts.append(contact)
        self.storage.save_contacts(self.contacts)
        print("Контакт успішно додано.")

    def show_notes(self):
        """Виводить усі нотатки користувача."""
        if not self.notes:
            print("Нотатки відсутні.")
            return
        for i, note in enumerate(self.notes, 1):
            print(f"{i}. {note}")

    def add_note(self):
        """Додає нову нотатку з тегами після перевірки введених даних."""
        title = input("Введіть заголовок нотатки: ").strip()
        content = input("Введіть текст нотатки: ").strip()
        tags_input = input("Введіть теги через кому (необов'язково): ").strip()
        tags = [tag.strip() for tag in tags_input.split(",")] if tags_input else []
        if not title or not content:
            print("Невірне введення. Заголовок та текст обов'язкові.")
            return
        note = Note(title, content, tags)
        self.notes.append(note)
        self.storage.save_notes(self.notes)
        print("Нотатку успішно додано.")

    def search_notes_by_tag(self):
        """Пошук нотаток за тегом."""
        tag = input("Введіть тег для пошуку: ").strip()
        if not tag:
            print("Тег не може бути порожнім.")
            return
        filtered_notes = [note for note in self.notes if tag in note.tags]
        if not filtered_notes:
            print(f"Нотаток з тегом '{tag}' не знайдено.")
            return
        print(f"Нотатки з тегом '{tag}':")
        for i, note in enumerate(filtered_notes, 1):
            print(f"{i}. {note}")


