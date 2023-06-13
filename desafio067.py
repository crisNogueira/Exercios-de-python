n = v = 0
print('='*20)
print('Desafio 067 Tabuada')
print('='*20)
while True:
    n = int(input('Digite um valor para qual que saber a tabuada: '))
    if n >= 0:
        print('-'*30)
        print(f'A tabuada do número {n} é:')
        print('-'*30)
        for c in range(0, 11):
            v = c * n
            print(f'{n}x{c}={v}')
        print('-'*20)
    else:
        print('Fim do programa')
        break
