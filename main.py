"""
Точка входу для запуску персонального асистента.
"""

from assistant import PersonalAssistant


def main():
    assistant = PersonalAssistant()
    assistant.run()


if __name__ == "__main__":
    main()


