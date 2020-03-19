import requests
from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO


app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"
socketio = SocketIO(app)

@app.route("/")
def index():
    return 'ok'