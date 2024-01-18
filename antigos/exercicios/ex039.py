from datetime import date

nascimento = int(input('Informe o ano do seu nascimento: '))
atual = date.today().year
idade = atual - nascimento

print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, atual))

if (idade == 18):
    print('Você deve se alistar IMEDIATAMENTE!')
elif (idade < 18):
    saldo = 18 - idade
    alist = nascimento + 18
    print('Você ainda não tem 18 anos. Faltam {} anos para o alistamento.'.format(saldo))
    print('Seu alistamento será em {}'.format(alist))
elif (idade > 18):
    saldo = idade - 18
    alist = nascimento + 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    print('Seu alistamento foi em {}.'.format(alist))