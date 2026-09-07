""" 
try:
  # código a ser executado. Caso uma exceção seja lançada, pare imediatamente
except:
  # Se uma exceção for lançada no try, rode esse código, senão pule esta etapa
else:
  # Se não houver uma exeção lançada pelo try, rode essa parte
finally:
  # Rode essa parte (com ou sem exceção)

raise NomeDoErro("mensagem_desejada")
#cria as suas próprias exceções para determinados comportamentos que deseja no código.
"""
""" Desafio 1: Consertando a Divisão de Lucros
Você recebeu um dicionário onde a chave é o nome da filial e o valor é uma lista contendo: 
[Lucro Mensal, Número de Funcionários]. O objetivo do código abaixo é imprimir a meta de lucro por 
funcionário de cada filial. Mas, se você rodar isso, o código vai quebrar feio. Imagine que você 
precisa guardar os nomes das filiais problemáticas — tanto aquelas com ZeroDivisionError quanto as 
com TypeError — para mandar num relatório à engenharia no final do processo. Como você modificaria 
esse código para ir guardando e acumulando essas filiais defeituosas em uma lista chamada 
filiais_com_erro = [] e exibindo-a apenas uma vez no fim da execução?"""
from typing import TypeAlias

DadosFiliais: TypeAlias = dict[str, list[int | None]]
FiliaisErro: TypeAlias = dict[str,tuple[str, str]]

dados_filiais: DadosFiliais = {
    "SP": [100000, 20],
    "RJ": [50000, 10],
    "MG": [30000, 0], # Filial recém-aberta, ainda sem funcionários no sistema
    "AM": [70000, None], # Filial com erro ao cadastrar funcionários no sistema
    "ES": [40000, 8]
}
#como você faria lá dentro dos blocos except para atribuir o erro diretamente à chave do dicionário,
#sem usar .append() (já que dicionários puros não têm append)?
filiais_com_erro: FiliaisErro = {}

for (filial, [lucro,funcionarios]) in dados_filiais.items():
  try:
    meta_por_funcionario = lucro / funcionarios
  except ZeroDivisionError as err:
    filiais_com_erro[filial]=(str(err),"Filial com 0 funcionários")
  except TypeError as err:
    filiais_com_erro[filial]=(str(err),"Filial com valor de funcionários não definido")
  else:
    print(f"Filial {filial}: Meta de R$ {meta_por_funcionario} por funcionário.\n")
    
print('Log filiais com erros:', filiais_com_erro,'\n')
print('Consulta filial by key:', filiais_com_erro["MG"])
