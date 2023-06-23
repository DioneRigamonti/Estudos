import pandas as pd

# - - - Caminhos - - - #
arquivo_principal = r'caminho\arquivo.xlsx'
nome_sheet = 'nome da sheet'
arquivo_final = r'caminho\arquivo.csv'

def processo(arquivo_principal, nome_sheet, arquivo_final):
    # - - - definindo os types - - - #
    schema = {
        'Coluna_01': str,
        'Coluna_02': int,
        'Coluna_03':float}
    # - - - Lendo o arquivo e passando o schema - - - #
    df = pd.read_excel(arquivo_principal, sheet_name= nome_sheet, dtype=schema)
    # - - - convertendo a sheet em um arquivo csv - - - #
    df.to_csv(arquivo_final, index=False, sep=';', encoding='utf-8-sig')

processo(arquivo_principal=arquivo_principal, nome_sheet=nome_sheet, arquivo_final=arquivo_final)