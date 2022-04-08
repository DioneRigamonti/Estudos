#Jogo Jokenpo

from time import sleep
from random import randint

controle = ''
while controle != 'N':
    jogadas = ['Pedra', 'Papel', 'Tesoura']
    pc = randint(0,2)
    print('''Tabela do jogo
    [ 0 ] Pedra
    [ 1 ] Papel
    [ 2 ] Tesoura
    ''')
    jogador = int(input('Digite sua jogada: '))
    print('Jo')
    sleep(1)
    print('ken')
    sleep(1)
    print('Po')
    
    print('-.-'*15)
    print(f'A máquina jogou {jogadas[pc]}')
    print(f'Você jogou {jogadas[jogador]}')

    if pc == 0:
        if jogador == 0:
            print('Empate')
        elif jogador == 1:
            print('Você venceu')
        elif jogador == 2:
            print('A máquina venceu')
    elif pc == 1:
        if jogador == 0:
            print('A máquina venceu')
        elif jogador == 1:
            print('Empate')
        elif jogador == 2:
            print('Você venceu')
    elif pc == 2:
        if jogador == 0:
            print('Você venceu')
        elif jogador == 1:
            print('A máquina venceu')
        elif jogador == 2:
            print('Empate')
    else:
        print('Jogada inválida, Tente novamente...')
    print('-.-'*15)
    
    controle = str(input('Deseja continuar [S/N]?: ')).strip().upper()[0]
print('Obrigado, Volte sempre.')
    