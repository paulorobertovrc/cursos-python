def aumentar(preco=0, taxa=0, formatar=False):
    aumento = preco * taxa / 100
    novo_preco = preco + aumento
    return novo_preco if not formatar else moeda(novo_preco)

def diminuir(preco=0, taxa=0, formatar=False):
    desconto = preco * taxa / 100
    novo_preco = preco - desconto
    return novo_preco if not formatar else moeda(novo_preco)

def dobro(preco=0, formatar=False):
    dobro = preco * 2
    return dobro if not formatar else moeda(dobro)

def metade(preco=0, formatar=False):
    metade = preco / 2
    return metade if not formatar else moeda(metade)

def moeda(preco=0, moeda='R$'):
    return f'{moeda} {preco:.2f}'.replace('.', ',')

def resumo(preco, aumento, desconto):
    print('-' * 35)
    print('RESUMO DO VALOR'.center(35))
    print('-' * 35)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preco, aumento, True)}')
    print(f'{desconto}% de desconto: \t{diminuir(preco, desconto, True)}')
    print('-' * 35)
