lista = []
while True:
    n = int(input('Digite um valor: '))
    while n in lista:
        print('Valor duplicado! Não vou adicionar.')
        n = int(input('Digite um valor: '))
    lista.append(n)
    print('Valor adicionado com sucesso...')
    cont = str(input('Quer continuar? [S/N] ').upper())
    if cont == 'N':
        break
print('-=' * 15)
lista.sort()
print(lista)
