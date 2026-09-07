"""10.Nessa mesma tabela de cadastro de filiais, há uma coluna
com as informações da quantidade de pessoas colaboradoras e o(a) gestor(a)
gostaria de ter um agrupamento da soma dessas pessoas para cada estado.
As informações contidas na tabela são: A partir da lista de tuplas,
crie um dicionário em que as chaves são os nomes dos Estados únicos e os
valores são as listas com o número de colaboradores(as) referentes ao Estado.
Crie também um dicionário em que as chaves são os nomes dos Estados
e os valores são a soma de colaboradores(as) por Estado.
"""
"""
Imagine que o nosso RH puxou o arquivo funcionarios de um banco de dados legado bem sujo. Algumas filiais vieram com a quantidade corrompida, aparecendo como nulas (None)... Exemplo: ("SP", 16), ("RJ", None), ("MG", 9)...
Se o seu código rodar do jeito que está agora e tentar fazer um lista.append(None) e depois rodar o nosso Dictionary Comprehension com sum(), ele vai dar um baita erro porque o Python não sabe somar inteiros com nulos.
O Desafio: Sem mudar quase nada na sua lógica, que alteração simples você faria lá no seu laço for original para garantir que ele proteja a integridade dos nossos dados e simplesmente ignore qualquer tupla que venha com um valor nulo?
"""
from typing import TypeAlias

EstadoFuncionario: TypeAlias = list[tuple[str, int | None]]
FuncionarioPorEstado: TypeAlias = dict[str, list[int]]
TotalFuncionariosPorEstado: TypeAlias = dict[str,int]

funcionarios: EstadoFuncionario = [
  ("SP", 16), ("ES", 8), ("MG", 9), ("MG", 6), ("SP", 10), ("MG", 4), ("ES", 9), ("ES", 7), 
  ("ES", 12), ("SP", 7), ("SP", 11), ("MG", 8), ("ES", 8), ("SP", 9), ("RJ", 13), ("MG", 5), 
  ("RJ", 9), ("SP", 12), ("MG", 10), ("SP", 7),("ES", 14), ("SP", 10), ("MG", 12)
]

funcionarios_por_estado: FuncionarioPorEstado = {}

for estado, quantidade in funcionarios:
  if quantidade is None:
    continue

    if estado not in funcionarios_por_estado:
      funcionarios_por_estado[estado] = [quantidade]
    else:
      funcionarios_por_estado[estado].append(quantidade)

# print('Funcionarios por Estado:\n',funcionarios_por_estado,'\n')

total_funcionarios_por_estado: TotalFuncionariosPorEstado = {
  estado:sum(lista_quantidade)
  for estado,lista_quantidade in funcionarios_por_estado.items()
}
# print('Total Funcionarios por Estado:\n',total_funcionarios_por_estado)

# Resolução do curso
estados_unicos = list(set([
  estado[0] 
  for estado in funcionarios
]))
#print(estados_unicos)
"""
("SP", 16), ("ES", 8), ("MG", 9), ("MG", 6), ("SP", 10), ("MG", 4), ("ES", 9), ("ES", 7), 
  ("ES", 12), ("SP", 7), ("SP", 11), ("MG", 8), ("ES", 8), ("SP", 9), ("RJ", 13), ("MG", 5), 
  ("RJ", 9), ("SP", 12), ("MG", 10), ("SP", 7),("ES", 14), ("SP", 10), ("MG", 12)
  ['RJ', 'ES', 'MG', 'SP']
"""
## Criando uma lista de listas com valores de funcionários de cada estado
estado_quantidade_funcionarios = []
for estado in estados_unicos:
  lista = [
    tupla[1] 
    for tupla in funcionarios 
    if tupla[0] == estado
  ]
  estado_quantidade_funcionarios.append(lista)

#print(estado_quantidade_funcionarios)
"""[
  [13, 9],
  [9, 6, 4, 8, 5, 10, 12],
  [16, 10, 7, 11, 9, 12, 7, 10],
  [8, 9, 7, 12, 8, 14]
]"""
## Criando um dicionário com dados agrupados de funcionário por estado
agrupamento_por_estado = {
  estados_unicos[i]: estado_quantidade_funcionarios[i] 
  for i in range(len(estados_unicos))
}
#print(agrupamento_por_estado)
""" {
  "RJ": [13, 9],
  "ES": [8, 9, 7, 12, 8, 14],
  "SP": [16, 10, 7, 11, 9, 12, 7, 10],
  "MG": [9, 6, 4, 8, 5, 10, 12],
} """

## Criando um dicionário com a soma de funcionários por estado
soma_por_estado = {
  estados_unicos[i]: sum(estado_quantidade_funcionarios[i]) 
  for i in range(len(estados_unicos))
}
#print(soma_por_estado)
# {"RJ": 22, "ES": 58, "SP": 82, "MG": 54}
