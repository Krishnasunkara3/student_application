from db import db


class StudentModel(db.Model):
    __tablename__ = "studentDetails"
    student_id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)
    student_class = db.Column(db.String(50), nullable=False)
    student_age = db.Column(db.Integer, nullable=False)
    student_address = db.Column(db.String(100), nullable=False)

    def __init__(self, student_id, student_name,student_class, student_age, student_address):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class
        self.student_age = student_age
        self.student_address = student_address

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def change_in_db(self):
        db.session.commit()