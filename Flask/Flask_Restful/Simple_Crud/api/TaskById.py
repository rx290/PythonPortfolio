from flask_restful import Resource
import  logging as logger

class TaskById(Resource):
    def get(self,task_id):
        logger.debug("Inside Get Method of TaskById!")
        return {"message": "Inside Get Method. ID = {}".format(task_id)},200
    
    def post(self,task_id):
        logger.debug("Inside Post Method of TaskById!")
        return {"message": "Inside Post Method. ID = {}".format(task_id)},200
    
    def put(self,task_id):
        logger.debug("Inside Put Method of TaskById!")
        return {"message": "Inside Put Method. ID = {}".format(task_id)},200
    
    def delete(self,task_id):
        logger.debug("Inside Delete Method of TaskById!")
        return {"message": "Inside Delete Method. ID = {}".format(task_id)},200