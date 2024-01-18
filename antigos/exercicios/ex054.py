from datetime import date

ano_atual = date.today().year
maiores = 0
maiores_array = []
menores = 0
menores_array = []
idades = []

for c in range(1, 8):
    pessoa = int(input('Em que ano nasceu a {}a pessoa? '.format(c)))
    idade = ano_atual - pessoa
    idades.append(idade)
    if (ano_atual - pessoa < 18):
        menores_array.append(pessoa)
        menores += 1
    else:
        maiores_array.append(pessoa)
        maiores += 1

print('MAIORES: {} {}| MENORES: {} {}'.format(maiores, maiores_array, menores, menores_array))
print(idades)
