#   Metodo de la Secante
import matplotlib.pyplot as plt
from math import e
import numpy

xn_reg = []
error_reg = []
error_reg.append(1)

def f(x):
    #   e**(-x) - x
    return e**(-x) - x

def solucion(xh, xi):   # xi-1, xi
    return xi - (f(xi)  * (xh - xi)/ (f(xh) - f(xi)))

def calcula():
    xh = input("Xi-1: ")    #xi-1 = 0
    xi = input("Xi: ")      #xi = 1
    xn_reg.append(float(xh))
    xn_reg.append(float(xi))
    contador = 0

    parada = input("Criterio de paro: ")

    if(parada == ""):
        parada = 0.0001

    while(contador <= 500):
        if(float(error_reg[contador]) <= float(parada)):
            break
        xn_reg.append(solucion(xn_reg[-2], xn_reg[-1]))
        error_reg.append(abs(xn_reg[contador+1] - xn_reg[contador]))
        '''
        print("xi-1 =", xn_reg[-2],"  ->  f(xi-1) =", f(xn_reg[-2]), "\nxi =",xn_reg[-1] , "  ->  f(xi) =", f(xn_reg[-1]), "\nSolucion =", solucion(xn_reg[-2], xn_reg[-1]))
        '''
        contador += 1

    muestra()

def muestra():

    for registro in xn_reg:
        print("x=", registro)

    for registro in error_reg:
        print("Error:", registro)

    plt.plot(xn_reg, label = "raiz")
    plt.show()

    plt.plot(error_reg, label = "error")
    plt.show()

calcula()
