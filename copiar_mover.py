import os
import shutil

class Funcionalidade:
    origem = r'caminho\etc'
    destino = r'caminho\etc'
    destino_outra_pasta = r'caminho\etc'
    nome_arquivo = 'arquivo.txt'

    def copiar(self):
        for arquivo in os.listdir(self.origem):
            if self.nome_arquivo in arquivo:
                print(f'Copiando o arquivo {arquivo} para {self.destino}')
                caminho_origem = os.path.join(self.origem,arquivo)
                caminho_destino = os.path.join(self.destino,arquivo)
                shutil.copy2(caminho_origem, caminho_destino)


    def mover(self):
        for arquivo in os.listdir(self.origem):
            if self.nome_arquivo in arquivo:
                print(f'Movendo o arquivo {arquivo} para {self.destino}')
                caminho_origem = os.path.join(self.origem,arquivo)
                caminho_destino = os.path.join(self.destino_outra_pasta,arquivo)
                shutil.move(caminho_origem, caminho_destino)


objeto = Funcionalidade()
objeto.copiar()
objeto.mover()