import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy.orm import Session

from models.member import Member


def generate_member_growth_chart(db: Session):

    members = db.query(Member).all()

    data = []

    for member in members:
        data.append({
            "join_date": str(member.join_date)
        })

    df = pd.DataFrame(data)

    if df.empty:
        return "No Members Found"

    growth = (
        df.groupby("join_date")
        .size()
        .cumsum()
    )

    plt.figure(figsize=(8, 5))

    growth.plot()

    plt.title("Member Growth Trend")
    plt.xlabel("Join Date")
    plt.ylabel("Total Members")

    plt.savefig("member_growth_chart.png")

    return "Member Growth Chart Generated"