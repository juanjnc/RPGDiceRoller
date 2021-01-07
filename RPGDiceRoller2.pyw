from tkinter import messagebox as mb
import tkinter as tk
import random


def info():  # Muestra la info de quien lo ha hecho
    mb.showinfo('Info RPG DR', 'Programmed in Python by Juan José Núñez')


def version():  # Muestra la version actual TODO actualizar los cambios
    mb.showinfo('Version RPG DR', 'Version 2.1.0')


def cambios():  # Muestra el registro de versiones TODO actualizar los cambios
    mb.showinfo('Changelog', '''2.1.0 - Added Mythras Hit Location die, use a sightly different table.
2.0.0 - Remade from the scratch. Now uses a completely new internal logic.''')


def limpiar():  # Limpia los resultados
    result.config(text='')


def salir():  # Menu de salida de la app
    valor = mb.askokcancel('Close', 'Are you sure?')
    if valor is True:
        raiz.destroy()


def genesys():  # Genera toda la interfaz de los dados Genesys
    def eliminar_g():  # Elimina toda la interfaz de Genesys
        result.config(text='')
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
        btn_g.destroy()
        menu.delete('Delete')
        raiz.geometry('400x330')

    def roll_g():  # Define los dados del sistema Genesys junto con el dado de fuerza de SW
        try:
            a, b, c = int(boost.get()), int(ability.get()), int(proficiency.get())
            d, e, f = int(setback.get()), int(difficulty.get()), int(challenge.get())
            g = int(force.get())
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
    # Ajusta el tamaño de la ventana
    raiz.geometry('800x330')
    # Crean las entradas de los dados
    force_label = tk.Label(cuadro, justify='right', text='Force Dice: ', font=('Arial', 12))
    challenge_label = tk.Label(cuadro, justify='right', text='Challenge Dice: ', font=('Arial', 12))
    difficulty_label = tk.Label(cuadro, justify='right', text='Difficulty Dice: ', font=('Arial', 12))
    setback_label = tk.Label(cuadro, justify='right', text='Setback Dice: ', font=('Arial', 12))
    proficiency_label = tk.Label(cuadro, justify='right', text='Proficiency Dice: ', font=('Arial', 12))
    ability_label = tk.Label(cuadro, justify='right', text='Ability Dice: ', font=('Arial', 12))
    boost_label = tk.Label(cuadro, justify='right', text='Boost Dice: ', font=('Arial', 12))
    force = tk.Entry(cuadro, width=5)
    challenge = tk.Entry(cuadro, width=5)
    difficulty = tk.Entry(cuadro, width=5)
    setback = tk.Entry(cuadro, width=5)
    proficiency = tk.Entry(cuadro, width=5)
    ability = tk.Entry(cuadro, width=5)
    boost = tk.Entry(cuadro, width=5)
    boost.grid(row=0, column=5, padx=10, pady=10)
    boost.config(justify='center', font=('Arial', 12))
    boost.insert(0, 0)
    ability.grid(row=1, column=5, padx=10, pady=10)
    ability.config(justify='center', font=('Arial', 12))
    ability.insert(0, 0)
    proficiency.grid(row=2, column=5, padx=10, pady=10)
    proficiency.config(justify='center', font=('Arial', 12))
    proficiency.insert(0, 0)
    setback.grid(row=3, column=5, padx=10, pady=10)
    setback.config(justify='center', font=('Arial', 12))
    setback.insert(0, 0)
    difficulty.grid(row=0, column=7, padx=10, pady=10)
    difficulty.config(justify='center', font=('Arial', 12))
    difficulty.insert(0, 0)
    challenge.grid(row=1, column=7, padx=10, pady=10)
    challenge.config(justify='center', font=('Arial', 12))
    challenge.insert(0, 0)
    force.grid(row=2, column=7, padx=10, pady=10)
    force.config(justify='center', font=('Arial', 12))
    force.insert(0, 0)
    # Crean los textos de los dados
    boost_label.grid(row=0, column=4, padx=10, pady=10, sticky='E')
    ability_label.grid(row=1, column=4, padx=10, pady=10, sticky='E')
    proficiency_label.grid(row=2, column=4, padx=10, pady=10, sticky='E')
    setback_label.grid(row=3, column=4, padx=10, pady=10, sticky='E')
    difficulty_label.grid(row=0, column=6, padx=10, pady=10, sticky='E')
    challenge_label.grid(row=1, column=6, padx=10, pady=10, sticky='E')
    force_label.grid(row=2, column=6, padx=10, pady=10, sticky='E')
    # Crea el boton para tirar los dados y eliminar la interfaz
    btn_g = tk.Button(cuadro, text="Genesys/SW", fg='green', command=roll_g, font=('Arial', 11), cursor='hand2')
    btn_g.grid(row=3, column=6, columnspan=2, padx=5, pady=5)
    menu.insert_command(5, label='Delete', command=eliminar_g, font=('Arial', 10))


class Raiz(tk.Tk):  # Crea la ventana principal
    def __init__(self):
        super().__init__()
        self.title('RPG Dice Roller v2')
        self.geometry('400x330')


class Frame(tk.Frame):  # Gestiona el marco de los botones
    def __init__(self, container):
        super().__init__(container)
        options = {'padx': 10, 'pady': 10}
        self.config(height='100', width='850')
        # Primera cantidad de dados
        self.pool = tk.Entry(self, width=5)
        self.pool.grid(row=0, column=2, **options)
        self.pool.config(justify='center', font=('Arial', 12))
        self.pool.insert(0, 1)
        # Primer dado
        self.dado = tk.Entry(self, width=5)
        self.dado.grid(row=1, column=2, **options)
        self.dado.config(justify='center', font=('Arial', 12))
        self.dado.insert(0, 2)
        # primer modificador
        self.mod = tk.Entry(self, width=5)
        self.mod.grid(row=2, column=2, **options)
        self.mod.config(justify='center', font=('Arial', 12))
        self.mod.insert(0, 0)
        # Seugunda cantidad de dados
        self.pool_2 = tk.Entry(self, width=5)
        self.pool_2.grid(row=0, column=3, **options)
        self.pool_2.config(justify='center', font=('Arial', 12))
        self.pool_2.insert(0, 0)
        # Segundo dado
        self.dado_2 = tk.Entry(self, width=5)
        self.dado_2.grid(row=1, column=3, **options)
        self.dado_2.config(justify='center', font=('Arial', 12))
        self.dado_2.insert(0, 0)
        # Segundo modificador
        self.mod_2 = tk.Entry(self, width=5)
        self.mod_2.grid(row=2, column=3,  **options)
        self.mod_2.config(justify='center', font=('Arial', 12))
        self.mod_2.insert(0, 0)
        # Etiqueta cantidad de dados
        self.pool_label = tk.Label(self, justify='right', text='nº of Dice: ', font=('Arial', 12))
        self.pool_label.grid(row=0, column=1, **options, sticky='E')
        # Etiqueta valor de dados
        self.dado_label = tk.Label(self, justify='right', text='Type of Dice: ', font=('Arial', 12))
        self.dado_label.grid(row=1, column=1, **options, sticky='E')
        # Etiqueta modificador
        self.mod_label = tk.Label(self, justify='right', text="Mod Value: ", font=('Arial', 12))
        self.mod_label.grid(row=2, column=1, **options, sticky='E')
        # Boton tirar dados
        self.btn0 = tk.Button(self, text="Roll", fg='green', command=self.roll, font=('Arial', 11), cursor='hand2')
        self.btn0.grid(row=0, column=0, **options)
        # Boton tirar FATE
        self.btn1 = tk.Button(self, text="FATE", fg='green', command=self.roll_fate, font=('Arial', 11), cursor='hand2')
        self.btn1.grid(row=1, column=0, **options)
        # Boton tirar RQ
        self.btn2 = tk.Button(self, text="RQ\nHit Loc", fg='green', command=self.roll_rq, font=('Arial', 11),
                              cursor='hand2')
        self.btn2.grid(row=3, column=2, **options)
        # Boton limpiar
        self.btn3 = tk.Button(self, text="Clear", fg='red', command=limpiar, font=('Arial', 11), cursor='hand2')
        self.btn3.grid(row=3, column=0, **options)
        # Boton tirar Mythras
        self.btn4 = tk.Button(self, text="Mythras\nHit Loc", fg='green', command=self.roll_mythras,
                              font=('Arial', 11), cursor='hand2')
        self.btn4.grid(row=3, column=1, **options)
        self.pack()  # Fin del Cuadro de los botones e inputs

    def roll(self):  # Define cualquier dado
        try:
            a, b, c = int(self.pool.get()), int(self.dado.get()), int(self.mod.get())
            d, e, f = int(self.pool_2.get()), int(self.dado_2.get()), int(self.mod_2.get())
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
                        result.config(text=f'{var_1}\n= {suma} + mod {c + f}\n= {suma + c + f}', fg='green')
                    else:
                        result.config(text=f'{var_1}\n{var_2}\n= {suma} + mod {c + f}\n= {suma + c + f}',
                                      fg='green')
            else:
                result.config(text='Error:\nEnter a valid number\nDice = 2 - 100\nNumber of dice = 1 - 100',
                              fg='red')
        except ValueError:
            result.config(text='Error:\nEnter a number', fg='red')

    def roll_fate(self):  # Define el dado usado en FATE, FUDGE y derivados
        try:
            a, c = int(self.pool.get()), int(self.mod.get())
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
                            result.config(text=f'{cut_1}\n{cut_2}\n + mod {c}\n= {total}', fg='green')
                            if not cut_2:
                                result.config(text=f'{cut_1}\n + mod {c}\n= {total}', fg='green')
                    else:
                        result.config(text=f'{cut_1}\n{cut_2}\n{cut_3}\n{cut_4}\n + mod {c}\n= {total}', fg='green')
            else:
                result.config(text='Error:\nEnter a valid number\nNumber of dice = 1 - 50', fg='red')
        except ValueError:
            result.config(text='Error:\nEnter a number', fg='red')

    def roll_rq(self):  # Define los rangos de cuerpo de BRP y derivados
        var = ('L. Leg', 'R. Leg', 'Abdomen', 'R. Arm', 'L. Arm', 'Chest', 'Head')
        fin = []
        for i in range(1):
            n = random.choices(var, weights=[4, 4, 3, 3, 3, 1, 2])
            fin.extend(n)
            result.config(text=f'{fin}', fg='green')

    def roll_mythras(self):  # Define los rangos de cuerpo de BRP y derivados
        var = ('L. Leg', 'R. Leg', 'Abdomen', 'R. Arm', 'L. Arm', 'Chest', 'Head')
        fin = []
        for i in range(1):
            n = random.choices(var, weights=[3, 3, 3, 3, 3, 3, 2])
            fin.extend(n)
            result.config(text=f'{fin}', fg='green')


class Lienzo(tk.Canvas):  # Gestiona el lienzo donde se muestra el resultado
    def __init__(self, container):
        super().__init__(container)
        options = {'side': 'bottom', 'expand': 'YES', 'fill': 'both'}
        self.config(bg='white', highlightthickness=5, highlightbackground="grey")
        self.pack(**options)


class Tutorials:  # Almacena todos los tutoriales
    @staticmethod
    def tutorial():  # Instrucciones de uso general
        tu = tk.Toplevel(raiz)
        tu.resizable(0, 0)
        tu.title('General Guide')
        tu_label = tk.Label(tu, text='\nFill the text fields with the numbers you want.\n\n\"Number of dice\" indicates'
                                     ' how many dice you want to roll.\n\"Type of dice\" indicates how many sides have'
                                     ' your dice.\n\"Mod value\" can add or subtract the number to the result.\nFATE '
                                     'use a custom Dice, you can change te amount of it.\nRQ Hit Location use a custom'
                                     ' die and roll only one.\nIn Genesys Dice they have custom names.\n',
                            justify='left', font=('Arial', 10), bg='white')
        tu_label.pack()

    @staticmethod
    def tut_roll():  # Instrucciones de botón roll
        tu_ro = tk.Toplevel(raiz)
        tu_ro.resizable(0, 0)
        tu_ro.title('Roll Guide')
        tu_ro_label = tk.Label(tu_ro, text='\nFill \"Number of dice\", \"Type of dice\" and \"Mod value\" text fields'
                                           ' with the numbers you want.\nYou can roll two types of dice with his owns'
                                           ' mod values, but first column must be filled.\nCombined values can not be'
                                           ' more of 100 and 1st die must be at least 2\n',
                               justify='left', font=('Arial', 10), bg='white')
        tu_ro_label.pack()

    @staticmethod
    def tut_fate():  # Instrucciones de botón fate
        tu_fa = tk.Toplevel(raiz)
        tu_fa.resizable(0, 0)
        tu_fa.title('FATE Guide')
        tu_fa_label = tk.Label(tu_fa, text='\nNeeds fill \"Number of dice\" and \"Mod value\".\n',
                               justify='left', font=('Arial', 10), bg='white')
        tu_fa_label.pack()

    @staticmethod
    def tut_rq():  # Instrucciones de botón RQ
        tu_rq = tk.Toplevel(raiz)
        tu_rq.resizable(0, 0)
        tu_rq.title('RQ Hit Location Guide')
        tu_rq_label = tk.Label(tu_rq, text='\nNo input needed. Roll once.\nUse the RuneQuest/BRP humanoid hit location'
                                           ' table.\n', justify='left', font=('Arial', 10), bg='white')
        tu_rq_label.pack()

    @staticmethod
    def tut_mythras():  # Instrucciones de botón RQ
        tu_rq = tk.Toplevel(raiz)
        tu_rq.resizable(0, 0)
        tu_rq.title('RQ Hit Location Guide')
        tu_rq_label = tk.Label(tu_rq, text='\nNo input needed. Roll once.\nUse the Mythras humanoid hit location'
                                           ' table.\n', justify='left', font=('Arial', 10), bg='white')
        tu_rq_label.pack()

    @staticmethod
    def tut_genesys():  # Instrucciones de botón Genesys/SW
        tu_ge = tk.Toplevel(raiz)
        tu_ge.resizable(0, 0)
        tu_ge.title('Genesys Guide')
        tu_ge_label = tk.Label(tu_ge,
                               text='Needs fill the Genesys Dice and the Star Wars Force Die, can roll with at least'
                                    ' one die of any type.', justify='left', font=('Arial', 10), bg='white')
        tu_ge_label.pack()

    @staticmethod
    def mostrar():  # Instrucciones del menú para mostrar más tipos de dados
        tu_sge = tk.Toplevel(raiz)
        tu_sge.resizable(0, 0)
        tu_sge.title('Show Genesys Guide')
        tu_sge_label = tk.Label(tu_sge,
                                text='Show the list for additional custom dice systems, and create the interface'
                                     ' for them.', justify='left', font=('Arial', 10), bg='white')
        tu_sge_label.pack()


class Menus(tk.Menu):  # Gestiona la barra de menú
    def __init__(self, container):
        super().__init__(container)
        # menu archivo
        archivo_menu = tk.Menu(self, tearoff=0)
        archivo_menu.add_command(label='Exit', command=salir, font=('Arial', 10))
        self.add_cascade(label='File', menu=archivo_menu, font=('Arial', 10))
        # menu de tutoriales
        tutorial_menu = tk.Menu(self, tearoff=0)
        tutorial_menu.add_command(label='Guide', command=Tutorials.tutorial, font=('Arial', 10))
        tutorial_menu.add_command(label='Roll', command=Tutorials.tut_roll, font=('Arial', 10))
        tutorial_menu.add_command(label='FATE', command=Tutorials.tut_fate, font=('Arial', 10))
        tutorial_menu.add_command(label='RuneQuest', command=Tutorials.tut_rq, font=('Arial', 10))
        tutorial_menu.add_command(label='Mythras', command=Tutorials.tut_rq, font=('Arial', 10))
        tutorial_menu.add_command(label='Show Menu', command=Tutorials.mostrar, font=('Arial', 10))
        tutorial_menu.add_separator()
        tutorial_menu.add_command(label='Genesys/SW', command=Tutorials.tut_genesys, font=('Arial', 10))
        self.add_cascade(label='User Guide', menu=tutorial_menu, font=('Arial', 10))
        # menu ed ayuda
        ayuda_menu = tk.Menu(self, tearoff=0)
        ayuda_menu.add_command(label='Version', command=version, font=('Arial', 10))
        ayuda_menu.add_command(label='Changelog', command=cambios, font=('Arial', 10))
        ayuda_menu.add_command(label='About...', command=info, font=('Arial', 10))
        self.add_cascade(label='Help', menu=ayuda_menu, font=('Arial', 10))
        # menu de dados adicionales
        dados_menu = tk.Menu(self, tearoff=0)
        dados_menu.add_command(label='Genesys', command=genesys, font=('Arial', 10))
        self.add_cascade(label='Show', menu=dados_menu, font=('Arial', 10))
        # Cierre
        raiz.config(menu=self, width=400, height=400)  # Fin de la config de la barra de menu


class Resultado(tk.Label):  # Gestiona la etiqueta de resultado
    def __init__(self, container):
        super().__init__(container)
        options = {'expand': 'YES'}
        self.config(justify='center', text='', font=('Arial', 15), fg='green', bg='white')
        self.pack(**options)


if __name__ == "__main__":  # Arranca toda la interfaz
    raiz = Raiz()
    menu = Menus(raiz)
    cuadro = Frame(raiz)
    canvas = Lienzo(raiz)
    result = Resultado(canvas)
    raiz.mainloop()
