sexo = str(input('Sexo [M/F]: ')).upper()[0].strip()

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválidos. Por favor, utilize M ou F: ')).upper()[0].strip()

print(sexo)
print('FIM')