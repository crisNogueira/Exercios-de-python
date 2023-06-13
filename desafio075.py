a = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite o ultimo número: ')))
n = 0
print('Você digitou os valores: ', end='')
for y in a:
    print(f'{y} ', end='')
x = a.count(9)
print(f'\nO valor 9 apareceu {x} vezes')
if 3 in a:
    print(f'O valor 3 apareceu pela primeira vez na {a.index(3)+1}° posição')
else:
    print('O valor 3 não foi digitado')
for c in a:
    if c % 2 == 0:
        n += 1
print(f'Os valores pares digitados foram {n}')

