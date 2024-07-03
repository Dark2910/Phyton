"""from Basics import Basics"""
from Basics import Invertir, ListaImpar, ListaPar, ListaPrimos, Unos, Triangulo, TranguloInvertido

class Numeros:
    def __init__(self):
        self.Invertir()
        self.ListImpar()
        self.ListPar()
        self.NumPrimos()
        self.Unos()
        self.Triangulo()
        self.TrianguloInvertido()

    def Invertir(self):
        print("Invertir numeros")
        """num = Basics.Invertir(int(input()))"""
        num = Invertir(int(input()))
        print(num)

    def ListImpar(self):
        print("Lista de numeros impares\nIngresa un valor inicial")
        c = int(input())
        print("Ingresa un valor final")
        f = int(input())
        ListaImpar(c, f)

    def ListPar(self):
        print("Lista de numeros pares\nIngresa un valor inicial")
        c = int(input())
        print("Ingresa un valor final")
        f = int(input())
        ListaPar(c, f)

    def NumPrimos(self):
        print("Lista de numeros primos\nIngresa un valor inicial")
        c = int(input())
        print("Ingresa un valor final")
        f = int(input())
        ListaPrimos(c, f)

    def Unos(self):
        print("Juego con numeros")
        num = int(input())
        Unos(num)

    def Triangulo(self):
        print("Triangulo")
        num = int(input())
        Triangulo(num)

    def TrianguloInvertido(self):
        print("Triangulo Invertido")
        num = int(input())
        TranguloInvertido(num)

