turma = list()

while True:
    aluno = list()
    aluno.append(str(input('Nome: ')).strip())
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    turma.append(aluno[:])
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break

print('-=' * 20)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 25)
for i, c in enumerate(turma):
    print(f'{i:<4}{c[0]:<10}{(c[1] + c[2]) / 2:>8.1f}')
print('-' * 25)
while True:
    mostrar_notas = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if mostrar_notas == 999:
        print('FINALIZANDO...')
        break
    if mostrar_notas <= len(turma) - 1:
        print(f'As notas de {turma[mostrar_notas][0]} são [{turma[mostrar_notas][1]}, {turma[mostrar_notas][2]}]')
        print('-' * 20)
    else:
        print('Opção inválida. Por favor, tente novamente.')
print('<<< Obrigado por utilizar nosso sistema >>>')
