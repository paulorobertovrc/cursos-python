import os

def exibir_menu():
    print('Meu App de Delivery')
    print('-------------------')
    print('[ 1 ] Cadastrar Restaurante')
    print('[ 2 ] Listar Restaurantes')
    print('[ 3 ] Ativar Restaurante')
    print('[ 4 ] Sair')


def escolher_opcao_menu():
    try:
        opcao_menu = int(input('Escolha uma opção >>> '))

        match opcao_menu:
            case 1:
                print('Cadastrar Restaurante')
            case 2:
                print('Listar Restaurantes')
            case 3:
                print('Ativar Restaurante')
            case 4:
                finalizar()
            case _:
                opcao_invalida()
    except ValueError:
        opcao_invalida()


def finalizar():
    os.system('clear')
    print('Finalizando o app...\n')


def opcao_invalida():
    print('\nOpção inválida\n')
    input('Pressione qualquer tecla para retornar ao menu principal...')
    main()


def main():
    os.system('clear')
    exibir_menu()
    escolher_opcao_menu()


if __name__ == '__main__':
    main()
