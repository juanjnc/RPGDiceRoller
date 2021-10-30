from tkinter import *
from tkinter.ttk import *


class Tutorials:  # Almacena todos los tutoriales


    @staticmethod
    def tutorial():  # Instrucciones de uso general
        tu = Toplevel(raiz)
        tu.resizable(0,0),tu.title('General Guide')
        tu_label = Label(tu,text='\nFill the text fields with the numbers you want.\n\n\"Number of dice\" indicates how many '
                                    'dice you want to roll.\n\"Type of dice\" indicates how many sides have your dice.\n\"Mod '
                                    'value\" can add or subtract the number to the result.\nFATE use a custom Dice, you can '
                                    'change te amount of it.\nRQ Hit Location use a custom die and roll only one.'
                                    '\nIn Genesys Dice they have custom names.\n',
                         justify='left',font=('Arial',10),background="white")
        tu_label.pack()

    @staticmethod
    def tut_roll():  # Instrucciones de botón roll
        tu_ro = Toplevel(raiz)
        tu_ro.resizable(0,0),tu_ro.title('Roll Guide')
        tu_ro_label = Label(tu_ro,text='\nFill \"Number of dice\", \"Type of dice\" and \"Mod value\" text fields with the '
                                          'numbers you want.\n\nYou can roll two types of dice with his owns mod values, but '
                                          'first column must be filled.\nCombined values can not be more of 100 for Number of '
                                          'dice.\n1st die must be at least 2 and second die can be 0 but not 1.'
                                          '\n',justify='left',font=('Arial',10),background="white")
        tu_ro_label.pack()

    @staticmethod
    def tut_fate():  # Instrucciones de botón fate
        tu_fa = Toplevel(raiz)
        tu_fa.resizable(0,0),tu_fa.title('FATE Guide')
        tu_fa_label = Label(tu_fa,text='\nNeeds fill \"Number of dice\" and \"Mod value\".\n',
                               justify='left',font=('Arial',10),background="white")
        tu_fa_label.pack()

    @staticmethod
    def tut_rq():  # Instrucciones de botón RQ
        tu_rq = Toplevel(raiz)
        tu_rq.resizable(0,0),tu_rq.title('RQ Hit Location Guide')
        tu_rq_label = Label(tu_rq,text='\nNo input needed. Roll once.\nUse the RuneQuest/BRP humanoid hit location'
                                          ' table.\n',justify='left',font=('Arial',10),background="white")
        tu_rq_label.pack()

    @staticmethod
    def tut_myth():  # Instrucciones de botón RQ
        tu_rq = Toplevel(raiz)
        tu_rq.resizable(0,0),tu_rq.title('Mythras Hit Location Guide')
        tu_rq_label = Label(tu_rq,text='\nNo input needed. Roll once.\nUse the Mythras humanoid hit location table.'
                                          '\n',justify='left',font=('Arial',10),background="white")
        tu_rq_label.pack()

    @staticmethod
    def tut_genesys():  # Instrucciones de botón Genesys/SW
        tu_ge = Toplevel(raiz)
        tu_ge.resizable(0,0),tu_ge.title('Genesys Guide')
        tu_ge_label = Label(tu_ge,
                               text='\nNeeds fill the Genesys Dice and the Star Wars Force Die, can roll with at least one '
                                    'die of any type.\n',justify='left',font=('Arial',10),background="white")
        tu_ge_label.pack()

    @staticmethod
    def mostrar():  # Instrucciones del menú para mostrar más tipos de dados
        tu_sge = Toplevel(raiz)
        tu_sge.resizable(0,0),tu_sge.title('Show Genesys Guide')
        tu_sge_label = Label(tu_sge,
                                text='\nShow the list for additional custom dice systems, and create the interface for them.\n',
                                justify='left',font=('Arial',10),background="white")
        tu_sge_label.pack()