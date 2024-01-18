maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input('Peso da {}a pessoa: '.format(c)))
    if peso > maior:
        maior = peso
    if peso < menor or menor == 0:
        menor = peso

print('O maior peso lido foi {:.1f}Kg'.format(maior))
print('O menor peso lido foi {:.1f}Kg'.format(menor))