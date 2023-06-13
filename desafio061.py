p = int(input('Digite o valor do primeiro termo: '))
r = int(input('Digite o valor da razão: '))
termo = p
c = 1
print('Os 10 primeiros termos da P.A é: ')
while c != 11:
    print('{}'.format(termo), end='-')
    termo += r
    c += 1
print('fim')
