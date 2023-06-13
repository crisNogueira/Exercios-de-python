aprov = {}
aprov['nome'] = str(input('Digite o nome do Jogador: ')).strip()
p = int(input('n° de partidas: '))
aprov['gols'] = []
if p > 0:
    for i in range(1, p+1):
        aprov['gols'].append(int(input(f' quantidade de gols na {i}° partida ')))
aprov['total'] = sum(aprov['gols'])
print('-=-'*30)
print(aprov)
print('-=-'*30)
for k, v in aprov.items():
    print(f'O campo {k} tem valor {v}')
print('-=-'*30)
print(f'O jogador {aprov["nome"]} jogou {p} partidas.')
if p > 0:
    for j in range(0, p):
        print(f' --> Na partida {j+1}, fez {aprov["gols"][j]} gols.')
    print(f'Foi um total de {aprov["total"]}')

