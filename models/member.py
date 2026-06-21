from sqlalchemy import Column, Integer, String, Date
from utils.database import Base
from datetime import date
from sqlalchemy import Column, Integer, String, Date



class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    age = Column(Integer)

    gender = Column(String)

    weight = Column(Integer)

    fitness_goal = Column(String)

    membership_plan = Column(String)

    membership_status = Column(String)

    join_date = Column(Date, default=date.today)

    expiry_date = Column(Date)