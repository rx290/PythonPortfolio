from flask_restful import Api
from app import flask_app
from .Task import  Task
from .TaskById import TaskById

restServer = Api(flask_app)

##URL to access the api
restServer.add_resource(Task,'/api/task')
##Accepting string parameter via URL
restServer.add_resource(TaskById,'/api/task/id/<string:task_id>')