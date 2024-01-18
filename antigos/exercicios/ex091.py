from random import randint
from time import sleep
from operator import itemgetter

jogadores = dict()
ranking = dict()

for c in range(0, 4):
    jogadores[c] = randint(1,6)
    print(f'O jogador {c + 1} tirou {jogadores[c]} no dado')
    sleep(0.5)
ranking = sorted(jogadores.items(), key=itemgetter(1),reverse=True)
print('-=' * 20)
print('== RANKING DOS JOGADORES ==')
for c in range(len(ranking)):
    print(f'{c + 1}o. lugar: jogador {ranking[c][0] + 1} com {ranking[c][1]}.')
    sleep(0.5)
