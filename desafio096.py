def área(l, c):
    print('-=-'*30)
    print(f'A área de um terreno {l}x{c} é {(l*c):.2f}m²')
    print('-=-'*30)


a = b = 0
print('  Controle de terrenos')
print('-'*24)
a = float(input('Largura (m): '))
b = float(input('Comprimento (m): '))
área(a, b)
