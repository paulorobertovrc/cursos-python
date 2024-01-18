def leiaInt():
    n = str(input('Digite um número: '))
    while True:
        if n.isnumeric():
            return n
        else:
            print('ERRO! Digite um número inteiro válido.')
            n = str(input('Digite um número: '))


n = leiaInt()
print(f'Você acabou de digitar o número {n}')
