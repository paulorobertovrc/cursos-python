dist = float(input('Qual a distância a ser percorrida: '))

tarifa = 0
preco_por_km = 0

if dist <= 200:
    preco_por_km = 0.5
else:
    preco_por_km = 0.45

tarifa = dist * preco_por_km

print('Para uma viagem de {} km, o valor da tarifa será de R$ {:.2f}, sendo considerado R$ {:.2f} por quilômetro rodado'.format(dist, tarifa, preco_por_km))
