n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
media = (n1 + n2) / 2
print('Tirndo {} e {}, a média do aluno é {}.'.format(n1, n2, media))

if (media < 5):
    print('O aluno está REPROVADO.')
elif (media < 7):
    print('O aluno está em RECUPERAÇÃO.')
else:
    print('O aluno está APROVADO.')