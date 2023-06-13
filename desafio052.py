x = int(input('Digite um número: '))
y = 0
for c in range(1, x+1):
    if (x % c) == 0:
        y = y + 1
if y == 2:
    print('O número {} é primo.'.format(x))
else:
    print('O número {} NÃO é primo'.format(x))
