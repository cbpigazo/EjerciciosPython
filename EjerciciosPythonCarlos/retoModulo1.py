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

PATH_FICHERO = '/home/carlos/Proyectos/Python/EjerciciosPythonCarlos/ficheroPrueba.csv'

def descargarFichero():
    urlretrieve('https://www.quandl.com/api/v3/datasets/EOD/IBM.csv?api_key=yNo4hVP-pJbZzv4Amz-a', PATH_FICHERO)

def eliminarFichero():
    remove('/home/carlos/Proyectos/Python/EjerciciosPythonCarlos/ficheroPrueba.csv')

def procesarFicheroComoCadena():
    with open(PATH_FICHERO) as ficheroDescargado:
        reader = csv.reader(ficheroDescargado, delimiter=',', quotechar=',',
                            quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            print(row)

def procesarFicheroComoDiccionario():
    with open(PATH_FICHERO) as ficheroDescargado:
        reader = csv.DictReader(ficheroDescargado)
        listaDiccionario = sorted(reader, key=(operator.itemgetter('Adj_Close')), reverse=False)

        valorMinimo = min(listaDiccionario, key=operator.itemgetter('Adj_Close'))
        valorMaximo = max(listaDiccionario, key=operator.itemgetter('Adj_Close'))
        valorMedio = reduce(lambda x, y: x + y, [float(valor['Adj_Close']) for valor in listaDiccionario]) / len(listaDiccionario)

        print(valorMinimo['Adj_Close'])
        print(valorMaximo['Adj_Close'])
        print(valorMedio)
        #for registro in listaDiccionario:
            #print (registro['Adj_Close'])

descargarFichero()
procesarFicheroComoDiccionario()