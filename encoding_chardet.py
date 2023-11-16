import pandas as pd
import chardet

########### CODIGO 100% CHATGPT
###### Descobrindo a lib chardet que busca o encoding de um arquivo quando mesmo definindo para UTF-8, latin-1 etc... toma o erro "unicodeDecodeError"

# Função para detectar a codificação do arquivo
def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

# Caminho para o arquivo CSV
file_path = 'seuarquivo.csv'

# Detectando a codificação do arquivo
encoding = detect_encoding(file_path)

# Lendo o arquivo CSV com a codificação detectada
df = pd.read_csv(file_path, encoding=encoding)

# Exibindo o DataFrame original
print("DataFrame Original:")
print(df)

# Convertendo a coluna 'sua_coluna' para timestamp
df['sua_coluna'] = pd.to_datetime(df['sua_coluna'], format="%d%b%Y:%H:%M:%S.%f", errors='coerce')

# Exibindo o DataFrame após a conversão
print("\nDataFrame após a conversão:")
print(df)
