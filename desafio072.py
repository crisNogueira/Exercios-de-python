num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze','treze', 'quartoze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um número entre 0 e 20: '))
if n < 0 or n > 20:
    while True:
        n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
        if n >= 0 and n <= 20:
            break
print(f'Você digitou o número {num[n]}')
