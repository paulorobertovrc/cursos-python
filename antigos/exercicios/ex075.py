tupla = (
int(input('Digite um número: ')),
int(input('Digite outro número: ')),
int(input('Digite mais um número: ')),
int(input('Digite o último número: '))
)
pares = 0
lista_pares = []

for numero in tupla:
    if numero % 2 == 0:
        pares += 1
        lista_pares.append(numero)

print(f'Você digitou {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vez/vezes.')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}a posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print(f'Foram digitados {pares} valores pares ({lista_pares})')
