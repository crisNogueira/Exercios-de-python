#minha versão:

#n = int(input('Digite um número: '))
#if (n % 2) == 0:
#    print('O número {} é par.'.format(n))
#else:
#    print('O número {} é impar.'.format(n))

# resolução:
numero = int(input('Digeite um número: '))
resultado = numero % 2
if resultado == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é IMPAR.'.format(numero))
