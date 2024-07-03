"""Metodos a utilizar"""
def mostrar():
    for list in lista1:
        print(list,end=", ")
    print("\r")
    for list in lista2:
        print(list,end=", ")
    print("\n")

def repetidos():
    for list in lista1:
        if(list in lista2):
            print(list,end=", ")
            eli.append(list)
    print("\n")

def elimina():
    for list in eli:
        lista1.remove(list)
        lista2.remove(list)

"""Listas con los datos a comparar"""
lista1=["Ford","Volkswagen","Maserati","Chevrolet","Mazda","Pagani","Lamborghini","Bugatti","koenigsegg"]
lista2=["BMW","Rolls Royce","Mercedes Benz","koenigsegg","Maserati","Aston Martin","Porsche","Pagani","Lamborghini"]
"""Lista que almacenara datos repetidos"""
eli=[]
"""Ordenamos de manera alfabetica"""
lista1.sort()
lista2.sort()
"""Mostramos los datos almacenados en cada lista"""
print("Listas de autos")
mostrar()
"""Mostramos datos repetidos"""
print("Autos repetidos:")
repetidos()
"""Eliminamos datos repetidos"""
elimina()
"""Mostramos nuevas listas"""
print("Nuevas listas:")
mostrar()
input()
