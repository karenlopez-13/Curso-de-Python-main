# -*- coding: utf-8 -*-
from typing import Final

print("Datos de la persona: ")
# Obtener el nombre de la persona
nombre_persona = input("Ingresa tu nombre: ")
nombre_empresa = "Blogic"
edad_empresa = 10
print(" Hola " + nombre_persona + " bienvenido " + nombre_empresa + " gracias por ser parte estos " + str(edad_empresa) + " años")

#Constante en python (las constantes siguen siendo variables por eso podemos modificar el valor)
#Todos los nombres de las constantes deben iniciar en mayúsculas
IVA= 1.16

"""
Esto es 
un texto
bastante
largooooo
"""

#lo que capture el usuario que es string lo pase a int 
#PARSEO
precio_producto = int(input("Ingresa el monto del producto: "))

#con esto sabemos el tipo de dato:
print(type(IVA))

precio_total = precio_producto * IVA

#variable string con el indice 0
resultado = "El costo total del producto es: {0}, con un subtotal de: {1}"

#el precio total es el indice 0, el precio producto es el indice 1
print(resultado.format(precio_producto, precio_total))

#Descuento (operación lógica) todas las operaciones lógicas nos regresan un true o un false
#Retorna true si el valor es mayor a $150
tiene_descuento = 0

print(type(tiene_descuento))
#imprimir el tipo de dato de la variable "tiene_descuento"

tiene_descuento = (precio_total >= 150)
print(type(tiene_descuento))

print("Tu producto tiene descuento?: " + str(tiene_descuento))

#espere un input (escribir)
input()
