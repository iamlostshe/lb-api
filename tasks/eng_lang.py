"""Поставщик заданий по премету: английский язык."""

import json
import random
from pathlib import Path

from tasks.exceptions import ClassNotSupported

_WORD_DICT_PATH = Path("assets") / "eng_lang" / "dict.json"


def _prepare_dict(file_path: Path) -> dict[str, str]:
    with file_path.open(encoding="utf-8") as f:
        return json.loads(f)


_WORD_DICT = _prepare_dict(_WORD_DICT_PATH)


def task(cls: int) -> tuple[str, str]:
    """Получить задание по английскому языку."""
    if cls in (2, 3, 4):
        return random.choice(_WORD_DICT.items())

    raise ClassNotSupported
