#   libreria para graficar -> variable plt
import matplotlib.pyplot as plt
from math import log

def solicitar():
    lista = []
    print("Intervalo")
    for i in range(2):
        lista.append((input()))
    return lista

def solucion(x):
    # f(x) = −0.5x^2 + 2.5x + 4.5
    fx = float(-0.5*x**2 + 2.5*x + 4.5)
    return fx

def comprobar(xl, xu):
    if (solucion(xl) * solucion(xu) < 0):
        return True
    return False

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
Ea = 0.0001
#   primer intervalo
intervalo = solicitar()
xl = float(intervalo[0])
xu = float(intervalo[1])
#   criterio de paro
Cp = abs(float(input("Criterio de paro: ")))
#   True -> el procedimiento funciona
if (comprobar(xl, xu)):
    while (Ea >= Cp):
        #   resultado de sustituir los valores del intervalo en la funcion
        fxl = solucion(xl)
        fxu = solucion(xu)
        #   mitad del intervalo
        xr = mitad(xl, xu, fxl, fxu)
        fxr = solucion(xr)
        print("xl: ", xl, " -> f(xl): ", fxl,"\nxr: ", xr, " -> f(xr): ", fxr, "\nxu: ", xu, " -> f(xu): ", fxu)
        #   nuevo intervalo
        xl, xu = nuevointervalo(fxl, fxr, fxu)
        #   calculamos nuestro error aproximado
        if (len(registroxr) > 1):
            #   Error aceptado -> Ea = |xr (nuevo) - xr (anterior) / xr (nuevo)|
            Ea = abs(float((registroxr[-1] - registroxr[-2]) / registroxr[-1]))

    #   criterio de paro vs error aceptado
    print("Criterio de paro: ", Cp, "\nError aceptado: ", Ea)
    #   mostramos grafico con todos los xr almacenados en el proceso
    plt.plot(registroxr)
    plt.show()
#   False -> el procedimiento no funciona
else:
    print("Este intervalo no es valido")
