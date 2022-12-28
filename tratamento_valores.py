#Tratando valores de um dicionario e adicionando imposto sobre o valor do produto.

produtos = {
    'TV':'R$ 5.456,21'
    ,'Radio':'R$ 1.245,45'
    ,'Celular':'R$ 4.785,78'
    ,'Computador':'R$ 10.580,50'
}

# - - - Função que trata valores com replace e modifica de string para float - - -

def tratar_valores(valor):
    valor = valor.replace('R$ ','').replace('.','').replace(',','.')
    valor = float(valor)
    return valor


# - - - Usando map para tratar cada valor dentro do dicionario produtos, com a função criada (tratar_valores) - - -

valores = list(map(tratar_valores,produtos.values()))

# - - - Adicionando imposto sobre o valor do produto (30%), utilizando map e lambda - - -

preco_produto_imposto = list(map(lambda preco: preco * 1.3, valores))

# - - - Utilizando o enumerate para adicionar novo valor com imposto para cada produto do dicionario - - -

for i, key in enumerate(produtos):
    produtos[key] = preco_produto_imposto[i]

print(produtos)