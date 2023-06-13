from time import sleep
from exe115.cadastro.cadastro import *
from exe115.cadastro import arquivo

arq = 'contatos.txt'

if not arquivo.arquivoExi(arq):
    arquivo.criaArquivo(arq)

while True:
    op = cadastro(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if op == 1:
        cabeçalho('PESSOAS CADASTRADAS')
        arquivo.lerArquivo(arq)
    elif op == 2:
        cabeçalho('NOVO CADASTRO')
        arquivo.adArquivo(arq)
    elif op == 3:
        cabeçalho('Saindo do programa ... ate logo')
        sleep(1)
        break
    else:
        print('\033[31mERRO, opção inválida\033[m')

