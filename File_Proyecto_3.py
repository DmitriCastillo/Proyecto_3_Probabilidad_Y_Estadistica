#File de Pyton destinado a el proyecto 3 de probabilidad y estadistica

"""
Proyecto 3 Probabilidad y Esatdística
Creado por:
           Axel Dmitri Castillo Collao 2023154988
	   Felipe Sánchez Segura 2023083272
           Yair González Núñez 2023048047
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
plt.figure()
plt.hist(datos_i,bins=clases,edgecolor='black')
plt.xlabel('Rendimiento')
plt.ylabel('Frecuencia')
plt.title('Datos iniciales')

# Histograma para el primer cambio
plt.figure()
plt.hist(datos_1,bins=clases,edgecolor='black')
plt.xlabel('Rendimiento')
plt.ylabel('Frecuencia')
plt.title('Primer cambio')

# Histograma para el segundo cambio
plt.figure()
plt.hist(datos_2,bins=clases,edgecolor='black')
plt.xlabel('Rendimiento')
plt.ylabel('Frecuencia')
plt.title('Segundo cambio')

# Desviación estándar por MLE
# def estimador_sigma(pdatos):
    # """
    # Calcula el estimador de máxima verosimilitud para la desviación estándar de una muestra de datos.

    # Parámetros:
    # pdatos (list o numpy array): La muestra de datos.

    # Salida:
    # float: Estimador de la desviación estándar.
    # """
    # n = len(pdatos)
    # x = np.mean(pdatos)
    # suma_cuadrados = np.sum((pdatos - x) ** 2)
    # sigma = np.sqrt(suma_cuadrados / n)
    
    # return sigma
# sigma_2=estimador_sigma(datos_2)
# print(f"El estimador de la desviación estándar para el segundo cambio es: {sigma_2}")

# Realizar la prueba t de una muestra

#   Prueba de Hipotesis H_0: \mu = 70

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
print("")

#----------------------------------------------------------------------------

#   Prueba de Hipotesis H_0: \mu = 75
print('prueba t para un 75%','\n')
#----------------------------------------------------------------------------
print('prueba t de los datos iniciales')
t_stat_i, p_value_i = stats.ttest_1samp(datos_i, 75, alternative='greater')

print(f'Estadístico t: {t_stat_i}')
print(f'Valor p: {p_value_i}','\n')
#----------------------------------------------------------------------------
print('prueba t del primer cambio')
t_stat_1, p_value_1 = stats.ttest_1samp(datos_1, 75, alternative='greater')

print(f'Estadístico t: {t_stat_1}')
print(f'Valor p: {p_value_1}','\n')
#----------------------------------------------------------------------------
print('prueba t del segundo cambio')
t_stat_2, p_value_2 = stats.ttest_1samp(datos_2, 75, alternative='greater')

print(f'Estadístico t: {t_stat_2}')
print(f'Valor p: {p_value_2}')

#----------------------------------------------------------------------------
print("")


# Ajustar los datos a una normal, estimando la desviacion estandar MLE (metodo empirico)

print("Estimacion de la desviacion estandar",'\n')
#----------------------------------------------------------------------------
print('Rendimiento de la maquina inicial')
media_i = np.mean(datos_i)
scale_inicial = stats.norm.fit(datos_i,floc=media_i)
print(f'Estimacion de la desviacion estandar: {scale_inicial[1]}','\n')
varianza_i = (scale_inicial[1])**2
print(f'Varianza: {varianza_i}','\n')
#----------------------------------------------------------------------------
print('Rendimiento de la maquina en el primer cambio')
media_1 = np.mean(datos_1)
scale_1 = stats.norm.fit(datos_1,floc=media_1)
print(f'Estimacion de la desviacion estandar: {scale_1[1]}','\n')
varianza_1 = (scale_1[1])**2
print(f'Varianza: {varianza_1}','\n')
#----------------------------------------------------------------------------
print('Rendimiento de la maquina en el segundo cambio cambio')
media_2 = np.mean(datos_2)
scale_2 = stats.norm.fit(datos_2,floc=media_2)
print(f'Estimacion de la desviacion estandar: {scale_2[1]}','\n')
varianza_2 = (scale_2[1])**2
print(f'Varianza: {varianza_2}','\n')
#----------------------------------------------------------------------------

#   Calculo de la desivicion estandar metodo analitico 

varianza_analitica_i = np.sum((datos_i - media_i) ** 2) / (len(datos_i) - 1)
varianza_analitica_1 = np.sum((datos_1 - media_1) ** 2) / (len(datos_1) - 1)
varianza_analitica_2 = np.sum((datos_2 - media_2) ** 2) / (len(datos_2) - 1)

print('Varianza por el metodo analitico')
print(f'Configuracion inicial: {varianza_analitica_i}\nPrimer cambio: {varianza_analitica_1}\nSegundo cambio: {varianza_analitica_2}\n')

#   Calculo del porcentaje de error

porcentaje_error_i= (np.abs(varianza_analitica_i - varianza_i)/varianza_analitica_i )*100
porcentaje_error_1= (np.abs(varianza_analitica_1 - varianza_1)/varianza_analitica_1 )*100
porcentaje_error_2= (np.abs(varianza_analitica_2 - varianza_2)/varianza_analitica_2 )*100

print('Porcentaje de error de la varianza')
print(f'Configuracion inicial: {porcentaje_error_i}%\nPrimer cambio: {porcentaje_error_1}%\nSegundo cambio: {porcentaje_error_2}%')
#mostrar los graficos
plt.show()
