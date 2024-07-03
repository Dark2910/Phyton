"""Escribir un programa que muestre los elementos que se repiten en dos listas de 20 elementos cada una, la lista debe ser llenada a través del teclado."""

def guarda():
    lista = []
    for i in range(20):
        lista.append((input("-")))
    return lista

print("Lista 1")
lis1 = guarda()
print("Lista 2")
lis2 = guarda()

def repetidos():
    print("Datos repetidos")
    for list in lis1:
        if(list in lis2):
            print(list,end=", ")
    print("\n")

repetidos()
input()
