from sqlalchemy import Column, Integer, String
from utils.database import Base


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    member_name = Column(String)
    attendance_date = Column(String)
    status = Column(String)