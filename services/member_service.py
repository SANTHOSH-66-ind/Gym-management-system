from sqlalchemy.orm import Session
from models.member import Member
from schemas.member_schema import MemberCreate
from utils.logger import logger


# CREATE MEMBER
def create_member(db: Session, member_data: MemberCreate):

    new_member = Member(
        name=member_data.name,
        age=member_data.age,
        gender=member_data.gender,
        weight=member_data.weight,
        fitness_goal=member_data.fitness_goal,
        membership_plan=member_data.membership_plan,
        membership_status=member_data.membership_status,
        join_date=member_data.join_date,
        expiry_date=member_data.expiry_date
        
    )

    db.add(new_member)
    db.commit()

    logger.info(
        f"Member Added: {new_member.name}"
    )

    db.refresh(new_member)

    return new_member


# READ ALL MEMBERS
def get_members(db: Session):

    return db.query(Member).all()


# UPDATE MEMBER
def update_member(
    db: Session,
    member_id: int,
    member_data: MemberCreate
):

    member = db.query(Member).filter(
        Member.id == member_id
    ).first()

    if not member:
        return None

    member.name = member_data.name
    member.age = member_data.age
    member.gender = member_data.gender
    member.weight = member_data.weight
    member.fitness_goal = member_data.fitness_goal
    member.membership_plan = member_data.membership_plan
    member.membership_status = member_data.membership_status
    member.join_date = member_data.join_date
    member.expiry_date = member_data.expiry_date

    db.commit()

    logger.info(
        f"Member Updated: {member.name}"
    )

    db.refresh(member)

    return member


# DELETE MEMBER
def delete_member(
    db: Session,
    member_id: int
):

    member = db.query(Member).filter(
        Member.id == member_id
    ).first()

    if not member:
        return None

    logger.info(
        f"Member Deleted: {member.name}"
    )

    db.delete(member)
    db.commit()

    return {
        "message": "Member Deleted Successfully"
    }