# 8. Um e-commerce possui as informações de id de venda, quantidade vendida e preço do produto divididos nas seguintes listas id_venda,quantidade e preco.
# O e-commerce precisa estruturar esses dados em uma tabela contendo o valor total da venda, que é obtida multiplicando a quantidade pelo preço unitário.
# Além disso, a tabela precisa conter um cabeçalho indicando as colunas: 'id', 'quantidade', 'preco' e 'total'. Crie uma lista de tuplas em que cada tupla tenha id, quantidade, preço e valor total, na qual a primeira tupla é o cabeçalho da tabela.

'''Criar tabela com: 
- PEGAR valor_total_venda = quantidade_vendida * preco_produto 
- Estrutura da tabela: 
  -- Uma lista[] de tuplas() "tabela_vendas"
  -- Primeira tupla cabeçalho ('id','quantidade','preco','total')
  -- Depois lista de tuplas [(dadosHere,dadosHere,etc...),(etc...),(etc...)]

tabela_vendas= [
  ('id','quantidade','preco','total'),
  (id_value,quantidade_value,preco_value,total_value)
]
'''
'''
  Nas listas dadas (id,quantidade, etc) tenho o numero total de itens.
  Entao posso usar o indice de uma das listas para percorrer ela e assim
  conseguir trazer cada dado na tupla(
    dado1[indice],dado2[indice],dado3[indice],dado4[indice]
  )
  no dado4 preciso fazer a multiplicação
'''
from typing import TypeAlias

id_venda = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
quantidade_vendida = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
preco_produto = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]

tabelaVendas: TypeAlias = list[tuple[str | int | float, ...]]

cabecalho_vendas= ('id','quantidade','preco','total')
'''
  (
    id_venda[index],
    quantidade_vendida[index],
    preco_produto[index],
    quantidade_vendida[index]*preco_produto[index]
  )
  for index,value in enumerate(id_venda)
'''
dados_vendas=zip(id_venda,quantidade_vendida,preco_produto,strict=True)

tabela_vendas: tabelaVendas=[
  (id,quantidade,preco,quantidade*preco)
  for id,quantidade, preco in dados_vendas
  #if len(id) == len(list(dados_vendas)[index do loop????])
]
tabela_vendas.insert(0,cabecalho_vendas)
print(list(tabela_vendas))
""" [
    ("id", "quantidade", "preco", "total"),
    (0, 15, 93.0, 1395.0),
    (1, 12, 102.0, 1224.0),
    (2, 1, 18.0, 18.0),
    (3, 15, 41.0, 615.0),
    (4, 2, 122.0, 244.0),
    (5, 11, 14.0, 154.0),
    (6, 2, 71.0, 142.0),
    (7, 12, 48.0, 576.0),
    (8, 2, 14.0, 28.0),
    (9, 4, 144.0, 576.0)
] """

