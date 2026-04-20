from pydantic import BaseModel

class ExerciseCheckRequest(BaseModel):
    exercise_id: int
    user_answer: float
