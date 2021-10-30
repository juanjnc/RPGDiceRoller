from raiz import Raiz
from lienzo import Lienzo
from interfaz import Interfaz
from resultado import Resultado
from menus import Menus

if __name__=="__main__":  # Arranca toda la interfaz
    raiz = Raiz()
    canvas = Lienzo(raiz)
    cuadro = Interfaz(raiz)
    result = Resultado(canvas)
    argumentos = dict(raiz=raiz)
    menu = Menus(raiz, **argumentos)
    cuadro.localtime()
    cuadro.playtime()
    raiz.mainloop()
