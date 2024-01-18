def leiaInt(msg):
    while True:
        try:
            n = int(input('Digite um número: '))
        except Exception as e:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            print(e)
        else:
            return n

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
