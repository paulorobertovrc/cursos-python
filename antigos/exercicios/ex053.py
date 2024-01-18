frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
tudo_junto = ''.join(palavras)
inverso = ''

for letra in range(len(tudo_junto) - 1, -1, -1):
    inverso += tudo_junto[letra]

print('O inverso de {} é {}.'.format(tudo_junto, inverso))
if (inverso == tudo_junto):
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
