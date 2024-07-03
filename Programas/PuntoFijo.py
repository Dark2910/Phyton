#   PuntoFijo
import matplotlib.pyplot as plt

error_reg = []
error_reg.append(1)
xn_reg = []

def gn(x):
    return (x+5/2)**1/2

#   error = |Xn - Xn-1| si el error es constante o se vuelve cero significa que converge, de lo contrario diverge y si es este el caso no se puede aplicar el metodo
def convergencia():
    vec_in = input("Vector inicial: ")
    parada = input("Criterio de paro: ")
    contador = 0

    if(vec_in == ""):
        vec_in = 0.0000
        xn_reg.append(float(vec_in))
    else:
        xn_reg.append(float(vec_in))

    if(parada == ""):
        parada = 0.0001

    while(contador <= 1000):
        if(float(error_reg[contador]) <= float(parada)):
            return contador
        xn_reg.append(gn(float(xn_reg[contador])))
        error_reg.append(abs(xn_reg[contador+1] - xn_reg[contador]))
        contador += 1
    return contador

def mostrar(contador):
    if(contador < 500):
        print("Converge")
    else:
        print("No converge")

    for registro in xn_reg:
        print("x=", registro)

    for registro in error_reg:
        print("Error:", registro)

    plt.plot(xn_reg, label = "raiz")
    plt.show()

    plt.plot(error_reg, label = "error")
    plt.show()

mostrar(convergencia())
