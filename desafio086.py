matriz = []
linha = []
for c in range(0, 3):
    for d in range(0, 3):
        linha.append(int(input(f'Digite o número na posição: [{c}, {d}] ')))
    matriz.append(linha[:])
    linha = []
print('-='*30)
for c in range(0, 3):
    for d in range(0, 3):
        print(f'[{matriz[c][d]:^5}]', end=' ')
    print()

