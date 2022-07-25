#Calculadora simples com eval
from time import sleep

chave = ''
print('\033[1;100mOlá, Vamos as contas!!!')
while chave != 'N':
    conta = input('\n\033[1;46mDigite a conta que você deseja saber: \33[m')
    resultado = eval(conta)
    print()
    for x in range(101):
        print(f'\033[1;100mCalculando {x}%\033[m',end='\r')
        sleep(0.01)
    print()
    print(f'\n\033[1;42mO resultado é {resultado} \033[m')
    chave = input('\n\033[1;100mDeseja continuar [S/N]?: \033[m').strip().upper()[0]

print('\n\033[1;102mPrograma Finalizado!\033[m')
