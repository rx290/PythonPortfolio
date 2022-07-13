from flask import Flask
from flask_socketio import SocketIO, send

app=Flask(__name__)
app.config['secret_key'] = "SomeSecret"
connection = SocketIO(app)

@connection.on('message')
def handle_message(msg):
    print('Message: '+ msg)
    send(msg,broadcast=True)

if __name__ == '__main__':
    #SocketIO wraps and replaces flask by default request response system
    connection.run(app)