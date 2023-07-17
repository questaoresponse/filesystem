from flask import Flask,render_template,redirect,request,session
from flask_session import Session
from flask_socketio import SocketIO,emit
import sqlite3
import subprocess
import os
import sys
app=Flask('app')
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
socketio=SocketIO(app)
@app.before_request
def before_request():
    if not session.get('usuario'):
        if request.path!='/cadastro' and request.path!='/teste_server' :
            return redirect('/cadastro')
    else:
        if request.path=='/cadastro':
            return redirect('/')
@app.route('/')
def inicio():
    return render_template('bem_vindo.html')
@app.route('/cadastro',methods=["GET","POST"])
def cadastro():
  if request.method=="GET":
    return render_template("cadastro_login.html")
  if request.method=="POST":
    banco=sqlite3.connect("banco_usuarios.db")
    cursor=banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS tabela_usuarios(usuario,email,senha)')
    email=request.form.get('email')
    tipo=request.form.get("tipo")
    if tipo=="google":
        usuario=email.split("@")[0]
        senha="nenhum"
        session['usuario']=usuario
        cursor.execute('SELECT * FROM tabela_usuarios WHERE usuario=?',(usuario,))
        usuarios=cursor.fetchall()
        if len(usuarios)==0:
           cursor.execute('INSERT INTO tabela_usuarios(usuario,email,senha) VALUES(?,?,?)',(usuario,email,senha))
           banco.commit()
        return 'true'
    if tipo=="account":
        usuario=request.form.get("usuario")
        senha=request.form.get("senha")
        tipo2=request.form.get("tipo2")
        cursor.execute('SELECT * FROM tabela_usuarios WHERE usuario=?',(usuario,))
        usuarios=cursor.fetchall()
        if tipo2=="cadastro":
            if len(usuarios)>0:
                return "false"
            else:
                cursor.execute('INSERT INTO tabela_usuarios(usuario,email,senha) VALUES(?,?,?)',(usuario,email,senha))
                banco.commit()
                session["usuario"]=usuario
                return "true"
        if tipo2=="login":
            if len(usuarios)>0:
                session["usuario"]=usuario
                return "true"
            else:
                return "false"
@socketio.on('teste')
def teste(data):
    emit('enviado','mensagem')
@socketio.on('ping')
def socket(data):
  emit('ping',data)
from projetos.sitepwa.sitepwa import bp
app.register_blueprint(bp)
if __name__=='__main__':
    socketio.run(app)