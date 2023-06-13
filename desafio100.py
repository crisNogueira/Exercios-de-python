from time import sleep
from random import randint
def sorteio(lista):
    a = 0
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        a = randint(0, 10)
        sleep(0.5)
        print(f' {a}', end='')
        lista.append(a)
        a = 0
    print(' Pronto!')
def somaPar(lista):
    s = 0
    print(f'Somando os valores pares de {lista}, temos', end='')
    for c in range(0, 5):
        if lista[c] % 2 == 0:
            s += lista[c]
    print(f' {s}')



lista = []
sorteio(lista)
somaPar(lista)
