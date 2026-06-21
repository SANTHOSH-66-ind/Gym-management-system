import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sqlalchemy.orm import Session
from models.member import Member


def generate_seaborn_report(db: Session):

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
        return "No Data Found"

    plt.figure(figsize=(8, 5))

    sns.histplot(
        data=df,
        x="weight",
        kde=True
    )

    plt.title("Weight Distribution")

    plt.savefig("weight_distribution.png")

    return "Seaborn Report Generated"