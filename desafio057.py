sexo = ''
print(sexo)
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o valor do seu sexo: [M/F]')).strip().upper()[0]
    if sexo != 'M' and sexo != 'F':
        print('Opção errada, tente novamente')


