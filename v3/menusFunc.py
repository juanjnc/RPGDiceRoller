from sys import platform  # Comprueba el SO
from tkinter import messagebox as mb
# Usa un import u otro según SO
if platform == "win32":
    from os import startfile
from subprocess import call


# Versión actual
def version(): return mb.showinfo('Version RPG DR 3', 'Version 3.3.2')


# Trae el changelog según el SO, es un problema relativamente común, lo encontré en diversos foros
def cambios():
    if platform == "win32":
        return startfile(r'.\data\CHANGELOG.txt')
    else:
        opener = "open" if platform == "darwin" else "xdg-open"
        return call([opener, r'./data/CHANGELOG.txt'])


def mitlicense(): return mb.showinfo('License', 'MIT License'
                                                '\n\nCopyright (c) 2021 Juan José Núñez Cózar'
                                                '\n\nPermission is hereby granted, free of charge, to any person '
                                                'obtaining a copy of this software and associated documentation files '
                                                '(the "Software"), to deal in the Software without restriction, '
                                                'including without limitation the rights to use, copy, modify, merge, '
                                                'publish, distribute, sublicense, and/or sell copies of the Software, '
                                                'and to permit persons to whom the Software is furnished to do so, '
                                                'subject to the following conditions: '
                                                '\n\nThe above copyright notice and this permission notice shall be '
                                                'included in all copies or substantial portions of the Software.'
                                                '\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, '
                                                'EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF '
                                                'MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND '
                                                'NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS '
                                                'BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN '
                                                'ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN '
                                                'CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE '
                                                'SOFTWARE.')


# Info y créditos básicos
def licenses(): return mb.showinfo('Licenses',
                                   '3rd party libraries: Playsound'
                                   '\nThis software is Copyright (c) 2021 Taylor Marks <taylor@marksfam.com>.'
                                   '\n(https://github.com/TaylorSMarks/playsound/blob/master/LICENSE)'
                                   '\n\nSounds obtained from FreeSound: (https://freesound.org/s/353975/) ('
                                   'https://freesound.org/s/350872/) '
                                   '\n(https://freesound.org/s/171494/) (https://freesound.org/s/242503/)'
                                   '\n\nUsed PyInstaller for creating the executables. ('
                                   'https://www.pyinstaller.org/license.html) '
                                   '\n\nUsed Inno Setup for creating the installer. ('
                                   'https://jrsoftware.org/files/is/license.txt)')


# Info y créditos básicos
def info(): return mb.showinfo('Info RPG DR 3',
                               'Copyright (c) 2021 Juan José Núñez Cózar under MIT License'
                               '\nWebsite: https://github.com/juanjnc/RPGDiceRoller'
                               '\n\nProgrammed in Python.\n(https://www.python.org/)'
                               '\n\nIcons made by Ana Canalejo.\n(https://www.deviantart.com/miyuminineko)'
                               '\n\nThanks to Rubén, Steph and Mauro for the help and support provided.')


# Menu de salida de la app
def crear_salir(raiz):
    def salir():
        valor = mb.askokcancel('Close', 'Are you sure?')
        if valor is True:
            raiz.destroy()

    return salir
