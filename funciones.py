#debemos importar un modulo que ya viene con el compilador, solo debemos ponerlo
#el import extrae todo, el from solo extrae una parte
import os

#importamos el modulo para generar un entero random
import random

import time

#indicamos que el color de nuestra terminal sea verde
os.system("color")

#definimos el alcance de una función
#la función va en minúsculas
#agregamos "notacion flecha" que significa que no va a retornar nada, solo va a validar el sistema operativo
def limpiar_pantalla() -> None:
    if(os.name == "posix"):
        os.system("clear")
    else:
        os.system("cls")

def generar_caracter() -> str:
    #utilizamos los codigos aski de 33 a 125
    numero = random.randint(33, 125)
    poner_espacio = random.choice([True, True, False])
    if(poner_espacio):
        return " "
    else:
        #coloca el numero de la tabla de aski y lo toma como si fuera un caracter
        return chr(numero)

def generar_linea(letras_por_fila: int) -> str:
    linea = ""
    for posicion in range(letras_por_fila):
        linea = linea + generar_caracter()
        return linea

def generar_lista_lineas(letras_por_fila, lineas):
    lista_lineas = []
    for linea in range(lineas):
        valor_retornado = generar_linea(letras_por_fila)
        lista_lineas.append(valor_retornado)
        return lista_lineas

limpiar_pantalla()
letras_por_fila, lineas = os.get_terminal_size()
lista_generada = generar_lista_lineas(letras_por_fila, lineas)
VERDE = "\033[0;32m"
print(VERDE)

#print(str(generar_caracter()))

while(True):
    for linea in lista_generada:
        print(linea)
    ultima_linea = lista_generada.pop(0)
    lista_generada.insert(0, ultima_linea)
    time.sleep(0.1)