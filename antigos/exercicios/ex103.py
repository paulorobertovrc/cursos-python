def exibir(nome, gols):    
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s).')


nome = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
exibir(nome, gols)
