cad = {}
list = []
listm = []
listA = []
op = ''
soma = 0
while True:
    cad['nome'] = str(input('Digite o Nome: ')).strip()
    while True:
        cad['sexo'] = str(input('Digite o seu sexo: [M/F] ')).upper().strip()
        if cad['sexo'] in 'MF':
            break
        else:
            print('ERRO! por favor, digite apenas M ou F')
            cad['sexo'] = ''
    if cad['sexo'] == 'F':
        listm.append(cad['nome'])
    cad['idade'] = int(input('Digite a idade: '))
    soma = soma + cad['idade']
    list.append(cad.copy())
    cad = {}
    while True:
        op = str(input('Deseja cadastrar mais uma pessoa? [S/N] ')).upper().strip()
        if op in 'SN':
            break
        else:
            print('ERRO! digite apenas S ou N.')
    if op == 'N':
        soma = soma / len(list)
        break
for i in range(0, len(list)):
    if list[i]['idade'] > soma:
        listA.append(list[i].copy())
print('-='*30)
print(f'Foi cadastrado um total de {len(list)} pessoas.')
print(f'A média das idades foi {soma:.2f} anos.')
print('As mulheres cadastradas foram ', end='')
for c in range(0, len(listm)):
    print(f'{listm[c]}', end=',')
print()
print('As pessoas que tem idade acima da média:')
for c in range(0, len(listA)):
    for k, v in listA[c].items():
        print(f'  {k} = {v};', end=' ')
    print()
