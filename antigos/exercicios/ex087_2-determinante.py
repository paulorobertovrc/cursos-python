matriz = [[0,0,0], [0,0,0], [0,0,0]]
nova_matriz = matriz[:]
nova_matriz.insert(3, nova_matriz[0])
nova_matriz.insert(4, nova_matriz[1])

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        
determinante = ((matriz[0][0] * matriz[1][1] * matriz[2][2]) + (matriz[0][1] * matriz[1][2] * matriz[2][0]) + (matriz[0][2] * matriz[1][0] * matriz[2][1])) - ((matriz[0][1] * matriz[1][0] * matriz[2][2]) + (matriz[0][0] * matriz[1][2] * matriz[2][1]) + (matriz[0][2] * matriz[1][1] * matriz[2][0]))
print('-=' * 15)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
    print()

print(matriz)
print(nova_matriz)
print(determinante)
