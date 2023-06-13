# minha versão:
#frase = input('Escreva uma frase: ')
#x = frase.count('a')
#y = frase.find('a')+1
#print('O numero de vezes que a letra a aparece é: \n{}'.format(x))
#print('A posição em que a letra a aparece pela 1° vez é: \n{}°'.format(y))

#resolução:

frase = str(input('Escreva uma frase: ')).upper().strip()
print('O n° de vezez que a letra a aparece na frase é {}.'.format(frase.count('A')))
print('A primeira letra a aparece na posição {}.'.format(frase.find('A')+1))
print('A ultima vez que a letra a aparece é na posição {}.'.format(frase.rfind('A')+1))

