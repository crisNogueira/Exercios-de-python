import math
cat1 = float(input('Digite o valor do primeiro cateto: '))
cat2 = float(input('Digite o valor do segundo cateto: '))
hip = math.sqrt(cat1**2+cat2**2)
hi = math.hypot(cat1, cat2)
print('O valor da hipotenusa do triângulo de catetos {} e {} é: {:.2f}.'.format(cat1, cat2, hi))
