import pyodbc 

SERVIDOR = 'tcp:198.38.83.200'
BASE_DATOS = 'aruizc_python'
USUARIO = 'aruizc_python_usr'
PASSWORD = 'Hola123'

def run():
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + SERVIDOR 
                            + ';DATABASE=' + BASE_DATOS + ';UID=' + USUARIO + ';PWD=' + PASSWORD)
    cursor = conexion.cursor()

    cursor.execute('SELECT @@version;')
    registro = cursor.fetchone() #trae el primer elemento
    while registro:
        print(registro[0])
        registro = cursor.fetchone()

    cursor.execute('SELECT * FROM Alumno')
    registros = cursor.fetchall()

    objetos = []
    nombres_columnas = [columna[0] for columna in cursor.description]
    for registro in registros:
        objetos.append(dict(zip(nombres_columnas, registro))) #mapeo en formato de un diccionario
    print(objetos)

    #INSERT
    numeros_registros = cursor.execute("INSERT INTO Alumno(ID,Nombre,Paterno,Materno,Edad) VALUES(61, 'Karen', 'Lopez', 'Rodriguez', 21)")
    conexion.commit()
    print(f'Se han insertado {str(numeros_registros)} registros')
    cursor.close()
    conexion.close()

if __name__ == '__main__':
    run()