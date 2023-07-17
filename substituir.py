import subprocess
import os
def run_file_in_folder(file_path, folder_path):
    current_directory = os.getcwd()
    os.chdir(folder_path)
    subprocess.run(["python", file_path])
    os.chdir(current_directory)
def rodar():
    file_path = "build_app.py"  # Substitua pelo caminho do arquivo que deseja executar
    folder_path = "./pwa"  # Substitua pelo caminho da pasta onde o arquivo está localizado
    run_file_in_folder(file_path, folder_path)
def clone_repository_and_replace_folder(repository_url, folder_path):
    # Clonar o repositório
    subprocess.run(["git", "clone", repository_url])
    # repository_name = repository_url.split("/")[-1].split(".git")[0]
    # os.replace(repository_name, folder_path)
    rodar()
    print("Repositório clonado e pasta substituída com sucesso!")
repository_url = "https://github.com/questaoresponse/pwa.git"  # URL do repositório a ser clonado
folder_path = os.getcwd()  # Caminho da pasta atual onde o arquivo Python está sendo executado
clone_repository_and_replace_folder(repository_url, folder_path)

# Exemplo de uso
