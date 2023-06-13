# minha versão:

#d = float(input('Qual é a distância da viagem: '))
#p = 0
#if d <= 200:
#    p = 0.5 * d
#else:
#    p = 0.45 * d
#print('O valor da passágem é R$ {:.2f}'.format(p))

# resolução:

distancia = float(input('Qual é a distância da sua viagem? '))
print('Voce está preste a começar uma viagem de {}km.'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O preço da sua passagem sera de R${:.2f}.'.format(preco))
