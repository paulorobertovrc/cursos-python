from random import randint
from time import sleep

def sortear(qtd):
    lista = []
    print(f'Sorteando {qtd} números: ', end='')
    for c in range (0, qtd):
        c = randint(0, 10)
        print(c, end=' ', flush=True)
        sleep(0.3)
        lista.append(c)
    print('PRONTO!')
    
    return lista

def somarPares(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'A soma dos números pares é igual a {soma}.')


somarPares(sortear(5))
