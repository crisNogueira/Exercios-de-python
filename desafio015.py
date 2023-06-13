d = float(input('Digite quantos dias você ficou com o carro: '))
k = float(input('Digite a quantidade de km rodados: '))
l = 60*d+0.15*k
print('O preço por ter ficado {:.0f} dias e rodado {}km sera de:'.format(d, k))
print('='*10)
print('R${:.2f}'.format(l))
print('='*10)


