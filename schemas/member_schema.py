from pydantic import BaseModel
from datetime import date



class MemberCreate(BaseModel):
    name: str
    age: int
    gender: str
    weight: int
    fitness_goal: str
    membership_plan: str
    membership_status: str
    join_date: date
    expiry_date: date