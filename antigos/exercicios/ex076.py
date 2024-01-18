listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

for x in listagem:
    if listagem.index(x) % 2 == 0:
        print(f'{x:.<30}', end='')
    else:
        print(f'R$ {x:>6.2f}')

print('-' * 40)
