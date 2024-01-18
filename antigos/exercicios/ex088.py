from random import randint
from time import sleep

print('-' * 15)
print('JOGO NA MEGA SENA')
print('-' * 15)

lista_de_jogos = []
jogos = int(input('Quantos jogos você quer que eu sorteie? '))

print(f'-=-=-= SORTEANDO {jogos} JOGOS =-=-=-')
for jogo in range(0, jogos):
    numeros = []
    for c in range(0, 6):
        while len(numeros) < 6:
            n = randint(1, 60)
            if n not in numeros:
                numeros.append(n)
    lista_de_jogos.append(sorted(numeros[:]))
    print(f'Jogo {jogo + 1}: ', end='')
    print(sorted(numeros))
    sleep(0.7)
print('-=-=-=-=-= < BOA SORTE! > =-=-=-=-=-')
print(lista_de_jogos)