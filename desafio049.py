x = int(input('Digite um número: '))
print('A tabuada de {} é:'.format(x))
for c in range(0, 11):
    print('{} x {:2} = {}'.format(x, c, x*c))
