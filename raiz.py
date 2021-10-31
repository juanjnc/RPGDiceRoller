from tkinter import *


class Raiz(Tk):  # Crea la ventana principal
    def __init__(self):
        super().__init__()
        self.title('RPG Dice Roller v3'),self.geometry('400x400'),self.iconbitmap('ico.ico')