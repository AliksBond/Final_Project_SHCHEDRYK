"""
Модуль notes.py містить клас Note для представлення нотаток користувача.
"""

class Note:
    """
    Клас Note представляє нотатку з заголовком, текстом та тегами.
    """
    def __init__(self, title, content, tags=None):
        self.title = title
        self.content = content
        self.tags = tags or []

    def __str__(self):
        tags_str = ", ".join(self.tags) if self.tags else "Без тегів"
        return f"{self.title}: {self.content} [Теги: {tags_str}]"

