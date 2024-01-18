jogador = dict()
partidas = 0

jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['gols'] = []
for c in range(0, partidas):
    jogador['gols'].append(int(input(f'Quantos gols na partida {c + 1}? ')))
jogador['total'] = sum(jogador['gols'])
print('-=' * 30)
print(jogador)
print('-=' * 30)
for i, v in jogador.items():
    print(f'O campo {i} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} fez {partidas} partidas.')
for c in range(0, partidas):
    print(f'  => Na partida {c + 1}, fez {jogador["gols"][c]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
