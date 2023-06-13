l = []
x = 0
for c in range(0, 5):
    if c == 0:
        x = int(input('Digite o 1° valor: '))
        l.append(x)
        print('O valor digitado está na ultima posição.')
    elif c == 1:
        x = int(input('Digite o 2° valor: '))
        if x < l[0]:
            l.insert(0, x)
            print('O valor foi adcionado na posição 0.')
        else:
            l.append(x)
            print('O valor foi adcionado na ultima posição.')
    elif c == 2:
        x = int(input('Digite o 3° valor: '))
        if x < l[0]:
            l.insert(0, x)
            print('O valor foi adcionado na posição 0.')
        elif l[0] <= x < l[1]:
            l.insert(1, x)
            print('O valor foi adcionado na posição 1.')
        else:
            l.append(x)
            print('O valor foi adcionado na posição 2.')
    elif c == 3:
        x = int(input('Digite o 4° valor: '))
        if x < l[0]:
            l.insert(0, x)
            print('O valor foi adcionado na posição 0.')
        elif l[0] <= x < l[1]:
            l.insert(1, x)
            print('O valor foi adcionado na posição 1.')
        elif l[1] <= x < l[2]:
            l.insert(2, x)
            print('O valor foi adcionado na posição 2.')
        else:
            l.append(x)
            print('O valor foi adcionado na ultima posição.')
    elif c == 4:
        x = int(input('Digite o 5° valor: '))
        if x < l[0]:
            l.insert(0, x)
            print('O valor foi adcionado na posição 0.')
        elif l[0] <= x < l[1]:
            l.insert(1, x)
            print('O valor foi adcionado na posição 1.')
        elif l[1] <= x < l[2]:
            l.insert(2, x)
            print('O valor foi adcionado na posição 2.')
        elif l[2] <= x < l[3]:
            l.insert(3, x)
            print('O valor foi adcionado na posição 3.')
        else:
            l.append(x)
            print('O valor foi adcionado na ultima posição.')
print('-='*30)
print('Os valores adcionados foram:')
for d in l:
    print(f'{d}', end=' ')
