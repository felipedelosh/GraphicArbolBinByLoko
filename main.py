"""
A los 18 dias de oct de 2019

Me dispongo a crear la interfaz grafica de un arbol binario.


"""

# Importo la wea que grafica
from tkinter import *

# Importo lo que controla el arbol
from controladora import *

class Software:
    def __init__(self):
        # Pantalla principal
        self.pantalla = Tk()
        # Aqui se van a pintar los controles
        self.telaControl = Canvas(self.pantalla, width=200, height=460, bg="gray40")
        self.lblInserValue = Label(self.telaControl, text="Ingrese Valor: ")
        self.txtInsertValue = Entry(self.telaControl, width=10)
        self.btnInsert = Button(self.telaControl, text="Insert", command=self.addNuArbol)

        # Estas son las estadisticas del arbol
        self.lblNumeroNodos = Label(self.telaControl, text="Numero Nodos: 0")

        # Aqui se va a pintar el arbol
        self.telaArbol = Canvas(self.pantalla, width=500, height=460, bg="white")

        """
        Nota: Esta es la controladora.
        Se encarga de realizar todas las operaciones sobre el arbol
        """
        self.controladora = Controladora()
        # Pinto
        self.VIZUALIZAR()


    # Este metodo se encarga de pintar todo lo referente a la interfaz grafica
    def VIZUALIZAR(self):
        # le pongo titulo
        self.pantalla.title("Arbol Bin by loko")
        # Le pongo dimenciones
        self.pantalla.geometry("720x480")

        # Procedo a pintar la tela de los controles
        self.telaControl.place(x=10, y=10)
        self.lblInserValue.place(x=10, y=20)
        self.txtInsertValue.place(x=100, y=21)
        self.btnInsert.place(x=20, y=70)

        self.lblNumeroNodos.place(x=10, y=400)
        # Procedo a pintar la tela arbol
        self.telaArbol.place(x=210, y=10)

        # Lanzo la pantalla
        self.pantalla.mainloop()

    # Agregar un numero al arbol
    def addNuArbol(self):
        try:
            self.controladora.agregarValorAlArbol(int(self.txtInsertValue.get()))
            # Actualizo el numero de nodos
            self.numeroDeNodos()
        except:
            print("Error Ingresando Nodo")

    # Este metodo me dice cuantos nodos tiene el arbol
    def numeroDeNodos(self):
        self.lblNumeroNodos['text'] = "Numero de Nodos: " + str(self.controladora.numeroNodos())
        


# Instancio esa wea
sw = Software()
