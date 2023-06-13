"""Minha versão:"""

"""sal = float(input('Digite o valor do seu salário: '))
nov = 0
if sal > 1250:
    nov = nov + (sal * 1.1)
else:
    nov = nov + (sal * 1.15)
print('O seu novo salário é R${:.2f}'.format(nov))"""

"""Resolução:"""

print('\033[42m  \033[m'*20)
salario = float(input('\033[1;32mQual é o salário do funcionário? R$\033[m'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganha \033[1;31mR${:.2f}\033[m passa a ganhar \033[1;33mR${:.2f}\033[m.'.format(salario, novo))

