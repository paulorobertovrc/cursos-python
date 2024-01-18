import math

angulo = float(input('Digite o valor do ângulo: '))
print('Ângulo: {} | Seno: {:.2f} | Cosseno: {:.2f} | Tangente: {:.2f}'.format(angulo, math.sin(math.radians(angulo)), math.cos(math.radians(angulo)), math.tan(math.radians(angulo))))
