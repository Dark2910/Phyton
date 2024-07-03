#   NewtonRaphson
import matplotlib.pyplot as plt
from math import e
import numpy

#x = float(input("X: "))

xn_reg = []
error_reg = []
error_reg.append(1)

def gn(x):
    #   e**(-x) - x     5/(2*x-1)   ((x+5)/2)**(1/2)   (x**x) - 100
    fx = (x**x) - 100
    #   -e**(-x) - 1    -(10/(2*x-1)**2)    (1/((2**(3/2))*((x+5)**(1/2))))    x**x * (1 + numpy.log(x))
    dfx = x**x * (1 + numpy.log(x))
    #('{0:4f}'.format(x - (fx/dfx)))
    return x - (fx/dfx)

#xn = gn(x)
#print(xn)
#print(float('{0:4f}'.format(gn(x))))

def calcula():
    x = input("X: ")
    parada = input("Criterio de paro: ")

    if(x == ""):
        x = 0.0
        xn_reg.append(float(x))
    else:
        xn_reg.append(float(x))

    if(parada == ""):
        parada = 0.0001

    contador = 0
    while(contador <= 500):
        if(float(error_reg[contador]) <= float(parada)):
            break
        xn_reg.append(gn(xn_reg[contador]))
        error_reg.append(abs(xn_reg[contador+1] - xn_reg[contador]))
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
