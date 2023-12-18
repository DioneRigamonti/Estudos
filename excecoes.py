class Novaexcecao(Exception):
    def __init__(self, valor) -> None:
        super().__init__(valor)

valor = 5

try:
    if valor > 5:
        print('Valor é maior')
    else:
        raise Novaexcecao('Valor é menor')
except Novaexcecao as e:
    print(f'Erro: {e}')
    