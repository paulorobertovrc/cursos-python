from time import sleep

def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for n in num:
        print(n, end=' ', flush=True)
        sleep(0.3)
        if maior <= n:
            maior = n
        cont += 1
    print(f'Foram informados {cont} valores.')
    print(f'O maior valor passado foi {maior}.')
    

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
