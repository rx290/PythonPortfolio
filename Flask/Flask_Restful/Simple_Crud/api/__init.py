from flask_restful import Api
from app import flask_app

restServer = Api(flask_app)

restServer.add_rep