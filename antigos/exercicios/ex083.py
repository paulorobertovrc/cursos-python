expressao = str(input('Digite uma expressão: '))
cont = 0

for x in expressao:
    if '(' in x:
        cont += 1
    if ')' in x:
        cont += 1

if cont % 2 == 0:
    print('Sua expressão é válida.')
else:
    print('Sua expressão não é válida')
