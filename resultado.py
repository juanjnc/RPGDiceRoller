from tkinter.ttk import *


class Resultado(Label):  # Gestiona la etiqueta de resultado
    def __init__(self,container):
        super().__init__(container)
        options = {'expand':'YES'}
        self.config(justify='center',text='',font=('Arial',15),foreground='green',background='white'),self.pack(**options)
