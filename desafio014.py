c = float(input('Digite o valor da temperatura em °C: '))
f = (9*c+160)/5
k = c+273.15
print('A temperatura {}°C equivale a: ')
print('-'*12)
print('{:.2f}°F \n\n{:.2f}°K'.format(f, k))
print('-'*12)

