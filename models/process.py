from pydantic import BaseModel

class Process(BaseModel):
    pid: str
    arrival_time: int
    burst_time: int
    priority: int | None = None
