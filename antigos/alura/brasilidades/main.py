import requests
from Acesso_cep import BuscaEndereco

#r = requests.get('https://viacep.com.br/ws/79022340/json')
#print(r.text)

cep = '79022340'
objeto_cep = BuscaEndereco(cep)
cep, logradouro, complemento, bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(cep, bairro, cidade, uf)