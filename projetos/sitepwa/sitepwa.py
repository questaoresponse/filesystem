from flask import render_template,Blueprint
namespace='/sitepwa'
bp=Blueprint('sitepwa','app')
@bp.route(namespace)
def inicio():
    socketio = bp.config['socketio']
    receber_socketio(socketio)
    return render_template('index.html')
def receber_socketio(socketio):
    @socketio.on('ping')
    def teste_ping(ping):
        print(ping)