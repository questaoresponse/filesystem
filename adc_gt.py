import subprocess
subprocess.run(["git","add","."])
subprocess.run(["git","commit","-m","adicionar pasta"])
subprocess.run(["git","push","-u","origin","main"])