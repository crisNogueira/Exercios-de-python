print('='*30)
print('Sequência de Fibonacci')
print('='*30)
n = int(input('Digite um número: '))
a = 0
p = 1
x = 0
print('Os {}° primeiros números da sequencia de fibonacci é:'.format(n))
if n == 0:
    print('zero números!')
else:
    while n != 0:
        if n >= 1:
            print(a, end=' ')
        if n >= 2:
            print(p, end=' ')
        if n >= 3:
            for c in range(2, n):
                x = a + p
                print(x, end=' ')
                a = p
                p = x
        n = 0
print('Fim!')
