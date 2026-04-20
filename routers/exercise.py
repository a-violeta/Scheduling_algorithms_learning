from fastapi import APIRouter
from database import SessionLocal
from models.db_exercise import Exercise
from models.db_process import Process
from models.exercise_check import ExerciseCheckRequest
import random

router = APIRouter()

@router.get("/exercise/{exercise_id}")
def get_exercise(exercise_id: int):
    db = SessionLocal()

    ex = db.query(Exercise).filter(Exercise.id == exercise_id).first()
    if not ex:
        return {"error": "Exercise not found"}

    processes = db.query(Process).filter(Process.exercise_id == ex.id).all()

    process_list = [
        {
            "pid": p.pid,
            "arrival_time": p.arrival_time,
            "burst_time": p.burst_time,
            "priority": p.priority
        }
        for p in processes
    ]

    # TODO: aici generăm și Gantt-ul
    # gantt = generate_gantt(ex.algorithm, process_list, ex.quantum)

    return {
        "id": ex.id,
        "title": ex.title,
        "description": ex.description,
        "algorithm": ex.algorithm,
        "quantum": ex.quantum,
        "expected_avg_waiting": ex.expected_avg_waiting,
        "processes": process_list,
        # "gantt": gantt
    }

from typing import cast

@router.post("/exercise/check")
def check_exercise_answer(data: ExerciseCheckRequest):
    db = SessionLocal()
    ex = db.query(Exercise).filter(Exercise.id == data.exercise_id).first()

    if ex is None or ex.expected_avg_waiting is None:
        return {"error": "Exercise not found or invalid"}

    expected = cast(float, ex.expected_avg_waiting)
    correct = abs(expected - data.user_answer) < 0.001

    return {"correct": correct}
