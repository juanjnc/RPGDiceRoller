from tkinter import Toplevel
from tkinter.ttk import Label


# Instrucciones de uso general
def create_tutorial(root):
    def tutorial():
        tu = Toplevel(root)
        tu.resizable(False, False), tu.title('General Guide')
        tu_label = Label(tu,
                         text='\nFill the text fields with the numbers you want.\n\n\"Number of dice\" indicates how '
                              'many dice you want to roll.\n\"Type of dice\" indicates how many sides have your '
                              'dice.\n\"Mod value\" can add or subtract the number to the result.\n\nFATE use a '
                              'custom Dice, you can change te amount of it using the first \"Number of dice\" text '
                              'field. \n\nRQ and Mythras Hit Location use a custom die and roll only once.'
                              '\n\nIn the custom system Genesys, the dice have specific proper names.\n',
                         justify='left', font=('Arial', 10), background="white")
        tu_label.pack()

    return tutorial


# Instrucciones de botón roll
def create_tut_roll(root):
    def tut_roll():
        tu_ro = Toplevel(root)
        tu_ro.resizable(False, False), tu_ro.title('Roll Guide')
        tu_ro_label = Label(tu_ro,
                            text='\nFill \"Number of dice\", \"Type of dice\" and \"Mod value\" text fields with the '
                                 'numbers you want.\n\nYou can roll up three types of dice with his owns mod values, '
                                 'but first column must be filled.\nCombined values can not be more of 100 for Number '
                                 'of dice.\n1st die must be at least 2 and 2nd or 3rd die can be 0 but not 1.\n',
                            justify='left', font=('Arial', 10), background="white")
        tu_ro_label.pack()

    return tut_roll


# Instrucciones de botón fate
def create_tut_fate(root):
    def tut_fate():
        tu_fa = Toplevel(root)
        tu_fa.resizable(False, False), tu_fa.title('FATE Guide')
        tu_fa_label = Label(tu_fa, text='\nNeeds fill \"Number of dice\" and \"Mod value\" in the first Column\n',
                            justify='left', font=('Arial', 10), background="white")
        tu_fa_label.pack()

    return tut_fate


# Instrucciones de botón RQ
def create_tut_rq(root):
    def tut_rq():
        tu_rq = Toplevel(root)
        tu_rq.resizable(False, False), tu_rq.title('RQ Hit Location Guide')
        tu_rq_label = Label(tu_rq,
                            text='\nNo input needed. Roll once. Use the RuneQuest/BRP humanoid hit location table.\n'
                                 '\nUse a 20-sided dice with a range of values for location, with this total '
                                 'probability: \nL. Leg - 4, R. Leg - 4, Abdomen - 3, R. Arm - 3, L. Arm - 3, '
                                 'Chest - 1, Head - 2\n',
                            justify='left', font=('Arial', 10), background="white")
        tu_rq_label.pack()

    return tut_rq


# Instrucciones de botón RQ
def create_tut_myth(root):
    def tut_myth():
        tu_rq = Toplevel(root)
        tu_rq.resizable(False, False), tu_rq.title('Mythras Hit Location Guide')
        tu_rq_label = Label(tu_rq, text='\nNo input needed. Roll once. Use the Mythras humanoid hit location table.\n'
                                        '\nUse a 20-sided dice with a range of values for location, with this total '
                                        'probability: \nL. Leg - 3, R. Leg - 3, Abdomen - 3, R. Arm - 3, L. Arm - 3, '
                                        'Chest - 3, Head - 2\n',
                            justify='left', font=('Arial', 10), background="white")
        tu_rq_label.pack()

    return tut_myth


# Instrucciones de botón Genesys/SW
def create_tut_genesys(root):
    def tut_genesys():
        tu_ge = Toplevel(root)
        tu_ge.resizable(False, False), tu_ge.title('Genesys Guide')
        tu_ge_label = Label(tu_ge,
                            text='\nNeeds fill the Genesys Dice and the Star Wars Force Die, can roll with at least '
                                 'one die of any type.\n\n'
                                 'Symbols meaning, can combinate in the results:'
                                 '\nS = success, A = Advantage, Tr = Triumph'
                                 '\nF = Failure, T = Threat, De = Despair'
                                 '\nD = Dark Force Energy L, = Light Force Energy\n',
                            justify='left', font=('Arial', 10), background="white")
        tu_ge_label.pack()

    return tut_genesys


# Instrucciones del menú para mostrar más tipos de dados
def create_show(root):
    def show():
        tu_sge = Toplevel(root)
        tu_sge.resizable(False, False), tu_sge.title('Show Genesys Guide')
        tu_sge_label = Label(tu_sge,
                             text='\nShow the list for additional custom dice systems, and create the interface for '
                                  'them.\n',
                             justify='left', font=('Arial', 10), background="white")
        tu_sge_label.pack()

    return show
