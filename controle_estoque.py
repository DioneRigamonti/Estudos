estoque = 0
lista_valores = []
qtd_ind = [] #caso não queira essa lista, mude o append do comentario número 4
qtd_saida = 0

while True:
    #--- Captura do dado ---# 0
    valor = int(input('Digite um valor: '))
    
    #--- Condição de saída ---# 1
    if valor == 0:
        lista_valores.append(valor)
        break

    #--- Se o dado inserido for positivo ---# 2
    if valor > 0:
        estoque = estoque + valor
        print(f'Estoque atual: {estoque}')
        lista_valores.append(valor)
        
    #--- Se o dado inserido for negativo, FAÇA: ---# 3
    elif valor < 0:
        estoque = estoque + valor
        conta = estoque

        #--- Se o dado inserido for negativo e o estoque tiver saldo ---# 3.1
        if conta >= 0:
            print(f'Saída com sucesso, Estoque altual: {estoque}')
            qtd_saida += 1
            lista_valores.append(valor)
     
        #--- Se o dado inserido for negativo e o estoque não tiver saldo ---# 3.2
        elif valor < 0 and conta < 0:
            print(f'Quantidade indisponível para {valor} unidades')
            estoque = estoque - valor
            print(f'Estoque altual: {estoque}')
            qtd_ind.append(valor) #--- APPEND ---# 4

#--- Mostre o print a sua escolha ---# 5
print(f'Quantidade de saídas realizadas:{qtd_saida}')
print(f'Quantidade final: {estoque}')
print(lista_valores)
print(qtd_ind)