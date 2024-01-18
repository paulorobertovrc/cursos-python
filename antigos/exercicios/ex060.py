numero = int(input('Informe um número: '))
cont = numero
f = 1

print('{}! = '.format(numero), end='')

while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    f *= cont
    cont -= 1

print(f)
