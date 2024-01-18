n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, o produto é {} e a divisão é {}.'.format(s,m,d))
print('===========================================================')
print('A divisão inteira é {}.'.format(di))
print('{} elevado a {} é igual a {}.'.format(n1,n2,e))