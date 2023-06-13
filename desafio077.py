palavra = ('aprender', 'programar', 'linguagem', 'python')
a = e = i = o = u = 0
v = len(palavra)
for c in range(0, v):
    x = len(palavra[c])
    print(f'Na palavra {palavra[c]} temos', end=' ')
    for d in range(0, x):
        if palavra[c][d] == 'a':
            a += 1
        if palavra[c][d] == 'e':
            e += 1
        if palavra[c][d] == 'i':
            i += 1
        if palavra[c][d] == 'o':
            o += 1
        if palavra[c][d] == 'u':
            u += 1
    if a >= 1:
        print('a', end=' ')
    if e >= 1:
        print('e', end=' ')
    if i >= 1:
        print('i', end=' ')
    if o >= 1:
        print('o', end=' ')
    if u >= 1:
        print('u', end=' ')
    a = e = i = o = u = x = 0
    print('\n')