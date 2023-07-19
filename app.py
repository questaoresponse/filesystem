# import mysql.connector
from flask import Flask,render_template,redirect,request,session
from flask_session import Session
from flask_socketio import SocketIO,emit
import subprocess
import sqlite3
import os
from admin.admin import before_request
# Estabeleça a conexão
# banco = mysql.connector.connect(
#     user='seu_usuario',
#     password='sua_senha',
#     host='localhost',
#     database='nome_do_banco_de_dados'
# )
# Crie o cursor
# cursor = banco.cursor()
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
app=Flask('app',static_folder=diretorio_atual+'/static/')
app.secret_key='secret_chave_key'
app.config['SECRET_KEY']='chave_para_teste'
app.config["SESSION_PERMANENT"] = True
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = f'{diretorio_atual}/flask_session'
print(diretorio_atual)
Session(app)
socketio=SocketIO(app)
def adicionar():
    os.getcwd()
    subprocess.run(["python",f"{diretorio_atual}/adc_gt.py"])
    #pass
ips_bloqueados = [ '10.0.0.1']
@app.before_request
def before_request_app():
# Função para verificar se um IP está bloqueado
 allowed_methods = ['GET', 'POST']  # Métodos permitidos
 if request.method in allowed_methods and not request.path.startswith('/templates') and not request.path.startswith('/static') and not request.path.startswith('/socket'):
  def ip_esta_bloqueado(ip):
    return ip in ips_bloqueados
  ip_cliente = request.remote_addr
  print(ip_cliente)
  if ip_esta_bloqueado(ip_cliente):
        return render_template('ip_bloqueado.html')
  if not session.get('usuario'):
    if request.path!='/cadastro':
        return redirect('/cadastro')
  else:
    if request.path=='/cadastro':
        return redirect('/')
    before_request()
@app.route('/')
def inicio():
    return render_template('bem_vindo.html')
@app.route('/cadastro',methods=["GET","POST"])
def cadastro():
  if request.method=="GET":
    return render_template("cadastro_login.html")
  if request.method=="POST":
    status=""
    banco=sqlite3.connect(diretorio_atual+'/usuarios.db')
    cursor=banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS tabela_usuarios(usuario,email,senha,status,tipo)')
    email=request.form.get('email')
    tipo=request.form.get("tipo")
    if tipo=="google":
        usuario=email.split("@")[0]
        senha="nenhum"
        session['usuario']=usuario
        cursor.execute('SELECT * FROM tabela_usuarios WHERE usuario=? and tipo="google"',(usuario,))
        usuarios=cursor.fetchall()
        if len(usuarios)==0:
           cursor.execute('INSERT INTO tabela_usuarios(usuario,email,senha,status,tipo) VALUES(?,?,?,?,?)',(usuario,email,senha,status,"google"))
           banco.commit()
           adicionar()
        return 'true'
    if tipo=="account":
        usuario=request.form.get("usuario")
        senha=request.form.get("senha")
        if usuario=="admin" and email=="contaprogramarv@gmail.com" and senha=="6626070":
            status="creator"
        tipo2=request.form.get("tipo2")
        cursor.execute('SELECT * FROM tabela_usuarios WHERE usuario=? and tipo="account"',(usuario,))
        usuarios=cursor.fetchall()
        if tipo2=="cadastro":
            if len(usuarios)>0:
                return "false"
            else:
                cursor.execute('INSERT INTO tabela_usuarios(usuario,email,senha,status,tipo) VALUES(?,?,?,?,?)',(usuario,email,senha,status,tipo))
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
from admin.admin import bp
app.register_blueprint(bp)

if __name__=='__main__':
    socketio.run(app)