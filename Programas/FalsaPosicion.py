#   libreria para graficar -> variable plt
import matplotlib.pyplot as plt
import math
from math import log
from math import e

def solucion(x):
    return x**3 + 4 * x**2 - 10

def nuevointervalo(fxl, fxr, fxu):
    if (fxl * fxr < 0):
        nxl = xl
        nxu = xr
        print("Nuevo intervalo: ", nxl," " ,nxu)
    elif(fxr * fxu < 0):
        nxl = xr
        nxu = xu
        print("Nuevo intervalo: ", nxl," " ,nxu)
    return nxl, nxu

def mitad(xl, xu, fxl, fxu):
    m = xu - (fxu * (xl - xu) / (fxl - fxu))
    #   guardamos m en registroxr para despues graficar
    registroxr.append(m)
    return m

#   registro de todos los xr calculados
registroxr = []
#   Ea (Error aceptado) -> valor a calcular y a comparar con el criterio de paro
Ea = 1
#   primer intervalo
print("Intervalo")
xl = float(input("xl: "))
xu = float(input("xu: "))
#   criterio de paro
Cp = abs(float(input("Criterio de paro: ")))

while (Ea > Cp):
    #   resultado de sustituir los valores del intervalo en la funcion
    fxl = solucion(xl)
    fxu = solucion(xu)
    #   mitad del intervalo
    xr = mitad(xl, xu, fxl, fxu)
    fxr = solucion(xr)
    print("xl: ", xl, " -> f(xl): ", fxl,"\nxr: ", xr, " -> f(xr): ", fxr, "\nxu: ", xu, " -> f(xu): ", fxu)
    #   calculamos nuestro error aproximado
    if (len(registroxr) > 1):
        #   Error aceptado -> Ea = |xr (nuevo) - xr (anterior) / xr (nuevo)|
        Ea = abs(float((registroxr[-1] - registroxr[-2]) / registroxr[-1]))
    #   nuevo intervalo
    xl, xu = nuevointervalo(fxl, fxr, fxu)

#   criterio de paro vs error aceptado
print("xr =", registroxr[-1],"\nCriterio de paro: ", Cp, "\nError aceptado: ", Ea)
#   mostramos grafico con todos los xr almacenados en el proceso
plt.plot(registroxr)
plt.show()
