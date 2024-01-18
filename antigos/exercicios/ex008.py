import os

n = int(input('Insira um número: '))
os.system('clear')

print('=====TABUADA=====')
print('O número informado foi {}.'.format(n))

i = 0
while i <= 10:
    print('{} * {:2} = {}'.format(n,i,n * i))
    i+=1
