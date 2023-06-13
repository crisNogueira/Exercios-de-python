lista = []
me = ma = 0
pa = []
pe = []
for c in range(0, 5):
    lista.append(int(input(f'Digite o {c}° número: ')))
for x in range(0, 5):
    if x == 0:
        me = lista[x]
        ma = lista[x]
    else:
        if x > ma:
            ma = lista[x]
        if x < me:
            me = lista[x]
for d in range(0, 5):
    if lista[d] == ma:
        pa.append(d)
    if lista[d] == me:
        pe.append(d)
pa.sort()
pe.sort()
print('-='*30)
print(f'Você digitou os valoes {lista}')
print(f'O maior valor, {ma} está nas posições ', end=' ')
for f in pa:
    print(f'{f}...', end=' ')
print(f'\nO menor valor, {me} está nas posições ', end=' ')
for h in pe:
    print(f'{h}...', end=' ')
