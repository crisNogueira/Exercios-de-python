n50 = n20 = n10 = n1 = 0
c = 1
print('-=-'*30)
print('                                   Banco Central')
print('-=-'*30)
print('                                   Notas disponíveis')
print('                          \033[31m R$50.00\033[m, \033[33m R$20.00\033[m, \033[35m R$10.00\033[m e \033[32mR$1.00\033[m')
valor = int(input('Digite o valor do seu saque R$ '))
saque = valor
while True:
    if (c * 50) <= valor:
        n50 += 1
        c += 1
    else:
        valor -= n50 * 50
        c = 1
        break
while True:
    if (c * 20) <= valor:
        n20 += 1
        c += 1
    else:
        valor -= n20 * 20
        c = 1
        break
while True:
    if (c * 10) <= valor:
        n10 += 1
        c += 1
    else:
        valor -= n10 * 10
        c = 1
        break
while True:
    if (c * 1) <= valor:
        n1 += 1
        c += 1
    else:
        valor -= n1 * 1
        c = 1
        break
print(f'A quantidade de notas do saque de {saque} será')
if n50 != 0:
    print(f'{n50} x \033[31m R$50.00\033[m', end=' ')
if n20 != 0:
    print(f'{n20} x \033[33m R$20.00\033[m', end=' ')
if n10 != 0:
    print(f'{n10} x \033[35m R$10.00\033[m', end=' ')
if n1 != 0:
    print(f'{n1} x \033[32m R$1.00\033[m', end=' ')


