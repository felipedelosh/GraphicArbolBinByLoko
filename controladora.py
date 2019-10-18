"""
A los 18 dias de oct de 2019


Se declara una clase controladora la cual es la interconexion entre arbol 
y la interfaz grafica
"""

# Se trabajara con un arbol por ello se importa
from DATA.Arbol import Arbol

class Controladora:
    def __init__(self):
        self.arbol = Arbol()


    # Este metodo agrega un valor al arbol
    def agregarValorAlArbol(self, dato):
        self.arbol.ADD(dato)


    # Este metodo me retorna cuantos nodos tiene el arbol
    def numeroNodos(self):
        return self.arbol.numeroDeNodos