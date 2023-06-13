l = []
lp = []
li = []
op = ' '
while True:
    l.append(int(input('Digite um valor numérico: ')))
    while True:
        op = str(input('Deseja adcionar mais um número: [S/N] ')).strip().upper()
        if op in 'SN':
            break
    if op == 'N':
        break
for c in range(0, len(l)):
    if l[c] % 2 == 0:
        lp.append(l[c])
    else:
        li.append(l[c])
print('-='*30)
print(f'A lista {l} apresenta os seguintes subconjuntos:')
print(f'A lista dos números pares é: {lp}')
print(f'A lista dos números impares é: {li}')
