#minha versão:
#nome = input('Digite o seu nome: ')
#x = 'Silva' in nome
#print('O seu nome tem a palavra Silva? \n{}'.format(x))

#resolução:
nome = str(input('Qual é o seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))
