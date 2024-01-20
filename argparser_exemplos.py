import argparse
import os
import pandas as pd

class MinhaClasse:
    def __init__(self, tabela, banco, caminho):
        self.tabela = tabela
        self.banco = banco
        self.caminho = caminho

    def criar_pasta(self):
        pasta = os.path.join(self.caminho, self.banco, self.tabela)
        os.makedirs(pasta, exist_ok=True)
        print(f'Pasta criada em: {pasta}')

    def apagar_pasta(self):
        pasta = os.path.join(self.caminho, self.banco, self.tabela)
        if os.path.exists(pasta):
            os.rmdir(pasta)
            print(f'Pasta apagada em: {pasta}')
        else:
            print(f'A pasta não existe em: {pasta}')

    def ler_dataframe(self):
        arquivo = os.path.join(self.caminho, self.banco, self.tabela, 'dados.csv')
        df = pd.read_csv(arquivo)
        return df

def main():
    # Criar um objeto ArgumentParser
    parser = argparse.ArgumentParser(description='Exemplo de argparse para múltiplos parâmetros')

    # Adicionar argumentos
    parser.add_argument('--tabela', type=str, required=True, help='Nome da tabela')
    parser.add_argument('--banco', type=str, required=True, help='Nome do banco de dados')
    parser.add_argument('--caminho', type=str, required=True, help='Caminho')
    parser.add_argument('--acao', choices=['criar_pasta', 'apagar_pasta'], help='Ação desejada')

    # Analisar os argumentos da linha de comando
    args = parser.parse_args()

    # Criar uma instância da classe
    minha_instancia = MinhaClasse(args.tabela, args.banco, args.caminho)

    # Executar a ação desejada
    if args.acao == 'criar_pasta':
        minha_instancia.criar_pasta()
    elif args.acao == 'apagar_pasta':
        minha_instancia.apagar_pasta()

if __name__ == '__main__':
    main()


#### terminal python meu_script.py --tabela MinhaTabela --banco MeuBanco --caminho /caminho/do/arquivo --acao criar_pasta
#### python meu_script.py --tabela MinhaTabela --banco MeuBanco --caminho /caminho/do/arquivo --acao apagar_pasta
