cadastro = {}
cadastro['nome'] = str(input('Digite o seu nome: ')).strip()
cadastro['media'] = float(input(f'Média de {cadastro["nome"]}: '))
if cadastro['media'] >= 7:
    cadastro['situação'] = 'APROVADO'
else:
    cadastro['situação'] = 'REPROVADO'
print('-='*30)
print(f'- nome é igual a {cadastro["nome"]}')
print(f'- Média é igual a {cadastro["media"]}')
print(f'- situaçao é igual a {cadastro["situação"]}')
