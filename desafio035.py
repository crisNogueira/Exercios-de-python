"""Minha versão"""

"""import math
x = float(input('Digite um lado do triângulo: '))
y = float(input('Digite outro lado do triângulo: '))
z = float(input('Digite o ultimo lado do triângulo: '))

dif = abs(x - z)
som = abs(x + z)

if y > dif:
    if y < som:
        print('Com os lados {}, {} e {} pode se fazer um triângulo.'.format(x, y, z))
    else:
        print('Com os lados {}, {} e {} não e pode fazer um triângulo.'.format(x, y, z))
else:
    print('Com os lados {}, {} e {} não se pode fazer um triângulo.'.format(x, y, z))"""

"""Resolução:"""

print('\033[35m-=-\033[m'*20)
print('\033[4;35mAnalisador de triângulo\033[m')
print('\033[35m-=-\033[m'*20)
r1 = float(input('\033[33mPrimeiro seguimento: \033[m'))
r2 = float(input('\033[34mSegundo seguimento: \033[m'))
r3 = float(input('\033[32mTerceiro seguimento: \033[m'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os seguimentos acima \033[1;33mPODEM FORMAR triângulos\033[m')
else:
    print('Os seguimentos acima \033[1;31mNÃO PODEM FORMAR triângulo\033[m')


