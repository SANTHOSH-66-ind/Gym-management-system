from sqlalchemy import Column, Integer, String
from utils.database import Base


class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True)

    member_name = Column(String)
    exercise_name = Column(String)
    sets = Column(Integer)
    repetitions = Column(Integer)
    duration = Column(Integer)
    trainer_notes = Column(String)