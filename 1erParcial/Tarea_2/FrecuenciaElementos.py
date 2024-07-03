"""Escribir un programa que cuente la frecuencia de los elementos de una lista"""

lista = []
j = ""
l = int(input("¿Cuatos datos desea anotar?\n"))

def guarda():
    for num in range(l):
        lista.append((input("-")))
guarda()

def cuenta(i):
    contador = 0
    for j in lista:
        if j == i:
            contador += 1
    print(i, "esta almacenado", contador, "veces")
    return i

for i in lista:
    if i != j:
        j = cuenta(i)

input()
