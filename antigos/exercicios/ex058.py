from random import randint

numero = randint(0, 10)
print(numero)

print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10. Você consegue adivinhar qual foi?')

palpite = int(input('Qual é o seu palpite? '))
tentativas = 0

while palpite != numero:
    if palpite < numero:
        print('Mais... Tente mais uma vez.')
    else:
        print('Menos... Tente mais uma vez.')
    tentativas += 1
    palpite = int(input('Qual é o seu palpite? '))

print('Acertou com {} tentativas. Parabéns!'.format(tentativas))
