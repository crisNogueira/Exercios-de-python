def aumentar(p, a, sit=False):
    """
    -> Calcula o novo preço com aumento
    :param p: valor do preço
    :param a: valor do aumento em %
    :param sit: se True formato monetário
    :return: valor aumentado em tantos %
    """
    f = (a / 100) +1
    p = p * f
    if sit:
        return moeda(p)
    else:
        return p


def diminuir(p, d, sit=False):
    """
    -> Calcula o desconto do preço em tantos %
    :param p: Valor do preço
    :param d: Valor do desconto, em %
    :param sit: se True retorna no formato monetário
    :return: valor do preço descontado em tantos %
    """
    f = 1 - (d / 100)
    p = p *f
    if sit:
        return moeda(p)
    else:
        return p


def dobro(p, sit=False):
    """
    -> Calcula o dobro do preço
    :param p: Valor do preço
    :param sit: se True retorna no formato monetário
    :return: O valor do preço dobrado
    """
    p *= 2
    if sit:
        return moeda(p)
    else:
        return p


def metade(p, sit=False):
    """
    ->Calcula a metade do preço
    :param p: valor do preço
    :param sit: se True retorna no formato monetário
    :return: O valor do preço pela metade
    """
    p /= 2
    if sit:
        return moeda(p)
    else:
        return p


def moeda(p):
    """
    -> coloca o valor em formato monetário.
    :param p: valor do preço
    :return: o valor do preço no formato R$ --,--.
    """
    return f'R${p:.2f}'.replace('.', ',')


def resumo(p, a, d):
    """
    -> Resumo, em uma tabela, com os possíveis valores para preço
    como o seu dobro, metade, aumentado de % e diminuido em %.
    :param p: Valor do preço
    :param a: Valor do aumento em %
    :param d: Valor do desconto em %
    """
    print('-'*30)
    print('       RESUMO DO VALOR')
    print('-'*30)
    print(f'Preço analizado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p, sit=True)}')
    print(f'Metade do preço: \t{metade(p, sit=True)}')
    print(f'{a}% de aumento: \t{aumentar(p, a, sit=True)}')
    print(f'{d}% de desconto: \t{diminuir(p, d, sit=True)}')
    print('-'*30)
