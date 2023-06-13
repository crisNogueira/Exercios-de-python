from datetime import datetime
cad = {}
data = datetime.now().year
niv = apo = 0
cad['nome'] = str(input('Digite o seu nome: '))
cad['ano'] = int(input('Digite o ano do seu nascimento: '))
cad['tra'] = int(input('Digite a sua carteira de trabalho: (0 não tem) '))
if cad['tra'] != 0:
    cad['anotra'] = int(input('Digite o ano de contratação: '))
    cad['salario'] = float(input('Digite o seu salário: R$'))
    apo = data - cad['anotra']
niv = data - cad['ano']
print('-=-'*30)
if cad['tra'] != 0:
    print(f'Nome = {cad["nome"]}')
    print(f'Idade = {niv} anos')
    if apo < 35:
        print(f'Faltam {35 - apo} anos para se aponsentar')
    else:
        print(f'Trabalhador apto para aposentar com {apo} anos de contribuição')
else:
    print(f'Nome = {cad["nome"]}')
    print(f'Idade = {niv}')
    print(f'Carteira de trabalho {cad["tra"]}')


