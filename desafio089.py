col = []
notas = []
op = ' '
x = 0
while True:
    col.append(str(input('Nome: ')).strip())
    col.append(float(input('Nota 1: ')))
    col.append(float(input('Nota 2: ')))
    col.append((col[1]+col[2])/2)
    notas.append(col[:])
    col = []
    while True:
        op = str(input('Quer continuar? [S/N] ')).strip().upper()
        if op in 'NS':
            break
    if op == 'N':
        op = ' '
        break
print('-='*30)
print(f'{"no.":<4}{"Nome":<10}{"Média":>8}')
print('_'*30)
for c in range(0, len(notas)):
    print(f'{c:<4}{notas[c][0]:<10}{notas[c][3]:>8.2f}')
print('_'*40)
while True:
    x = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if x == 999:
        print('FINALIZADO...')
        print('<<< volte sempre >>>')
        break
    else:
        print(f'Notas de {notas[x][0]} são [{notas[x][1]}], [{notas[x][2]}]')
        print('_'*40)
