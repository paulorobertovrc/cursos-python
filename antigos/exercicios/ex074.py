from random import randint

valores = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram ', end='')
for valor in valores:
    print(valor, end=' ')
valores_sorted = sorted(valores)
print(f'\nO maior valor sorteado foi {valores_sorted[3]} e o menor valor sorteado foi {valores_sorted[0]}')
