from flask import Flask
import  logging as logger
logger.basicConfig(level='DEBUG')


flask_app = Flask(__name__)

if __name__ == '__main__':
    logger.debug("Starting the application")
    flask_app.run()