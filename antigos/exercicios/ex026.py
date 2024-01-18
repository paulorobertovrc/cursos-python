frase = str(input('Digite uma frase: ')).strip().lower()
print('A letra A aparece {} vezes na frase'.format(frase.count('a')))
print('A primeira vez em que aparece é na posição {}'.format(frase.find('a')))
print('A última vez em que aparece é na posição {}'.format(frase.rfind('a')))