from func.ex115.interface import *
from func.ex115.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Cadastrar pessoas', 'Listar pessoas', 'Sair do sistema'])
    if resposta == 1:
        # Cadastrar uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 2:
        # Listar o conteúdo de um arquivo
        cabecalho('PESSOAS CADASTRADAS')
        lerArquivo(arq)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(1)
