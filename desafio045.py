import random
lista = ['Pedra', 'Papel', 'Tesoura']
pc = random.choice(lista)
print('\033[33m-=-\033[m'*20)
print('            \033[1;33m JOGO PEDRA PAPEL E TESOURA\033[m')
print('\033[33m-=-\033[m'*20)

print('''\033[33m Escolha uma opção:\033[m
\033[37m [1] Pedra\033[m
\033[30m [2] Papel\033[m
\033[35m [3] Tesoura\033[m''')
y = int(input(' '))

if y == 1:
    eu = 'Pedra'
elif y == 2:
    eu = 'Papel'
elif y == 3:
    eu = 'Tesoura'
else:
    eu = random.choice(lista)

if eu == pc:
    print('Voce escolheu: {}'.format(eu))
    print('O computador escolheu: {}'.format(pc))
    print('\033[1;34m DEU EMPATE\033[m')
elif (eu == 'Pedra' and pc == 'Tesoura') or (eu == 'Tesoura' and pc == 'Papel') or (eu == 'Papel' and pc == 'Pedra'):
    print('Você escolheu: {}'.format(eu))
    print('O computador escolheu: {}'.format(pc))
    print('\033[1;33m PARABÉNS VOCÊ VENCEU\033[m')
else:
    print('Você escolheu: {}'.format(eu))
    print('O computador escolheu: {}'.format(pc))
    print('\033[1;31m VOCÊ PERDEU\033[m')
