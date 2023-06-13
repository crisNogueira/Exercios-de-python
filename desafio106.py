from time import sleep

c = ['\033[m',
     '\033[0;30;41m',
     '\033[0;30;42m',
     '\033[0;30;44m',
     '\033[0;7;40m',
    ]


def ajuda(aju):
    """
    -> Fornesse o manual de uma função ou biblioteca
    :param aju: função ou biblioteca a qual deseja ajuda
    """
    Título(f'Acessando o manual do comando {aju}', 2)
    sleep(1)
    print(c[4], end='')
    help(aju)
    print(c[0], end='')
    sleep(0.5)


def Título(tex, cor=0):
    """
    -> Cria um título personalizado
    :param tex: texto do título
    :param cor: a cor do título
    """
    tam = len(tex) + 4
    print(c[cor], end='')
    print('~'*tam)
    print(f' {tex}')
    print('~'*tam)
    print(c[0], end='')


while True:
    Título('SISTEMA DE AJUDA PYHELP', 3)
    aj = str(input('Função ou biblioteca > ')).strip()
    if aj.upper() == 'FIM':
        Título('ATE LOGO', 1)
        break
    else:
        ajuda(aj)
