"""Поставщик заданий по премету: математика."""

import random

from tasks.exceptions import ClassNotSupportedError
from tasks.models import Task


def _plus_or_minus(min_: int, max_: int) -> tuple[str, str]:
    """Случайная задача на сложение/вычитание чисел (в заданном диапазное)."""
    op = random.choice(("+", "-"))
    nums = random.choices(range(min_, max_ + 1), k=2)

    expression = f"{max(nums)} {op} {min(nums)}"
    answer = str(eval(expression))

    answer_options = [str(random.randint(0, max_ * 2)) for _ in range(3)]
    answer_options.append(answer)

    return Task(
        text=f"Решите пример:\n\n{expression} =",
        answer=answer,
        answer_options=tuple(set(answer_options)),
    )


def _multiply(min_: int, max_: int) -> tuple[str, str]:
    """Случайная задача на умножение (в заданном диапозоне)."""
    nums = random.choices(range(min_, max_ + 1), k=2)

    expression = f"{max(nums)} * {min(nums)}"
    answer = str(eval(expression))

    answer_options = [str(random.randint(min_ * min_, max_ * max_)) for _ in range(3)]
    answer_options.append(answer)

    return Task(
        text=f"Решите пример:\n\n{expression} =",
        answer=answer,
        answer_options=tuple(set(answer_options)),
    )


# TODO(@iamlostshe): Действия со скобками (parenthesis) (2 класс)
# TODO(@iamlostshe): Уравнения (1 класс)


def task() -> None:
    """Получить задание по математике."""
    # if cl == 1:
    # return random.choice(_plus_or_minus(0, 20))

    # if cl == 2:
    return random.choice((_plus_or_minus(0, 100), _multiply(0, 10)))

    raise ClassNotSupportedError
