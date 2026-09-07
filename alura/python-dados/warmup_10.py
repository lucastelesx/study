""" 
SETS:
- foo.isdisjoint(bar) no parametro pode ser utilizado (list, tuple, dictionary e string)
Compara dois conjuntos e verifica se eles tem pelo menos 1 elemento em comum. Pode ser utilizado

- set.intersection(foo,bar) or foo&bar 
É apenas o que eles têm em comum.

- set.union(foo,bar, {'one more'}) or foo | bar
Une os dois grupos, removendo duplicatas automaticamente

- foo.difference(bar) or foo - bar
Pega os elementos que estão no primeiro conjunto, mas NÃO estão no segundo.

- foo.symmetric_difference(bar) or foo ^ bar
Pega tudo o que é exclusivo de cada um.
  SomeSet= {'string'}
  - 'string' in SomeSet 
  -- output:True

- foo.update(bar) 
Cria um novo set e alterando o set Original.

*Os símbolos operadores (|, &, -, ^) sempre geram um conjunto novo e deixam os originais intactos.


Desafio: Imagine que você está cruzando os IDs dos clientes que compraram em duas campanhas de 
marketing diferentes. Só que, como de costume na vida real, os dados vêm "sujos" 
com duplicatas (IDs repetidos na mesma lista, porque o cliente fez duas transações).


Sua missão não é apenas fazer funcionar, mas pensar como um Analista de Dados e usar os sets que 
você acabou de estudar para responder a essas 3 perguntas de negócios:

- Clientes Únicos Globais: Como você obteria uma base de todos os clientes únicos que compraram 
conosco, considerando as duas campanhas e sem qualquer ID duplicado?
- Fidelidade (Retenção): Quem são os clientes ultra-fiéis que compraram tanto no verão quanto 
no inverno?
- Público Exclusivo de Verão: Quem foram os clientes que compraram apenas na campanha de verão e 
ignoraram a de inverno?
- Desafio extra de Integridade: Se essas listas vierem com alguma string vazia "" indicando 
um erro do sistema na hora da coleta, seu código que usa os operadores de set vai quebrar ou 
vai tratar ela como um elemento qualquer dentro do conjunto? Como você validaria isso?
"""
# Dados brutos recebidos do time de Marketing
from typing import TypeAlias
ClientesList: TypeAlias = list[str | None]
ClientsValidos: TypeAlias = set[str]

clientes_verao: ClientesList = ["", "  ","id_01", "id_03", "id_05", "id_03", "", "id_02", "id_01"]
clientes_inverno: ClientesList = ["id_02", "id_04", "id_05", "id_06","", None, "  "]

print('verao:',clientes_verao)
print('inverno:',clientes_inverno,'\n')

def clean_client_data(client_list: ClientesList) -> ClientsValidos:
  client_validos: ClientsValidos ={
    cliente
    for cliente in client_list
    if cliente and cliente.strip()
  }
  return client_validos

clientes_verao=clean_client_data(clientes_verao)
clientes_inverno=clean_client_data(clientes_inverno)
print('Dados limpos:\n',clientes_verao,'\n',clientes_inverno,'\n')

unique_clients=clientes_verao.union(clientes_inverno)
print('Clientes Únicos Globais:\n',unique_clients,'\n')

loyal_clients=clientes_verao.intersection(clientes_inverno)
print('Clientes fiéis:\n',loyal_clients,'\n')

summer_clients=clientes_verao.difference(clientes_inverno)
print('Clientes Exclusivos do Verão:\n',summer_clients)