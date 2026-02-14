"""Генерация задачи."""

from typing import Literal

from tasks.providers import eng_lang, math


def gen_task(subject: str, cl: Literal[*range(1, 12)] | None = None) -> dict:
    """Генерация задачи по предмету и классу."""
    if subject == "math":
        return math.task()

    if subject == "eng_lang":
        return eng_lang.task()
    return None
