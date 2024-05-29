
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
from scipy import stats

archivoXl = pd.read_excel(r'Conjunto_datos_proyecto3.xlsx')
datos_i = np.array(archivoXl['Inicial'])
datos_1 = np.array(archivoXl['Primer_cambio'])
datos_2 = np.array(archivoXl['Segundo_cambio'])

# Histograma para cada muestra de datos
n = 90
clases = math.ceil(math.sqrt(n))

# Histograma para muestra inicial
min_iniciales = min(datos_i)
print("mínimo de la muestra inicial: ",min_iniciales)
plt.figure()
plt.hist(datos_i,bins=clases,edgecolor='black')
plt.xlabel('Rendimiento')
plt.ylabel('Frecuencia')
plt.title('Datos iniciales')

# Histograma para el primer cambio
min_primer_cambio = min(datos_1)
print("mínimo del primer cambio: ",min_primer_cambio)
plt.figure()
plt.hist(datos_1,bins=clases,edgecolor='black')
plt.xlabel('Rendimiento')
plt.ylabel('Frecuencia')
plt.title('Primer cambio')

# Histograma para el segundo cambio
min_segundo_cambio = min(datos_2)
print("mínimo del segundo cambio: ",min_segundo_cambio,'\n')
plt.figure()
plt.hist(datos_2,bins=clases,edgecolor='black')
plt.xlabel('Rendimiento')
plt.ylabel('Frecuencia')
plt.title('Segundo cambio')

# Ajustar los datos a una normal, estimando la media y la desviacion estandar


print("Estimacion de la media y desviacion estandar",'\n')
#----------------------------------------------------------------------------
print('Rendimiento de la maquina inicial')
loc_inicial, scale_inicial = stats.norm.fit(datos_i)
print(f'Estimacion de la media: {loc_inicial}')
print(f'Estimacion de la desviacion estandar: {scale_inicial}','\n')
#----------------------------------------------------------------------------
print('Rendimiento de la maquina en el primer cambio')
loc_cambio1, scale_cambio1 = stats.norm.fit(datos_1)
print(f'Estimacion de la media: {loc_cambio1}')
print(f'Estimacion de la desviacion estandar: {scale_cambio1}','\n')
#----------------------------------------------------------------------------
print('Rendimiento de la maquina en el segundo cambio cambio')
loc_cambio2, scale_cambio2 = stats.norm.fit(datos_2)
print(f'Estimacion de la media: {loc_cambio2}')
print(f'Estimacion de la desviacion estandar: {scale_cambio2}','\n')
#----------------------------------------------------------------------------

# Realizar la prueba t de una muestra

print('prueba t','\n')
#----------------------------------------------------------------------------
print('prueba t de los datos iniciales')
t_stat_i, p_value_i = stats.ttest_1samp(datos_i, 70, alternative='greater')

print(f'Estadístico t: {t_stat_i}')
print(f'Valor p: {p_value_i}','\n')
#----------------------------------------------------------------------------
print('prueba t del primer cambio')
t_stat_1, p_value_1 = stats.ttest_1samp(datos_1, 70, alternative='greater')

print(f'Estadístico t: {t_stat_1}')
print(f'Valor p: {p_value_1}','\n')
#----------------------------------------------------------------------------
print('prueba t del segundo cambio')
t_stat_2, p_value_2 = stats.ttest_1samp(datos_2, 70, alternative='greater')

print(f'Estadístico t: {t_stat_2}')
print(f'Valor p: {p_value_2}')

#mostrar los graficos
plt.show()
