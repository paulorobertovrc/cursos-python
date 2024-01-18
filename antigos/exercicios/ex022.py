nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome com todas as letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome com todas as letras minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

separa = nome.split()
print(separa)