from random import randint
comp = randint(0, 10)
c = 0
print('tente adivinhar num número que pensei')
eu = int(input('Qual é a sua aposta: '))
while eu != comp:
    c += 1
    if eu < comp:
        eu = int(input('Tente novamente, o valor que pensei vale mais: '))
    if eu > comp:
        eu = int(input('Tente novamete, o valor que pensei vale menos: '))
print('Parabéns você acertou o número {} na tentativa {}°.'.format(eu, c+1))

