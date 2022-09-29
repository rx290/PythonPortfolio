from flask import Flask
from flask_socketio import SocketIO, send

app=Flask(__name__)
app.config['SECRET_KEY'] = 'SomeSecret'
connection = SocketIO(app)

@connection.on('message')
def handleMessage(msg):
    print('Message: '+ msg)
    send(msg,broadcast=True)

if __name__ == '__main__':
    #SocketIO wraps and replaces flask by default request response system
    connection.run(app)