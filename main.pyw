from raiz import Raiz
from lienzo import Lienzo
from interfaz import Interfaz
from resultado import Resultado
from menus import Menus

if __name__=="__main__":  # Arranca toda la interfaz
    raiz = Raiz()
    canvas = Lienzo(raiz)
    result = Resultado(canvas)
    argumentos1 = dict(result=result)
    cuadro = Interfaz(raiz, **argumentos1)
    argumentos2 = dict(raiz=raiz)
    menu = Menus(raiz, **argumentos2)
    cuadro.localtime()
    cuadro.playtime()
    raiz.mainloop()
