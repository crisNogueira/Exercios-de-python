#Minha versão:
#nome = str(input('Digite o seunome completo: '))
#lista = nome.split()
#x = len(lista)-1
#print('O seu 1°nome é: \n{} \nO seu ultimo nome é: \n{}'.format(lista[0], lista[x]))

# Resolução:
n = str(input('Digite o seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!!!')
print('O seu 1° nome é: {}.'.format(nome[0]))
print('O seu ultimo nome é: {}.'.format(nome[len(nome)-1]))

