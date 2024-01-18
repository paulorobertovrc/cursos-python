matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma_pares = soma_terceira_coluna = maior_valor_segunda_coluna = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
        if matriz[l][2]:
            soma_terceira_coluna += matriz[l][2]
        if matriz[1][c]:
            if maior_valor_segunda_coluna == 0:
                maior_valor_segunda_coluna = matriz[1][c]
            else:
                if maior_valor_segunda_coluna < matriz[1][c]:
                    maior_valor_segunda_coluna = matriz[1][c]

print('-=' * 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
    print()
print('-=' * 20)
print(f'A soma dos valores pares é {soma_pares}')
print(f'A soma dos valores da teceira coluna é {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é {maior_valor_segunda_coluna}')
