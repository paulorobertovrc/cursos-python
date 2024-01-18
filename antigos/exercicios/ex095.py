time = list()
jogador = dict()
gols = list()

while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, jogador['partidas']):
        gols.append(int(input(f'     Quantos gols na partida {c + 1}? ')))
        jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        continuar = str(input('Deseja continuar? [S/N]: '))
        if continuar in 'SsNn':
            break
        print('ERRO! Responda apenas Sim ou Não.')
    if continuar in 'Nn':
        break

print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 60)

while True:
    resp = int(input('Mostrar dados de qual jogador? (999 para sair) '))
    if resp == 999:
        break
    if resp < 0 or resp >= len(time):
        print(f'ERRO! Não existe jogador com código {resp}')
    else:
        print(f'  -- LEVANTAMENTO DO JOGADOR {time[resp]["nome"]}')
        for k, v in enumerate(time[resp]['gols']):
            print(f'      Na partida {k + 1} fez {v} gol(s).')
        print('-' * 60)

print('<< PROGRAMA FINALIZADO >>')
