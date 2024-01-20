import getpass
from datetime import datetime

# capturando o user do usuario e gravando em um .txt onde o valor mais recente fica no topo.

def obter_nome_usuario_sistema():
    return getpass.getuser()

# Obtém o nome de usuário do sistema
nome_usuario = obter_nome_usuario_sistema()

# Obtém a data e hora atual
data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Cria a string a ser gravada no arquivo
registro = f"{data_hora_atual} - Nome de usuário: {nome_usuario}"

# Lê o conteúdo atual do arquivo
with open("registro.txt", "r") as arquivo:
    conteudo_atual = arquivo.read()

# Abre o arquivo no modo de escrita e escreve a nova string no topo
with open("registro.txt", "w") as arquivo:
    arquivo.write(registro + "\n" + conteudo_atual)

print(f"Nome de usuário gravado em registro.txt: {nome_usuario}")