import getpass
import os
import platform
from datetime import datetime

nome_usuario = getpass.getuser()
diretorio_atual = os.getcwd()
sistema_operacional = platform.system()
versao_sistema = platform.version()
arquitetura = platform.architecture()
data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("arquivo_teste.txt", "a") as arquivo:
    print(f"Usuário: {nome_usuario}\nDiretório Atual: {diretorio_atual}\nSistema Operacional: {sistema_operacional}\nVersão do Sistema: {versao_sistema}\nArquitetura: {arquitetura}\nData e Hora: {data_hora_atual}\nTestando", file=arquivo)

