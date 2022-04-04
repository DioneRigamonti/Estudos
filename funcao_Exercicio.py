# Python - Treinando funções

from time import sleep

def somar(a=0,b=0):
    s = a + b
    print('-='*15)
    print(f'A soma entre {a} + {b} = {s}')
    print('-='*15)


def subtrair(a=0,b=0):
    sub = a - b
    print('-='*15)
    print(f'A subtração entre {a} - {b} = {sub}')
    print('-='*15)


def multiplicacao(a=0,b=0):
    m = a * b
    print('-='*15)
    print(f'A multiplicação entre {a} * {b} = {m}')
    print('-='*15)


def divisao(a=0,b=0):
    d = a / b
    print('-='*15)
    print(f'A Divisão entre {a} / {b} = {d}')
    print('-='*15)


chave = 0

while chave != 4:
    print('''Escolha uma operação:
    [ 0 ] Soma
    [ 1 ] Subtração
    [ 2 ] Multiplicação
    [ 3 ] Divisão
    [ 4 ] Sair''')
    chave = int(input('Digite uma opção: '))
    if chave == 0:
        a = float(input('Digite o primeiro número: '))
        b = float(input('Digite o Segundo número: '))
        print('Calculando...')
        sleep(1)
        somar(a,b)
    elif chave == 1:
        a = float(input('Digite o primeiro número: '))
        b = float(input('Digite o Segundo número: '))
        print('Calculando...')
        sleep(1)
        subtrair(a,b)
    elif chave == 2:
        a = float(input('Digite o primeiro número: '))
        b = float(input('Digite o Segundo número: '))
        print('Calculando...')
        sleep(1)
        multiplicacao(a,b)
    elif chave == 3:
        a = float(input('Digite o primeiro número: '))
        b = float(input('Digite o Segundo número: '))
        print('Calculando...')
        sleep(1)
        divisao(a,b)
    elif chave == 4:
        print('Finalizando programa...')
        sleep(1)
        break
    else:
        print('Digite uma opção válida!!!')
    sleep(1)
print('Obrigado, Volte sempre.')