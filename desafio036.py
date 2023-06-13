casa = float(input('Digite o valor da casa: '))
sal = float(input('Qual é o valor do seu salário? '))
ano = int(input('Em quantos anos pretende paga-la? '))
num = 12 * ano
pres = casa / num
if pres > 0.3 * sal:
    print('O seu emprestimo infelizmente foi negado.')
    print('O valor do seu imprestimo R${:.2f} excede em 30% do seu salário'.format(pres))
else:
    print('O seu imprestimo foi aprovado! você ira pagar R${:.2f} em {} prestações.'.format(pres, num))
