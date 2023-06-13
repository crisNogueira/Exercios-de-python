from exe108 import moeda

preço = float(input('Digite o valor do preço: R$'))
print(f'O preço {moeda.moeda(preço)} aumentado de 10% é de {moeda.moeda(moeda.aumentar(preço, 10))}')
print(f'O preço {moeda.moeda(preço)} diminuido de 10% é de {moeda.moeda(moeda.diminuir(preço, 10))}')
print(f'O dobro de {moeda.moeda(preço)} é {moeda.moeda(moeda.dobro(preço))}')
print(f'A metade de {moeda.moeda(preço)} é {moeda.moeda(moeda.metade(preço))}')
