print('==========================')
print('SIMULADOR DE FINANCIAMENTO')
print('==========================')

valor_do_imovel = float(input('Informe o valor total do imóvel: R$ '))
valor_da_entrada = float(input('Informe o valor da entrada: R$ '))
valor_financiado = valor_do_imovel - valor_da_entrada
renda = float(input('Informe sua renda mensal: R$ '))
quantidade_de_meses = int(input('Informe a quantidade de meses para quitação: '))
valor_da_parcela = valor_financiado / quantidade_de_meses
percentual_comprometimento = (valor_da_parcela / renda) * 100

print('=====================')
print('RESULTADO DA ANÁLISE')
print('=====================')
print('Valor do imóvel: R$ {:.2f} | Valor da entrada: R$ {:.2f} | Valor financiado: R$ {:.2f}'.format(valor_do_imovel, valor_da_entrada, valor_financiado))
print('Condições de pagamento: {} prestações mensais, cada uma no valor de R$ {:.2f}'.format(quantidade_de_meses, valor_da_parcela))
print('O valor da prestação equivale a {:.2f}% da renda informada, de R$ {:.2f}'.format(percentual_comprometimento, renda))

if (percentual_comprometimento > 30):
    print('Infelizmente, o empréstimo não pode ser realizado porque a prestação compromete mais de 30% da renda mensal declarada.')
else:
    print('EMPRÉSTIMO APROVADO.')
