from time import sleep

def contar(inicio, fim, passo):
    if inicio < fim:
        for c in range(inicio, fim + passo, passo):
            print(c, end=' ', flush=True)
            sleep(0.5)
        print('FIM!')
    else:
        for c in range(inicio, fim - passo, -passo):
            print(c, end=' ', flush=True)
            sleep(0.5)
        print('FIM!')

print('-=' * 30)
print('Contagem de 1 até 10 de 1 em 1')
for c in range(1, 11):
    print(c, end=' ', flush=True)
    sleep(0.5)
print('FIM!')
print('-=' * 30)
print('Contagem de 10 até 0 de 2 em 2')
for c in range(10, -2, -2):
    print(c, end=' ', flush=True)
    sleep(0.5)
print('FIM!')
print('-=' * 30)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
print('-=' * 30)
if passo == 0:
    passo = 1
    print('O passo não pode ser igual a zero, portanto, foi automaticamente substituído por 1')
print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')
contar(inicio, fim, abs(passo))
