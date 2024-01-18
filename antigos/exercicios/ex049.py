print('-=' * 6)
print('TABUADA 2.0')
print('-=' * 6)

numero = int(input('Informe um número inteiro: '))

for c in range(0, 11):
    print('{} x {:2} = {}'.format(numero, c, numero * c))
print('FIM')
