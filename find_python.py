#Buscando um valor dentro de uma nomenclatura fixa.

#Pegando uma data

nome_arquivo = "NOME_ARQUIVO_DATA_20230101.csv"
captura = nome_arquivo.find("DATA_") # jogando o valor anterior ao dado que quero e que seja FIXO!
valor_capturado = nome_arquivo[captura + len("DATA_"): nome_arquivo.find(".",captura)]
print(valor_capturado)

#Output : 20230101

#Pegando a quantidade de linhas

nome_arquivo = "ESTE_ARQUIVO_TEM_12345_LINHAS.txt"
captura = nome_arquivo.find("TEM_") 
valor_capturado = nome_arquivo[captura + len("TEM_"): nome_arquivo.find("_LINHAS",captura)]
print(valor_capturado)

#Output : 12345