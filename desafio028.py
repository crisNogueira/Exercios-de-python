#minha versão:

#import random
#x = random.randint(0, 5)
#print('Tente adivinhar o que o computador está pensando!!')
#y = int(input('Digite um número de 0 a 5: '))
#if x == y:
#    print('PARABÉNS VOCÊ ACERTOU!!!')
#    print('O número pensando foi {}.'.format(y))
#else:
#    print('Que pena você errou.')
#    print('O numero pensado foi: {}.'.format(x))

# correção:

from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5!!!')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(4)
if jogador == computador:
    print('PARABÉNS você conseguiu me vencer')
else:
    print('Eu ganhei, pensei no número {} e vc no número {}.'.format(computador, jogador))
