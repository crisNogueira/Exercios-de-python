from datetime import date
idade = int(input('Digite o seu ano de nascimento: '))
data = date.today()
ano = int(data.year)
if (ano - idade) <= 9:
    print('A sua idade é {} anos e a sua categoria é \033[31m MIRIM \033[m.'.format(ano - idade))
elif 9 < (ano - idade) <= 14:
    print(' A sua idade é {} anos e a sua categoria é \033[32m INFANTIL \033[m.'.format(ano - idade))
elif 14 < (ano - idade) <= 19:
    print('A sua idade é {} anos e a sua categoria é \033[33m JUNIOR \033[m'.format(ano - idade))
elif (ano - idade) == 20:
    print('A sua idade é 20 anos e a sua categoria é \033[34m SÊNIOR \033[m')
else:
    print('A sua idade é {} anos e a sua categoria é \033[35m MASTER \033[m'.format(ano - idade))
