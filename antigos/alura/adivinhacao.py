import random

def jogar():
    numero = random.randint(1, 5)
    print(numero)

    print('-=' * 45)
    print('Bem vindo ao jogo da adivinhação!')
    print('Tente descobrir qual foi o número escolhido pelo computador. Você tem três tentativas.')
    print('-=' * 45)

    print('Qual o nível de dificuldade desejado?')
    print('(1) Fácil | (2) Médio | (3) Difícil')

    tentativas = 0
    nivel = int(input('Defina o nível: '))

    if (nivel == 1):
        tentativas = 3
    elif  (nivel == 2):
        tentativas = 2
    else:
        tentativas = 1

    while tentativas > 0:
        print('Tentativas disponíveis: {}'.format(tentativas))
        palpite = int(input('Digite seu palpite (entre 1 e 5): '))

        if palpite < 1 or palpite > 5:
            print('Seu palpite deve ser um número entre 1 e 5!')
            continue

        if palpite == numero:
            print('Parabéns! Você acertou!')
            tentativas = 0
        else:
            if palpite > numero:
                print('Você errou! O palpite foi maior do que o número sorteado.')
                tentativas -= 1
            elif palpite < numero:
                print('Você errou! O palpite foi menor do que o número sorteado.')
                tentativas -= 1

    print('Fim de jogo!')

if (__name__ == '__main__'):
    jogar()
