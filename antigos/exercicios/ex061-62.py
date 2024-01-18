print('Gerador de Progressão Aritmética')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
n1 = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
qtd_termos = int(input('Quantos termos deseja exibir? '))
continuar = True
nx = n1
termo_atual = 1

while continuar:
    while termo_atual <= qtd_termos:
        print('{} -> '.format(nx), end='')
        nx += r
        termo_atual += 1
    print('PAUSA')
    prosseguir = str(input('Deseja prosseguir? [S/N] ')).upper()
    if prosseguir == 'S':
        novos_termos = int(input('Quantos termos adicionais deseja exibir? '))
        qtd_termos += novos_termos
    elif prosseguir == 'N':
        continuar = False
    else:
        print('Opção inválida.')
        prosseguir = str(input('Deseja prosseguir? [S/N] '))

print('A progressão com {} termos foi exibida com sucesso.'.format(termo_atual - 1))
print('FIM')
