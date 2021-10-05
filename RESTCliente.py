import requests
import logging
import json

#importar archivos locales
from constantes import *
from modelos import *

logging.basicConfig(filename='client-rest.log', level=logging.INFO)

def run():
    logging.info('Inicia la ejecución')
    logging.info(f'Consulta a {URL_SERVICIO}')
    try:
        respuesta = requests.get(URL_SERVICIO)
    except requests.ConnectionError as error:
        logging.error(f'Ha ocurrido un error al consultar {URL_SERVICIO} Descripción: {error.strerror}')
    except requests.Timeout as error:
        logging.error(f'La petición a {URL_SERVICIO} no responde timeout')
    except:
        logging.error(f'Ha ocurrido un error inesperado')

    logging.error(f'Esto es un error programado')

    print(respuesta)
    print(str(respuesta.content)) #Regresar el contenido de la respuesta como arreglo bytes
    print(respuesta.text) #Retorna la respuesta en formato de texto como string
    print(respuesta.json()) #Retora la respuesta en formato json

    #Validar HTTO Code
    if(respuesta.status_code == 200):
        logging.info(f'Respuesta de {URL_SERVICIO} : {respuesta.json()}')
        diccionario = json.loads(respuesta.text) #loads recibre un string, load pide un filepath (archivo local)
        respuesta_satelite = RespuestaSatelite(**diccionario) #el doble asterisco es la llave valor, un solo asterisco es por cantidad o por posición
        print(respuesta_satelite.people[0]['name'])
        persona = Persona(**respuesta_satelite.people[0])
        print(persona)

    elif(respuesta.status_code == 404):
        logging.warning(f'Ha ocurrido un error en la consulta {URL_SERVICIO}')
        logging.error(f'Ha ocurrido un error en la consulta {URL_SERVICIO}')

#Entre point
if __name__ == '__main__':
    run()