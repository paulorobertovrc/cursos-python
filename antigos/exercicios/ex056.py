soma_idades = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ''
mulheres_menos_20 = 0

for p in range(1, 5):
    print('---- {}a PESSOA ----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    
    soma_idades += idade

    if sexo == 'M' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

media_idades = soma_idades / 4

print('--------------------')
print('A média de idade do grupo é de {:.1f}.'.format(media_idades))
print('O homem mais velho tem {} anos e se chama {}.'.format(idade_homem_mais_velho, nome_homem_mais_velho))
print('Ao todo, são {} mulheres com menos de 20 anos de idade.'.format(mulheres_menos_20))

