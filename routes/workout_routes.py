from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from utils.database import SessionLocal
from schemas.workout_schema import WorkoutCreate

from services.workout_service import (
    create_workout,
    get_workouts,
    update_workout,
    delete_workout
)
from auth.auth_dependency import get_current_user

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/add-workout")
def add_workout(
    workout: WorkoutCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return create_workout(db, workout)
@router.get("/workouts")
def read_workouts(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return get_workouts(db)
@router.put("/workouts/{workout_id}")
def edit_workout(
    workout_id: int,
    workout: WorkoutCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return update_workout(
        db,
        workout_id,
        workout
    )
@router.delete("/workouts/{workout_id}")
def remove_workout(
    workout_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return delete_workout(
        db,
        workout_id
    )