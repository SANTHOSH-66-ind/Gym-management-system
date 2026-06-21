import pandas as pd

from sqlalchemy.orm import Session
from models.member import Member


def export_members_csv(db: Session):

    members = db.query(Member).all()

    data = []

    for member in members:
        data.append({
            "id": member.id,
            "name": member.name,
            "age": member.age,
            "weight": member.weight,
            "goal": member.fitness_goal
        })

    df = pd.DataFrame(data)

    df.to_csv(
        "members_report.csv",
        index=False
    )

    return "CSV Exported Successfully"