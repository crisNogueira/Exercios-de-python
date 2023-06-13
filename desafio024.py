# minha versão
#nome = input('Digite o nome da cidade: ')
#lista = nome.split()
#x = 'Santo' in lista[0]
#print('O nome da cidade começa com Santo? \n{}'.format(x))

#resolução:
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')


