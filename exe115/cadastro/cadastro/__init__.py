def leiaInt(mes=''):
    """
    -> identifica se um n° inteiro válido foi digitado
    :param mes: Menssagem padrão
    :return: numero verificado
    """
    while True:
        try:
            num = int(input(mes))
        except KeyboardInterrupt:
            num = 0
        except:
            print('\033[31mERRO valor invalido\033[m')
        else:
            break
    return num


def linha(n=60):
    """
    -> forma uma linha na tela
    :param n: quantidade de traços
    :return: linha com n traços
    """
    return '-' * n


def cabeçalho(txt):
    """
    -> cria um cabeçalho
    :param txt: texto do cabeçalho entre linhas
    """
    print(linha())
    print(f'{txt}'.center(60))
    print(linha())


def cadastro(lista):
    """
    -> mostra um menu de opções
    :param lista: As opções do menu
    :return: a opção desejada.
    """
    cabeçalho('MENU PRINCIPAL')
    for c in range(1, len(lista)+1):
        print(f'\033[33m{c}\033[m-\033[34m{lista[c-1]}\033[m', end='')
        print('\n')
    print(linha())
    op = leiaInt('\033[32mSua opção: \033[m')
    return op

