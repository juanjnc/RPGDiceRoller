from tkinter import Tk

# Gestiona la ventana principal
class Raiz(Tk):
    def __init__(self):
        super().__init__()
        self.title('RPG Dice Roller v3'),self.geometry('400x400'),self.iconbitmap('ico.ico')
