p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite o valor da razão da PA: '))
print('Os 10 primeiros termos da PA a={}+(n-1){} é:'.format(p, r))
for c in range(p, p+(9*r), r):
    print('{}'.format(c), end='-')
print('ACABOU')




