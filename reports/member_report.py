import matplotlib.pyplot as plt
from sqlalchemy.orm import Session
from models.member import Member


def generate_member_chart(db: Session):

    members = db.query(Member).all()

    names = [m.name for m in members]
    weights = [m.weight for m in members]

    plt.figure(figsize=(8,5))
    plt.bar(names, weights)

    plt.title("Member Weight Analysis")
    plt.xlabel("Members")
    plt.ylabel("Weight")

    plt.savefig("member_weight_report.png")

    return "Chart Generated"