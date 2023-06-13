idade = cont1 = cont2 = cont3 = p = 0
sexo = op = ''
print('-'*20)
print('Cadastramento')
print('-'*20)
while True:
    sexo = str(input('Digite o valor do sexo: [M/F] ')).strip().upper()[0]
    if sexo in 'MmFf':
        idade = int(input('Digite o valor da idade: '))
        if idade >= 18:
            cont1 += 1
        if sexo in 'Mm':
            cont2 += 1
        if sexo in 'Ff':
            if idade < 20:
                cont3 += 1
        while True:
            op = str(input('Quer continuar a cadastrar: [S/N] ')).strip().upper()[0]
            if op in 'SsNn':
                if op in 'Ss':
                   p = 0
                   break
                else:
                    p += 1
                    break
    if  p == 1:
        break
print(f'O número de pessoas com mais de 18 é {cont1}')
print(f'O número de homens cadastrados é {cont2}')
print(f'O número de mulheres com menos de 20 é {cont3}')




