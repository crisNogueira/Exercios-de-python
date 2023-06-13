from exe115.cadastro import cadastro

from time import sleep


def arquivoExi(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criaArquivo(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print('ERRO na criação do arquivo')
    else:
        print(f'Arquivo {arq} criado com sucesso')


def padrao(nome='', idade=0):
    """
    -> Cria um cadastro de forma tabular
    :param nome: nome do usuário
    :param idade: idade do usuário
    :return: cadastro (nome + idade) formatada
    """
    n = 43 - len(nome)
    cad = nome + ' ' * n + str(idade) + ' anos'
    return cad


def lerArquivo(arq):
    """
    -> Lé o arquivo de cadastro
    """
    try:
        a = open(arq, 'rt')
    except:
        print('ERRO de leitura')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')


def adArquivo(arq):
    """
    ->Adciona um novo cadastro ao arquivo.
    """
    try:
        a = open(arq, 'at')
    except:
        print('ERRO, não teve como abrir o arquivo')
    else:
        try:
            nome = str(input('Nome: ')).strip()
            idade = cadastro.leiaInt('Idade: ')
            a.write(f'{nome};{idade}\n')
        except:
            print('ERRO, não foi possível adicionar o arquivo')
        else:
            sleep(1)
            print(f'Novo registro de {nome} adcionado.')

