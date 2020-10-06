#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 19:35:08 2020

@author: carlos
"""
import operator
from functools import reduce
from os import remove
from urllib.request import urlretrieve
import csv
from numpy import mean

PATH_FICHERO = '/home/carlos/Proyectos/Python/EjerciciosPython/EjerciciosPythonCarlos/ficheroPrueba.csv'

def descargarFichero():
    urlretrieve('https://www.quandl.com/api/v3/datasets/EOD/IBM.csv?api_key=yNo4hVP-pJbZzv4Amz-a', PATH_FICHERO)

def eliminarFichero():
    remove('/home/carlos/Proyectos/Python/EjerciciosPython/EjerciciosPythonCarlos/ficheroPrueba.csv')

def procesarFicheroComoCadena():
    with open(PATH_FICHERO) as ficheroDescargado:
        reader = csv.reader(ficheroDescargado, delimiter=',', quotechar=',',
                            quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            print(row)

def procesarFicheroComoDiccionario():
    with open(PATH_FICHERO) as ficheroDescargado:
        reader = csv.DictReader(ficheroDescargado)
        listaDiccionario = sorted(reader, key=(operator.itemgetter('Close')), reverse=False)

        valorMinimo = min(listaDiccionario, key=operator.itemgetter('Close'))
        valorMaximo = max(listaDiccionario, key=operator.itemgetter('Close'))
        valorMedio = reduce(lambda x, y: x + y, [float(valor['Close']) for valor in listaDiccionario]) / len(listaDiccionario)

        print("El valor mínimo del campo Close es: ",valorMinimo['Close'])
        print("El valor máximo del campo Close es: ", valorMaximo['Close'])
        print("El valor medio del campo Close es: ",    valorMedio)
        #for registro in listaDiccionario:
            #print (registro['Close'])

def procesarPintarFicheroParaPruebas():
    with open(PATH_FICHERO) as ficheroDescargado:
        reader = csv.DictReader(ficheroDescargado)
        listaDiccionario = sorted(reader, key=(operator.itemgetter('Close')), reverse=False)
        for registro in listaDiccionario:
            print (registro['Close'])
def calcularMediaConLibreriaNumpy():
    number_list = [45, 34, 10, 36, 12, 6, 80]
    avg = mean(number_list)
    print("The average is ", round(avg, 2))

def iniciarFLujoNormalApp():
    descargarFichero()
    procesarFicheroComoDiccionario()
    eliminarFichero()

#iniciarFLujoNormalApp()
calcularMediaConLibreriaNumpy()