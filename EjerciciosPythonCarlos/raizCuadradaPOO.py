# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math

class EcuacionSegundoGrado:
    
    def __init__(self, a ,b ,c):
        
        self.a = a
        self.b = b
        self.c = c
    
    
    def solucionarEcuacion(self):
        
        if (self.errorRaizNegativaOIgualACero() == "continua"):
            solucion1 = (-self.b + self.calculoRaiz())/(2*self.a)
            solucion2 = (-self.b - self.calculoRaiz())/(2*self.a)
            solucionEcuacion = print("solucion1: ",solucion1 ,"solucion2: ",solucion2)
            
        else:
            solucionEcuacion = self.errorRaizNegativaOIgualACero()
            print(solucionEcuacion)    
    
    
    def errorRaizNegativaOIgualACero(self):
        
        if(self.b**2 < 4*self.a*self.c or self.b**2 - 4*self.a*self.c == 0):
            mensaje = "La Ecuación no tiene solución real"
        else:
            mensaje = "continua"
        return mensaje
    
    def calculoRaiz (self):
        resultado = math.sqrt(self.b**2 -4*self.a*self.c)
        return resultado

ecuacionSegundoGrado1 = EcuacionSegundoGrado(2, 7, 10).solucionarEcuacion()
