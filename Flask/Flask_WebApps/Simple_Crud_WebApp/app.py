from flask import Flask,render_template,request,redirect
from  models import db,StudentModel

flask_app=Flask(__name__)

# Database Path
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'

flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Calling the constructor
db.init_app(flask_app)


#Creating Database
@flask_app.before_first_request
def create_db():
    db.create_all()
    
@flask_app.route('/create',methods=['GET', 'POST',])
def create():
    return render_template('Create.html')    
    # if request.method == 'GET':
    #     return render_template('/pages/Create.html')
    

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    flask_app.run(port=5000,debug=True)
    
