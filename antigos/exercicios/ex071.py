print('-=-=-=-=-=-=-=-=')
print('CAIXA ELETRÔNICO')
print('-=-=-=-=-=-=-=-=')

print('Cédulas disponíveis: R$ 100 | R$ 50 | R$ 20 | R$ 10 | R$ 5 | R$ 2 | R$ 1')
valor = int(input('Qual valor você quer sacar? R$ '))
total = valor
valor_cedula = 100
total_cedula = 0

while True:
    #if valor % 2 != 0:
    #    print('O valor sacado deve ser múltiplo de 2')
    #    valor = int(input('Qual valor você quer sacar? R$ '))
    if total >= valor_cedula:
        total -= valor_cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cédulas de R$ {valor_cedula}')
        if valor_cedula == 100:
            valor_cedula = 50
        elif valor_cedula == 50:
            valor_cedula = 20
        elif valor_cedula == 20:
            valor_cedula = 10
        elif valor_cedula == 10:
            valor_cedula = 5
        elif valor_cedula == 5:
            valor_cedula = 2
        elif valor_cedula == 2:
            valor_cedula = 1
        total_cedula = 0
        if total == 0:
            break