#File de Pyton destinado a el proyecto 3 de probabilidad y estadistica

"""
Proyecto 3 Probabilidad y Esatdística
Creado por:
           Axel Dmitri Castillo Collao 2023154988
	   Felipe Sánchez Segura 2023083272
           Yair González Núñez 202304804
"""

# Importamos los módulos necesarios
import math
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

archivoXl = pd.read_excel(r'Conjunto_datos_proyecto3.xlsx')
datos_iniciales = np.array(archivoXl['Inicial'])
datos_primer_cambio = np.array(archivoXl['Primer_cambio'])
datos_segundo_cambio = np.array(archivoXl['Segundo_cambio'])

# Histograma para cada muestra de datos
n = 90
clases = math.ceil(math.sqrt(n))

# Histograma para muestra inicial
min_iniciales = min(datos_iniciales)
print("mínimo de la muestra inicial: ",min_iniciales)
plt.figure()
plt.hist(datos_iniciales,bins=clases,edgecolor='black')
plt.xlabel('Rendimiento')
plt.ylabel('Frecuencia')
plt.title('Datos iniciales')

# Histograma para el primer cambio
min_primer_cambio = min(datos_primer_cambio)
print("mínimo del primer cambio: ",min_primer_cambio)
plt.figure()
plt.hist(datos_primer_cambio,bins=clases,edgecolor='black')
plt.xlabel('Rendimiento')
plt.ylabel('Frecuencia')
plt.title('Primer cambio')

# Histograma para el segundo cambio
min_segundo_cambio = min(datos_segundo_cambio)
print("mínimo del segundo cambio: ",min_segundo_cambio)
plt.figure()
plt.hist(datos_segundo_cambio,bins=clases,edgecolor='black')
plt.xlabel('Rendimiento')
plt.ylabel('Frecuencia')
plt.title('Segundo cambio')
plt.show()
