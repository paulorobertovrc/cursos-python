import random

aluno1 = str(input('Aluno 1: '))
aluno2 = str(input('Aluno 2: '))
aluno3 = str(input('Aluno 3: '))
aluno4 = str(input('Aluno 4: '))

lista = [aluno1, aluno2, aluno3, aluno4]

sorteado = random.randint(1, 4)

'''print('O sorteado foi o aluno {}, {}'.format(sorteado, lista[sorteado - 1]))'''

print(random.choice(lista))
