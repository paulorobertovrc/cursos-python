temp = []
principal = []
maior_peso = menor_peso = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior_peso = menor_peso = temp[1]
    else:
        if temp[1] >= maior_peso:
            maior_peso = temp[1]
        if temp[1] <= menor_peso:
            menor_peso = temp[1]
    principal.append(temp[:])
    temp.clear()

    continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'Nn':
        break

print('-=' * 30)
print()
print(f'Foi/Foram cadastrada(s) {len(principal):.0f} pessoa(s).')
print(f'O maior peso foi de {maior_peso} Kg.')
print('A(s) pessoa(s) mais pesada(s) foi/foram ', end='')
for pessoa in principal:
    if pessoa[1] == maior_peso:
        print(pessoa[0], end=' ')
print(f'\nO menor peso foi de {menor_peso} Kg.')
print('A(s) pessoa(s) mais leve(s) foi/foram ', end='')
for pessoa in principal:
    if pessoa[1] == menor_peso:
        print(pessoa[0], end=' ')
print()
