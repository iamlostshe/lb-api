"""Поставщик заданий по премету: математика."""

import random
from ast import literal_eval

from tasks.exceptions import ClassNotSupported


def _plus_or_minus(min_: int, max_: int) -> tuple(str, str):
    """Случайная задача на сложение/вычитание чисел (в заданном диапазное)."""
    op = random.choice(("+", "-"))
    nums = random.choices(range(min_, max_ + 1), k=2)

    expression = f"{max(nums)} {op} {min(nums)}"
    return f"Решите пример:\n\n{expression} =", literal_eval(expression)


def _multiply(min_: int, max_: int) -> tuple(str, str):
    """Случайная задача на умножение (в заданном диапозоне)."""
    nums = random.choices(range(min_, max_ + 1), k=2)

    expression = f"{max(nums)} * {min(nums)}"
    return f"Решите пример:\n\n{expression} =", literal_eval(expression)


# TODO(): def _parenthesis -
#    """Случайная задача на действия со скобками."""
# это второй класс


def task(cls: int) -> None:
    """Получить задание по математике."""
    if cls == 1:
        return random.choice(_plus_or_minus(0, 20), _multiply(0, 10))

    if cls == 2:
        return random.choice(_plus_or_minus(0, 100))

    raise ClassNotSupported
