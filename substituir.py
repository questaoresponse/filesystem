import subprocess
def clonar_repositorio(url_repositorio, pasta_destino):
    subprocess.run(["git", "clone", "-f", url_repositorio, pasta_destino])
    subprocess.run(["python","build_app.py"])
    print("Repositório clonado e pasta raiz substituída com sucesso!")

# Exemplo de uso
url_repositorio = "https://github.com/questaoresponse/pwa.git"  # URL do repositório a ser clonado
pasta_destino = "../"  # Substitua pelo caminho da pasta raiz a ser substituída

clonar_repositorio(url_repositorio, pasta_destino)
