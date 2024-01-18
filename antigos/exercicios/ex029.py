v = float(input('Informe a velocidade do veículo: '))
print('Velocidade registrada: {} km/h' . format(v))

if v > 80:
    print('Você foi multado!')
    print('Calculando o valor da multa...')
    v_ex = v - 80
    multa = v_ex * 7
    print('O valor da multa é de R$ {:.2f}'.format(multa))
else:
    print('Pode seguir viagem. Dirija com atenção.')