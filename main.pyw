from raiz import Raiz
from menus import Menus
from lienzo import Lienzo
from interfaz import Interfaz
from resultado import Resultado


# Arranca el programa
if __name__=="__main__":
    raiz = Raiz()
    canvas = Lienzo(raiz)
    result = Resultado(canvas)
    argumentos1 = dict(result=result)
    cuadro = Interfaz(raiz, **argumentos1)
    argumentos2 = dict(raiz=raiz, result=result, cuadro=cuadro)
    menu = Menus(raiz,**argumentos2)
    raiz.mainloop()
