from flask_sqlalchemy import SQLAlchemy
 
db =SQLAlchemy()
 
class StudentModel(db.Model):
    __tablename__ = "students"
 
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    email = db.Column(db.String())
    dob = db.Column(db.String())
    amount_due = db.Column(db.Integer)
 
    def __init__(self,id, first_name,last_name,email,dob,amount_due):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.dob = dob
        self.amount_due = amount_due
 
    def __repr__(self):
        return f"{self.first_name}:{self.last_name}"