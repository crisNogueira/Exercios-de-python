from random import randint
me = ma = 0
lista = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram:', end=' ')
for n in lista:
    print(f'{n} ', end='')
for c in range(0, 5):
    if c == 0:
       me = lista[c]
       ma = lista[c]
    else:
        if lista[c] < me:
            me = lista[c]
        if lista[c] > ma:
            ma = lista[c]
print(f'\nO maior valor sorteado foi {ma}')
print(f'O menor valor sorteado foi {me}')
