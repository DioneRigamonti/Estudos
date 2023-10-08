arquivo_entrada = r"C:\Users\rigam\OneDrive\Área de Trabalho\teste\Contoso - Promocoes.csv"
arquivo_saida = r"C:\Users\rigam\OneDrive\Área de Trabalho\teste\Contoso - Promocoes_sem_duplicatas_ordenado.csv"

# Lista para armazenar o cabeçalho
cabecalho = ""

# Lista para armazenar as linhas únicas
linhas_unicas = []

# Le o cabeçalho
with open(arquivo_entrada, 'r', encoding='utf-8-sig') as arq_entrada:
    cabecalho = arq_entrada.readline()

# Le o restante do arquivo e adicione as linhas únicas à lista
with open(arquivo_entrada, 'r', encoding='utf-8-sig') as arq_entrada:
    # Pula o cabeçalho ao iterar pelas linhas
    next(arq_entrada)
    for linha in arq_entrada:
        linhas_unicas.append(linha)

# Remove as duplicatas mantendo apenas a primeira ocorrência de cada linha
linhas_unicas = list(set(linhas_unicas))

# Ordena as linhas pelo valor numérico da primeira coluna (ID)
linhas_ordenadas = sorted(linhas_unicas, key=lambda x: int(x.split(';')[0]))

# Escreve o cabeçalho e as linhas ordenadas no arquivo de saída
with open(arquivo_saida, 'w', encoding='utf-8-sig') as arq_saida:
    arq_saida.write(cabecalho)
    for linha in linhas_ordenadas:
        arq_saida.write(linha)


print('fim')