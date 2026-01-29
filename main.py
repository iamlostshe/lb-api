"""lb-api - сервис для учёта лидеров."""

from fastapi import FastAPI

import db

db.connect()
app = FastAPI()


@app.get("/add")
def add(time: int) -> dict[str, str]:
    """Добавляем пользователя в список лидеров."""
    if time < 1:
        return {"err": "Число должно быть натуральным"}

    db.add(time)
    return {"err": "ok"}


@app.get("/res")
def res() -> list[int]:
    """Возвращает топ-10 игроков."""
    return db.res()
