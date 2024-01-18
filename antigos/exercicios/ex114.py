from urllib import request, error

try:
    site = request.urlopen('http://www.pudim.com.br')
except error.URLError:
    print('O site Pudim não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso.')
