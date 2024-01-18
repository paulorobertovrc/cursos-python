def calcular_area(l, c):
    area = l * c
    return area


print('Controle de terrenos')
print('-' * 20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
print(f'A área de um terreno {largura} x {comprimento} é igual a {calcular_area(largura, comprimento)} m2.')
