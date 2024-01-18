from time import sleep

def menu():
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')

primeiro_numero = int(input('Informe um número inteiro: '))
segundo_numero = int(input('Informe outro número inteiro: '))

opcao = 0

while opcao != 5:
    menu()
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        print('O resultado da expressão {} + {} é igual a {}'.format(primeiro_numero, segundo_numero, primeiro_numero + segundo_numero))
    elif opcao == 2:
        print('O resultado da expressão {} x {} é igual a {}'.format(primeiro_numero, segundo_numero, primeiro_numero * segundo_numero))
    elif opcao == 3:
        if primeiro_numero == segundo_numero:
            print('Os números informados são iguais')
        else:
            maior = primeiro_numero
            menor = segundo_numero
            if segundo_numero > primeiro_numero:
                maior = segundo_numero
                menor = primeiro_numero
            print('O número {} é maior que {}'.format(maior, menor))
    elif opcao == 4:
        print('Informe os números novamente: ')
        primeiro_numero = int(input('Informe um número inteiro: '))
        segundo_numero = int(input('Informe outro número inteiro: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(1)
        print('-=' * 10)
        print('FIM DO PROGRAMA')
    else:
        print('Opção inválida. Tente novamente.')
    