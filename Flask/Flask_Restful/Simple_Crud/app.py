from flask import Flask
import  logging as logger
from api import *

logger.basicConfig(level='DEBUG')


flask_app = Flask(__name__)

if __name__ == '__main__':
    logger.debug("Starting the application")
    flask_app.run(debug=True,use_reloader=True,port=5000)