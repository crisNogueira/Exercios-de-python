s = 0
for c in range(1, 500):
    if (c % 2) == 1:
        if (c % 3) == 0:
            s += c
print('A soma dos números impares multiplos de 3 é: {}'.format(s))
