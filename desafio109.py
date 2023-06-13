import moeda

preço = float(input('Digite o valor do preço: R$ '))
print(f'O preço {moeda.moeda(preço)} aumentado de 10% é {moeda.aumentar(preço, 10, sit=True)}')
print(f'O preço {moeda.moeda(preço)} descontado de 10% é {moeda.diminuir(preço, 10, sit=True)}')
print(f'O preço {moeda.moeda(preço)} dobrado é {moeda.dobro(preço, sit=True)}')
print(f'O preço {moeda.moeda(preço)} pela metade é {moeda.metade(preço, sit=True)}')
