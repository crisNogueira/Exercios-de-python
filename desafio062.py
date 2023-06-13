p = int(input('Digite o valor do 1° termo: '))
r = int(input('Digite o valor da razão: '))
termo = p
x = 0
d = 1
t = 10
c = 1
n = 10
while c != 0:
    for n in range(d, d+t):
       print('{} '.format(termo), end='')
       termo += r
    d = d + t
    print('\n')
    x = int(input('quantos termos você quer mostrar a mais? '))
    t = x
    if x != 0:
        n += 1
    else:
        c = 0
print('O programa termina mostrando {} termos.'.format(n))
