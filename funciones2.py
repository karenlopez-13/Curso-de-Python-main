# importar el sistema opertaivo
import os
import random
import time
os.system('color')


def limpiar_pantalla() -> None:
    if(os.name == 'posix'):
        os.system("clear")
    else:
        os.system('cls')


def generar_caracter():
    numero = random.randint(33, 125)
    poner_espacio = random.choice([True, True, False])
    if(poner_espacio):
        return " "
    else:
        return chr(numero)


def generar_linea(letras_por_fila):
    linea = ""
    for position in range(letras_por_fila):
        linea = linea+generar_caracter()
    return linea


def generar_lista_lineas(letras_por_fila, lineas):
    lista_lineas = []
    for lineas in range(lineas):
        valor_retornado = generar_linea(letras_por_fila)
        lista_lineas.append(valor_retornado)
    return lista_lineas


limpiar_pantalla()
letras_por_fila, lineas = os.get_terminal_size()
lista_generada = generar_lista_lineas(letras_por_fila, lineas)
VERDE = '\033[0;32m'
print(VERDE)

while(True):
    for linea in lista_generada:
        print(linea)
    ultima_linea = lista_generada.pop()
    lista_generada.insert(0, ultima_linea)
    time.sleep(0.1)