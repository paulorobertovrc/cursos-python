print('====================')
print('10 TERMOS DE UMA PA')
print('====================')

n1  = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo_termo = n1 + (10 - 1) * r

for c in range(n1, decimo_termo + r, r):
    print(c, end=" -> ")

print('FIM')