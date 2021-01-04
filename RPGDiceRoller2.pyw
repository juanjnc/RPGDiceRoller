from tkinter import messagebox as mb
import tkinter as tk
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
    mb.showinfo('Version RPG DR', 'Version 2.0.0')


def cambios():  # TODO actualizar los cambios
    mb.showinfo('Changelog', '''2.0.0 - Remade from the scratch''')


def tutorial():  # Instrucciones de uso general
    tu = tk.Toplevel(raiz)
    tu.resizable(0, 0)
    tu.title('General Guide')
    tu_label = tk.Label(tu, text='Fill the text fields with the numbers you want.\n\n\"Number of dice\" indicates '
                                 'how many dice you want to roll.\n\"Type of dice\" indicates how many sides have '
                                 'your dice.\n\"Mod value\" can add or subtract the number to the result.\nFATE use '
                                 'a custom Dice, you can change te amount of it.\nRQ Hit Location use a custom die'
                                 ' and roll only one.\nIn Genesys Dice they have custom names.',
                        justify='left', font=('Arial', 10), bg='white')
    tu_label.pack()


def tut_roll():  # Instrucciones de botón roll
    tu_ro = tk.Toplevel(raiz)
    tu_ro.resizable(0, 0)
    tu_ro.title('Roll Guide')
    tu_ro_label = tk.Label(tu_ro, text='Fill \"Number of dice\", \"Type of dice\" and \"Mod value\" text fields with the '
                                      'numbers you want.\nYou can roll two types of dice with his owns mod values, but'
                                    'first column must be filled. Combined values can not be more of 100 and 1st die '
                                    'must be at least 2', justify='left', font=('Arial', 10), bg='white')
    tu_ro_label.pack()


def tut_fate():  # Instrucciones de botón fate
    tu_fa = tk.Toplevel(raiz)
    tu_fa.resizable(0, 0)
    tu_fa.title('FATE Guide')
    tu_fa_label = tk.Label(tu_fa, text='Needs fill \"Number of dice\" and \"Mod value\".',
                        justify='left', font=('Arial', 10), bg='white')
    tu_fa_label.pack()


def tut_rq():  # Instrucciones de botón RQ
    tu_rq = tk.Toplevel(raiz)
    tu_rq.resizable(0, 0)
    tu_rq.title('RQ Hit Location Guide')
    tu_rq_label = tk.Label(tu_rq, text='No input needed. Roll once.\nUse the RuneQuest/BRP/Mythras hit location table.',
                        justify='left', font=('Arial', 10), bg='white')
    tu_rq_label.pack()


def tut_genesys():  # Instrucciones de botón Genesys/SW
    tu_ge = tk.Toplevel(raiz)
    tu_ge.resizable(0, 0)
    tu_ge.title('Genesys Guide')
    tu_ge_label = tk.Label(tu_ge, text='Needs fill the Genesys Dice and the Star Wars Force Die, can roll with at least'
                                    ' one die of any type.', justify='left', font=('Arial', 10), bg='white')
    tu_ge_label.pack()


def mostrar():  # Instrucciones del menú para mostrar más tipos de dados
    tu_sge = tk.Toplevel(raiz)
    tu_sge.resizable(0, 0)
    tu_sge.title('Show Genesys Guide')
    tu_sge_label = tk.Label(tu_sge, text='Show the list for additional custom dice systems, and create the interface for'
                                      ' them.', justify='left', font=('Arial', 10), bg='white')
    tu_sge_label.pack()


class Genesys:  # Genera toda la interfaz de los dados Genesys
    def __init__(self, container):
        super().__init__(container)
        # Ajusta el tamaño de la ventana
        raiz.geometry('800x330')
        # Crean las entradas de los dados
        self.boost = tk.Entry(cuadro, width=5)
        self.boost.grid(row=0, column=5, padx=10, pady=10)
        self.boost.config(justify='center', font=('Arial', 12))
        self.boost.insert(0, 0)
        self.ability = tk.Entry(cuadro, width=5)
        self.ability.grid(row=1, column=5, padx=10, pady=10)
        self.ability.config(justify='center', font=('Arial', 12))
        self.ability.insert(0, 0)
        self.proficiency = tk.Entry(cuadro, width=5)
        self.proficiency.grid(row=2, column=5, padx=10, pady=10)
        self.proficiency.config(justify='center', font=('Arial', 12))
        self.proficiency.insert(0, 0)
        self.setback = tk.Entry(cuadro, width=5)
        self.setback.grid(row=3, column=5, padx=10, pady=10)
        self.setback.config(justify='center', font=('Arial', 12))
        self.setback.insert(0, 0)
        self.difficulty = tk.Entry(cuadro, width=5)
        self.difficulty.grid(row=0, column=7, padx=10, pady=10)
        self.difficulty.config(justify='center', font=('Arial', 12))
        self.difficulty.insert(0, 0)
        self.challenge = tk.Entry(cuadro, width=5)
        self.challenge.grid(row=1, column=7, padx=10, pady=10)
        self.challenge.config(justify='center', font=('Arial', 12))
        self.challenge.insert(0, 0)
        self.force = tk.Entry(cuadro, width=5)
        self.force.grid(row=2, column=7, padx=10, pady=10)
        self.force.config(justify='center', font=('Arial', 12))
        self.force.insert(0, 0)
        # Crean los textos de los dados
        self.boost_label = tk.Label(cuadro, justify='right', text='Boost Dice: ', font=('Arial', 12))
        self.boost_label.grid(row=0, column=4, padx=10, pady=10, sticky='E')
        self.ability_label = tk.Label(cuadro, justify='right', text='Ability Dice: ', font=('Arial', 12))
        self.ability_label.grid(row=1, column=4, padx=10, pady=10, sticky='E')
        self.proficiency_label = tk.Label(cuadro, justify='right', text='Proficiency Dice: ', font=('Arial', 12))
        self.proficiency_label.grid(row=2, column=4, padx=10, pady=10, sticky='E')
        self.setback_label = tk.Label(cuadro, justify='right', text='Setback Dice: ', font=('Arial', 12))
        self.setback_label.grid(row=3, column=4, padx=10, pady=10, sticky='E')
        self.difficulty_label = tk.Label(cuadro, justify='right', text='Difficulty Dice: ', font=('Arial', 12))
        self.difficulty_label.grid(row=0, column=6, padx=10, pady=10, sticky='E')
        self.challenge_label = tk.Label(cuadro, justify='right', text='Challenge Dice: ', font=('Arial', 12))
        self.challenge_label.grid(row=1, column=6, padx=10, pady=10, sticky='E')
        self.force_label = tk.Label(cuadro, justify='right', text='Force Dice: ', font=('Arial', 12))
        self.force_label.grid(row=2, column=6, padx=10, pady=10, sticky='E')
        # Crea el boton para tirar los dados
        self.btn3 = tk.Button(cuadro, text="Genesys/SW", fg='green', command=self.roll_g, font=('Arial', 11),
                              cursor='hand2')
        self.btn3.grid(row=3, column=6, columnspan=2, padx=5, pady=5)
        # dados_menu.add_command(label='Delete', command=eliminar_g, font=('Arial', 10))

    def roll_g(self):  # Define los dados del sistema Genesys junto con el dado de fuerza de SW
        try:
            a, b, c = int(self.boost.get()), int(self.ability.get()), int(self.proficiency.get())
            d, e, f = int(self.setback.get()), int(self.difficulty.get()), int(self.challenge.get())
            g = int(self.force.get())
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

    def eliminar_g(self):
        result.config(text='')
        self.boost.destroy()
        self.ability.destroy()
        self.proficiency.destroy()
        self.setback.destroy()
        self.difficulty.destroy()
        self.challenge.destroy()
        self.force.destroy()
        self.boost_label.destroy()
        self.ability_label.destroy()
        self.proficiency_label.destroy()
        self.setback_label.destroy()
        self.difficulty_label.destroy()
        self.challenge_label.destroy()
        self.force_label.destroy()
        self.btn3.destroy()
        #dados_menu.delete('Delete')
        raiz.geometry('400x330')



def menu():
    barra_menu = tk.Menu(raiz)  # Config de las barras de menu
    archivo_menu = tk.Menu(barra_menu, tearoff=0)
    tutorial_menu = tk.Menu(barra_menu, tearoff=0)
    ayuda_menu = tk.Menu(barra_menu, tearoff=0)
    dados_menu = tk.Menu(barra_menu, tearoff=0)
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
    dados_menu.add_command(label='Genesys', command=Genesys, font=('Arial', 10))
    barra_menu.add_cascade(label='File', menu=archivo_menu, font=('Arial', 10))
    barra_menu.add_cascade(label='User Guide', menu=tutorial_menu, font=('Arial', 10))
    barra_menu.add_cascade(label='Show', menu=dados_menu, font=('Arial', 10))
    barra_menu.add_cascade(label='Help', menu=ayuda_menu, font=('Arial', 10))
    raiz.config(menu=barra_menu, width=400, height=400)  # Fin de la config de la barra de menu


class Raiz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('RPG Dice Roller')
        self.geometry('400x330')


class Frame(tk.Frame):
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
        self.btn2 = tk.Button(self, text="RQ\nHit Location", fg='green', command=self.roll_rq, font=('Arial', 11), cursor='hand2')
        self.btn2.grid(row=2, column=0, **options)
        # btn3 está dentro de Genesys
        # Boton limpiar
        self.btn4 = tk.Button(self, text="Clear", fg='blue', command=limpiar, font=('Arial', 11), cursor='hand2')
        self.btn4.grid(row=3, column=0, **options)
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


class Lienzo(tk.Canvas):
    def __init__(self, container):
        super().__init__(container)
        options = {'side': 'bottom', 'expand': 'YES', 'fill': 'both'}
        self.config(bg='white', highlightthickness=5, highlightbackground="grey")
        self.pack(**options)


class Resultado(tk.Label):
    def __init__(self, container):
        super().__init__(container)
        options = {'expand': 'YES'}
        self.config(justify='center', text='', font=('Arial', 15), fg='green', bg='white')
        self.pack(**options)


if __name__ == "__main__":
    raiz = Raiz()
    cuadro = Frame(raiz)
    canvas = Lienzo(raiz)
    result = Resultado(canvas)
    menu()
    raiz.mainloop()
