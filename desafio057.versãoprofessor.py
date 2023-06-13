sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor, informe se sexo: ')).strip().upper()[0]
print('Sexo {} registrado co sucesso.'.format(sexo))