from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from utils.database import SessionLocal
from schemas.attendance_schema import AttendanceCreate
from services.attendance_service import (
    create_attendance,
    get_attendance
)
from auth.auth_dependency import get_current_user
router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/add-attendance")
def add_attendance(
    attendance: AttendanceCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return create_attendance(db, attendance)


@router.get("/attendance")
def view_attendance(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return get_attendance(db)