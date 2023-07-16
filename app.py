from flask import Flask,render_template
from flask_socketio import SocketIO,emit
app=Flask('app')
socketio=SocketIO(app)
@app.route('/')
def inicio():
    return render_template('index.html')
@socketio.on('teste')
def teste(data):
    emit('enviado','mensagem')
@socketio.on('ping')
def socket(data):
  emit('ping',data)
if __name__=='__main__':
    socketio.run(app)