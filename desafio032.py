# minha versão

'''a = int(input('Digite o valor do ano: '))
if (a % 4) == 0:
    if (a % 100) == 0:
        if (a % 400) == 0:
            print('O ano {} é bissexto'.format(a))
        else:
            print('O ano {} não é bissexto.'.format(a))
    else:
        print('O ano {} é bissexto.'.format(a))
else:
    print('O ano {} não é bissexto.'.format(a))'''

# resolução:
print('\033[45m \033[m'*52)
print('\033[1;35m             Analisador de ano bissexto\033[m')
print('\033[45m \033[m'*52)
from datetime import date
ano = int(input('\033[1;32mQue ano quer analisar?\033[m \033[1;33mColoque 0 para analisar o ano atual: \033[m'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano \033[1;32m{}\033[m é \033[1;34mbissexto\033[m.'.format(ano))
else:
    print('O ano \33[1;32m{}\033[m não é \033[1;31mbissexto\033[m.'.format(ano))

