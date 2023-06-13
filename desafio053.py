frase = str(input('Digite uma frase ')).strip()
f = ''.join(frase.split())
f = f.lower()
x = len(f)
y = 0
for c in range(0, x):
    if f[c] == f[x-1-c]:
        y = y+1
print('A frase "{}" :'.format(frase))
if y == x:
    print('É um palindromo')
else:
    print('Não é um palindromo')




