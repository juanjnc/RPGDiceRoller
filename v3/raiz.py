from tkinter import Tk, PhotoImage

# Gestiona la ventana principal
class Raiz(Tk):
    def __init__(self):
        super().__init__()
        self.title('RPG Dice Roller v3')
        self.geometry('400x400')
        img = PhotoImage(file=r'./data/ico.png')
        self.wm_iconphoto(True, img)
