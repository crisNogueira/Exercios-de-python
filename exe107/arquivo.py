def lerArquivo():
    arquivo = open('contatos', 'r')
    copia = []
    for c in arquivo:
        copia.append(c.replace('\n', ''))
    for n in range(0, len(copia)):
        if n % 2 == 0:
            print(f'{copia[n]}', end='')
            print(f'\t{copia[n+1]}')
