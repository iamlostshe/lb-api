"""lb-api - сервис для учёта лидеров."""

from typing import Literal

from fastapi import FastAPI

import db
from tasks import ALLOWED_SUBJECTS, gen_task, random_subject
from tasks.models import Task

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


@app.get("/task")
def task(
    subject: Literal[*ALLOWED_SUBJECTS] | None = None,
    cl: int | None = None,
) -> Task:
    """Возвращает случайную задачу по предмету и классу."""
    if not subject:
        subject = random_subject()

    return gen_task(subject, cl)
