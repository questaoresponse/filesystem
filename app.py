# import mysql.connector
from flask import Flask,render_template,redirect,request,session
from flask_session import Session
from flask_socketio import SocketIO,emit
import subprocess
import sqlite3
import os
# Estabeleça a conexão
# banco = mysql.connector.connect(
#     user='seu_usuario',
#     password='sua_senha',
#     host='localhost',
#     database='nome_do_banco_de_dados'
# )
# Crie o cursor
# cursor = banco.cursor()
app=Flask('app')
# app.config["SESSION_PERMANENT"] = False
app.secret_key='chave_para_teste'
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
print(diretorio_atual)
app.config['SESSION_FILE_DIR'] = f'{diretorio_atual}/flask_session'
app.config['SESSION_COOKIE_PATH'] =f"{diretorio_atual}/flask_session"
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
socketio=SocketIO(app)
def adicionar():
    os.getcwd()
    subprocess.run(["python",f"{diretorio_atual}/adc_gt.py"])
@app.before_request
def before_request():
    if not session.get('usuario'):
        if request.path!='/cadastro':
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
    banco=sqlite3.connect(diretorio_atual+'/usuarios.db')
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
           adicionar()
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
                adicionar()
                return "true"
        if tipo2=="login":
            if len(usuarios)>0:
                session["usuario"]=usuario
                adicionar()
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