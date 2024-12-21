from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on("connect")
def handle_connect():
    emit("message", {"message": "Connected to server"})

@socketio.on("update")
def handle_update(data):
    # Handle incoming update
    emit("update", {"status": "success", "data": data}, broadcast=True)
