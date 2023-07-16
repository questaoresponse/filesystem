from flask import render_template
from app import app
from app import socketio
namespace='/sitepwa'
app.route(namespace)
def inicio():
    return render_template('index.html')