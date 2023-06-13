cads = []
lista = []
op = ' '
ma = me = 0
while True:
    cads.append(str(input('Digite o nome: ')))
    cads.append(float(input('Digite o seu peso: ')))
    lista.append(cads[:])
    cads = []
    while True:
        op = str(input('Deseja cadastra mais uma pessoa? [S/N] ')).strip().upper()
        if op in 'NS':
            break
    if op == 'N':
        break
print('-='*30)
print(f'No total foram cadastrados {len(lista)} pessoas')
for c in range(0, len(lista)):
    if c == 0:
       ma = lista[c][1]
       me = lista[c][1]
    else:
       if lista[c][1] > ma:
           ma = lista[c][1]
       if lista[c][1] < me:
           me = lista[c][1]
print(f'O maior peso foi de {ma}kg e são das pessoas ', end='')
for p in lista:
    if p[1] == ma:
        print(f'[{p[0]}]', end='')
print(f'O menor peso foi de {me}kg e são das pessoas ', end='')
for p in lista:
    if p[1] == me:
        print(f'[{p[0]}]', end='')






