from tkinter import *
from os import startfile  # De momento la única función usada
from tkinter import messagebox as mb
from tutorials import Tutorials
from genesys import genesys_iface


class Menus(Menu):  # Gestiona la barra de menú
    def __init__(self,container):
        super().__init__(container)
        # menu archivo
        archivo_menu = Menu(self,tearoff=0)
        archivo_menu.add_command(label='Exit',command=self.salir,font=('Arial',10))
        self.add_cascade(label='File',menu=archivo_menu,font=('Arial',10))
        # menu de tutoriales
        tutorial_menu = Menu(self,tearoff=0)
        tutorial_menu.add_command(label='Guide',command=Tutorials.tutorial,font=('Arial',10))
        tutorial_menu.add_command(label='Roll',command=Tutorials.tut_roll,font=('Arial',10))
        tutorial_menu.add_command(label='FATE',command=Tutorials.tut_fate,font=('Arial',10))
        tutorial_menu.add_command(label='RuneQuest',command=Tutorials.tut_rq,font=('Arial',10))
        tutorial_menu.add_command(label='Mythras',command=Tutorials.tut_myth,font=('Arial',10))
        tutorial_menu.add_command(label='Show Menu',command=Tutorials.mostrar,font=('Arial',10))
        tutorial_menu.add_separator()
        tutorial_menu.add_command(label='Genesys/SW',command=Tutorials.tut_genesys,font=('Arial',10))
        self.add_cascade(label='User Guide',menu=tutorial_menu,font=('Arial',10))
        # menu de ayuda
        ayuda_menu = Menu(self,tearoff=0)
        ayuda_menu.add_command(label='Version',command=self.version,font=('Arial',10))
        ayuda_menu.add_command(label='Changelog',command=self.cambios,font=('Arial',10))
        ayuda_menu.add_command(label='About...',command=self.info,font=('Arial',10))
        self.add_cascade(label='Help',menu=ayuda_menu,font=('Arial',10))
        # menu de dados adicionales
        dados_menu = Menu(self,tearoff=0)
        dados_menu.add_command(label='Genesys',command=genesys_iface,font=('Arial',10))
        self.add_cascade(label='Show',menu=dados_menu,font=('Arial',10))
        # Cierre
        container.config(menu=self)

    @staticmethod
    def info(): mb.showinfo('Info RPG DR 2','Programmed in Python by Juan José Núñez.\n(https://www.python.org/)'
                                            '\n\nIcons made by Ana Canalejo.\n(https://www.deviantart.com/miyuminineko)')

    @staticmethod
    def version(): mb.showinfo('Version RPG DR 2','Version 2.4.1')

    @staticmethod
    def cambios(): startfile('CHANGELOG.txt')

    @staticmethod
    def salir():  # Menu de salida de la app
        valor = mb.askokcancel('Close','Are you sure?')
        if valor is True: raiz.destroy()
