import matplotlib.pyplot as plt
import csv

x = []
y = []

#Bloques de codigos seguros
with open('edades.csv', 'r') as archivo_csv:
    lineas = csv.reader(archivo_csv, delimiter=',')

    for linea in lineas:
        x.append(linea[0])
        y.append(int(linea[2]))

plt.bar(x, y, color= 'g', width=0.72, label= "Edad")
plt.xlabel('Nombre')
plt.ylabel('Edad')
plt.title('Edades del equipo')
plt.legend()
plt.show()

x = []
y = []

with open('clima.csv', 'r') as archivo_csv:
    lineas = csv.reader(archivo_csv, delimiter=',')

    for linea in lineas:
        x.append(linea[0])
        y.append(linea[1])

plt.plot(x, y, color= 'g', linestyle= 'dashed',
        marker= 'o', label= 'Clima ultimos 30 días')
plt.xticks(rotation= 25)
plt.xlabel('Fechas')
plt.ylabel('Temperatura (°C)')
plt.title('Reporte del clima', fontsize = 20)
plt.grid()
plt.legend()
plt.show()