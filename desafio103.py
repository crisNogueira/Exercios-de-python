def ficha(nome='<desconhecido>', gols=0):
    """
    -> O programa diz a quantidade de gols do jogador no campeonato.
    :param nome: Recebe o nome do Jogador.
    :param gols: Recebe o n° de gols.
    """
    print(f'O jogado {nome} fez {gols} gols no campeonato.')


print('-'*30)
n = str(input('Nome do jogador: '))
if n == '':
    n = '<desconhecido>'
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
ficha(n, g)
