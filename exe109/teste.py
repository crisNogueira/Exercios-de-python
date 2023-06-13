from exe109 import moeda

preço = float(input('Digite o valor do preço: R$'))
print(f'O preço {moeda.moeda(preço)} aumentado de 10% é de {moeda.aumentar(preço, 10, sit=True)}')
print(f'O preço {moeda.moeda(preço)} diminuido de 10% é de {moeda.diminuir(preço, 10, sit=True)}')
print(f'O dobro de {moeda.moeda(preço)} é {moeda.dobro(preço, sit=True)}')
print(f'A metade de {moeda.moeda(preço)} é {moeda.metade(preço, sit=True)}')
