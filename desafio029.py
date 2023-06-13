#minha versão:

#v = int(input('Digite o valor da velocidade do carro: '))
#m = 0
#if v > 80:
#    print('VOCÊ FOI MULTADO!!!')
#    m = 7*(v-80)
#    print('A SUA MULTA FOI DE R$ {:.2f}.'.format(m))
#else:
#    print('Voce não foi multado')

# resolução:

velocidade = float(input('Qual é a velocidade atual do carro: '))
if velocidade > 80:
    print('Multado, você excedeu o limete de 80km/h')
    multa = (velocidade - 80) * 7
    print('A sua multa foi de R${:.2f}.'.format(multa))
print('Tenha um bom dia, dirige com segurança.')