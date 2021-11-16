from os import startfile  # De momento la única función usada
from tkinter import messagebox as mb

# Versión actual
def version(): return mb.showinfo('Version RPG DR 3','Version 3.2.1')

#Trae el changelog
def cambios(): return startfile('CHANGELOG.txt')

# Info y créditos básicos
def info(): return mb.showinfo('Info RPG DR 3','Programmed in Python by Juan José Núñez.\n(https://www.python.org/)'
                                               '\n\nIcons made by Ana Canalejo.\n(https://www.deviantart.com/miyuminineko)'
                                               '\n\nThanks to Rubén, Steph and Mauro for the help and support provided.')
# Menu de salida de la app
def crear_salir(raiz):
    def salir():
        valor=mb.askokcancel('Close','Are you sure?')
        if valor is True: raiz.destroy()
    return salir
