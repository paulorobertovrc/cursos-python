maior_18 = 0
homens = 0
mulher_menos_20 = 0

while True:
    print('-------------------')
    print('CADASTRE UMA PESSOA')
    print('-------------------')
    
    idade = int(input('Idade: '))
    while idade < 0:
        print('Opção inválida.')
        idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'FM':
        print('Opção inválida.')
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        maior_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher_menos_20 += 1
    print('-------------------')
    continuar = str(input('Quer continuar? [S/N] '))
    while continuar not in 'SsNn':
        print('Opção inválida')
        continuar = str(input('Quer continuar? [S/N] '))
    if continuar == 'N' or continuar == 'n':
        break
print(f'''Total de pessoas com mais de 18 anos: {maior_18}
Ao todo, temos {homens} pessoa(s) do sexo masculino e {mulher_menos_20} mulher(es) com menos de 20 anos.''')
