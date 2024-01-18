from random import randint

print('----- PAR OU ÍMPAR -----')
controle = str(input('PAR OU ÍMPAR? [P/I] ')).strip()
print(controle)
while controle not in 'PpIi':
    print('Opção inválida.')
    controle = str(input('PAR OU ÍMPAR? ')).strip()

vit_pares = 0
vit_impares = 0
vit_jogador = 0
vit_computador = 0

while vit_computador == 0:
    if vit_computador == 1:
        break
    
    jogador = int(input('Digite um número: '))
    computador = randint(0, 10)
    print(computador)

    if (jogador + computador) % 2 == 0:
        vit_pares += 1
    else:
        vit_impares += 1

    if controle == 'P' or controle == 'p':
        vit_jogador = vit_pares
        vit_computador = vit_impares
    else:
        vit_jogador = vit_impares
        vit_computador = vit_pares

print(f'Vitórias consecutivas do jogador: {vit_jogador}')
