import random

def mensagem_abertura():
    print('-=' * 14)
    print('Bem vindo ao jogo de Forca!')
    print('-=' * 14)

def definir_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip().lower()
        palavras.append(linha)
    
    arquivo.close()

    indice = random.randrange(0, len(palavras))
    palavra_secreta = palavras[indice]
    return palavra_secreta

def inicializar_letras_acertadas(palavra):
    return ['_' for letra in palavra]

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \\     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \\|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |      / \\   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar():
    mensagem_abertura()
    palavra_secreta = definir_palavra_secreta()
    letras_acertadas = inicializar_letras_acertadas(palavra_secreta)
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    
    while (not enforcou and not acertou):
        chute = input('Qual letra? ').strip().lower()
        
        if (chute in palavra_secreta):
            index = 0

            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                    print('Encontrei a letra {} na posição {}'.format(chute, index))
                index += 1
        else:
            erros += 1
            desenha_forca(erros)
        
        print(letras_acertadas)
    
        if (erros > 6):
            enforcou = True
            print('Você foi enforcado! A palavra correta era {}.'.format(palavra_secreta))
        
        if ('_' not in letras_acertadas):
            acertou = True
            print('Você venceu!')    
    
    print('Fim do jogo')

if (__name__ == '__main__'):
    jogar()
