from pydantic import BaseModel


class AttendanceCreate(BaseModel):
    member_name: str
    attendance_date: str
    status: str