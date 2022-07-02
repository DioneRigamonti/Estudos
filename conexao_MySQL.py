import mysql.connector
from time import sleep

# - - Criando uma variavel para adicionar o comando de conexao e passando os parametros para acessar o banco de dados.
conexao = mysql.connector.connect(host = 'localhost',
database = 'cadastro',
user = 'root',
password = '')

if conexao.is_connected():
    print('Conectado com SUCESSO!')
    cursor = conexao.cursor()

cursor.execute('select * from pessoas;')
r = cursor.fetchone()
for r in cursor:
    print(r)
    sleep(0.3)

if conexao.is_connected():
    cursor.close()
    conexao.close()
    print('CONEXÃO ENCERRADA COM SUCESSO!')

