from tkinter import Canvas


# Gestiona el lienzo donde se muestra el resultado
class Lienzo(Canvas):
    def __init__(self, container):
        super().__init__(container)
        options = {'side': 'bottom', 'expand': 'YES', 'fill': 'both'}
        self.config(background='white', highlightthickness=5, highlightbackground="grey")
        self.pack(**options)
