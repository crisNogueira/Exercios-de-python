from exe107 import moeda

preço = float(input('Digite o valor do preço: R$'))
print(f'O preço R${preço} aumentado de 10% é de R${moeda.aumentar(preço, 10):.2f}')
print(f'O preço R${preço} diminuido de 10% é de R${moeda.diminuir(preço, 10):.2f}')
print(f'O dobro de R${preço} é R${moeda.dobro(preço)}')
print(f'A metade de R${preço} é R${moeda.metade(preço)}')
