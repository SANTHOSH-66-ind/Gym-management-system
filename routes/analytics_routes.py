from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from auth.auth_dependency import get_current_user
from reports.member_growth_report import generate_member_growth_chart
from utils.database import SessionLocal
from services.analytics_service import (
    get_dashboard_data,
    member_statistics,
    get_expired_members,
    get_monthly_registrations
)
from reports.member_report import generate_member_chart
from reports.seaborn_report import generate_seaborn_report
from reports.export_report import export_members_csv
from services.analytics_service import workout_distribution
from services.analytics_service import revenue_analytics
from services.analytics_service import attendance_trend

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/analytics/dashboard")
def dashboard(db: Session = Depends(get_db),
              current_user: str = Depends(get_current_user)
              ):
    return get_dashboard_data(db)
@router.get("/analytics/member-stats")
def member_stats(db: Session = Depends(get_db),
                 current_user: str = Depends(get_current_user)):
    return member_statistics(db)
@router.get("/analytics/member-chart")
def member_chart(db: Session = Depends(get_db),
                 current_user: str = Depends(get_current_user)):
    return {"message": generate_member_chart(db)}
@router.get("/analytics/weight-distribution")
def weight_distribution(db: Session = Depends(get_db),
                        current_user: str = Depends(get_current_user)):
    return {
        "message": generate_seaborn_report(db)
    }
@router.get("/analytics/export-members")
def export_members(db: Session = Depends(get_db),
                   current_user: str = Depends(get_current_user)):
    return {
        "message": export_members_csv(db)
    }
@router.get("/analytics/expired-members")
def expired_members(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return get_expired_members(db)


@router.get("/analytics/monthly-registrations")
def monthly_registrations(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return get_monthly_registrations(db)
@router.get("/analytics/workout-distribution")
def workout_distribution_data(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return workout_distribution(db)
@router.get("/analytics/revenue")
def revenue(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return revenue_analytics(db)
@router.get("/analytics/member-growth")
def member_growth(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return {
        "message": generate_member_growth_chart(db)
    }
@router.get("/analytics/attendance-trend")
def attendance_trend_data(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return attendance_trend(db)