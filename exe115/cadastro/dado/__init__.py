def leiaidade(mes=''):
    """
    -> Verifica se a idade está no formato inteiro.
    :param mes: menssagem padrão
    :return: idade verificada
    """
    while True:
        try:
            num = int(input(mes))
        except KeyboardInterrupt:
            print('\033[31mO usuário decidiu não digitar a idade\033[m')
            num = 0
        except:
            print('\033[31mERRO valor digitado é inválido\033[m')
        else:
            break
    return num
