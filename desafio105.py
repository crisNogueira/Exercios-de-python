def notas(*n, sit=False):
    """
    -> Mostra a quantidade, a maior, a menor e a média das notas de um aluno
       e se desejavel a sua situação.
    :param n: As notas do aluno.
    :param sit: Se True informe a situação, caso contrario não.
    :return: Um dicionário com os dados da nota do aluno.
    """
    r = {}
    md = ma = me = 0
    r['Total'] = len(n)
    for c in range(0, len(n)):
        if c == 0:
            ma = n[0]
            me = n[0]
        if n[c] >= ma:
            ma = n[c]
        if n[c] <= me:
            me = n[c]
        md += n[c]
    r['Maior'] = ma
    r['Menor'] = me
    r['Média'] = md / len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'Boa'
        elif r['Média'] >= 5 and r['Média'] < 7:
            r['Situação'] = 'Razoaval'
        else:
            r['Situação'] = 'Ruim'
    return r


print('-'*100)
resp = notas(5.5, 2.5, 10, 6.5, 8, 10, sit=True)
print(resp)
