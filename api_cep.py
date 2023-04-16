import requests
import json

try:
    cep = input('Digite seu cep: ')
    cep_req = requests.get(f'https://cep.awesomeapi.com.br/json/{cep}')
    cep_dict = cep_req.json()

    print(f"Endereço: {cep_dict['address']}")
    print(f"Bairro: {cep_dict['district']}")
    print(f"Estado: {cep_dict['state']}")
    print(f"Cidade: {cep_dict['city']}")
    print(f"IBGE: {cep_dict['city_ibge']}")

except:
    print('Numero de CEP invalido')

print('Fim')