from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Process(Base):
    __tablename__ = "processes"

    id = Column(Integer, primary_key=True, index=True)
    exercise_id = Column(Integer, ForeignKey("exercises.id"), nullable=False)
    pid = Column(String, nullable=False)
    arrival_time = Column(Integer, nullable=False)
    burst_time = Column(Integer, nullable=False)
    priority = Column(Integer, nullable=True)
