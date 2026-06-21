from pydantic import BaseModel


class WorkoutCreate(BaseModel):
    member_name: str
    exercise_name: str
    sets: int
    repetitions: int
    duration: int
    trainer_notes: str


class WorkoutResponse(WorkoutCreate):
    id: int

    class Config:
        from_attributes = True