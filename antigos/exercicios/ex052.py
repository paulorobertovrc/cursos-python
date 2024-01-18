numero = int(input('Digite um número: '))
tot_divisivel = 0

for c in range(1, numero + 1):
    if (numero % c == 0):
        print('\033[33m', end=' ')
        tot_divisivel += 1
    else:
        print('\33[31m', end=' ')
    print('{}'.format(c), end=' ')

print('\n\033[m O número {} foi divisível {} vezes'.format(numero, tot_divisivel), end='')
if (tot_divisivel == 2):
    print(' e por isso é primo.')
else:
    print(' e por isso não é primo.')
    