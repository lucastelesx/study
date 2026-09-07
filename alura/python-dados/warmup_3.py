#1- escrever um código que pegue uma lista de nomes e tente imprimir apenas o primeiro nome de cada string
nameList= ['lucas teles rosa','daniela nakatani goncalves','','   ',123]

first_names= [str(name).split()[0].capitalize() for name in nameList if str(name).strip() ]

print(first_names)

#2- crie um código para gerar uma lista que armazena o terceiro elemento de cada tupla contida na seguinte lista de tuplas:
lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]