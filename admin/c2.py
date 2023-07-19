import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect('../usuarios.db')

# Criar um cursor para executar as consultas
cursor = conexao.cursor()

# Executar uma consulta para obter as tabelas do banco de dados
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")

# Obter os resultados da consulta
tabelas = cursor.fetchall()

# Imprimir o nome das tabelas
for tabela in tabelas:
    print(tabela[0])

# Fechar a conexão com o banco de dados
conexao.close()