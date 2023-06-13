from exe112.utilidadecev import moeda
from exe112.utilidadecev import dados

preço = dados.leiadinheiro('Digite o valor do preço: R$')
moeda.resumo(preço, 20, 12)
