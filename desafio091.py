from random import randint
from time import sleep
jo = {}
ordem = []
colocação = []
jo['1'] = randint(1, 6)
jo['2'] = randint(1, 6)
jo['3'] = randint(1, 6)
jo['4'] = randint(1, 6)
print('-=-'*30)
for c, j in jo.items():
    sleep(1)
    print(f'O jogador {c} tirou: {j}')
print('-=-'*30)
for i in sorted(jo, key=jo.get, reverse=True):
    ordem.append(i)
    ordem.append(jo[i])
    colocação.append(ordem)
    ordem = []
for i in range(0, 4):
    sleep(1)
    print(f'  {i+1}° foi o jogador {colocação[i][0]} que tirou {colocação[i][1]}')
