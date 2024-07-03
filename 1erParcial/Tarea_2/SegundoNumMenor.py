"""lista de 10 elementos que indique el segundo número menor de la lista"""
def guarda():
    for num in range(10):
        lista.append(int(input("-")))

"""Lista de numeros almacenados"""
lista=[]
"""Ingresamos los datos solicitados"""
print("Escribe diez numeros enteros:")
guarda()
"""Eliminamos los datos repetidos en caso de haber"""
"""En un conjunto no pueden existir datos repetidos"""
conjunto = set(lista)
"""Sobrescribimos la lista"""
lista = list(conjunto)
"""La ordenamos de menor a mayor"""
lista.sort()
"""Mostramos nueva lista"""
for num in lista:
    print(num,end=", ")
print("\n")
"""Segundo número menor de la lista"""
print("Segundo número menor de la lista: ",lista[1])
input()
