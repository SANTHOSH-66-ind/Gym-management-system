🏋️ Gym Management & Fitness Analytics System

A Python-based Gym Management & Fitness Analytics System developed using FastAPI, SQLite, SQLAlchemy, Pandas, NumPy, Matplotlib, and Seaborn.

This system helps gyms manage members, assign workout plans, track attendance, analyze fitness data, and generate reports through REST APIs.

📌 Project Overview

The Gym Management & Fitness Analytics System is designed to automate common gym operations such as:

Member Management
Workout Assignment
Attendance Tracking
Membership Monitoring
Fitness Analytics
Revenue Analysis
Data Visualization
Authentication & Security

The project follows a modular architecture with separate layers for:

Models
Schemas
Services
Routes
Reports
Authentication
Utilities
🚀 Features
1. Member Management
Supported Operations
Add Member
View Members
Update Member
Delete Member
Member Information Stored
Name
Age
Gender
Weight
Fitness Goal
Membership Plan
Membership Status
Membership Plans
Monthly
Quarterly
Yearly
2. Workout Management
Supported Operations
Assign Workout
View Workouts
Update Workout
Delete Workout
Workout Information Stored
Member Name
Exercise Name
Sets
Repetitions
Duration
Trainer Notes
3. Attendance Management
Supported Operations
Add Attendance
View Attendance
Update Attendance
Delete Attendance
Attendance Information Stored
Member Name
Attendance Date
Status
4. Analytics Dashboard

The system generates analytical insights such as:

Dashboard Metrics
Total Members
Total Workouts
Total Attendance
Member Statistics
Average Age
Average Weight
Maximum Weight
Minimum Weight
Expired Membership Analysis
Count of expired members
Monthly Registration Analysis
Monthly member registrations
Workout Distribution Analysis
Most popular workout programs
Revenue Analytics

Estimated gym revenue based on membership plans.

📊 Data Visualization

The system generates the following visual reports:

Member Weight Analysis

Generated using:

Matplotlib

Output:

member_weight_report.png
Weight Distribution Analysis

Generated using:

Seaborn

Output:

weight_distribution.png
Member Growth Analysis

Tracks growth in gym memberships.

Output:

member_growth_report.png
Attendance Trend Analysis

Tracks attendance patterns over time.

Output:

attendance_trend_report.png
🔐 Authentication System

JWT Authentication has been implemented.

Features
Secure Login
JWT Token Generation
Protected Routes
Bearer Authentication
Login Credentials
{
  "username": "admin",
  "password": "admin123"
}
Authorization Process
Login
Receive JWT Token
Click "Authorize" in Swagger
Use Protected APIs
🧪 API Endpoints
Authentication
Login
POST /login
Member APIs
Add Member
POST /add-member
Get Members
GET /members
Update Member
PUT /members/{member_id}
Delete Member
DELETE /members/{member_id}
Workout APIs
Add Workout
POST /add-workout
Get Workouts
GET /workouts
Update Workout
PUT /workouts/{workout_id}
Delete Workout
DELETE /workouts/{workout_id}
Attendance APIs
Add Attendance
POST /add-attendance
Get Attendance
GET /attendance
Update Attendance
PUT /attendance/{attendance_id}
Delete Attendance
DELETE /attendance/{attendance_id}
Analytics APIs
Dashboard
GET /analytics/dashboard
Member Statistics
GET /analytics/member-stats
Member Weight Chart
GET /analytics/member-chart
Weight Distribution
GET /analytics/weight-distribution
Export Members CSV
GET /analytics/export-members
Expired Members
GET /analytics/expired-members
Monthly Registrations
GET /analytics/monthly-registrations
Workout Distribution
GET /analytics/workout-distribution
Revenue Analytics
GET /analytics/revenue
Member Growth
GET /analytics/member-growth
Attendance Trend
GET /analytics/attendance-trend
📝 Logging & Error Handling
Logging

The system logs:

Member Registration
Workout Assignment
Attendance Entries
API Activity
System Events
Errors

Log File:

gym.log
Error Handling

Implemented handling for:

Missing Fields
Invalid Inputs
Authentication Errors
Database Errors
Internal Server Errors
🗄️ Database

Database Used:

SQLite

Database File:

gym.db

ORM:

SQLAlchemy
📁 Project Structure
python-gym-system
│
├── auth
│   ├── auth_routes.py
│   ├── auth_service.py
│   ├── auth_schema.py
│   └── auth_dependency.py
│
├── data
│   └── gym.db
│
├── models
│   ├── member.py
│   ├── workout.py
│   └── attendance.py
│
├── routes
│   ├── member_routes.py
│   ├── workout_routes.py
│   ├── attendance_routes.py
│   └── analytics_routes.py
│
├── schemas
│   ├── member_schema.py
│   ├── workout_schema.py
│   └── attendance_schema.py
│
├── services
│   ├── member_service.py
│   ├── workout_service.py
│   ├── attendance_service.py
│   └── analytics_service.py
│
├── reports
│   ├── member_report.py
│   ├── seaborn_report.py
│   ├── member_growth_report.py
│   ├── attendance_report.py
│   └── export_report.py
│
├── utils
│   ├── database.py
│   ├── logger.py
│   └── validator.py
│
├── app.py
├── test.py
├── requirements.txt
├── README.md
└── gym.log
⚙️ Installation
Clone Repository
git clone <repository-url>
Move into Project
cd python-gym-system
Create Virtual Environment
python -m venv venv
Activate Environment

Windows:

venv\Scripts\activate
Install Dependencies
pip install -r requirements.txt
Run Application
uvicorn app:app --reload
📖 Swagger Documentation

Open:

http://127.0.0.1:8000/docs
🧪 Testing

Testing performed using:

Swagger UI
Pytest

Run tests:

pytest test.py -v
🛠 Technologies Used
Python
FastAPI
SQLAlchemy
SQLite
Pandas
NumPy
Matplotlib
Seaborn
JWT Authentication
Pytest
📈 Future Enhancements
Email Notifications
Streamlit Dashboard
Docker Deployment
Cloud Deployment (AWS / Render / Railway)
Trainer Management
Diet Plan Tracking
Mobile Application Integration
👨‍💻 Developer

santhosh
Electronics and Communication Engineering (ECE) Student

⭐ Project Status
Project Completion: 100%
All Internship Requirements Implemented Successfully