
# coding: utf-8

# # Evaluación. Análisis de datos financieros

# ## Orígenes de datos financieros
# Obtenidos a partir de la web:
#      https://www.quandl.com/api/v3/datasets/EOD/IBM.csv?api_key=yNo4hVP-pJbZzv4Amz-a

# ### Funciones de apoyo
# **a1.Función de lectura de los datos del fichero .csv**
# * Recibe como entrada el fichero.
# * Lo abre para lectura y recoge todos los valores de cierre de las acciones de la empresa.

def leer_datos(fichero):


# **a2.Función para el cálculo de la media.**
# * Recibe como entrada todos los datos y devuelve el valor medio

def avg(lista):


# **a3.Función de transformación.**
# * Recoge una línea del csv y devuelve una lista con valores numéricos

def coge_cierre(linea):


# ## PASOS 1 y 2
# ### Sentencias para descargar el fichero desde Quandl

from urllib.request import urlretrieve


# ## PASO 3. Cuerpo principal del programa. 
# * Procesar el fichero línea a línea (cada línea refleja la cotización de un día)
# * Hace uso de la función de apoyo leer_datos()

cierre = # función de lectura del .csv


# ### PASO 4.	Calcular e imprimir el mínimo, el máximo y el promedio de los valores solicitados
# * Realiza la lectura del fichero y devuelve por pantalla los valores solicitados: min, max y media.
# * Hace uso de las funciones de apoyo.

print("Adj_Close de la fila 0: ",...
print("Adj_Close de la fila 1: ",...
print("Número de líneas: ", ...
print("Máximo: %f  Mínimo: %f  Media: %f" \
     % ( ..., ..., ...)

