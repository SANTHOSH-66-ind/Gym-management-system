from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from utils.database import SessionLocal
from schemas.member_schema import MemberCreate
from services.member_service import (
    create_member,
    get_members,
    update_member,
    delete_member
)
from auth.auth_dependency import get_current_user
router = APIRouter()


# Database connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# API to add member
@router.post("/add-member")
def add_member(
    member: MemberCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return create_member(db, member)
@router.get("/members")
def read_members(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return get_members(db)
@router.put("/members/{member_id}")
def edit_member(
    member_id: int,
    member: MemberCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return update_member(db, member_id, member)
@router.delete("/members/{member_id}")
def remove_member(
    member_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return delete_member(db, member_id)