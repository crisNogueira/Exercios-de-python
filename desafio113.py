def leiaInt(mes):
    """
    -> Analisa se o número inteiro digitado é válido.
    :param mes: menssagem de entrada
    :return: numero intero.
    """
    while True:
        try:
            num = int(input(mes))
        except KeyboardInterrupt:
            print('\n')
            print('\033[31mO usuário preferiu não digitar o valor.\033[m')
            num = 0
            break
        except:
            print('\033[31m ERRO valor inválido\033[m')
        else:
            break
    return num


def leiaFloat(mes):
    while True:
        try:
            num = input(mes).replace(',', '.')
            num = float(num)
        except KeyboardInterrupt:
            print('\n')
            print('\033[31m O usuário preferiu não digitar o valor\033[m')
            num = 0
            break
        except:
            print('\033[31m ERRO Valor inválido\033[m')
        else:
            break
    return num


num = leiaInt('Digite um número Inteiro: ')
num1 = leiaFloat('Digite um número Real: ')
print(f'O número inteiro digitado foi o {num}')
print(f'O número real digitado foi o {num1}')
