#Metodos especiales y cuando hay 1 o 2 guiones bajos son metodos privados
nombre = "Karen Lopez"
print("Primero")
print(nombre[2:4:2])

#strip quita los espacios de una cadena de texto ejemplo: "blusa azul" pasa a "blusaazul"
#no jalo el strip así que pusimos en su lugar "replace"
#lower lo hace minuscula
def valida_palindromo(palabra):
    palabra = str(palabra).replace(" ", "").lower()
    return(palabra == palabra[::-1]) #corta la palabra desde el inicio hasta el fin y vete en pasos de -1 [inicial:final:pasos]

def palindromo(palabra):
    palabra = palabra.replace("", "")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False

def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = valida_palindromo(palabra)
    if(es_palindromo):
        print(f'La palabra {palabra} es un palindromo')
    else:
        print(f'La palabra {palabra} no es un palindromo')

#Entry point 
if __name__ == '__main__':
    run()