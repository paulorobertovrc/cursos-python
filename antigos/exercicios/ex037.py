numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
opcao = int(input('Sua opçãO: '))

if (opcao == 1):
    print('{} convertido para BINÁRIO é igual a {}'.format(numero, bin(numero)[2:]))
elif (opcao == 2):
    print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)[2:]))
elif (opcao == 3):
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida. Tente novamente.')