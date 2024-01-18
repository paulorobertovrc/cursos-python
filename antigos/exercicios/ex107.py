from func import moeda

v = int(input('Digite um valor: '))
p = int(input('Digite o acréscimo/desconto: '))

print(f'A metade de {v} é igual a {moeda.metade(v)}')
print(f'O dobro de {v} é igual a {moeda.dobro(v)}')
print(f'Aumentando {p}%, temos {moeda.aumentar(v, p)}')
print(f'Diminuindo {p}%, temos {moeda.diminuir(v, p)}')
