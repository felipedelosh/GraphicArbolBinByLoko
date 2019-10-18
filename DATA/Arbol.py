"""
a los 18 dias de oct de 2019

Se declara una estructura de tipo nodo que sera Kernel de un arbol

>>Se comprobo el funcionamiento de esto por ello se agregan los valores 
que seran los encargados de graficar

"""

class Nodo:
    def __init__(self):
        self.IZQ = None
        self.data = None
        self.DER = None
        # Estos valores son para graficar
        self.posx = 0
        self.posy = 0


"""
a los 18 dias de oct de 2019

Se declara una clase arbol que guarda Numeros enteros

"""
class Arbol:
    def __init__(self):
        self.raiz = Nodo()
        self.numeroDeNodos = 0

    # Este metodo agrega un valor al arbol
    def ADD(self, x):
        self._ADD(self.raiz, x)
    # Este metodo es el que en realidad agrega el nodo al arbol
    def _ADD(self, NODO, x):
        # Si la raiz esta vacia pues se crea
        if(self.raiz.data == None):
            self.raiz.data = x
            self.numeroDeNodos = 1
        else:
            """
            Procedo a buscar un espacio disponible.
            """
            if(NODO.data < x):
                # Si la der esta vacia guarde
                if (NODO.DER == None):
                    NODO.DER = Nodo()
                    NODO.DER.data = x
                    self.numeroDeNodos = 1 + self.numeroDeNodos
                else:
                    # Ojo: no hay espacio siga buscando
                    self._ADD(NODO.DER, x)
            else:
                # Si la izq esta vacia guarde
                if (NODO.IZQ == None):
                    NODO.IZQ = Nodo()
                    NODO.IZQ.data = x
                    self.numeroDeNodos = 1 + self.numeroDeNodos
                else:
                    # Ojo: no hay espacio siga buscando
                    self._ADD(NODO.IZQ, x)

    


    # Este metodo es solo para pruebas
    def inorder(self):
        self._inorder(self.raiz)
    # Complemento del inorder
    def _inorder(self, NODO):
        if(NODO != None):
            self._inorder(NODO.IZQ)
            print(NODO.data)
            self._inorder(NODO.DER)