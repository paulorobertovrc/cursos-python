soma_pares = 0

for c in range(0, 6):
    num = int(input('Informe um número inteiro: '))
    if num % 2 == 0:
        soma_pares += num

print(soma_pares)
