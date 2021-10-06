from os import access
import re
import requests
import logging
import json
import configparser

from requests.models import HTTPBasicAuth

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

    #Parametros en petición
    #http://api.blogic.com.mx/api?lat=123.23&lon=221.23
    parametros = { 'lat' : '45', 'lon': '180' }
    logging.info(f'Consulta a {URL_SATELITE} con los parametros {parametros}')
    respuesta = requests.get(URL_SATELITE, params=parametros)
    print(respuesta.json())

    #Ejemplo POST
    datos = {'llave' : 'valor'} #diccionario
    logging.info(f'Consulta a {MOCK_POST_URL}')
    respuesta = requests.post(MOCK_POST_URL, data=datos)
    print(respuesta.text)

    #Acceder a los headers
    print(respuesta.headers['date'])
    print(respuesta.headers)

    #Autenticación con GitHub
    logging.info(f'Extrayendo información de configuración')
    parser = configparser.ConfigParser() #instancia a una clase
    parser.read(ENVIROMENT_DEV)
    usuario = parser.get('credenciales', 'usuario')
    password = parser.get('credenciales', 'password')

    respuesta = requests.post(URL_GITHUB, auth=HTTPBasicAuth(username=usuario, password=password)) #forma llave valor
    print(respuesta.json())

    #Envio de encabezados 
    access_token = parser.get('tokens','github')
    encabezados = { 'Authorization' : f'Bearer {access_token}'}
    respuesta = requests.get(URL_ACCESS_TOKEN, headers=encabezados)
    print(respuesta.json())

    #utilizando sessions para la persistencia de token
    sesion = requests.Session()
    sesion.headers.update({ 'Authorization' : f'Bearer {access_token}'})
    respuesta = sesion.get(URL_ACCESS_TOKEN)
    print(respuesta.json())
    respuesta = sesion.post(MOCK_POST_URL, data=datos)
    print(respuesta.json())

#Entre point
if __name__ == '__main__':
    run()