#   Sistema de ecuaciones
from matplotlib import pyplot as plt

x1_reg = []
x2_reg = []
x3_reg = []
x4_reg = []

error_x1 = []
error_x1.append(1)
error_x2 = []
error_x2.append(1)
error_x3 = []
error_x3.append(1)
error_x4 = []
error_x4.append(1)

def igualar():
    if not x1_reg:
        x1_reg.append(0)
    if len(x2_reg) < len(x1_reg):
        x2_reg.append(0)
    if len(x3_reg) < len(x1_reg):
        x3_reg.append(0)
    if len(x4_reg) < len(x1_reg):
        x4_reg.append(0)

def gn(v,x1,x2,x3,x4):
    if v == 1:
        return (0.25 + 0.25*x2)
    elif v == 2:
        return (0.25 + 0.25*x2 + 0.25*x3)
    elif v == 3:
        return (0.25 + 0.25*x2 + 0.25*x4)
    elif v == 4:
        return (0.25 + 0.25*x3)

def convergencia():
    contador = 0
    num = 4 #Numero de incognitas
    v = 1

    parada = input("Presiona ENTER si tu criterio de paro es igual a 0.0001, de lo contrario anotalo: ")
    if(parada == ""):
        parada = 0.0001

    a = input("Si tus valores inciales son iguales a 0 presiona ENTER de lo contrario ingresa el valor de x1: ")

    if a == "":
        igualar()

    elif a != "":
        x1_reg.append(float(a))
        x2_reg.append(float(input("x2: ")))
        x3_reg.append(float(input("x3: ")))
        x4_reg.append(float(input("x4: ")))

    igualar()

    while(contador <= 500):
        if v > num:
            igualar()

            if( error_x1[contador] <= float(parada) and error_x2[contador] <= float(parada) and error_x3[contador] <= float(parada) and error_x4[contador] <= float(parada)):
                return contador

            contador += 1
            v = 1

        x1 = float(x1_reg[contador])
        x2 = float(x2_reg[contador])
        x3 = float(x3_reg[contador])
        x4 = float(x4_reg[contador])

        x = gn(v,x1,x2,x3,x4)

        if v == 1:
            x1_reg.append(x)
            error_x1.append(abs(x1_reg[contador + 1] - x1_reg[contador]))
        elif v == 2:
            x2_reg.append(x)
            error_x2.append(abs(x2_reg[contador + 1] - x2_reg[contador]))
        elif v == 3:
            x3_reg.append(x)
            error_x3.append(abs(x3_reg[contador + 1] - x3_reg[contador]))
        elif v == 4:
            x4_reg.append(x)
            error_x4.append(abs(x4_reg[contador + 1] - x4_reg[contador]))

        v += 1
    return contador

def mostrar(contador):
    if(contador < 500):
        print("Converge")
    else:
        print("No converge")

    for registro in x1_reg:
        print("x1=", registro)
    for registro in x2_reg:
        print("x2=", registro)
    for registro in x3_reg:
        print("x3=", registro)
    for registro in x4_reg:
        print("x4=", registro)

    for registro in error_x1:
        print("Error x1:", registro)
    for registro in error_x2:
        print("Error x2:", registro)
    for registro in error_x3:
        print("Error x3:", registro)
    for registro in error_x4:
        print("Error x4:", registro)

    plt.plot(x1_reg,label='x1')
    plt.plot(x2_reg,label='x2')
    plt.plot(x3_reg,label='x3')
    plt.plot(x4_reg,label='x4')

    plt.xlabel('Eje: x')
    plt.ylabel('Eje: y')
    plt.title("Valores")
    plt.legend()
    plt.show()

    plt.plot(error_x1,label= 'x1')
    plt.plot(error_x2,label= 'x2')
    plt.plot(error_x3,label= 'x3')
    plt.plot(error_x4,label= 'x4')

    plt.xlabel('Eje: x')
    plt.ylabel('Eje: y')
    plt.title("Error")
    plt.legend()
    plt.show()

mostrar(convergencia())
