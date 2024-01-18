def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não o cálculo.
        Se False, exibirá apenas o resultado.
    :return: O valor do fatorial de um número qualquer.
    """
    f = 1
    cont = num
    while cont > 0:
        f *= cont
        if show:
            print(f'{cont}', end='')
            if cont != 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        cont -= 1
    print(f)


fatorial(5, show=True)
