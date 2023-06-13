def aumentar(p=0, a=0, sit=False):
     f = p * ((a / 100) + 1)
     if sit:
         return moeda(f)
     else:
         return f


def diminuir(p=0, d=0, sit=False):
    f = p * (1-(d / 100))
    if sit:
        return moeda(f)
    else:
        return f


def dobro(p=0, sit=False):
    p *= 2
    if sit:
        return moeda(p)
    else:
        return p


def metade(p=0, sit=False):
    p /= 2
    if sit:
        return moeda(p)
    else:
        return p


def moeda(p=0, m='R$'):
    return f'{m}{p:.2f}'.replace('.', ',')
