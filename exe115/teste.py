arquivo = open('contatos', 'a')
nome = input('nome: ')
idade = int(input('idade:'))
n = 43 - len(nome)
cad = nome + ' ' * n + str(idade) + ' anos'
print('-'*50)
print(cad)
arquivo.writelines(f'{cad}\n')
#arquivo = open('contatos', 'r')
#print(arquivo.read())
#copia = []
#for c in arquivo:
#    copia.append(c.replace('\n', ''))
#for n in range(0, len(copia)):
#    if n % 2 == 0:
#        print(f'{copia[n]}', end=' ')
#        print(f'\t{copia[n+1]}')
