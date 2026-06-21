from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


# -----------------------------
# HOME API
# -----------------------------
def test_home():
    response = client.get("/")
    assert response.status_code == 200


# -----------------------------
# MEMBER API
# -----------------------------
def test_add_member():

    payload = {
        "name": "Test User",
        "age": 25,
        "gender": "Male",
        "weight": 70,
        "fitness_goal": "Muscle Gain",
        "membership_plan": "Monthly",
        "membership_status": "Active"
    }

    response = client.post(
        "/add-member",
        json=payload
    )

    assert response.status_code == 200


def test_get_members():

    response = client.get("/members")

    assert response.status_code == 200


# -----------------------------
# WORKOUT API
# -----------------------------
def test_add_workout():

    payload = {
        "member_name": "Test User",
        "exercise_name": "Bench Press",
        "sets": 4,
        "repetitions": 12,
        "duration": 45,
        "trainer_notes": "Increase weight gradually"
    }

    response = client.post(
        "/add-workout",
        json=payload
    )

    assert response.status_code == 200


def test_get_workouts():

    response = client.get("/workouts")

    assert response.status_code == 200


# -----------------------------
# ATTENDANCE API
# -----------------------------
def test_add_attendance():

    payload = {
        "member_name": "Test User",
        "attendance_date": "2026-06-17",
        "status": "Present"
    }

    response = client.post(
        "/add-attendance",
        json=payload
    )

    assert response.status_code == 200


def test_get_attendance():

    response = client.get("/attendance")

    assert response.status_code == 200


# -----------------------------
# ANALYTICS API
# -----------------------------
def test_dashboard():

    response = client.get(
        "/analytics/dashboard"
    )

    assert response.status_code == 200


def test_member_stats():

    response = client.get(
        "/analytics/member-stats"
    )

    assert response.status_code == 200


def test_export_members():

    response = client.get(
        "/analytics/export-members"
    )

    assert response.status_code == 200