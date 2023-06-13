from datetime import date
ano = date.today()
nun = int(ano.year)
ani = int(input('Digite o ano do seu nascimento: '))
if nun - ani < 18:
    print('Você ainda vai se alistar: faltam {} anos.'.format(18 - (nun - ani)))
elif nun - ani == 18:
    print('Já está na hora de se alistar')
else:
    print('Já se passou {} anos para se alistar.'.format((nun - ani)-18))

