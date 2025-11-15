from collections import UserDict
from datetime import datetime, timedelta, date
import re



class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty")
        super().__init__(value)


class Address(Field):
    pass


class Phone(Field):
    @staticmethod
    def validate(phone: str) -> bool:
        return phone.isdigit() and len(phone) == 10

    def __init__(self, value):
        if not self.validate(value):
            raise ValueError("Phone must contain exactly 10 digits.")
        super().__init__(value)


class Email(Field):
    EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    @staticmethod
    def validate(email: str) -> bool:
        return bool(re.match(Email.EMAIL_REGEX, email))

    def __init__(self, value):
        if not self.validate(value):
            raise ValueError("Incorrect email format.")
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value: str):
        try:
            parsed = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Birthday must be in format DD.MM.YYYY")
        super().__init__(parsed)



class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.email: Email | None = None
        self.address: Address | None = None
        self.birthday: Birthday | None = None

    def add_phone(self, phone: str):
        if any(p.value == phone for p in self.phones):
            raise ValueError("This phone number already exists.")
        self.phones.append(Phone(phone))

    def set_email(self, email: str):
        self.email = Email(email)

    def set_address(self, address: str):
        self.address = Address(address)

    def set_birthday(self, birthday: str):
        self.birthday = Birthday(birthday)

    def edit_phone(self, old: str, new: str):
        for p in self.phones:
            if p.value == old:
                if not Phone.validate(new):
                    raise ValueError("Phone must contain exactly 10 digits.")
                p.value = new
                return
        raise ValueError("Old phone not found.")

    def delete_phone(self, phone: str):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return
        raise ValueError("Phone not found.")

    def find_phone(self, phone: str):
        return next((p for p in self.phones if p.value == phone), None)

    def __str__(self):
        phones = ", ".join(p.value for p in self.phones) if self.phones else "—"
        email = self.email.value if self.email else "—"
        address = self.address.value if self.address else "—"
        birthday = self.birthday.value.strftime("%d.%m.%Y") if self.birthday else "—"

        return (f"Name: {self.name.value}\n"
                f"Phones: {phones}\n"
                f"Email: {email}\n"
                f"Address: {address}\n"
                f"Birthday: {birthday}")



class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str):
        return self.data.get(name)

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError(f"Record '{name}' not found.")

    def birthdays_in_days(self, days: int):
        today = date.today()
        target_date = today + timedelta(days=days)

        result = []

        for record in self.data.values():
            if record.birthday:
                bday = record.birthday.value

                # Handle birthdays like 29.02 safely
                try:
                    next_bday = bday.replace(year=today.year)
                except ValueError:
                    # For Feb 29 in a non-leap year → shift to Mar 1
                    next_bday = date(today.year, 3, 1)

                if next_bday < today:
                    try:
                        next_bday = bday.replace(year=today.year + 1)
                    except ValueError:
                        next_bday = date(today.year + 1, 3, 1)

                if next_bday == target_date:
                    result.append({
                        "name": record.name.value,
                        "birthday": next_bday.strftime("%d.%m.%Y")
                    })

        return result



class Note:
    def __init__(self, text: str, tags=None):
        self.text = text
        self.tags = tags or []
        self.id: int | None = None

    def edit(self, new_text=None, new_tags=None):
        if new_text:
            self.text = new_text
        if new_tags is not None:
            self.tags = new_tags

    def __str__(self):
        tags_str = ", ".join(self.tags) if self.tags else "—"
        return f"[{self.id}] {self.text} (tags: {tags_str})"


class NotesBook(UserDict):
    def __init__(self):
        super().__init__()
        self.counter = 1

    def add_note(self, text: str, tags=None):
        note = Note(text, tags)
        note.id = self.counter
        self.data[self.counter] = note
        self.counter += 1
        return note

    def delete_note(self, note_id: int):
        if note_id in self.data:
            del self.data[note_id]
        else:
            raise KeyError("Note not found")

    def find_by_tag(self, tag: str):
        return [note for note in self.data.values() if tag in note.tags]

    def find_by_keywords(self, keyword: str):
        keyword = keyword.lower()
        return [note for note in self.data.values() if keyword in note.text.lower()]

    def sort_by_tags(self):
        return sorted(self.data.values(), key=lambda note: (note.tags[0] if note.tags else ""))



if __name__ == "__main__":

    book = AddressBook()

    r = Record("John Doe")
    r.add_phone("0501234567")
    r.set_email("john@example.com")
    r.set_address("Kyiv, Main Street 12")
    r.set_birthday("12.10.1992")

    book.add_record(r)

    print("=== AddressBook Demo ===")
    print(book.find("John Doe"))
    print()

    notes = NotesBook()

    notes.add_note("Buy milk", tags=["shopping"])
    notes.add_note("Plan vacation", tags=["travel", "summer"])
    notes.add_note("Learn Python", tags=["study"])

    print("=== NotesBook Demo ===")
    print("All notes:")
    for note in notes.data.values():
        print(note)

    print("\nFind by tag 'shopping':")
    for note in notes.find_by_tag("shopping"):
        print(note)

    print("\nNotes containing 'python':")
    for note in notes.find_by_keywords("python"):
        print(note)

