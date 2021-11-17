from sys import version_info
from tkinter import messagebox as mb

def checker_version():
    if version_info<(3,10):
        return mb.showinfo('Error: Python Version',f'Minimum Python version is 3.10'
                                                  f'\nYour version is {version_info.major}.{version_info.minor}')

def checker_playsound():
    return mb.showinfo('Error: Module Missing','Playsound 1.2.2 required\n(https://pypi.org/project/playsound/)')
