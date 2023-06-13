s = 0
for c in range(1, 7):
    x = int(input('Digite um número: '))
    if (x % 2) == 0:
        s += x
print('A soma dos números pares é {}.'.format(s))
