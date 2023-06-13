val = []
for n in range(0, 5):
    val.append(int(input('Digite um valor: ')))
for c, v in enumerate(val):
    print(f'Na posição {c} tenho o número {v}')
val.sort()
print(val)
