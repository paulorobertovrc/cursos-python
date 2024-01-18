lista = []

while True:
    num = int(input('Digite um valor: '))
    lista.append(num)

    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar in 'Nn':
        break

print(f'Você digitou {len(lista)} elemento(s)')
print(f'Os valores em ordem decrescente são {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
