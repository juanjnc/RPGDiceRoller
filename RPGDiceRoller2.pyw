from tkinter import *
from tkinter import messagebox as mb
import tkinter as raiz

import random


def limpiar():
    result.config(text='')


def salir():
    valor = mb.askokcancel('Close', 'Are you sure?')
    if valor is True:
        raiz.destroy()


def info():
    mb.showinfo('Info RPG DR', 'Programmed in Python by Juan José Núñez')


def version():  # TODO actualizar los cambios
    mb.showinfo('Version RPG DR', 'Version 1.5.9')


def cambios():  # TODO actualizar los cambios
    mb.showinfo('Changelog', '''1.5.9 - Small changes and grammar fixes. Fixed the initial values reset in Genesys dice.
1.5.8 - Reverted "Changelog" to message box. Small fixes.
1.5.7 - Now the limit for FATE dice and combined Genesys dice is 50.
1.5.6 - Now the limit of 100 dice is tracking the combined values for 1st and 2nd die.
1.5.5 - Fixed a bug with the 2nd die (rolls using the first die as an exponent). Now shows both dice separately
1.5.4 - Improved internal logic. Improved the way to show the results.
1.5.3 - Changed "User Guide's" and "Changelog" messages box to windows.
1.5.2 - HOTFIX: Capped values for the second die.\n1.5.1 - Improved stability. Grammar fixing. Adjusted default size.
1.5.0 - Added the option for roll two type of dice with two mods values.
1.4.0 - Improved how probability works.\n1.3.0 - Changed result background. Hidden by default Genesys Custom Dice.
1.2.0 - Changed the way to show the results, Minor fixes.\n1.1.1 - FATE now support Mod values. Minor fixes.
1.1.0 - Added Genesys. Added "Clear" button. Smaller texts fields.\n1.0.1 - Minor fixes.\n1.0.0 - Initial Release.''')


def tutorial():  # Instrucciones de uso general
    tu = Toplevel(raiz)
    tu.resizable(0, 0)
    tu.title('General Guide')
    tu_label = Label(tu, text='Fill the text fields with the numbers you want.'
                              '\n\n\"Number of dice\" indicates how many dice you want to roll.'
                              '\n\"Type of dice\" indicates how many sides have your dice.'
                              '\n\"Mod value\" can add or subtract the number to the result.'
                              '\nFATE use a custom Dice, you can change te amount of it.'
                              '\nRQ Hit Location use a custom die and roll only one.'
                              '\nIn Genesys Dice they have custom names.',
                     justify='left', font=('Arial', 10), bg='white')
    tu_label.pack()


def tut_roll():  # Instrucciones de botón roll
    tu_ro = Toplevel(raiz)
    tu_ro.resizable(0, 0)
    tu_ro.title('Roll Guide')
    tu_ro_label = Label(tu_ro, text='Fill \"Number of dice\", \"Type of dice\" and \"Mod value\" text fields with the '
                                    'numbers you want.\nYou can roll two types of dice with his owns mod values, but'
                                    'first column must be filled. Combined values can not be more of 100 and 1st die '
                                    'must be at least 2', justify='left', font=('Arial', 10), bg='white')
    tu_ro_label.pack()


def tut_fate():  # Instrucciones de botón fate
    tu_fa = Toplevel(raiz)
    tu_fa.resizable(0, 0)
    tu_fa.title('FATE Guide')
    tu_fa_label = Label(tu_fa, text='Needs fill \"Number of dice\" and \"Mod value\".',
                        justify='left', font=('Arial', 10), bg='white')
    tu_fa_label.pack()


def tut_rq():  # Instrucciones de botón RQ
    tu_rq = Toplevel(raiz)
    tu_rq.resizable(0, 0)
    tu_rq.title('RQ Hit Location Guide')
    tu_rq_label = Label(tu_rq, text='No input needed. Roll once.\nUse the RuneQuest/BRP/Mythras hit location table.',
                        justify='left', font=('Arial', 10), bg='white')
    tu_rq_label.pack()


def tut_genesys():  # Instrucciones de botón Genesys/SW
    tu_ge = Toplevel(raiz)
    tu_ge.resizable(0, 0)
    tu_ge.title('Genesys Guide')
    tu_ge_label = Label(tu_ge, text='Needs fill the Genesys Dice and the Star Wars Force Die, can roll with at least'
                                    ' one die of any type.', justify='left', font=('Arial', 10), bg='white')
    tu_ge_label.pack()


def mostrar():  # Instrucciones del menú para mostrar más tipos de dados
    tu_sge = Toplevel(raiz)
    tu_sge.resizable(0, 0)
    tu_sge.title('Show Genesys Guide')
    tu_sge_label = Label(tu_sge, text='Show the list for additional custom dice systems, and create the interface for'
                                      ' them.', justify='left', font=('Arial', 10), bg='white')
    tu_sge_label.pack()


def roll():  # Define cualquier dado
    try:
        a, b, c = int(pool.get()), int(dado.get()), int(mod.get())
        d, e, f = int(pool_2.get()), int(dado_2.get()), int(mod_2.get())
        var_1, var_2 = [], []
        if (101 > b > 1) and (101 > e >= 0) and (101 > a + d > 0) and (a != 0) and (e != 1):
            for i in range(a):
                n = random.randint(1, b)
                var_1.append(n)
            for j in range(d):
                m = random.randint(1, e)
                var_2.append(m)
            suma = sum(var_1 + var_2)
            if c == 0 and f == 0:
                if not var_2:
                    result.config(text=f'{var_1}\n= {suma}', fg='green')
                else:
                    result.config(text=f'{var_1}\n{var_2}\n= {suma}', fg='green')
            else:
                if not var_2:
                    result.config(text=f'{var_1}\n= {suma} + mod\n= {suma + c + f}', fg='green')
                else:
                    result.config(text=f'{var_1}\n{var_2}\n= {suma} + mod\n= {suma + c + f}', fg='green')
        else:
            result.config(text='Error:\nEnter a valid number\nDice = 2 - 100\nNumber of dice = 1 - 100', fg='red')
    except ValueError:
        result.config(text='Error:\nEnter a number', fg='red')


def roll_fate():  # Define el dado usado en FATE, FUDGE y derivados
    try:
        a, c = int(pool.get()), int(mod.get())
        var = ('+', '-', '0')
        fin = []
        if 51 > a > 0:
            for i in range(a):
                n = random.choices(var, weights=[2, 2, 2])
                fin.extend(n)
                total = fin.count('+') - fin.count('-') + c
                cut_1, cut_2, cut_3, cut_4 = fin[:12], fin[12:24], fin[24:36], fin[36:]
                if not cut_4:
                    result.config(text=f'{cut_1}\n{cut_2}\n{cut_3}\n= {total}', fg='green')
                    if not cut_3:
                        result.config(text=f'{cut_1}\n{cut_2}\n= {total}', fg='green')
                        if not cut_2:
                            result.config(text=f'{cut_1}\n= {total}', fg='green')
                else:
                    result.config(text=f'{cut_1}\n{cut_2}\n{cut_3}\n{cut_4}\n= {total}', fg='green')
        else:
            result.config(text='Error:\nEnter a valid number\nNumber of dice = 1 - 50', fg='red')
    except ValueError:
        result.config(text='Error:\nEnter a number', fg='red')


def roll_rq():  # Define los rangos de cuerpo de BRP y derivados
    var = ('L. Leg', 'R. Leg', 'Abdomen', 'R. Arm', 'L. Arm', 'Chest', 'Head')
    fin = []
    for i in range(1):
        n = random.choices(var, weights=[4, 4, 3, 3, 3, 1, 2])
        fin.extend(n)
        result.config(text=f'{fin}', fg='green')


def genesys():  # Genera toda la interfaz de los dados Genesys

    def roll_g():  # Define los dados del sistema Genesys junto con el dado de fuerza de SW
        try:
            a, b, c, d = int(boost.get()), int(ability.get()), int(proficiency.get()), int(setback.get())
            e, f, g = int(difficulty.get()), int(challenge.get()), int(force.get())
            var_boost = ('0', 'success', 'advantage', 'advantage, advantage', 'advantage, success')
            var_ability = ('success', 'success, success', '0', 'advantage', 'advantage, success',
                           'advantage, advantage')
            var_proficiency = ('0', 'triumph', 'success', 'advantage', 'success, success', 'advantage, advantage',
                               'advantage, success')
            var_setback = ('success', 'success, success', '0', 'advantage', 'advantage, success',
                           'advantage, advantage')
            var_difficulty = ('failure', 'failure, failure', '0', 'threat', 'threat, failure', 'threat, threat')
            var_challenge = ('failure', 'failure, failure', '0', 'threat', 'threat, failure', 'threat, threat',
                             'despair')
            var_force = ('DARK', 'LIGHT', 'DARK, DARK', 'LIGHT, LIGHT')
            fin = []
            if 51 > a + b + c + d + e + f + g > 0:
                for i in range(a):
                    n = random.choices(var_boost, weights=[2, 1, 1, 1, 1])
                    fin.extend(n)
                for j in range(b):
                    n = random.choices(var_ability, weights=[2, 1, 1, 2, 1, 1])
                    fin.extend(n)
                for ii in range(c):
                    n = random.choices(var_proficiency, weights=[1, 1, 2, 1, 2, 2, 3])
                    fin.extend(n)
                for jj in range(d):
                    n = random.choices(var_setback, weights=[2, 1, 1, 2, 1, 1])
                    fin.extend(n)
                for iii in range(e):
                    n = random.choices(var_difficulty, weights=[1, 2, 3, 3, 1, 1])
                    fin.extend(n)
                for jjj in range(f):
                    n = random.choices(var_challenge, weights=[2, 2, 1, 2, 2, 2, 1])
                    fin.extend(n)
                for iiii in range(g):
                    n = random.choices(var_force, weights=[6, 2, 1, 3])
                    fin.extend(n)
                suc = fin.count('success') + 2 * fin.count('success, success') + fin.count('advantage, success')
                adv = fin.count('advantage') + 2 * fin.count('advantage, advantage') + fin.count('advantage, success')
                tri = fin.count('triumph')
                thr = fin.count('threat') + 2 * fin.count('threat, threat') + fin.count('threat, failure')
                fail = fin.count('failure') + 2 * fin.count('failure, failure') + fin.count('threat, failure')
                des = fin.count('despair')
                fds = fin.count('DARK') + 2 * fin.count('DARK, DARK')
                fls = fin.count('LIGHT') + 2 * fin.count('LIGHT, LIGHT')
                cut_1, cut_2, cut_3, cut_4, cut_5 = fin[:5], fin[5:10], fin[10:20], fin[20:30], fin[30:]
                if not cut_5:
                    result.config(text=f'{cut_1}\n{cut_2}\n{cut_3}\n{cut_4}\nsuccess = {suc}; advantage = {adv}'
                                       f'; triumph = {tri}\nfailure = {fail}; threat = {thr}; despair = {des}'
                                       f'\nForce Dark Side = {fds}; Force Light Side = {fls}', fg='green')
                    if not cut_4:
                        result.config(text=f'{cut_1}\n{cut_2}\n{cut_3}\nsuccess = {suc}; advantage = {adv}'
                                           f'; triumph = {tri}\nfailure = {fail}; threat = {thr}; despair = {des}'
                                           f'\nForce Dark Side = {fds}; Force Light Side = {fls}', fg='green')
                        if not cut_3:
                            result.config(text=f'{cut_1}\n{cut_2}\nsuccess = {suc}; advantage = {adv}'
                                               f'; triumph = {tri}\nfailure = {fail}; threat = {thr}; despair = {des}'
                                               f'\nForce Dark Side = {fds}; Force Light Side = {fls}', fg='green')
                            if not cut_2:
                                result.config(text=f'{cut_1}\nsuccess = {suc}; advantage = {adv}; triumph = {tri}'
                                                   f'\nfailure = {fail}; threat = {thr}; despair = {des}\nForce Dark'
                                                   f' Side = {fds}; Force Light Side = {fls}', fg='green')
                else:
                    result.config(text=f'{cut_1}\n{cut_2}\n{cut_3}\n{cut_4}\n{cut_5}'
                                       f'\nsuccess = {suc}; advantage = {adv}; triumph = {tri}\n'
                                       f'failure = {fail}; threat = {thr}; despair = {des}\n'
                                       f'Force Dark Side = {fds}; Force Light Side = {fls}', fg='green')
            else:
                result.config(text='Error:\nEnter a valid number\nNumber of dice = 1 - 50', fg='red')
        except ValueError:
            result.config(text='Error:\nEnter a number', fg='red')

    def eliminar_g():
        boost.destroy()
        ability.destroy()
        proficiency.destroy()
        setback.destroy()
        difficulty.destroy()
        challenge.destroy()
        force.destroy()
        boost_label.destroy()
        ability_label.destroy()
        proficiency_label.destroy()
        setback_label.destroy()
        difficulty_label.destroy()
        challenge_label.destroy()
        force_label.destroy()
        btn3.destroy()
        dados_menu.delete('Delete')
        raiz.geometry('400x330')

    # Ajusta el tamaño de la ventana
    raiz.geometry('800x330')
    # Crean las entradas de los dados
    boost = Entry(cuadro, width=5)
    boost.grid(row=0, column=5, padx=10, pady=10)
    boost.config(justify='center', font=('Arial', 12))
    boost.insert(0, 0)
    ability = Entry(cuadro, width=5)
    ability.grid(row=1, column=5, padx=10, pady=10)
    ability.config(justify='center', font=('Arial', 12))
    ability.insert(0, 0)
    proficiency = Entry(cuadro, width=5)
    proficiency.grid(row=2, column=5, padx=10, pady=10)
    proficiency.config(justify='center', font=('Arial', 12))
    proficiency.insert(0, 0)
    setback = Entry(cuadro, width=5)
    setback.grid(row=3, column=5, padx=10, pady=10)
    setback.config(justify='center', font=('Arial', 12))
    setback.insert(0, 0)
    difficulty = Entry(cuadro, width=5)
    difficulty.grid(row=0, column=7, padx=10, pady=10)
    difficulty.config(justify='center', font=('Arial', 12))
    difficulty.insert(0, 0)
    challenge = Entry(cuadro, width=5)
    challenge.grid(row=1, column=7, padx=10, pady=10)
    challenge.config(justify='center', font=('Arial', 12))
    challenge.insert(0, 0)
    force = Entry(cuadro, width=5)
    force.grid(row=2, column=7, padx=10, pady=10)
    force.config(justify='center', font=('Arial', 12))
    force.insert(0, 0)
    # Crean los textos de los dados
    boost_label = Label(cuadro, justify='right', text='Boost Dice: ', font=('Arial', 12))
    boost_label.grid(row=0, column=4, padx=10, pady=10, sticky='E')
    ability_label = Label(cuadro, justify='right', text='Ability Dice: ', font=('Arial', 12))
    ability_label.grid(row=1, column=4, padx=10, pady=10, sticky='E')
    proficiency_label = Label(cuadro, justify='right', text='Proficiency Dice: ', font=('Arial', 12))
    proficiency_label.grid(row=2, column=4, padx=10, pady=10, sticky='E')
    setback_label = Label(cuadro, justify='right', text='Setback Dice: ', font=('Arial', 12))
    setback_label.grid(row=3, column=4, padx=10, pady=10, sticky='E')
    difficulty_label = Label(cuadro, justify='right', text='Difficulty Dice: ', font=('Arial', 12))
    difficulty_label.grid(row=0, column=6, padx=10, pady=10, sticky='E')
    challenge_label = Label(cuadro, justify='right', text='Challenge Dice: ', font=('Arial', 12))
    challenge_label.grid(row=1, column=6, padx=10, pady=10, sticky='E')
    force_label = Label(cuadro, justify='right', text='Force Dice: ', font=('Arial', 12))
    force_label.grid(row=2, column=6, padx=10, pady=10, sticky='E')
    # Crea el boton para tirar los dados
    btn3 = Button(cuadro, text="Genesys/SW", fg='green', command=roll_g, font=('Arial', 11), cursor='hand2')
    btn3.grid(row=3, column=6, columnspan=2, padx=5, pady=5)
    dados_menu.add_command(label='Delete', command=eliminar_g, font=('Arial', 10))


def barra_menu(Menu):
    barra_menu = Menu(raiz)  # Config de las barras de menu
    archivo_menu = Menu(barra_menu, tearoff=0)
    tutorial_menu = Menu(barra_menu, tearoff=0)
    ayuda_menu = Menu(barra_menu, tearoff=0)
    dados_menu = Menu(barra_menu, tearoff=0)

    archivo_menu.add_command(label='Exit', command=salir, font=('Arial', 10))

    tutorial_menu.add_command(label='Guide', command=tutorial, font=('Arial', 10))
    tutorial_menu.add_command(label='Roll', command=tut_roll, font=('Arial', 10))
    tutorial_menu.add_command(label='FATE', command=tut_fate, font=('Arial', 10))
    tutorial_menu.add_command(label='RuneQuest', command=tut_rq, font=('Arial', 10))
    tutorial_menu.add_command(label='Show Menu', command=mostrar, font=('Arial', 10))
    tutorial_menu.add_separator()
    tutorial_menu.add_command(label='Genesys/SW', command=tut_genesys, font=('Arial', 10))

    ayuda_menu.add_command(label='Version', command=version, font=('Arial', 10))
    ayuda_menu.add_command(label='Changelog', command=cambios, font=('Arial', 10))
    ayuda_menu.add_command(label='About...', command=info, font=('Arial', 10))

    dados_menu.add_command(label='Genesys', command=genesys, font=('Arial', 10))

    barra_menu.add_cascade(label='File', menu=archivo_menu, font=('Arial', 10))
    barra_menu.add_cascade(label='User Guide', menu=tutorial_menu, font=('Arial', 10))
    barra_menu.add_cascade(label='Show', menu=dados_menu, font=('Arial', 10))
    barra_menu.add_cascade(label='Help', menu=ayuda_menu, font=('Arial', 10))


class App(raiz.Tk):
    def __init__(self):
        super().__init__()
        self.title('RPG Dice Roller')
        self.geometry('400x330')
        self.config(menu=barra_menu, width=400, height=400)  # Fin de la config de la barra de menu


if __name__ == "__main__":
    app = App()
    app.mainloop()
