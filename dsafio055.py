ma = 0
me = 0
for c in range(0, 5):
    y = float(input('Digite o valor do seu peso: kg'))
    if c == 0:
        ma = y
        me = y
    else:
        if y > ma:
            ma = y
        if y < me:
            me = y
print('O maior é {} e o menor é {}'.format(ma, me))


