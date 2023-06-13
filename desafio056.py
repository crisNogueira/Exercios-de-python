soma = 0
ma = 0
nome1 = ''
c = 0
m = 0
f = 0
for p in range(1, 5):
    nome = str(input('Digite o nome da {}°pessoa: '.format(p))).strip()
    sexo = str(input('Digite m para masculino ou f para feminino da {}°pessoa: '.format(p))).strip()
    idade = int(input('Digite a idade da {}°pessoa: '.format(p)))
    soma = soma + idade
    if sexo == 'm':
        m = 1
        if p == 1:
          ma = idade
        if idade > ma:
          nome1 = nome
    else:
        f = 1
        if idade < 20:
            c = c+1
print('A média das idades é {}'.format(soma/4))
if m == 1:
    print('O nome do homem mais velho é {}'.format(nome1))
if f == 1:
    print('O número de mulheres com menos de 20 é {}'.format(c))



