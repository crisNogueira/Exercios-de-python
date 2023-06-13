print('\033[33m-=-\033[m'*20)
print('           \033[4;33mANALIZADOR DE TRIÂNGULO\033[m')
print('\033[33m-=-\033[m'*20)
r1 = float(input('Digite o 1° lado do triângulo: '))
r2 = float(input('Digite o 2° lado do triângulo: '))
r3 = float(input('Digite o 3° lado do triângulo: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os segmentos acima \033[33m podem forma um triangulo\033[m')
    if r1 == r2 == r3:
        print('Esse triângulo é \033[33m EQUILÁTERO\033[m')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Esse triângulo é \033[33m ISÓSCELES\033[m')
    else:
        print('Esse triângulo é \033[33m ESCALENO\033[m')
else:
    print('Os segmentos acima \033[31m Não podem formar triângulo\033[m')
