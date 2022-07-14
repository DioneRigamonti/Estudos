""""""
"""
List Comprehensions

Gerar uma lista a partir do processamento de uma coleção de dados.

Sintaxe: [operação/função for elemento in iterável]

# Exemplos de List Comprehensions

impares = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

#Loop for
pares = []
for num in impares:
    pares.append(num * 2)

print(pares)

# Comprehensions
print([num * 2 for num in impares])

# List Comprehensions com estruturas condicionais

#if

numeros = list(range(1, 11))

pares = [num * 10 for num in numeros if num % 2 == 0]
impares = [num ** 2 for num in numeros if num % 2 != 0]

print(pares)
print(impares)

# Else

numeros = list(range(1, 11))

nova = [num if num <= 5 else num * 10 for num in numeros]
print(nova)

# Comprehensions em matrizes

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

[[print(num, end=' ') for num in linha] for linha in matriz]

matriz3 = [[num * 3 for num in linha] for linha in matriz]
print(f'\n{matriz3}')
"""

n = list(range(1,11))

tabuada1 = [num * 1 for num in n]
print(tabuada1)
tabuada2 = [num * 2 for num in n]
print(tabuada2)
tabuada3 = [num * 3 for num in n]
print(tabuada3)