""" 9. Uma empresa possui filiais espalhadas nos Estados da região 
  Sudeste do Brasil. 
  - Em uma das tabelas de cadastro das filiais há uma coluna 
  contendo a informação de qual é o Estado a que pertence: 
  - A empresa sempre está abrindo novas filiais, de modo que a tabela está 
  constantemente recebendo novos registros e o gestor gostaria de possuir 
  a informação atualizada da quantidade de filiais em cada Estado.
  - A partir da coluna com a informação dos Estados, crie um dicionário usando 
  dict comprehension com a chave sendo o nome de um Estado e o valor sendo a 
  contagem de vezes em que o Estado aparece na lista.
  - Dica: Você pode fazer um passo intermediário para gerar uma lista de listas 
  em que cada uma das listas possui o nome de apenas um Estado com valores repetidos."""

""" Primeiro filtrar a lista de estados
listaFiltrada=list(set(estados))

Utilizando o dict Comprehension posso:
- contar o numero de filiais com base na listaFiltrada
dict={
  filial: n vezes que aparece
}
"""
from email.policy import strict
from typing import TypeAlias

ListEstados: TypeAlias = list[str]
CountDictFiliais: TypeAlias = dict[str,int]

estados: ListEstados = [
  'SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 
  'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG'
]

#filtered_estados: ListEstados = list(set(estados))
def info_estados():
  for estado in estados:
    print('here')

  

# count_dict_filiais: CountDictFiliais= {
#   estado_filial: estados.count(estado_filial)
#   for estado_filial in filtered_estados
# }

# print(count_dict_filiais)
""" frutas_na_esteira = ['maçã', 'maçã', 'banana', 'banana']
quantidade_anotada = {}
for fruta in frutas_na_esteira:
  if fruta not in quantidade_anotada:
    quantidade_anotada[fruta]=1
  else:
    quantidade_anotada[fruta]+=1
print(dict(quantidade_anotada)) """

# Como você faria para alterar esse nosso código para que ele consiga ignorar 
# magicamente esses dados "lixo" (ou seja: espaços contínuos " ", 
# strings vazias "" e nulos/None) e contasse apenas os estados 
# que realmente importam?
estados_sujos = ['SP', 'MG', '', 'SP', ' ', None, 'RJ']

estados_limpos= [
  estado
  for estado in estados_sujos
  if estado and estado.strip()
]
print(estados_limpos)
