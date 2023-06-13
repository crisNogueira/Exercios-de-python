lista = []
x = c = a = 0
op = ''
while True:
    if c == 0:
        lista.append(int(input('Digite um valor: ')))
        print('Valor adcionado com sucesso!')
    else:
        x = int(input('Digite um valor: '))
        for d in range(0, len(lista)):
            if x == lista[d]:
                print('Número repitido, não será adcionado ')
                a = 1
        if a == 0:
            print('Valor adcionado com sucesso!')
            lista.append(x)
    a = 0
    c = 1
    while True:
        op = str(input('Você quer continuar a digitar? [S/N]')).strip().upper()
        if op in 'SN':
            break
    if op == 'N':
        break
lista.sort()
print(f'A lista digitada foi: {lista}')
