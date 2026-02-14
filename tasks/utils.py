"""Утилиты используемые при генерации задач."""

import random

ALLOWED_SUBJECTS = ("math", "eng_lang")


def random_subject() -> str:
    """Возвращает случайный доступный предмет."""
    return random.choice(ALLOWED_SUBJECTS)
