from tkinter import *
from tkinter import messagebox
import random

raiz = Tk()  # Inicio raiz
raiz.title('RPG Dice Roller')
raiz.geometry('400x330')


def limpiar():
    result.config(text='')


def salir():
    valor = messagebox.askokcancel('Close', 'Are you sure?')
    if valor is True:
        raiz.destroy()


def info():
    messagebox.showinfo('Info RPG DR', 'Programmed in Python by Juan José Núñez')


def version():  # TODO actualizar los cambios
    messagebox.showinfo('Version RPG DR', 'Version 1.5.7')


def cambios():  # TODO actualizar los cambios
    cl = Toplevel(raiz)
    cl.resizable(0, 0)
    cl.title('Changelog RPG Dice Roller')
    cl_label = Label(cl, text='1.5.7 - Now the limit for FATE dice is 50. Now the combined limit for GENESYS is 50'
                              '\n1.5.6 - Now the limit of 100 dice is tracking the combined values for 1st and 2nd die'
                              '\n1.5.5 - HOTFIX: Fixed a bug with the 2nd die (rolls using the first die as a exponent)'
                              '.\nNow shows both dice separately instead of combined and sliced in four'
                              '\n1.5.4 - Improved internal logic. Improved the way to show the results'
                              '\n1.5.3 - Changed \"User Guide\'s\" and \"Changelog\" messages box to windows'
                              '\n1.5.2 - HOTFIX: Capped values for the second die'
                              '\n1.5.1 - Improved stability. Grammar fixing. Adjusted default size'
                              '\n1.5.0 - Added the option for roll two type of dice with two mods values'
                              '\n1.4.0 - Improved how probability works'
                              '\n1.3.0 - Changed result background. Hidden by default Genesys Custom Dice'
                              '\n1.2.0 - Changed the way to show the results, Minor fixes'
                              '\n1.1.1 - FATE now support Mod values. Minor fixes'
                              '\n1.1.0 - Added Genesys. Added \"Clear\" button. Smaller texts fields'
                              '\n1.0.1 - Minor fixes\n1.0.0 - Initial Release',
                     justify='left', font=('Arial', 9), bg='white')
    cl_label.pack()


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


def blue_genesys():  # Instrucciones de botón mostrar Genesys
    tu_sge = Toplevel(raiz)
    tu_sge.resizable(0, 0)
    tu_sge.title('Show Genesys Guide')
    tu_sge_label = Label(tu_sge, text='Show the Genesys Custom Dice expanding the window.',
                         justify='left', font=('Arial', 10), bg='white')
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


def fate():  # Define el dado usado en FATE, FUDGE y derivados
    try:
        a, c = int(pool.get()), int(mod.get())
        var = ('+', '-', '0')
        dest = []
        if 51 > a > 0:
            for i in range(a):
                n = random.choices(var, weights=[2, 2, 2])
                dest.extend(n)
                total = dest.count('+') - dest.count('-') + c
                cut_1, cut_2, cut_3, cut_4 = dest[:12], dest[12:24], dest[24:36], dest[36:]
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


def rq():  # Define los rangos de cuerpo de BRP y derivados
    var = ('L. Leg', 'R. Leg', 'Abdomen', 'R. Arm', 'L. Arm', 'Chest', 'Head')
    dest = []
    for i in range(1):
        n = random.choices(var, weights=[4, 4, 3, 3, 3, 1, 2])
        dest.extend(n)
        result.config(text=f'{dest}', fg='green')


def genesys_interfaz():  # Genera toda la interfáz de los dados Genesys

    def genesys():  # Define los dados del sistema Genesys junto con el dado de fuerza de SW
        genesys_interfaz()
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
            dest = []
            if 51 > a + b + c + d + e + f + g > 0:
                for i in range(a):
                    n = random.choices(var_boost, weights=[2, 1, 1, 1, 1])
                    dest.extend(n)
                for i in range(b):
                    n = random.choices(var_ability, weights=[2, 1, 1, 2, 1, 1])
                    dest.extend(n)
                for i in range(c):
                    n = random.choices(var_proficiency, weights=[1, 1, 2, 1, 2, 2, 3])
                    dest.extend(n)
                for i in range(d):
                    n = random.choices(var_setback, weights=[2, 1, 1, 2, 1, 1])
                    dest.extend(n)
                for i in range(e):
                    n = random.choices(var_difficulty, weights=[1, 2, 3, 3, 1, 1])
                    dest.extend(n)
                for i in range(f):
                    n = random.choices(var_challenge, weights=[2, 2, 1, 2, 2, 2, 1])
                    dest.extend(n)
                for i in range(g):
                    n = random.choices(var_force, weights=[6, 2, 1, 3])
                    dest.extend(n)
                suc = dest.count('success') + 2 * dest.count('success, success') + dest.count('advantage, success')
                adv = dest.count('advantage') + 2 * dest.count('advantage, advantage') \
                    + dest.count('advantage, success')
                tri = dest.count('triumph')
                thr = dest.count('threat') + 2 * dest.count('threat, threat') + dest.count('threat, failure')
                fail = dest.count('failure') + 2 * dest.count('failure, failure') + dest.count('threat, failure')
                des = dest.count('despair')
                fds = dest.count('DARK') + 2 * dest.count('DARK, DARK')
                fls = dest.count('LIGHT') + 2 * dest.count('LIGHT, LIGHT')
                cut_1, cut_2, cut_3, cut_4, cut_5 = dest[:5], dest[5:10], dest[10:20], dest[20:30], dest[30:]
                if not cut_5:
                    result.config(text=f'{cut_1}\n{cut_2}\n{cut_3}\n{cut_4}\nsuccess = {suc}; advantage = {adv}'
                                       f'; triumph = {tri}\nfailure = {fail}; threat = {thr}; despair = {des}'
                                       f'\nForce Dark Side = {fds}, Force Light Side = {fls}', fg='green')
                    if not cut_4:
                        result.config(text=f'{cut_1}\n{cut_2}\n{cut_3}\nsuccess = {suc}; advantage = {adv}'
                                           f'; triumph = {tri}\nfailure = {fail}; threat = {thr}; despair = {des}'
                                           f'\nForce Dark Side = {fds}, Force Light Side = {fls}', fg='green')
                        if not cut_3:
                            result.config(text=f'{cut_1}\n{cut_2}\nsuccess = {suc}; advantage = {adv}'
                                               f'; triumph = {tri}\nfailure = {fail}; threat = {thr}; despair = {des}'
                                               f'\nForce Dark Side = {fds}, Force Light Side = {fls}', fg='green')
                            if not cut_2:
                                result.config(
                                    text=f'{cut_1}\nsuccess = {suc}; advantage = {adv}; triumph = {tri}'
                                         f'\nfailure = {fail}; threat = {thr}; despair = {des}\nForce Dark Side = {fds}'
                                         f', Force Light Side = {fls}', fg='green')
                else:
                    result.config(text=f'{cut_1}\n{cut_2}\n{cut_3}\n{cut_4}\n{cut_5}'
                                       f'\nsuccess = {suc}; advantage = {adv}; triumph = {tri}\n'
                                       f'failure = {fail}; threat = {thr}; despair = {des}\n'
                                       f'Force Dark Side = {fds}, Force Light Side = {fls}', fg='green')
            else:
                result.config(text='Error:\nEnter a valid number\nNumber of dice = 1 - 50', fg='red')
        except ValueError:
            result.config(text='Error:\nEnter a number', fg='red')
    # Ajusta el tamaño de la ventana
    raiz.geometry('800x330')
    # Destruye el boton que crea la interfaz
    btn5.destroy()
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
    btn3 = Button(cuadro, text="Genesys/SW", fg='green', command=genesys, font=('Arial', 11), cursor='hand2')
    btn3.grid(row=3, column=6, columnspan=2, padx=5, pady=5)


barra_menu = Menu(raiz)  # Config de las barras de menu
archivo_menu = Menu(barra_menu, tearoff=0)
tutorial_menu = Menu(barra_menu, tearoff=0)
ayuda_menu = Menu(barra_menu, tearoff=0)

archivo_menu.add_command(label='Exit', command=salir, font=('Arial', 10))

tutorial_menu.add_command(label='Guide', command=tutorial, font=('Arial', 10))
tutorial_menu.add_command(label='Roll', command=tut_roll, font=('Arial', 10))
tutorial_menu.add_command(label='FATE', command=tut_fate, font=('Arial', 10))
tutorial_menu.add_command(label='RuneQuest', command=tut_rq, font=('Arial', 10))
tutorial_menu.add_command(label='Show Genesys', command=blue_genesys, font=('Arial', 10))
tutorial_menu.add_command(label='Genesys/SW', command=tut_genesys, font=('Arial', 10))

ayuda_menu.add_command(label='Version', command=version, font=('Arial', 10))
ayuda_menu.add_command(label='Changelog', command=cambios, font=('Arial', 10))
ayuda_menu.add_command(label='About...', command=info, font=('Arial', 10))

barra_menu.add_cascade(label='File', menu=archivo_menu, font=('Arial', 10))
barra_menu.add_cascade(label='User Guide', menu=tutorial_menu, font=('Arial', 10))
barra_menu.add_cascade(label='Help', menu=ayuda_menu, font=('Arial', 10))
raiz.config(menu=barra_menu, width=400, height=400)  # Fin de la config de la barra de menu

cuadro = Frame(raiz, height='100', width='850')  # Inicio del Cuadro de los botones e inputs
# Primera cantidad de dados
pool = Entry(cuadro, width=5)
pool.grid(row=0, column=2, padx=10, pady=10)
pool.config(justify='center', font=('Arial', 12))
pool.insert(0, 1)
# Primer dado
dado = Entry(cuadro, width=5)
dado.grid(row=1, column=2, padx=10, pady=10)
dado.config(justify='center', font=('Arial', 12))
dado.insert(0, 2)
# primer modificador
mod = Entry(cuadro, width=5)
mod.grid(row=2, column=2, padx=10, pady=10)
mod.config(justify='center', font=('Arial', 12))
mod.insert(0, 0)
# Seugunda cantidad de dados
pool_2 = Entry(cuadro, width=5)
pool_2.grid(row=0, column=3, padx=10, pady=10)
pool_2.config(justify='center', font=('Arial', 12))
pool_2.insert(0, 0)
# Segundo dado
dado_2 = Entry(cuadro, width=5)
dado_2.grid(row=1, column=3, padx=10, pady=10)
dado_2.config(justify='center', font=('Arial', 12))
dado_2.insert(0, 0)
# Segundo modificador
mod_2 = Entry(cuadro, width=5)
mod_2.grid(row=2, column=3, padx=10, pady=10)
mod_2.config(justify='center', font=('Arial', 12))
mod_2.insert(0, 0)
# Etiqueta cantidad de dados
pool_label = Label(cuadro, justify='right', text='nº of Dice: ', font=('Arial', 12))
pool_label.grid(row=0, column=1, padx=10, pady=10, sticky='E')
# Etiqueta valor de dados
dado_label = Label(cuadro, justify='right', text='Type of Dice: ', font=('Arial', 12))
dado_label.grid(row=1, column=1, padx=10, pady=10, sticky='E')
# Etiqueta modificador
mod_label = Label(cuadro, justify='right', text="Mod Value: ", font=('Arial', 12))
mod_label.grid(row=2, column=1, padx=10, pady=10, sticky='E')
# Boton tirar dados
btn0 = Button(cuadro, text="Roll", fg='green', command=roll, font=('Arial', 11), cursor='hand2')
btn0.grid(row=0, column=0, padx=5, pady=5)
# Boton tirar FATE
btn1 = Button(cuadro, text="FATE", fg='green', command=fate, font=('Arial', 11), cursor='hand2')
btn1.grid(row=1, column=0, padx=5, pady=5)
# Boton tirar RQ
btn2 = Button(cuadro, text="RQ\nHit Location", fg='green', command=rq, font=('Arial', 11), cursor='hand2')
btn2.grid(row=2, column=0, padx=5, pady=5)
# btn3 está dentro de Genesys
# Boton limpiar
btn4 = Button(cuadro, text="Clear", fg='blue', command=limpiar, font=('Arial', 11), cursor='hand2')
btn4.grid(row=3, column=0, padx=5, pady=5)
# Boton mostrar Genesys
btn5 = Button(cuadro, text="Show Genesys", fg='blue', command=genesys_interfaz, font=('Arial', 11), cursor='hand2')
btn5.grid(row=3, column=1, padx=5, pady=5, columnspan=2)

cuadro.pack()  # Fin del Cuadro de los botones e inputs

canvas = Canvas(raiz, bg='white', highlightthickness=5, highlightbackground="grey")  # Inicio de Canvas y resultado
result = Label(canvas, justify='center', text='', font=('Arial', 16), fg='green', bg='white')
result.pack(expand=YES)
canvas.pack(expand=YES, fill=BOTH)  # Fin de Canvas y resultado

raiz.mainloop()  # Fin raiz
