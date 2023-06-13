from random import randint
from time import sleep
cont = numjog = numcomp = soma = p = 0

parimpajog = ''
print('-'*20)
print('Par ou impar')
print('-'*20)
while True:
    parimpajog = str(input('Escolha entre par ou impar: [P/I] ')).strip().upper()[0]
    if parimpajog in 'PpIi':
        while True:
            numjog = int(input('Escolha um número entre 0 e 10: '))
            if numjog >= 0 and numjog <= 10:
                numcomp = randint(0, 10)
                soma = numjog + numcomp
                if soma % 2 == 0 and parimpajog == 'P':
                    cont += 1
                    print(f'Você pediu {parimpajog} e jogou {numjog}')
                    print(f'O computador pediu impar e jogou {numcomp}')
                    print('Parabéns você ganhou')
                    break
                elif soma % 2 != 0 and parimpajog == 'I':
                    cont += 1
                    print(f'Você pediu {parimpajog} e jogou {numjog}')
                    print(f'O computador pediu par e jogou {numcomp}')
                    print('Parabéns você ganhou')
                    break
                else:
                    p += 1
                    print('Você perdeu')
                    break
    if p == 1:
        break
print(f'Você obteve um total de {cont} vitórias')

