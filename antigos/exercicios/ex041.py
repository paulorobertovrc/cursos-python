from datetime import date

nasc = int(input('Informe o ano do seu nascimento: '))
atual = date.today().year
idade = atual - nasc

print('O atleta tem {} anos de idade.'.format(idade))

if (idade <= 9):
    categoria = 'MIRIM'
elif (idade <= 14):
    categoria = 'INFANTIL'
elif (idade <= 19):
    categoria = 'JÚNIOR'
elif (idade <= 25):
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'

print('Categoria: {}'.format(categoria))