palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
vogais = ('AaEeIiOoUu')

for pos in range(0, len(palavras)):
    print(f'\nNa palavra {palavras[pos]} temos ', end='')
    for vogal in vogais:
        if vogal in palavras[pos]:
            print(vogal, end=' ')

print('\n')