num = []
par = []
imp = []
x = 0
for c in range(0, 7):
    x = int(input(f'Digite o valor {c}: '))
    if x % 2 == 0:
        par.append(x)
    else:
        imp.append(x)
num.append(par[:])
num.append(imp[:])
num[0].sort()
num[1].sort()
print('-='*30)
print(f'Os números páres digitados foram: {num[0]}')
print(f'Os números impares digitados foram: {num[1]}')


