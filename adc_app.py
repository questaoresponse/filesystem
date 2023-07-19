import subprocess
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
subprocess.run(["git","--config","user.email","contaprogramarv@gmail.com"])
subprocess.run(["git","--config","user.name","questaoresponse"])
subprocess.run(["git","add","."])
subprocess.run(["git","commit","-m","adicionar pasta"])
subprocess.run(["git","push","-u","https://github.com/questaoresponse/filesystem.git","main"])