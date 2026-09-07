from typing import TypeAlias

ListResumo: TypeAlias = list[str]
ListNotas: TypeAlias = list[float | int]
DictCadastro: TypeAlias = dict[str, list[ListNotas] | ListNotas | list[str] ]

lista_completa = [
    [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')],
    [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]],
    [9.0, 7.3, 5.8, 6.7, 8.5],
    ['Aprovado', 'Aprovado', 'Reprovado', 'Aprovado', 'Aprovado']]

lista_resumo_Aluno: ListResumo = ["Notas", "Media Final", "Situação"]


cadastro: DictCadastro = {
    lista_resumo_Aluno[i]: lista_completa[i+1] 
    for i in range(len(lista_resumo_Aluno))
}
print(cadastro,"\n\ndict_cadastro")

cadastro["Estudante"] = [lista_completa[0][i][0] for i in range(len(lista_completa[0]))]
print(cadastro["Estudante"])

cadastro["ID_Matricula"]= [lista_completa[0][i][1] for i in range(len(lista_completa[0]))]
print(cadastro["ID_Matricula"])
""" {
    "Notas": [
        [8.0, 9.0, 10.0],
        [9.0, 7.0, 6.0],
        [3.4, 7.0, 7.0],
        [5.5, 6.6, 8.0],
        [6.0, 10.0, 9.5],
    ],
    "Media Final": [9.0, 7.3, 5.8, 6.7, 8.5],
    "Situação": ["Aprovado", "Aprovado", "Reprovado", "Aprovado", "Aprovado"],
}
 """