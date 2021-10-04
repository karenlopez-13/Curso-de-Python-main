#TUPLAS

#los corchetes indican lista y los parentesis tuplas(las tuplas son estáticas)
lista_autos = [
    ("Rojo", "4859-A", "P"),
    ("Azul", "2901-Z", "T"),
    ("Verde", "1892-B", "P")
]

#Vamos a ordenar por placa, la funcion sorted significa ordenado
#la funcion lambda o anonima
# auto[1] esto va a ordenar por placa
lista_autos_ordenada = sorted(lista_autos, key=lambda auto : auto[1])
print(lista_autos_ordenada)
lista_autos_ordenada_color = sorted(lista_autos, key=lambda auto : auto[0])
print(lista_autos_ordenada_color)

lista_numeros = [9, 432, 34, 1, 5, 3, 2, 4, 6]
lista_numeros_ordenada = sorted(lista_numeros, reverse=True)
print(lista_numeros_ordenada)

#DICCIONARIO DE AUTOS
diccionario_autos = [
    {"color" : "Rojo", "placa" : "4859-A", "tipo" : "P"},
    {"color" : "Azul", "placa" : "2901-Z", "tipo" : "T"},
    {"color" : "Negro", "placa" : "1892-B", "tipo" : "P"}
]

diccionario_ordenado = sorted(diccionario_autos, key=lambda auto : auto["color"])
print(diccionario_ordenado)

#Comprensión de listas
#utilizamos la lista y generamos una operacion en esa lista
lenguajes_programación = [
    "python",
    "c#",
    "php",
    "c",
    "c++",
    "swift",
    "java",
    "kotlin"
]

#QUEREMOS PONER LOS ELEMENTOS DE LA LISTA DE LENGUAJES_PROGRAMACION EN MAYUSCULA Y PARA ESO SON 2 OPCIONES

#1 OPCION
lista_mayusculas = []
for lenguaje in lenguajes_programación:
    lista_mayusculas.append(lenguaje.upper())
print(lista_mayusculas)

#2 OPCION
lista_comprension = [lenguaje.upper() for lenguaje in lenguajes_programación]
print(lista_comprension)

#ENCONTRAR MULTIPLOS DEL 5 con lista de comprension
lista_multiplos_5 = [numero for numero in range(1, 101) if numero % 5 == 0]
print(lista_multiplos_5)

#ENCONTRAR MULTIPLOS DEL 5 con programacion funcional
multiplos_5 = list(filter(lambda numero : numero % 5 == 0, range(1, 101)))
print(multiplos_5)

nombres_1 = ["Karen", "Victor", "Ernesto", "Juan", "Antonio"]
nombres_2 = ["Francisco", "Angel", "Ernesto", "Karen", "Christian"]

#Iteracion multiples listas
#Opcion 1
en_comun = [nombre_1 for nombre_1 in nombres_1 for nombre_2 in nombres_2 if nombre_1 == nombre_2]
print(en_comun)

lista_en_comun = []
for nombre_1 in nombres_1:
    for nombre_2 in nombres_2:
        if nombre_1 == nombre_2:
            lista_en_comun.append(nombre_1)
            
print(lista_en_comun)