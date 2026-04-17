from fastapi import APIRouter
from database import SessionLocal
from models.db_exercise import Exercise
from models.db_process import Process
import random

router = APIRouter()

@router.get("/exercise/random")
def get_random_exercise():
    db = SessionLocal()

    # luăm toate exercițiile
    exercises = db.query(Exercise).all()
    ex: Exercise = random.choice(exercises)

    # luăm procesele aferente exercițiului
    processes = db.query(Process).filter(Process.exercise_id == ex.id).all()  # type: ignore[attr-defined]

    # convertim procesele în dict-uri JSON-friendly
    process_list = [
        {
            "pid": p.pid,
            "arrival_time": p.arrival_time,
            "burst_time": p.burst_time,
            "priority": p.priority
        }
        for p in processes
    ]

    return {
        "id": ex.id,
        "title": ex.title,
        "description": ex.description,
        "algorithm": ex.algorithm,
        "quantum": ex.quantum,
        "expected_avg_waiting": ex.expected_avg_waiting,
        "processes": process_list
    }

from typing import cast

@router.post("/exercise/check")
def check_exercise_answer(exercise_id: int, user_answer: float):
    db = SessionLocal()
    ex: Exercise | None = db.query(Exercise).filter(Exercise.id == exercise_id).first()

    if ex is None or ex.expected_avg_waiting is None:
        return {"error": "Exercise not found or invalid"}

    expected = cast(float, ex.expected_avg_waiting)
    correct = abs(expected - user_answer) < 0.001

    return {"correct": correct}
