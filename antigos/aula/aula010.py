n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = float((n1 + n2) / 2)

situacao = 0
if media >= 7 :
    situacao = 'Aprovado'
else :
    situacao = 'Reprovado'

print('A sua média foi {:.1f}'.format(media))
print('Situação do aluno: {}'.format(situacao))