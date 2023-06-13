def leiaint(tes):
    """
    -> Lê um número, se não for número dá erro.
    :param tes: string do input
    :return: num, se for número.
    """
    ok = False
    while True:
        num = input(f'{tes}').upper()
        if num.isnumeric():
            num = int(num)
            ok = True
        else:
            print('\033[31m ERRO! digite um número inteiro válido\033[m')
        if ok:
            break
    return num


print('-'*30)
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
