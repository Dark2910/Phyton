def Longitud(num):
    contador = 0
    while (num > 0):
        num = num // 10
        contador += 1
    return contador
def Invertir(num):
    v = 0
    contador = Longitud(num)
    while (num > 0):
        contador -= 1
        d = num % 10
        num = num // 10
        v = v + d * (10 ** contador)
    return v
def ParImpar(num):
    if (num % 2 != 0):
        return 1
    else:
        return 0
def ListaImpar(i, f):
    for j in range(i, f):
        if (ParImpar(j) == 1):
            print(j)
def ListaPar(i, f):
    for j in range(i,f):
        if (ParImpar(j) == 0):
            print(j)
def NumPrimo(num):
    d = 2
    c = 0
    while (d != 0):
        if (d == num):
            break
        if (num % d == 0):
            c += 1
        d += 1
    if (c == 0):
        return 1
    return 0
def ListaPrimos(i, f):
    if (i == 0 or i == 1):
        i=2
    for j in range(i, f):
        if (NumPrimo(j) == 1):
            print(j)
def Unos(num):
    v = 0
    for potencia in range(0, int(num)):
        v += 10 ** potencia
        print(v, "*", v, " = ", v * v)
def Triangulo(num):
    # "k" es el numero de espacios maximos que necesita cada nivel
    k = 2 * num - 2
    """"Declaramos dos for con el fin de hacer los espacios
    que tiene que llavar cada nivel del triangulo"""
    for i in range(0, num):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        """Declaramos otro for con el cual vamos a imprimir 
        los asteriscos de cada nivel del triangulo"""
        for j in range(0, i + 1):
            print("*", end=" ")
        print("\r")
def TranguloInvertido(num):
    k = 2 * num - 2
    for i in range(num, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i):
            print("*", end=" ")
        print("\r")


"""
class Basics:
    def Longitud(num):
        contador = 0
        while(num > 0):
            num = num // 10
            contador += 1
        return contador
    def Invertir(num):
        v = 0
        contador = Basics.Longitud(num)
        while(num > 0):
            contador -= 1
            d = num % 10
            num = num // 10
            v = v + d * (10 ** contador)
        return v
"""
