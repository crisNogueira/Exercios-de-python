n = float(input('Digite o valor do metro: '))
print('{}m equivale a:\n{:.2f}km \n{:.2f}hm \n{:.2f}dam \n{:.2f}dc \n{:.2f}cm \n{:.2f}mm'.format(n, n/1000, n/100, n/10, n*10, 100*n, 1000*n))
