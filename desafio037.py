num = int(input('Digite um número: '))
print('''Escolha uma das opções abaixo:
 [1] converter para binário
 [2] converter para octal
 [3] converter para hexadecimál''')
op = int(input('Sua opção: '))

if op == 1:
    print('O número {} convertido em binário é {}.'.format(num, bin(num)[2:]))
elif op == 2:
    print('O número {} convertido em octal é {}.'.format(num, oct(num)[2:]))
elif op == 3:
    print('O número {} convertido em hexadecimal é {}.'.format(num,hex(num)[2:]))
else:
    print('OPÇÃO INVALIDA.')
