aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input('Média: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'aprovado'
elif aluno['média'] >= 5:
    aluno['situação'] = 'recuperação'
else:
    aluno['situação'] = 'reprovado'

for k, v in aluno.items():
    print(f'{k} -> {v}')
