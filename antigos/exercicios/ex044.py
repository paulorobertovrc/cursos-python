print('========== LOJAS GUANABARA ==========')
compras = float(input('Valor das compras: R$ '))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))

if (opcao == 1):
    total = compras * 0.9
    print('Nesta opção, você terá 10% de desconto.')
    print('O total a pagar será de R$ {:.2f}'.format(total))
elif (opcao == 2):
    total = compras * 0.95
    print('Nesta opção, você terá 5% de desconto.')
    print('O total a pagar será de R$ {:.2f}'.format(total))
elif (opcao == 3):
    valor_parcela = compras / 2
    print('Você pode pagar suas compras em 2x sem juros no cartão de crédito.')
    print('Nesta opção, você não terá desconto.')
    print('O valor total da sua compra é de R$ {}, para pagamento em duas parcelas de R$ {:.2f}'.format(compras, valor_parcela))
else:
    parcelas = int(input('Qual é a quantidade de parcelas? '))
    total = compras * 1.2
    valor_parcela = total / parcelas
    print('Para pagamento em {} parcelas, haverá a incidência de 20% de juros.'.format(parcelas))
    print('Nesta opção, o total a pagar será de R$ {}, em {} parcelas de R$ {:.2f}'.format(total, parcelas, valor_parcela))
print('========== LOJAS GUANABARA ==========')
print('Volte sempre!')
