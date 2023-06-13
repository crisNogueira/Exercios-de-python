n = input('Digite algo: ')
print('O seu tipo primitivo é:', type(n))
print('É numerico?', n.isnumeric())
print('É letra?', n.isalpha())
print('É num ou letra?', n.isalnum())
print('É somente maiusculo?', n.isupper())
print('É somente minusculo?', n.islower())
print('É capitalizado?', n.istitle())

