lista_pares = []
lista_impares = []

while True:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        lista_pares.append(n)
    else:
        lista_impares.append(n)
    continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'Nn':
        break

lista_impares.sort()
lista_pares.sort()

print(f'A lista completa é {lista_pares + lista_impares}')
print(f'A lista de pares é {lista_pares}')
print(f'A lista de ímpares é {lista_impares}')
