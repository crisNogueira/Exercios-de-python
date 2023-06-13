aprov = {}
lista = []
l = []
soma = 0
op = ''
p = 0
while True:
    aprov.clear()
    aprov['nome'] = str(input('Digite o nome do jogdor: ')).strip()
    p = int(input(f'Quantas partidas o jogador {aprov["nome"]} fez '))
    aprov['gols'] = []
    for i in range(0, p):
        aprov['gols'].append(int(input(f'Quantos gols ele fez na partida {i+1}? ')))
        soma = soma + aprov['gols'][i]
    aprov['total'] = soma
    lista.append(aprov.copy())
    soma = 0
    while True:
        op = str(input('Deseja cadastrar mais um jogador? [S/N] ')).upper().strip()
        if op in 'SN':
            break
        print('ERRO! responda apenas S ou N')
    if op == 'N':
        break
print(lista[0]["gols"])
print('-='*30)
print('cod', end=' ')
for c in aprov.keys():
    print(f'{c:<15}', end='')
print()
print('-'*40)
for c in range(0, len(lista)):
    print(f'{c:>3} {lista[c]["nome"]:<15}{lista[c]["gols"]!s:<15}{lista[c]["total"]:<15}')
print('-'*40)
while True:
    p = int(input('Mostrar os dados de qual jogador? (999 para parar) '))
    if p >= len(lista):
        if p == 999:
            print('---<Fim do program>---')
            break
        else:
            print('Opção invalida')
    else:
        print(f'--LEVANTAMENTO DO JOGADOR {lista[p]["nome"]}:')
        for i in range(0, len(lista[p]['gols'])):
            print(f'  No jogo {i+1} ele fez {lista[p]["gols"][i]} gols.')
