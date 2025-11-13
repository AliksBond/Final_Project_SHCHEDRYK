class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __repr__(self):
        return f"{self.name} - {self.phone}"

