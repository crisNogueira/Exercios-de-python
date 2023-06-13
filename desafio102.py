from time import sleep


def fatorial(x=1, show=False):
    """
    -> calcula o fatorial de x.
    :param x: É o número a se calculado o fatorial.
    :param show: se for True mostra o processo, caso contrario não.
    """
    f = 1
    for c in range(x, 0, -1):
        f *= c
    print('-'*30)
    if show == True:
        for c in range(x, 1, -1):
            sleep(0.5)
            print(f'{c}', end=' ')
            sleep(0.5)
            print('x', end=' ')
        sleep(0.5)
        print('1', end=' ')
        sleep(0.5)
        print('=', end=' ')
        sleep(0.5)
        print(f'{f}')
    else:
        print(f)


fatorial(5, True)
fatorial(4)
fatorial(show=True)
fatorial()
fatorial(7, False)
