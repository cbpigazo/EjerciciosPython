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
import urllib as urllib

PATH_FICHERO = 'ficheroPrueba.csv'

def descargarFichero(nombreDataset,keyIntroducida,fechaInicio,fechaFin):
    try:
        urlretrieve('https://www.quandl.com/api/v3/datasets/'+nombreDataset+'.csv?start_date='+fechaInicio+'&end_date='+fechaFin+'&api_key='+keyIntroducida, PATH_FICHERO)
    except urllib.error.HTTPError as error:
        print(error," -->No se ha podido descargar el fichero csv. Compruebe sus datos de entrada")
        menu()

def eliminarFichero():
    remove(PATH_FICHERO)
def procesarFicheroComoCadena():
    with open(PATH_FICHERO) as ficheroDescargado:
        reader = csv.reader(ficheroDescargado, delimiter=',', quotechar=',',
                            quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            print(row)

def procesarFicheroComoDiccionario(nombreDataset,keyIntroducida,fechaInicio,fechaFin):
    try:
        with open(PATH_FICHERO) as ficheroDescargado:
            reader = csv.DictReader(ficheroDescargado)
            listaDiccionario = sorted(reader, key=(operator.itemgetter('Close')), reverse=False)

            valorMinimo = min(listaDiccionario, key=operator.itemgetter('Close'))
            valorMaximo = max(listaDiccionario, key=operator.itemgetter('Close'))
            valorMedio = reduce(lambda x, y: x + y, [float(valor['Close']) for valor in listaDiccionario]) / len(listaDiccionario)
            calcularDesviacionMedia(nombreDataset,keyIntroducida,fechaInicio,fechaFin)

            print("El valor mínimo del campo Close es: ", valorMinimo['Close'])
            print("El valor máximo del campo Close es: ", valorMaximo['Close'])
            print("El valor medio del campo Close es: ", valorMedio)
    except KeyError as error:
        print(error," -->Error al procesar el fichero. Asegúrate de que el dataset posee el campo 'Close'")
        menu()

"""
def calcularMediaConLibreriaPanda(nombreDataset,keyIntroducida,fechaInicio,fechaFin):
    #readerPanda = panda.read_csv('https://www.quandl.com/api/v3/datasets/'+nombreDataset+'.csv?start_date='+fechaInicio+'&end_date='+fechaFin+'&api_key='+keyIntroducida)
    #valorMedio = readerPanda["Close"].mean
    #print("El valor medio calculado con panda del campo Close es: ", valorMedio)
    return readerPanda"""
def calcularDesviacionMedia(nombreDataset,keyIntroducida,fechaInicio,fechaFin):
    readerPanda = panda.read_csv('https://www.quandl.com/api/v3/datasets/'+nombreDataset+'.csv?start_date='+fechaInicio+'&end_date='+fechaFin+'&api_key='+keyIntroducida)
    desviacionMedia = readerPanda["Close"].mad()
    print("el valor de la desviación media es:",desviacionMedia)

def menu():
    while True:
        print("Pulse 'Y' si desea empezar, o 'N' si no desea continuar")
        opcionElegida =input("Desea continuar? Y/N")
        if opcionElegida.strip().upper() == "Y":
            print("Introduzca dataset, su apiKey y la fecha de inicio y fin para procesar un fichero")

            dataset = input("dataSet. Dataset recomendado EOD/IBM")
            apiKey = input("apiKey. apiKey recomendada yNo4hVP-pJbZzv4Amz-a")
            fechaInicio = input("fechaInicio recomendada 2016-10-06")
            fechaFin = input("fechaFin recomendada 2017-10-06")

            descargarFichero(dataset, apiKey, fechaInicio, fechaFin)
            procesarFicheroComoDiccionario(dataset, apiKey, fechaInicio, fechaFin)
            eliminarFichero()
        elif opcionElegida.strip().upper() == "N":
            print("Saliendo del sistema =)")
            exit()
        else:
            print("Solo se aceptan los valores 'Y' / 'N'")
menu()