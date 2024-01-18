matriz = []

for i in range(0, 3):
    for j in range(0, 3):
        n = int(input(f'Digite um valor para [{i}, {j}]: '))
        matriz.append(n)
    
print('-=' * 20)
for c in range(0, len(matriz)):
    print(f'[{matriz[c]}]', end=' ')
    if (c + 1) % 3 == 0:
        print()
print()
print()
