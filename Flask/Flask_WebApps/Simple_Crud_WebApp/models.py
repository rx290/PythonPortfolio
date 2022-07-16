from flask_sqlalchemy import  SQLAlchemy

#Wrapper initialization
db = SQLAlchemy()

class StudentModel(db.Model):
    #Table Name
    __tablename__ = 'student'
    
    # Fields and Datatype initialization
    id = db.Column(db.Integer, primary_key=True)
    fullName = db.Column(db.String())
    email = db.Column(db.Email())
    password = db.Column(db.Password())
    gender = db.Column(db.Boolean())
    hobbies = db.Column(db.String())
    country = db.Column(db.String(80))
    
    # Constructor
    def __init__(self, full_name,email,gender,country,hobbies,password):
      self.full_name = full_name
      self.email = email
      self.gender = gender
      self.country = country
      self.hobbies = hobbies
      self.password=password
      
    