grupo = list()
mulheres = list()
acima_media = list()
pessoa = dict()
continuar = ''
soma_idades = 0

while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F] '))
    while pessoa['sexo'] not in 'MmFf':
        print('ERRO! Por favor, digite apenas M ou F.')
        pessoa['sexo'] = str(input('Sexo: [M/F] '))
    if pessoa['sexo'] in 'Ff':
        mulheres.append(pessoa['nome'])
    pessoa['idade'] = int(input('Idade: '))
    continuar = str(input('Quer continuar? [S/N] '))
    while continuar not in 'SsNn':
        print('ERRO! Por favor, responda apenas S ou N.')
        continuar = str(input('Quer continuar? [S/N] '))
    grupo.append(pessoa.copy())
    if continuar in 'Nn':
        break

print('-=' * 30)
print(grupo)
print(f'A) Ao todo, temos {len(grupo)} pessoas cadastradas.')
for c in range(0, len(grupo)):
    soma_idades += grupo[c]['idade']
print(f'B) A média de idade é de {soma_idades / len(grupo):5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for c in mulheres:
    print(c, end='; ')
print()
for c in range(0, len(grupo)):
    if grupo[c]['idade'] > soma_idades / len(grupo):
        acima_media.append(grupo[c])
print('D) Lista das pessoas que estão acima da média: ')
for c in range(0, len(acima_media)):
    for k, v in acima_media[c].items():
        print(f'{k} = {v}', end='; ')
    print()
print('<< ENCERRADO >>')
print()
