from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)

print('Suas opções: ')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')

jogador = int(input('Qual é a sua jogada? '))
if jogador > 2:
    print('Opção inválida. Tente novamente.')
    exit()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('-=' * 15)
print('Você escolheu {}'.format(itens[jogador]))
print('O computador escolheu {}'.format(itens[computador]))
print('-=' * 15)

if computador == 0: #PEDRA
    if jogador == 0: #PEDRA
        print('EMPATE')
    elif jogador == 1: #PAPEL
        print('JOGADOR VENCE')
    elif jogador == 2: #TESOURA
        print('COMPUTADOR VENCE')
elif computador == 1: #PAPEL
    if jogador == 0: #PEDRA
        print('COMPUTADOR VENCE')
    elif jogador == 1: #PAPEL
        print('EMPATE')
    elif jogador == 2: #TESOURA
        print('JOGADOR VENCE')
elif computador == 2: #TESOURA
    if jogador == 0: #PEDRA
        print('JOGADOR VENCE')
    elif jogador == 1: #PAPEL
        print('COMPUTADOR VENCE')
    elif jogador == 2: #TESOURA
        print('EMPATE')
