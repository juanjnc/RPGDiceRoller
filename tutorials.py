from tkinter import Toplevel
from tkinter.ttk import Label

# Instrucciones de uso general
def crear_tutorial(raiz):
    def tutorial():
        tu = Toplevel(raiz)
        tu.resizable(0,0),tu.title('General Guide')
        tu_label = Label(tu,text='\nFill the text fields with the numbers you want.\n\n\"Number of dice\" indicates how many '
                                    'dice you want to roll.\n\"Type of dice\" indicates how many sides have your dice.\n\"Mod '
                                    'value\" can add or subtract the number to the result.\n\nFATE use a custom Dice, you can '
                                    'change te amount of it.\n\nRQ and Mythras Hit Location use a custom die and roll only once.'
                                    '\n\nIn Genesys Dice they have custom names.\n',
                            justify='left',font=('Arial',10),background="white")
        tu_label.pack()
    return tutorial

# Instrucciones de botón roll
def crear_tut_roll(raiz):
    def tut_roll():
        tu_ro = Toplevel(raiz)
        tu_ro.resizable(0,0),tu_ro.title('Roll Guide')
        tu_ro_label = Label(tu_ro,text='\nFill \"Number of dice\", \"Type of dice\" and \"Mod value\" text fields with the '
                                            'numbers you want.\n\nYou can roll up three types of dice with his owns mod values, but '
                                            'first column must be filled.\nCombined values can not be more of 100 for Number of '
                                            'dice.\n1st die must be at least 2 and 2nd or 3rd die can be 0 but not 1.'
                                            '\n',justify='left',font=('Arial',10),background="white")
        tu_ro_label.pack()
    return tut_roll

# Instrucciones de botón fate
def crear_tut_fate(raiz):
    def tut_fate():
        tu_fa = Toplevel(raiz)
        tu_fa.resizable(0,0),tu_fa.title('FATE Guide')
        tu_fa_label = Label(tu_fa,text='\nNeeds fill \"Number of dice\" and \"Mod value\" in the first Column\n',
                            justify='left',font=('Arial',10),background="white")
        tu_fa_label.pack()
    return tut_fate

# Instrucciones de botón RQ
def crear_tut_rq(raiz):
    def tut_rq():
        tu_rq = Toplevel(raiz)
        tu_rq.resizable(0,0),tu_rq.title('RQ Hit Location Guide')
        tu_rq_label = Label(tu_rq,text='\nNo input needed. Roll once. Use the RuneQuest/BRP humanoid hit location table.\n'
                                       '\nUse a 20-sided dice with a range of values for location, with this total probability:'
                                       '\nL. Leg - 4, R. Leg - 4, Abdomen - 3, R. Arm - 3, L. Arm - 3, Chest - 1, Head - 2\n'
                            ,justify='left',font=('Arial',10),background="white")
        tu_rq_label.pack()
    return tut_rq

# Instrucciones de botón RQ
def crear_tut_myth(raiz):
    def tut_myth():
        tu_rq = Toplevel(raiz)
        tu_rq.resizable(0,0),tu_rq.title('Mythras Hit Location Guide')
        tu_rq_label = Label(tu_rq,text='\nNo input needed. Roll once. Use the Mythras humanoid hit location table.\n'
                                       '\nUse a 20-sided dice with a range of values for location, with this total probability:'
                                       '\nL. Leg - 3, R. Leg - 3, Abdomen - 3, R. Arm - 3, L. Arm - 3, Chest - 3, Head - 2\n'
                            ,justify='left',font=('Arial',10),background="white")
        tu_rq_label.pack()
    return tut_myth

# Instrucciones de botón Genesys/SW
def crear_tut_genesys(raiz):
    def tut_genesys():
        tu_ge = Toplevel(raiz)
        tu_ge.resizable(0,0),tu_ge.title('Genesys Guide')
        tu_ge_label = Label(tu_ge,text='\nNeeds fill the Genesys Dice and the Star Wars Force Die, can roll with at least one '
                                        'die of any type.\n',justify='left',font=('Arial',10),background="white")
        tu_ge_label.pack()
    return tut_genesys

# Instrucciones del menú para mostrar más tipos de dados
def crear_mostrar(raiz):
    def mostrar():
        tu_sge = Toplevel(raiz)
        tu_sge.resizable(0,0),tu_sge.title('Show Genesys Guide')
        tu_sge_label = Label(tu_sge,text='\nShow the list for additional custom dice systems, and create the interface for them.\n',
                             justify='left',font=('Arial',10),background="white")
        tu_sge_label.pack()
    return mostrar
