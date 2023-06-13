#minha versão
#num = input('Digite um número de 0 a 9999: ')
#print('O número {} tem: \nunidade {} \ndezenas {} \ncentenas {} \nmilhar {}'.format(num, num[3], num[2], num[1], num[0]))

#resolução
num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o n°{}...'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

