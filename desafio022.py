# minha versão:
#nome = input('Digite o seu nome completo: ')
#print('O seu nome com todas as letras maiusculas: \n{}'.format(nome.upper()))
#print('O seu nome com todas as letras minusculas: \n{}'.format(nome.lower()))
#nome.strip()
#x = len(nome)-nome.count(' ')
#print('A quantidade de letras do nome é: {}'.format(x))
#lista = nome.split()
#y = len(lista[0])
#print('O 1° nome tem {} letras'.format(y))

#versão resolvida:
nome = str(input('Digite o seu nome competo: ')).strip()
print('Analisando o seu nome ...')
print('Seu nome em maiusculo é: {}'.format(nome.upper()))
print('O seu nome em minusculo é: {}'.format(nome.lower()))
print('A quantidade de letras do seu nome é: {}'.format(len(nome) - nome.count(' ')))
print('O seu primeiro nome tem {} letras.'.format(nome.find(' ')))




