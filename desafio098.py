from time import sleep
def contador(a, b, c):
    d = a
    print('-='*30)
    print(f'Contagem de {a} ate {b} de {c} em {c}')
    if c < 0:
        c = c * (-1)
    if c == 0:
        c = 1
    if a < b:
        while d <= b:
            sleep(0.5)
            print(f' {d}', end='')
            d += c
        print(' FIM!')
    if a > b:
        while d >= b:
            sleep(0.5)
            print(f' {d}', end='')
            d -= c
        print(' FIM!')


x = y = z = 0
contador(1, 10, 1)
contador(10, 0, 2)
print('-='*30)
print('Agora é a sua vez de personalizar a contagem')
x = int(input('Início: '))
y = int(input('Fim: '))
z = int(input('Passo: '))
contador(x, y, z)
