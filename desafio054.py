from datetime import date
anoa = date.today().year
y = 0
for c in range(0, 8):
    x = int(input('Digite o seu ano de nascimento: '))
    if anoa - x >= 18:
        y = y + 1
print('Das sete pessoas as que não tem maioridade é {} e as que tem é {}'.format(7-y, y))
