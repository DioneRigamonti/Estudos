from dotenv import load_dotenv
from cryptography.fernet import Fernet
import os

'''
primeiro : encriptar os dados sensiveis com o codigo abaixo:

# from cryptography.fernet import Fernet

# chave = Fernet.generate_key()
# cipher_suite = Fernet(chave)

# login_cifrado = cipher_suite.encrypt(b'seu_login').decode('utf-8')
# senha_cifrada = cipher_suite.encrypt(b'sua_senha').decode('utf-8')

# print(f"CHAVE_CRIPTOGRAFIA={chave.decode('utf-8')}")
# print(f"LOGIN_CIFRADO={login_cifrado}")
# print(f"SENHA_CIFRADA={senha_cifrada}")

segundo : pegar o codigo gerado e salvar no .env

terceiro: apagar o primeiro passo do script.
'''

class ConfiguracoesSeguras:
    def __init__(self):
        load_dotenv()

        chave = os.getenv("CHAVE_CRIPTOGRAFIA")
        self.cipher_suite = Fernet(chave)

        login_cifrado = os.getenv("LOGIN_CIFRADO")
        senha_cifrada = os.getenv("SENHA_CIFRADA")

        self.login = self.descriptografar(login_cifrado)
        self.senha = self.descriptografar(senha_cifrada)

    def descriptografar(self, texto_cifrado):
        return self.cipher_suite.decrypt(texto_cifrado.encode()).decode('utf-8')

    def obter_login(self):
        return self.login

    def obter_senha(self):
        return self.senha










