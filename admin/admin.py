from flask import render_template,Blueprint,session,request
import sqlite3
import os
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
bp=Blueprint('admin','app',template_folder=diretorio_atual+"/templates/",static_folder=diretorio_atual+"/static/")
def before_request():
    if request.path.startswith('/admin'):
        usuario=session["usuario"]
        caminho_banco_dados = os.path.join(diretorio_atual, '..', 'usuarios.db')
        banco = sqlite3.connect(caminho_banco_dados)
        cursor=banco.cursor()
        cursor.execute('SELECT * FROM tabela_usuarios WHERE usuario=? and status="admin"',(usuario,))
        usuarios=cursor.fetchall()
        if len(usuarios)==0:
           return render_template("sem_permissao.html")
@bp.route('/admin',methods=["GET","POST" ])
def admin():
    return render_template("admin.html")
@bp.route('/admin/usuarios',methods=["GET","POST"])
def admin_usuarios():
    if request.method=="GET":
        return render_template('admin_usuarios.html')
    if request.method=="POST":
        usuario=session["usuario"]
        banco=sqlite3.connect('../usuarios.db')
        cursor=banco.cursor()
        cursor.execute('SELECT usuario FROM tabela_usuarios WHERE status="normal"')
        usuarios=cursor.fetchall()
        return usuarios
@bp.route('/admin/usuarios_admin',methods=["GET","POST"])
def admin_usuarios_admin():
    if request.method=="GET":
        return render_template('admin_usuarios_admin.html')
    if request.method=="POST":
        usuario=session["usuario"]
        banco=sqlite3.connect('../usuarios.db')
        cursor=banco.cursor()
        cursor.execute('SELECT usurio FROM tabela_usuarios WHERE status="admin"')
        usuarios_admin=cursor.fetchall()
        return usuarios_admin
