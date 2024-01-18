num = 0
soma_numeros = 0
qtd_termos = 0
num = int(input('Digite um número [digite 999 para parar]: '))

while num != 999:
    soma_numeros += num
    qtd_termos += 1
    num = int(input('Digite um número [digite 999 para parar]: '))

print(f'Foram inseridos {qtd_termos} termos, cuja soma é {soma_numeros}.')