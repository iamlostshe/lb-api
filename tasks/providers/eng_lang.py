"""Поставщик заданий по премету: английский язык."""

import json
import random
from pathlib import Path

from tasks.exceptions import ClassNotSupportedError
from tasks.models import Task

_WORD_DICT_PATH = Path("assets") / "eng_lang" / "dict.json"


def _prepare_dict(file_path: Path) -> dict[str, str]:
    with file_path.open(encoding="utf-8") as f:
        return json.load(f)


WORD_DICT = _prepare_dict(_WORD_DICT_PATH)

WORD_DICT_ITEMS = tuple(WORD_DICT.items())
WORD_DICT_VALUES = tuple(WORD_DICT.values())
WORD_DICT_KEYS = tuple(WORD_DICT.keys())


def task() -> tuple[str]:
    """Получить задание по английскому языку."""
    # if cl in (2, 3, 4):
    words = random.choice(WORD_DICT_ITEMS)

    if random.randint(0, 1):
        text = f'Переведите "{words[0]}" на английский язык.'
        answer = words[1]

        answer_options = [random.choice(WORD_DICT_VALUES) for _ in range(3)]

    else:
        text = f'Переведите "{words[1]}" на русский язык.'
        answer = words[0]

        answer_options = [random.choice(WORD_DICT_KEYS) for _ in range(3)]

    answer_options.append(answer)

    return Task(
        text=text,
        answer=answer,
        answer_options=tuple(set(answer_options)),
    )

    raise ClassNotSupportedError
