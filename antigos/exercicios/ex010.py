l = float(input('Informe a largura da parede: '))
a = float(input('Informe a altura da parede: '))
area = l * a
print('A área da parede é igual a {} metros quadrados.'.format(area))
print('Considerando que cada litro de tinta é suficiente para pintar uma área de 2 metros quadrados, serão necessários {} litros para pintar a parede.'.format(area / 2))
