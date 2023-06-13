n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
op = 0
e = 0
while op != 5:
    print('Escolha uma das seguintes opções: ')
    print('''   [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    e = int(input())
    if e == 1:
        print('{}+{}={}'.format(n1, n2, n1+n2))
    elif e == 2:
        print('{}x{}={}'.format(n1, n2, n1*n2))
    elif e == 3:
        if n1 >= n2:
            print('{} é o maior número'.format(n1))
        else:
            print('{} é o maior número'.format(n2))
    elif e == 4:
        n1 = int(input('Digite o 1° número: '))
        n2 = int(input('Digite o 2° número: '))
    elif e == 5:
        print('Fim do programa')
        op = 5
    else:
        print('OPÇÃO INVALIDA')






