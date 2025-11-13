"""
Модуль contacts.py містить клас Contact та функцію для перевірки номера телефону.
"""

def is_valid_phone(phone):
    """
    Перевіряє, чи є номер телефону дійсним.

    Параметри:
    phone (str): рядок, що представляє номер телефону

    Повертає:
    bool: True, якщо номер містить лише цифри та довжина >= 7
    """
    return phone.isdigit() and len(phone) >= 7


class Contact:
    """
    Клас Contact представляє контакт користувача з ім'ям та номером телефону.
    """
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.name} - {self.phone}"

