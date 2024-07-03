"""Tomando en cuenta lo realizado en clase, diseñar el código para el funcionamiento del método de la bisección, éste debe de estar en una función."""

"""
Para encontrar la raiz de una funcion es necesario que los simbolos de cada valor obtenido sean diferentes, ya que con esto nosotros aseguramos que la "gráfica" cruza el plano en donde "y" es igual a 0 (raiz)

    Intervalo
|-------------------|
xl                 xu

xr es la mitar del intervalo en donde estan ubicados xl y xu, si tomamos a xr como otro punto que parte la recta, se generan dos valores nuevos (Δx/2) sumando estos dos valores obtenemos como resultado el valor de Δx (delta x) en donde Δx es igual a la diferencia de xu respecto a xl.

Hacemos esto con el fin de hacer mas pequeño nuestro intervalo y encontar de una manera mas exacta nuestra raiz

Para saber hasta que punto tenemos que iterar el programa existe una formula en donde nosotros calculamos un error aproximado, tenemos que comparar el valor que obtuvimos en xr con el valor obtenido en la iteracion anterior, si este cumple con los valores solicitados es momento de para el programa

Ea = |xr (nuevo) - xr (anterior) / xr (nuevo)|




funcion a utilizar en el programa
f(x) = x^3 + 4x^2 - 10    intervalo [1,2]

criterio de paro 0.0001 (error aproximado)

Formulas:
Δx = xu - xl
xr = xu + xl / 2
Ea = |xr (nuevo) - xr (anterior) / xr (nuevo)|

f(xl) = (1)^3 + 4(1)^2 - 10    ->  f(xl) = -5
f(xu) = (2)^3 + 4(2)^2 - 10    ->  f(xu) = 14

Si comparamos los valores obtenidos podemos observar que si se cumple la condicion solicitada (signos diferentes), ahora que sabemos que nuestra funcion tiene una raiz, tenemos que calcular el valor de xr y determinar en que parte de la mitad se encuentra nuestra raiz

xr = 2 + 1 / 2      ->      xr = 1.5
f(xr) = (1.5)^3 + 4(1.5)^2 - 10    ->  f(xr) = 2.375

f(xl) = -5
            Esta mitad cumple con la condicion solicitada (signos diferentes)
f(xr) = 2.375
            Esta otra no
f(xu) = 14

Ya que sabemos en que lado del intervalo se encuentra nuestra raiz solo hay que repetir los pasos anteriores, hay que tomar en cuenta que nuestro nuevo intervalo sera de:

|------------------|
xl                xr

Y xr se convertira en xu    ->    nuevo intervalo [1, 1.5]

f(xl) = (1)^3 + 4(1)^2 - 10    ->  f(xl) = -5
                                                    Cumplen con la condicion
f(xu) = (1.5)^3 + 4(1.5)^2 - 10    ->  f(xu) = 2.375


xr = 1.5 + 1 / 2      ->      xr = 1.25
f(xr) = (1.25)^3 + 4(1.25)^2 - 10    ->  f(xr) = -1.7969


f(xl) = -5
                    Esta mitad no cumple con las condiciones solicitadas
f(xr) = -1.7969
                    Esta otra sí
f(xu) = 2.375


Nuevo intervalo [1.25 , 1.5]

f(xl) = (1.25)^3 + 4(1.25)^2 - 10    ->  f(xl) = -1.7969

f(xu) = (1.5)^3 + 4(1.5)^2 - 10    ->  f(xu) = 2.375

xr = 1.5 + 1.25 / 2      ->      xr = 1.375
f(xr) = (1.375)^3 + 4(1.375)^2 - 10    ->  f(xr) = 0.1621

f(xl) = -1.7969

f(xr) = 0.1621

f(xu) = 2.375

Nuevo intervalo [1.25 , 1.375]
"""



"""Objetivo graficar los puntos obtenidos 'xr' de cada iteracion hasta obtener un criterio de paro igual a 0.0001"""

"""import matplotlib.pyplot as plt
lst = [1,4,9,7,50,87]
plt.plot(lst)
plt.show()"""

#   libreria para graficar -> variable plt
import matplotlib.pyplot as plt

def solicitar():
    lista = []
    print("Intervalo")
    for i in range(2):
        lista.append((input()))
    return lista

def solucion(x):
    fx = x**3 + 4*x**2 - 10
    return fx

def comprobar():
    if (solucion(xl) * solucion(xu) < 0):
        return True
    return False

def nuevointervalo():
    if (fxl * fxr < 0):
        nxl = xl
        nxu = xr
        print("Nuevo intervalo: ", nxl," " ,nxu)
    elif(fxr * fxu < 0):
        nxl = xr
        nxu = xu
        print("Nuevo intervalo: ", nxl," " ,nxu)
    return nxl, nxu

def mitad():
    m = (xu + xl) / 2
    #   guardamos m en registroxr para despues graficar
    registroxr.append(m)
    return m
    
#   registro de todos los xr calculados
registroxr = []
#   Ea -> valor a calcular y a comparar con el criterio de paro, igualado a una unidad solo para cumplir con la condicion del ciclo while
Ea = 1
#   primer intervalo
intervalo = solicitar()
xl = float(intervalo[0])
xu = float(intervalo[1])
#   criterio de paro
Cp = abs(float(input("Criterio de paro: ")))
#   True -> el procedimiento funciona
if (comprobar()):
    while (Ea > Cp):
        #   resultado de sustituir los valores del intervalo en la funcion
        fxl = solucion(xl)
        fxu = solucion(xu)
        #   mitad del intervalo
        xr = mitad()
        fxr = solucion(xr)
        print("xl: ", xl, " -> f(xl): ", fxl,"\nxr: ", xr, " -> f(xr): ", fxr, "\nxu: ", xu, " -> f(xu): ", fxu)
        #   nuevo intervalo
        xl, xu = nuevointervalo()
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
