import math

cateto1 = float(input('Informe o cateto x: '))
cateto2 = float(input('Informe o cateto y: '))
hipo = pow(cateto1, 2) + pow(cateto2, 2)

print('O valor da hipotenusa é {}'.format(math.sqrt(hipo)))
print(math.hypot(cateto1, cateto2))
