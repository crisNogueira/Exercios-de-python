# minha versão:

# x = int(input('Digite o valor do 1° número: '))
# y = int(input('Digite o valor do 2° número: '))
# z = int(input('Digite o valor do 3° número: '))
# cx = 0
# cy = 0
# cz = 0
# ma = 0
# me = 0
# if x >= y:
#    cx = cx+1
# else:
#    cy = cy+1
# if x >= z:
#    cx = cx+1
# else:
#    cz = cz+1
# if y >= z:
#    cy = cy+1
# else:
#    cz = cz+1
# if cx == 2:
#    ma = ma + x
# if cy == 2:
#    ma = ma + y
# if cz == 2:
#    ma = ma + z
# if cx == 0:
#    me = me + x
# if cy == 0:
#    me = me + y
# if cz == 0:
#    me = me + z
# if x == y == z:
#    print('Os três números são iguais a {}.'.format(x))
# else:
#    print('O maior número é: {} \nO menor número é: {}'.format(ma, me))

"""Resolução:"""

a = int(input('\033[1;34mPrimeiro valor: \033[m'))
b = int(input('\033[1;34mSegundo valor: \033[m'))
c = int(input('\033[1;34mTerceiro valor: \033[m'))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior número é o \033[1;32m{}\033[m.'.format(maior))
print('O menor número é o \033[1;32m{}\033[m.'.format(menor))
