matriz = []
linha = []
par = so = ma = 0
for c in range(0, 3):
    for d in range(0, 3):
        linha.append(int(input(f'Digite o número na posição: {c} {d} ')))
        if linha[d] % 2 == 0:
            par = par + linha[d]
        if d == 2:
            so = so + linha[d]
    matriz.append(linha[:])
    if c == 1:
        for e in range(0, 3):
            if e == 0:
                ma = linha[e]
            else:
                if linha[e] > ma:
                    ma = linha[e]

    linha = []
print('-='*30)
for c in range(0, 3):
    for d in range(0, 3):
        print(f'[{matriz[c][d]:^5}]', end=' ')
    print()
print(f'A soma dos valores páres é: {par}')
print(f'A soma dos valores da 3° coluna é {so}')
print(f'O maior valor da 2° linha é {ma}')


