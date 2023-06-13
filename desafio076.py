lista = ('bala', 0.5,
         'pirulito', 1.25,
         'chiclete', 0.45)
n = 34
d = 0
x = len(lista)
print('_'*40)
print(f'{"Lista de preços":^40}')
print('_'*40)
for c in range(0, x):
    if c % 2 == 0:
        print(f'{lista[c]:.<30}', end='')
    else:
        print(f'R${lista[c]:>7.2f}')
print('_'*40)

