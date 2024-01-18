numeros = []

for c in range(0, 5):
    n = int(input(f'Digite um valor para a posição {c}: '))
    numeros.append(n)

print('-=' * 10)
print(f'Você digitou os valores {numeros}')
print(f'O maior número digitado foi {max(numeros)} nas posições ', end='')
for i, n in enumerate(numeros):
    if n == max(numeros):
        print(f'{i}... ', end='')
print(f'\nO menor número digitado foi {min(numeros)} nas posições ', end='')
for i, n in enumerate(numeros):
    if n == min(numeros):
        print(f'{i}... ', end='')
print('\n')
