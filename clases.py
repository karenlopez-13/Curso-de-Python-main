import time

#vamos a generar una clase
#cuando creamos una clase sin argumentos es que NO hereda o no implementa
class Persona:
    #Todas las funciones dentro de un obejto requieren la referencia de ellos "self"
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    #f es el formato
    def saludar(self, persona) -> str:
        return f'Hola {persona} mi nombre es {self.nombre}'

    #funcion especial
    def __str__(self) -> str:
        #return f'{self.nombre} tengo {self.edad} años'
        return f'{self.nombre}'

    def __eq__(self, o: object) -> bool:
        return self.nombre == o.nombre and self.edad == o.edad

    #funcion privada
    def __dormir(self) -> None:
        print(f'ire a dormir {self.nombre}')

    def __del__(self):
        self.__dormir()

class Empleado:
    #metodo de inicialización
    def __init__(self) -> None:
        pass

    #se agrega el parametro self siempre que esten dentro de una clase
    def trabajar(self):
        print("Iré a trabajar")
        time.sleep(1)
        print("Termine de trabajar")

#cuando creamos una clase con argumentos es que SI hereda e implementa
class Desarrollador(Persona, Empleado):
    #constructor
    def __init__(self, nombre, edad, cargo):
        super().__init__(nombre, edad)
        self.cargo = cargo
    
    def estudiar(self):
        print('Estudiar maestria')

class MultiConstructor:

    def __init__(self, *args) -> None:
        
        if len(args) > 1:
            self.acumulado = 0
            for i in args:
                self.acumulado += i

        elif isinstance(args[0], int):
            self.cuadrado = args[0]*args[0]

        elif isinstance(args[0], str):
            self.nombre = f"Hola {args[0]} !"

def run():
    karen = Desarrollador('Karen', 21, 'Ingeniera en Software')
    alter_karen = Persona('Karen', 21)
    jose = Persona('Jose', 21)
    hector = Persona('Hector', 17)

    print(karen.saludar(jose))
    print(jose.saludar(hector))
    print(karen == alter_karen)

    karen.trabajar()
    karen.estudiar()

    print(isinstance(karen, Persona)) #valida si es instancia de la clase Persona
    print(isinstance(karen, str))
    #print(karen is int)

    instancia_1 = MultiConstructor(1,2,3,4,5)
    print(f"El acumulado es {instancia_1.acumulado}")

    instancia_2 = MultiConstructor(5)
    print(f"El cuadrado de 5 es {instancia_2.cuadrado}")

    instancia_3 = MultiConstructor("Ana")
    print(f"Como string {instancia_3.nombre}")

if __name__ == "__main__":
    run()

#DECORADOR es una funcion que le pasamos como argumento una funcion
def medir_tiempo(nombre_funcion):
    def medicion(funcion):
        def wrapper(*args, **kargs): #el primer asterisco manda n cantidad de argumentos, el asterisco doble lo hace de forma explicita
            inicio = time.time()
            resultado = funcion(*args, **kargs)
            tiempo_total = time.time() - inicio
            print(f'La funcion {nombre_funcion} tomó {tiempo_total} segundos')
            return resultado
        return wrapper
    return medicion

@medir_tiempo(nombre_funcion="loop") #DECORADOR
def loop():
    for i in range(0,1000):
        print(i)

loop()