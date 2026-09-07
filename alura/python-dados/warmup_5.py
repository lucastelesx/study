# 1- escrever um código que pegue uma lista de nomes e tente imprimir apenas o primeiro nome de cada string
nameList= ['lucas teles rosa','daniela nakatani goncalves','','   ',123]

first_names= [str(name).split()[0].capitalize() for name in nameList if str(name).strip() ]

# print(first_names)

# 2- crie um código para gerar uma lista que armazena o terceiro elemento de cada tupla contida na seguinte lista de tuplas:
lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]

newList = [item[-1] for item in lista_de_tuplas]
# print(newList)
# Alternative
# tupla=[]
# for tupla in lista_de_tuplas:
#   lista.append(tupla[2])

# 3. A partir da lista Dada, escreva um código que organize esses dados em pares. Cada par deve conter o índice (posição) e o nome correspondente."
lista_pares = ['  Pedro  ', '', 'Júlia', '   ', 'Otávio', 'Eduardo']

ordered_list= { 
    #int(item): lista_pares[item] 
    #for item in range(len(lista_pares))
    index: value.strip() 
    for index, value in enumerate(lista_pares)
    if str(value).strip()
}
# print(ordered_list)

# 4. Crie uma lista usando o list comprehension que armazena somente o valor numérico de cada tupla caso o primeiro elemento seja 'Apartamento', a partir da seguinte lista de tuplas:
aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]

valorApartamentos= [ 
    # aluguel[item][1] 
    # for item in range(len(aluguel)) 
    # if aluguel[item][0] == 'Apartamento'
    valor_reais
    for tipo_imovel, valor_reais in aluguel
    if tipo_imovel == 'Apartamento'
]
# print(valorApartamentos)

# 5. Crie um dicionário usando o dict comprehension em que as chaves estão na lista meses e o e os valores estão em despesa:
from typing import TypeAlias

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']  
despesas= [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]

ValorDespesaMes: TypeAlias = dict[str, int]

dict_despesa_mes: ValorDespesaMes = {
    mes: despesa
    for mes,despesa in zip(meses, despesas)
    # meses[index]: despesas[index]
    # for index,value in enumerate(meses)
}
# print(dict_despesa_mes)

# 6. Uma loja possui um banco de dados com a informação de venda de cada representante e de cada ano e precisa filtrar somente os dados do ano 2022 com venda maior do que 6000. A loja forneceu uma amostra contendo apenas as colunas com os anos e os valores de venda para que você ajude a realizar a filtragem dos dados a partir de um código. Crie uma lista usando list comprehension para filtrar os valores de *2022* e que sejam maiores que *6000*.

vendas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]

ListVendas2022: TypeAlias = list[tuple[str, int]]

vendas2022: ListVendas2022 = [
    (ano,valor)
    for ano,valor in vendas
    if ano == '2022' and valor > 6000
]
# print(list(vendas2022))
"""7. Uma clínica analisa dados de pacientes e armazena o valor numérico da glicose em um banco de dados e gostaria de rotular os dados da seguinte maneira:

Glicose igual ou inferior a 70: 'Hipoglicemia'
Glicose entre 70 a 99: 'Normal'
Glicose entre 100 e 125: 'Alterada'
Glicose superior a 125: 'Diabetes'
A clínica disponibilizou parte dos valores e sua tarefa é criar uma lista de tuplas usando list comprehension contendo o rótulo e o valor da glicemia em cada tupla."""
glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]

ListResult: TypeAlias = list[tuple[str,int | float]]

def check_criterio(value):
    if value < 71:
        return "Hipoglicemia"
    if value < 100:
        return "Normal"
    if value < 125:
        return "Alterada"
    
    return "Diabetes"

result_List: ListResult = [
    (check_criterio(value_glicemia),value_glicemia)
    for value_glicemia in glicemia
]
print(result_List)
# result: ListResult = [
#   ('Hipoglicemia',value) if value <= 70 else ('Normal',value) if value in range(71,100) 
#   else ('Alterada',value) if value in range(100,125) else 
#   ('Diabetes',value) if value > 125 else ('not included',value)
#   for value in glicemia ]