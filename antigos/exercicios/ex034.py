salario = float(input('Digite o salário do funcionário: '))

if salario > 1250:
    salario *= 1.1
else:
    salario *= 1.15

print('O novo salário do funcionário será de {:.2f}'.format(salario))
