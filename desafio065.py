op = ''
x = c = s = ma = me = 0
while op != 'N':
    x = int(input('Digite um valor para x: '))
    c += 1
    s = s + x
    if c == 1:
        ma = me = x
    else:
        if x > ma:
            ma = x
        if x < me:
            me = x
    op = str(input('Deseja continuar a digitar? [S/N]: ')).strip().upper()
s = s / c
print('A média dos números é {:.2F}.'.format(s))
print('O maior número é {} e o menor é {}.'.format(ma, me))

