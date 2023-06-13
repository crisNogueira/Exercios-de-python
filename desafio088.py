from random import randint
from time import sleep
num = int(input('Quantas apostas você deseja fazer: '))
d = 0
aposta = []
x = []
for c in range(0, num):
    for f in range(0, 6):
        if f == 0:
            d = randint(1, 60)
            x.append(d)
        else:
            while True:
                if d in x:
                    d = randint(1, 60)
                else:
                    break
            x.append(d)
    x.sort()
    aposta.append(x[:])
    x = []
print('-='*30)
print(f'A suas {num} apostas são: ')
for c in range(0, num):
    sleep(1)
    print(f'jogo {c+1} {aposta[c]}')



