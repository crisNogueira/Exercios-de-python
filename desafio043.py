peso = float(input('Digite o valor do seu peso: '))
alt = float(input('Digite o valor da sua: '))
imc = peso / (alt * alt)
if imc <= 18.5:
    print('Seu IMC é {:.2f}. você está abaixo do peso.'.format(imc))
elif 18.5 < imc <= 25:
    print('Seu IMC é {:.2f}. você esta com peso ideal.'.format(imc))
elif 25 < imc <= 30:
    print('Seu IMC é {:.2f}. você está com sobrepeso'.format(imc))
elif 30 < imc <= 40:
    print('Seu IMC é {:.2f}. você está com obesidade'.format(imc))
else:
    print('Seu IMC é {:.2f}. você está com obsidade mórbida'.format(imc))
