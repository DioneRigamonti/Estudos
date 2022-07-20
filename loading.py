from time import sleep

# Criando um for de carregamento (loading) simples

for i in range(0,101,5):
    print(f'Carregando {i}%',end="\r")
    sleep(0.1)

print('\nFim')