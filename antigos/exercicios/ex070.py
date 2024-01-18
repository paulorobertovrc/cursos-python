print('--------------------------------------')
print('{: ^40}'.format(' LOJA SUPER BARATÃO '))
print('--------------------------------------')

total = mais_mil = mais_barato = 0
nome_mais_barato = ''

while True:
    produto = str(input('Nome do produto: ')).strip().capitalize()
    preco = float(input('Preço: R$ '))
    total += preco
    if preco > 1000:
        mais_mil += 1
    if mais_barato == 0 or preco < mais_barato:
        mais_barato = preco
        nome_mais_barato = produto
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar not in 'SN':
        print('Opção inválida.')
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
    else:
        print('**********')

print('-------- FIM DO PROGRAMA --------')
print(f'O total da compra foi R$ {total:.2f}')
print(f'{mais_mil} produto(s) custa(m) mais de R$ 1.000,00')
print(f'O produto mais barato foi o/a {nome_mais_barato}, custando R$ {mais_barato:.2f}')
