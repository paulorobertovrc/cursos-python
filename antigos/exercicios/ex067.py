while True:
    num = int(input('Quer ver a tabuada de qual número? '))
    if num < 0:
        break
    print('-' * 20)
    for c in range (0,11):
        print(f'{num} x {c} = {num * c}')
        c += 1
    print('-' * 20)
print('Programa encerrado')
