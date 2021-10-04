#Posibles posiciones: CENTRO / DERECHA / IZQUIERDA
posicion_jugador = "CENTRO"
tiene_llave = False
puerta_abierta = False

print("BIENVENIDO AL JUEGO DEL CALABOZO")

while (True):    
    print("MENU OPCIONES")

    #SALA CENTRAL
    if(posicion_jugador == "CENTRO"):
        print("Estas en la sala CENTRAL")
        print("- DERECHA")
        print("- IZQUIERDA")
        seleccion = input("Selecciona una opción: ")
        if(seleccion == "IZQUIERDA"):
            posicion_jugador = "IZQUIERDA"
        elif (seleccion == "DERECHA"):
            posicion_jugador = "DERECHA"
        else:
            print("Opción invalida")

    # SALA IZQUIERDA (LLAVE)
    elif (posicion_jugador == "IZQUIERDA"):
        print("Estas en la sala IZQUIERDA")
        print("Te encuentras en el cuarto donde está la llave para poder abrir la puerta que está en la derecha")
        print("- DERECHA")
        if(tiene_llave == False):
           print("- RECOGER [Llave detectada]")
        seleccion = input("Selecciona una opción: ") 

        if(seleccion == "DERECHA"):
            posicion_jugador = "CENTRO"
        if(seleccion == "RECOGER" and tiene_llave == False): 
            tiene_llave = True
            print("Has obtenido: LLAVE")
        else: 
            print("Opción invalida")

    # SALA DERECHA (PUERTA)
    elif (posicion_jugador == "DERECHA"):
        print("Estas en la sala DERECHA")
        print("- IZQUIERDA")
        if(tiene_llave == True):
           print("- USAR [LLAVE]")
        seleccion = input("Selecciona una opción: ")
        if(seleccion == "IZQUIERDA"):
           posicion_jugador = "CENTRO"
        elif(seleccion == "USAR" and tiene_llave == True):
            print("Felicidades! Has logrado salir")
            print("GAME_OVER")
            input()
            exit()
        else:
            print("Opción invalida")

    else:
        print("Sala incorrecta")
        seleccion = input("Presiona cualquier tecla para salir")  