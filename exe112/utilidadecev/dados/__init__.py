def leiadinheiro(msg):
    ok = False
    while True:
        num = input(msg).strip().replace(',', '.')
        if num.replace('.', '').isnumeric():
            num = float(num)
            ok = True
        else:
            print(f'\033[31m"{num}" NÃO É UM VALOR VÁLIDO, TENTE NOVAMENTE.\033[m')
        if ok:
            break
    return num


