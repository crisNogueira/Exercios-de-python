nota1 = float(input('Digite a sua 1° nota: '))
nota2 = float(input('Digite a sua 2° nota: '))
media = (nota1+nota2)/2
if media <= 5.0:
    print('\033[31m Sua média foi {:.2f}, você foi REPROVADO.\033[m'.format(media))
elif 5.0 < media <= 6.9:
    print('\033[33m Sua média foi {:.2f}, você está de RECUPERAÇÃO.\033[m'.format(media))
else:
    print('\033[34m Sua média foi {:.2f}, Você foi APROVADO.\033[m'.format(media))
