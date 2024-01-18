def analisarValores(* num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    if len(num) == 0:
        print('Não foram informados valores.')
    else:
        print(num)
        print(f'Foram informados {len(num)} valores.')
        print(f'O maior valor informado foi {max(num)}')

analisarValores(2, 9, 4, 5, 7, 1)
analisarValores(4, 7, 0)
analisarValores(1, 2)
analisarValores(1)
analisarValores(0)
analisarValores()
