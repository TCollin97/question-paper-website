from flask import render_template
from app import app

# Home page - shows semesters
@app.route('/')
def home():
    semesters = list(range(1, 9))  # [1,2,3,4,5,6,7,8]
    return render_template('index.html', semesters=semesters)

# Semester page - shows subjects inside a semester
@app.route('/semester/<int:semester_id>')
def semester(semester_id):
    # Example subjects for each semester
    subjects = [
        "Subject 1",
        "Subject 2",
        "Subject 3",
        "Subject 4",
        "Subject 5",
        ]
    return render_template('semester.html', semester_id=semester_id, subjects=subjects)

# Subject page - shows details for a specific subject inside a semester
@app.route('/semester/<int:semester_id>/subject/<int:subject_id>')
def subject(semester_id, subject_id):
    # Example subjects for each semester
    subjects = [
        "Subject 1",
        "Subject 2",
        "Subject 3",
        "Subject 4",
        "Subject 5",
    ]

    # Get the subject name from the list based on subject_id
    subject_name = subjects[subject_id - 1]  # Adjust index since subject_id starts from 1

    # Exam categories in the set format
    exams = {
        "Assignments",
        "Unit Tests",
        "Mid Terms",
        "End Terms"
    }

    return render_template('subject.html', semester_id=semester_id, subject_id=subject_id, subject_name=subject_name, exams=exams)
