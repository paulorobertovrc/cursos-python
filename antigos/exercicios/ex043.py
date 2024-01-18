peso = float(input('Informe seu peso (Kg): '))
altura = float(input('Informe sua altura (m): '))
imc = peso / (altura ** 2)

if imc < 18.5:
    resultado = 'abaixo do peso'
elif imc < 25:
    resultado = 'peso ideal'
elif imc < 30:
    resultado = 'sobrepeso'
elif imc < 40:
    resultado = 'obesidade'
else:
    resultado = 'obesidade mórbida'

print('Para o peso e altura informados ({} kg e {} m), o Índice de Massa Corpórea (IMC) é {:.1f}.'.format(peso, altura, imc))
print('Seu resultado é {}.'.format(resultado))