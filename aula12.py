nome = str(input('Digite o seu nome: ')).strip()
if nome == 'Cristiano':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print('Seu nome é bem popular')
elif nome in 'Juliana Ana':
    print('Belo nome feminino')
else:
    print('O seu nome é bem normal')
print('Tenha um bom dia, {}.'.format(nome))

