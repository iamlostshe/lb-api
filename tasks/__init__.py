"""Модуль генерации заданий."""

from .gen_task import gen_task
from .utils import ALLOWED_SUBJECTS, random_subject

__all__ = ("ALLOWED_SUBJECTS", "gen_task", "random_subject")
