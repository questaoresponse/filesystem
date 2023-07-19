import subprocess
import os
diretorio_atual=os.path.dirname(os.path.abspath(__file__))
os.chdir(diretorio_atual)
subprocess.run(["git","config","--global","user.email","eneagonlosamigos@gmail.com"])
subprocess.run(["git","config","--global","user.name","questaoresponse"])
subprocess.run(["git","add",diretorio_atual+"/flask_session",diretorio_atual+"/usuarios.db"])
subprocess.run(["git","commit","-m","adicionar pasta"])
subprocess.run(["git","push","-u","https://github.com/questaoresponse/filesystem.git","main"])