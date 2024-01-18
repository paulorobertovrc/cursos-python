num = maior = menor = soma = termos = 0
continuar = True

while continuar:
    num = int(input('Digite um número: '))
    soma += num
    termos += 1
    if termos == 1:
        maior = menor = num
    else:
        if num < menor:
            menor = num
        if num > maior:
            maior = num
    
    if str(input('Deseja continuar? [S/N]: ')).strip().upper()[0] == 'N':
        continuar = False

media = soma / termos
print('Você digitou {} números, cuja soma é {}. A média entre eles é {:.2f}.'.format(termos, soma, media))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
