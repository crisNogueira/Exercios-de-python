from random import sample, shuffle
n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto nome: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
ordem = sample([n1, n2, n3, n4], k=4)
print('A ordem de apresentação sera: \n{}.'.format(lista))

