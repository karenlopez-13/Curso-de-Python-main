#inicializamos lista
lista_nombres = ["Amed", "Karen", "Victor", "Antonio", "Ernesto", "Christian", "Angel"]

#constantes
#colores en la tabla de unicode, convierte el string a ese color
ROJO = "\033[0;31m"
VERDE = "\033[0;32m"
AZUL = "\033[0;34m"
FIN = "\033[0m"

#colores específicos para los nombres
lista_colores = [ROJO, VERDE, AZUL]

#Imprimir la lista con el ciclo while junto con una longitud(len)
while(len(lista_nombres) >0 ):
    color = lista_colores.pop(0)
    #pop extrae el último elemento y por eso le colocamos el indice 0 para que saque el primer nonbre
    nombre = lista_nombres.pop(0)
    #END: deja un espacio entre cada nombre mientras que el print hace un salto de línea después de cada uno de los nombres
    print(color + nombre, end=" " )
    #Asigna elementos a una lista(ciclamos la lista)
    lista_colores.append(color)

print(FIN)
print("Fin de la lista")
