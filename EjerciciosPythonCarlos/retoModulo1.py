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
import pandas as panda

URL_DESCARGA = 'https://www.quandl.com/api/v3/datasets/EOD/IBM.csv?api_key=yNo4hVP-pJbZzv4Amz-a'

PATH_FICHERO = '/home/carlos/Proyectos/Python/EjerciciosPython/EjerciciosPythonCarlos/ficheroPrueba.csv'

def descargarFichero(keyIntroducida):
    urlretrieve('https://www.quandl.com/api/v3/datasets/EOD/IBM.csv?api_key='+keyIntroducida, PATH_FICHERO)

def eliminarFichero():
    remove(PATH_FICHERO)

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
        calcularDesviacionMedia()

        print("El valor mínimo del campo Close es: ",valorMinimo['Close'])
        print("El valor máximo del campo Close es: ", valorMaximo['Close'])
        print("El valor medio del campo Close es: ",    valorMedio)

def procesarPintarFicheroParaPruebas():
    with open(PATH_FICHERO) as ficheroDescargado:
        reader = csv.DictReader(ficheroDescargado)
        listaDiccionario = sorted(reader, key=(operator.itemgetter('Close')), reverse=False)
        for registro in listaDiccionario:
            print (registro['Close'])

def calcularMediaConLibreriaPanda():
    readerPanda = panda.read_csv(URL_DESCARGA)
    #valorMedio = readerPanda["Close"].mean
    #print("El valor medio calculado con panda del campo Close es: ", valorMedio)
    return readerPanda
def calcularDesviacionMedia():
    readerPanda = calcularMediaConLibreriaPanda()
    desviacionMedia = readerPanda["Close"].mad()
    print("el valor de la desviación media es:",desviacionMedia)

def iniciarFLujoNormalApp():
    descargarFichero('yNo4hVP-pJbZzv4Amz-a')
    procesarFicheroComoDiccionario()
    eliminarFichero()

iniciarFLujoNormalApp()
#calcularMediaConLibreriaNumpy()