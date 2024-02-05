import os

# Variáveis globais
restaurantes = []

def exibir_menu():
    print('Meu App de Delivery')
    print('-------------------')
    print('[ 1 ] Cadastrar restaurante')
    print('[ 2 ] Listar restaurantes')
    print('[ 3 ] Alternar estado do restaurante')
    print('[ 4 ] Sair')


def escolher_opcao_menu():
    try:
        opcao_menu = int(input('Escolha uma opção >>> '))

        match opcao_menu:
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_estado()
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
    voltar_ao_menu_principal()


def cadastrar_restaurante():
    exibir_subtitulo('Cadastrar restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'\nRestaurante: {nome_do_restaurante.upper()} | Categoria: {categoria.upper()} cadastrado com sucesso!\n')
    voltar_ao_menu_principal()


def listar_restaurantes():
    exibir_subtitulo('Listar restaurantes')

    if len(restaurantes) == 0:
        print('Nenhum restaurante cadastrado\n')
    else:
        for restaurante in restaurantes:
            nome = restaurante['nome']
            categoria = restaurante['categoria']
            estado = 'Ativo' if restaurante['ativo'] else 'Inativo'
            print(f'Nome: {nome} | Categoria: {categoria} | Estado: {estado}')

    voltar_ao_menu_principal()


def alternar_estado():
    exibir_subtitulo('Alternar estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja ativar/desativar: ')

    restaurante_encontrado = False

    for restaurante in restaurantes:
        if restaurante['nome'] == nome_restaurante:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo'] # Inverte o valor booleano do estado atual
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso.' if restaurante['ativo'] \
                else f'O restaurante {nome_restaurante} foi desativado com sucesso.'
            print(mensagem)
            voltar_ao_menu_principal()

    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado.')
        voltar_ao_menu_principal()


def voltar_ao_menu_principal():
    input(print('\nPressione ENTER para voltar ao menu principal...'))
    main()


def exibir_subtitulo(subtitulo):
    os.system('clear')
    print(subtitulo)
    print('-' * len(subtitulo))
    print()


def main():
    os.system('clear')
    exibir_menu()
    escolher_opcao_menu()


if __name__ == '__main__':
    main()
