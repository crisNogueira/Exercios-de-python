produto = op = nome = ''
preco = total = p = me = c = 0
while True:
    produto = str(input('Digite o nome do produto comprado:' )).strip()
    preco = float(input('Digite o valor do produto comprado R$'))
    c += 1
    total += preco
    if preco > 1000:
        p += 1
    if c == 1:
        me = preco
        nome = produto
    if c > 1:
        if preco < me:
            me = preco
            nome = produto
    while True:
        op = str(input('Você vai continuar comprando? [S/N]')).strip().upper()[0]
        if op in 'SsNn':
            break
    if op in 'Nn':
        break
print(f'O total gasto na compra foi de R${total:.2f}')
print(f'O número de produtos que custaram mais que R$1000.00 foi de {p}')
print(f'O produto mais barato foi a/o {nome} custando R${me:.2f}')
