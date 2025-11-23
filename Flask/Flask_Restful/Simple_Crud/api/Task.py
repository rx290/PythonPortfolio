from flask_restful import Resource
import  logging as logger

class Task(Resource):
    def get(self):
        logger.debug("Inside Get Method!")
        return {"message": "Inside Get Method"},200
    
    def post(self):
        logger.debug("Inside Post Method!")
        return {"message": "Inside Post Method"},200
    
    def put(self):
        logger.debug("Inside Put Method!")
        return {"message": "Inside Put Method"},200
    
    def delete(self):
        logger.debug("Inside Delete Method!")
        return {"message": "Inside Delete Method"},200