from sqlalchemy.orm import Session
from models.workout import Workout
from schemas.workout_schema import WorkoutCreate
from utils.logger import logger


def create_workout(db: Session, workout: WorkoutCreate):

    db_workout = Workout(
        member_name=workout.member_name,
        exercise_name=workout.exercise_name,
        sets=workout.sets,
        repetitions=workout.repetitions,
        duration=workout.duration,
        trainer_notes=workout.trainer_notes
    )

    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)

    logger.info(
        f"Workout Added: {workout.exercise_name} for {workout.member_name}"
    )

    return db_workout


def get_workouts(db: Session):
    return db.query(Workout).all()


def update_workout(
    workout_id: int,
    workout: WorkoutCreate,
    db: Session
):

    db_workout = (
        db.query(Workout)
        .filter(Workout.id == workout_id)
        .first()
    )

    if not db_workout:
        return None

    db_workout.member_name = workout.member_name
    db_workout.exercise_name = workout.exercise_name
    db_workout.sets = workout.sets
    db_workout.repetitions = workout.repetitions
    db_workout.duration = workout.duration
    db_workout.trainer_notes = workout.trainer_notes

    db.commit()
    db.refresh(db_workout)

    logger.info(
        f"Workout Updated: ID {workout_id}"
    )

    return db_workout


def delete_workout(
    workout_id: int,
    db: Session
):

    db_workout = (
        db.query(Workout)
        .filter(Workout.id == workout_id)
        .first()
    )

    if not db_workout:
        return None

    db.delete(db_workout)
    db.commit()

    logger.info(
        f"Workout Deleted: ID {workout_id}"
    )

    return {
        "message": "Workout deleted successfully"
    }