from checker import checker_version, checker_playsound

# Si no se cumplen los requisitos lanza una ventana con los Errores
try:
    from raiz import Raiz
    from menus import Menus
    from lienzo import Lienzo
    from interfaz import Interfaz
    from resultado import Resultado

    # Arranca el programa
    if __name__ == "__main__":
        raiz = Raiz()
        canvas = Lienzo(raiz)
        result = Resultado(canvas)
        argumentos1 = dict(result=result)
        iface = Interfaz(raiz, **argumentos1)
        argumentos2 = dict(raiz=raiz, result=result, iface=iface)
        menu = Menus(raiz, **argumentos2)
        raiz.mainloop()
except SyntaxError:
    raiz = Raiz()
    checker_version()
except ModuleNotFoundError:
    raiz = Raiz()
    checker_playsound()
