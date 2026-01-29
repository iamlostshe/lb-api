"""Модуль БД."""

import json
from pathlib import Path

_DB_NAME = Path("index.json")


def connect() -> None:
    """Проверка существования БД."""
    if not _DB_NAME.exists():
        with _DB_NAME.open("w") as f:
            f.write("[]")


def add(time: int) -> None:
    """Добавляем рекорд пользователя в таблицу лидеров."""
    with _DB_NAME.open("r+") as f:
        data = json.load(f)
        data.append(time)
        f.seek(0)
        json.dump(data, f)


def res() -> list[int]:
    """Возвращаем топ-10 лидеров."""
    with _DB_NAME.open() as f:
        return sorted(json.load(f))[:10]
