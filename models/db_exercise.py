from sqlalchemy import Column, Integer, String, Text, Float
from database import Base

class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    algorithm = Column(String, nullable=False)
    quantum = Column(Integer, nullable=True)
    description = Column(Text, nullable=True)
    expected_avg_waiting = Column(Float, nullable=True)
