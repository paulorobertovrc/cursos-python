cores = {
    'sem_cor': '\033[m',
    'vermelho': '\033[0;30;41m',
    'verde': '\033[0;30;42m',
    'amarelo': '\033[0;30;43m',
    'azul': '\033[0;30;44m',
    'roxo': '\033[0;30;45m',
    'branco': '\033[7;30m'

}

def ajuda(comando):
    titulo(f'Acessando o manual do comando \"{comando}\"', 'azul')
    print(cores['branco'], end='')
    help(comando)
    print(cores['sem_cor'], end='')

def titulo(msg, cor=cores.keys()):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(cores['sem_cor'], end='')


# Programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 'verde')
    comando = str(input('Função ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 'vermelho')