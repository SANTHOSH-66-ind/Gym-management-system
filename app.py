from fastapi import FastAPI

from utils.database import engine, Base

from models.member import Member
from models.workout import Workout

from routes.member_routes import router
from routes.workout_routes import router as workout_router
from models.attendance import Attendance
from routes.attendance_routes import router as attendance_router
from routes.analytics_routes import router as analytics_router
from auth.auth_routes import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Gym Management System Running"}


app.include_router(router)
app.include_router(workout_router)
app.include_router(attendance_router)
app.include_router(analytics_router)
app.include_router(auth_router)