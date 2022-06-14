from checker import checker_version, checker_playsound


# Si no se cumplen los requisitos lanza una ventana con los Errores
try:
    from root import Root
    from menus import Menus
    from result_canvas import ResultCanvas
    from main_interface import MainInterface
    from result_label import ResultLabel

    # Arranca el programa
    if __name__ == "__main__":
        root = Root()
        canvas = ResultCanvas(root)
        result = Result_Label(canvas)
        arg1 = dict(result=result)
        iface = MainInterface(root, **arg1)
        arg2 = dict(root=root, result=result, iface=iface)
        menu = Menus(root, **arg2)
        root.mainloop()
except SyntaxError:
    root = Root()
    checker_version()
except ModuleNotFoundError:
    root = Root()
    checker_playsound()
