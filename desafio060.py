n = int(input('Digite o valor de um número: '))
if n == 0 or n == 1:
    f = 1
    print('O fatorial de {}!={}.'.format(n, f))
    p = 1
else:
    f = n
    p = n
print('O fatorial de {}!={}x'.format(n, f), end='')
while p != 1:
    f = f * (p-1)
    p -= 1
    print('{}'.format(p), end='')
    if p != 1:
       print('x', end='')
    else:
        print('=', end='')
print('{}'.format(f), end='')


