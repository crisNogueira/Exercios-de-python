from datetime import date


def voto(ano):
    """
    -> Determina se o voto é optativo, obrigatório ou negado
    :param ano: ano de nascimento
    """
    idade = date.today().year - ano
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        print('\033[31m VOTO NEGADO\033[m')
    elif (idade >= 16 and idade < 18 ) or (idade >= 70):
        print('\033[33m VOTO OPTATIVO\033[m')
    else:
        print('\033[32m VOTO OBRIGATÓRIO\033[m')


n = 0
print('-'*40)
n = int(input('Em que ano você nasceu? '))
voto(n)
