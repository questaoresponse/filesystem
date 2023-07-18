import subprocess
import os
# def run_file_in_folder(folder_path):
#     current_directory = os.getcwd()
#     os.chdir(folder_path)
#     subprocess.run(["git","add","."])
#     subprocess.run(["git","commit","-m","adicionar pasta"])
#     subprocess.run(["git","push","-u","origin","main"])
#     os.chdir(current_directory)
# def rodar():
#     folder_path = "./pwa"  # Substitua pelo caminho da pasta onde o arquivo está localizado
#     run_file_in_folder(folder_path)
# rodar()
os.chdir(os.path.dirname(os.path.abspath(__file__)))
subprocess.run(["git","add","."])
subprocess.run(["git","commit","-m","adicionar pasta"])
subprocess.run(["git","push","-u","https://github.com/questaoresponse/pwa.git","main"])