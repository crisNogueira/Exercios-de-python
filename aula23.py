try:
    a = int(input('Digite o numerador: '))
    b = int(input('Digite o denominador: '))
    r = a / b
except Exception as erro:
    print('Infelizmente tivemos um erro :(')
    print(f'erro {erro.__class__}')
else:
    print(f'O valor de r é {r}')
