l = []
x = 0
op = ' '
while True:
    l.append(int(input('Digite um valor: ')))
    while True:
        op = str(input('Deseja adcionar mais um número: [S/N]')).strip().upper()
        if op in 'SN':
            break
    if op == 'N':
        break
print('-='*30)
print(l)
print(f'Foram digitados {len(l)} números.')
l.sort(reverse=True)
print(f'Os números digitado na ordem foi {l}')
for n, c in enumerate(range(0, len(l))):
    if l[c] == 5:
        print(f'O número 5 foi adcionado na {n+1}° posição')
        x += 1
if x == 0:
    print('O número 5 não foi adcionado.')


