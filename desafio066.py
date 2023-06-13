num = cont = soma = 0
print('-+-'*5)
print('Desafio 066')
print('-+-'*5)
while True:
    num = int(input('Digite um valor para numero: caso queira para digite 999 '))
    if num != 999:
        cont += 1
        soma += num
    else:
        break
print(f'No total foram digitados {cont} números, cuja a soma vale {soma}')
