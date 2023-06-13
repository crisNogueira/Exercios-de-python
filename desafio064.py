n = s = c = 0
while n!= 999:
    n = int(input('Digite um valor: '))
    if n != 999:
        s = s + n
        c += 1
print('Foram digitados {} números cuja a soma é {}'.format(c, s))

