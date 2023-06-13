print('\033[35m-=-\033[m'*20)
print('                  \033[1;34m Loja tudo caro\033[m')
print('\033[35m-=-\033[m'*20)
valor = float(input('Digite o valor da suas compras: R$ '))
print('Escolha a forma de pagamento')
print('[1] A vista dinheiro/cheque')
print('[2] A vista no cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')
op = int(input())
if op == 1:
    print('A sua compra de R${:.2f} irá custar R${:.2f}'.format(valor, valor*0.9))
elif op == 2:
    print('A sua compra de R${:.2f} irá custar R${:.2f}'.format(valor, valor*0.95))
elif op == 3:
    print('A sua compra de R${:.2f} vai ser paga em 2 parcelas de R${:.2f}'.format(valor, valor/2))
    print('O total a pagar será de R${:.2f}'.format(valor))
elif op == 4:
    p = int(input('Quantas parcelas? '))
    x = valor*1.2
    print('A sua compra de R${:.2f} vai ser paga em {} parcelas de R${:.2f}'.format(valor, p, x/p))
    print('O total a pagar será de R${:.2f}'.format(x))
else:
    print('Opção invalida!')
