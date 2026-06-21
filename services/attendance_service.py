from sqlalchemy.orm import Session
from models.attendance import Attendance
from utils.logger import logger


def create_attendance(db: Session, attendance_data):
    new_attendance = Attendance(
        member_name=attendance_data.member_name,
        attendance_date=attendance_data.attendance_date,
        status=attendance_data.status
    )

    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)

    return new_attendance
    logger.info(
    f"Attendance Marked: {new_attendance.member_name}"
)

def get_attendance(db: Session):
    return db.query(Attendance).all()