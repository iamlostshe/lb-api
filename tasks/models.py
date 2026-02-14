"""Объекты, необходимые для генерации задач."""

from pydantic import BaseModel


class Task(BaseModel):
    """Задача.

    - Текст (условие).
    - Ответ.
    - Варианты ответа.
    """

    text: str
    answer: str
    answer_options: list[str]


# TODO(@iamlostshe): ПО идее он не должен тут быть
class WordDict(BaseModel):
    """Словарь для задач английского языка."""

    items: tuple[tuple[str]]
    keys: tuple[str]
    values: tuple[str]
