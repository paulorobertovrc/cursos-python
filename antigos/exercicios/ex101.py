def votar(nasc):
    from datetime import date

    idade = date.today().year - nasc
    if idade > 65 or (idade >= 16 and idade < 18):
        voto = 'VOTO FACULTATIVO'
    elif idade >= 18:
        voto = 'VOTO OBRIGATÓRIO'
    else:
        voto = 'NÃO PODE VOTAR'
    
    return print(f'Para pessoas nascidas em {nasc}, com {idade} anos de idade, a situação eleitoral é: {voto}')

while True:
    nasc = int(input('Qual o ano de seu nascimento? (Digite 999 para sair) '))
    if nasc == 999:
        break
    votar(nasc)

print('<< PROGRAMA ENCERRADO >>')
