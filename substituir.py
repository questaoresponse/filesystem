import subprocess
import os
def clone_repository_and_replace_folder(repository_url, folder_path):
    # Clonar o repositório
    subprocess.run(["git", "clone", repository_url])
    # repository_name = repository_url.split("/")[-1].split(".git")[0]
    # os.replace(repository_name, folder_path)
    subprocess.run(["python","build_app.py"])
    print("Repositório clonado e pasta substituída com sucesso!")
repository_url = "https://github.com/questaoresponse/pwa.git"  # URL do repositório a ser clonado
folder_path = os.getcwd()  # Caminho da pasta atual onde o arquivo Python está sendo executado
clone_repository_and_replace_folder(repository_url, folder_path)