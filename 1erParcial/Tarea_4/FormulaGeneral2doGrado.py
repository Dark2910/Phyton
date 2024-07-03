#   Determinar las raíces reales utlizando la fórmula general de segundo grado     f(x) = −0.5x^2 + 2.5x + 4.5
#   -b +- Raíz(b^2 - 4ac)/2a

def chicharronera():
    print("Formula general de segundo grado")
    a = float(input("Valor de a: "))
    b = float(input("Valor de b: "))
    c = float(input("Valor de c: "))

    x1 = ((-b) + (b**2 -4*(a*c))**(1/2))/(2*a)
    x2 = ((-b) - (b**2 -4*(a*c))**(1/2))/(2*a)
    print("x1: ", x1, "\nx2: ", x2)
chicharronera()
