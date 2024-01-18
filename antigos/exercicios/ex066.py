num = soma = qtd = 0

while num != 999:
    num = int(input('Digite um número [digite 999 para sair]: '))
    if num == 999:
        break
    soma += num
    qtd += 1

print(f'Foram digitados {qtd} números, cuja soma é {soma}.')