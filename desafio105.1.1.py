def notas(*n, sit=False):
    """
    -> Função para analizar as notas e situaçãoes de vários alunos.
    :param n: Uma ou mais notas dos alunos (Aceita mais)
    :param sit: Valor opcional, se deve ou não adcionar a situação
    :return: um dicionário com as informações sobre as notas dos alunos
    """
    r = {}
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'BOA'
        elif 5 <= r['Média'] < 7:
            r['Situação'] = 'RAZOAVEL'
        else:
            r['Situação'] = 'RUIM'
    return r


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)
