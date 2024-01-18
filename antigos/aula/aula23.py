try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as e:
    print('Oops... Infelizmente, tivemos um problema =(')
    print(e)
else:
    print(f'O resultado encontrado foi {r:.1f}')
finally:
    print('<< PROGRAMA ENCERRADO >>')
    