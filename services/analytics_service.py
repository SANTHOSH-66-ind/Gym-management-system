from models.workout import Workout
from sqlalchemy.orm import Session
from models.member import Member
from models.workout import Workout
from models.attendance import Attendance

import pandas as pd
import numpy as np
from datetime import date


def get_dashboard_data(db: Session):

    total_members = db.query(Member).count()
    total_workouts = db.query(Workout).count()
    total_attendance = db.query(Attendance).count()

    return {
        "total_members": total_members,
        "total_workouts": total_workouts,
        "total_attendance": total_attendance
    }


def member_statistics(db: Session):

    members = db.query(Member).all()

    data = []

    for member in members:
        data.append({
            "name": member.name,
            "age": member.age,
            "weight": member.weight
        })

    df = pd.DataFrame(data)

    if df.empty:
        return {"message": "No members found"}

    return {
        "average_age": float(np.mean(df["age"])),
        "average_weight": float(np.mean(df["weight"])),
        "max_weight": float(np.max(df["weight"])),
        "min_weight": float(np.min(df["weight"]))
    }


# NEW FEATURE
def get_expired_members(db: Session):

    today = date.today()

    expired_count = db.query(Member).filter(
        Member.expiry_date < today
    ).count()

    return {
        "expired_members": expired_count
    }


# NEW FEATURE
def get_monthly_registrations(db: Session):

    members = db.query(Member).all()

    data = []

    for member in members:

        if member.join_date:

            data.append({
                "month": member.join_date.strftime("%B")
            })

    df = pd.DataFrame(data)

    if df.empty:
        return {
            "message": "No registration data"
        }

    registrations = (
        df["month"]
        .value_counts()
        .to_dict()
    )

    return registrations
def attendance_trends(db: Session):

    attendance = db.query(Attendance).all()

    if not attendance:
        return {"message": "No attendance records"}

    trend = {}

    for record in attendance:
        date = record.attendance_date

        if date not in trend:
            trend[date] = 0

        trend[date] += 1

    return trend
def workout_distribution(db: Session):

    workouts = db.query(Workout).all()

    if not workouts:
        return {"message": "No workout records"}

    distribution = {}

    for workout in workouts:

        exercise = workout.exercise_name

        if exercise not in distribution:
            distribution[exercise] = 0

        distribution[exercise] += 1

    return distribution
def revenue_analytics(db: Session):

    members = db.query(Member).all()

    revenue = 0

    for member in members:

        if member.membership_plan == "Monthly":
            revenue += 1000

        elif member.membership_plan == "Quarterly":
            revenue += 2500

        elif member.membership_plan == "Yearly":
            revenue += 10000

    return {
        "estimated_revenue": revenue
    }



def attendance_trend(db: Session):

    attendance = db.query(Attendance).all()

    data = []

    for record in attendance:
        data.append({
    "date": str(record.attendance_date)
})
    df = pd.DataFrame(data)

    if df.empty:
        return {"message": "No Attendance Data"}

    trend = (
        df.groupby("date")
        .size()
        .reset_index(name="count")
    )

    return trend.to_dict(orient="records")