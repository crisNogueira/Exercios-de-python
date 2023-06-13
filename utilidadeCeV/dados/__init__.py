def leiadinheiro(tex):
    """
    analisa se é um número válido.
    :param tex: texto para imprimir
    :return: valor númerico válido.
    """
    ok = False
    while True:
        num = str(input(f'{tex}')).upper().strip().replace(',', '.')
        if num.replace('.', '').isnumeric():
            num = float(num)
            ok = True
        else:
            print(f'\033[31m ERRO "{num}" não é um número monetário válido\033[m')
            num = ''
        if ok:
            break
    return num
