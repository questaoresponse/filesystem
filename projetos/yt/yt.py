from flask import Blueprint,session,render_template,request,redirect
import sqlite3
import os
caminho='/yt'
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
bp=Blueprint('yt','app',template_folder=diretorio_atual+"/templates/",static_folder=diretorio_atual+"/static/")
def router(cm):
    return bp.route(caminho+cm)
@router('/')
def inicio():
    return render_template('index.html')
