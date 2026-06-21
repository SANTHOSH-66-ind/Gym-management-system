import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy.orm import Session
from models.attendance import Attendance


def generate_attendance_chart(db: Session):

    attendance = db.query(Attendance).all()

    data = []

    for record in attendance:
        data.append({
            "date": str(record.date)
        })

    df = pd.DataFrame(data)

    if df.empty:
        return "No Attendance Data"

    trend = (
        df.groupby("date")
        .size()
    )

    plt.figure(figsize=(8, 5))

    trend.plot()

    plt.title("Attendance Trend")
    plt.xlabel("Date")
    plt.ylabel("Attendance Count")

    plt.savefig("attendance_trend_chart.png")

    return "Attendance Trend Chart Generated"