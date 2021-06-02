# - *- coding: utf- 8 - *-
import tkinter as tk
from os import startfile  # De momento la única función usada
from random import choices,randint,choice  # Solo los módulos utilizados
from tkinter import messagebox as mb


def genesys_iface():  # Genera toda la interfaz de los dados Genesys
    def eliminar_g():  # Elimina toda la interfaz de Genesys
        result.config(text=''),bst.destroy(),abi.destroy(),prof.destroy(),sback.destroy(),diff.destroy(),cha.destroy()
        frc.destroy(),bst_label.destroy(),abi_label.destroy(),prof_label.destroy(),sback_label.destroy(),diff_label.destroy()
        cha_label.destroy(),frc_label.destroy(),btn_g.destroy(),menu.delete('Delete Genesys'),raiz.geometry('400x340')

    def roll_g():  # Define los dados del sistema Genesys junto con el dado de fuerza de SW
        a,b,c = int(bst.get()),int(abi.get()),int(prof.get())
        d,e,f = int(sback.get()),int(diff.get()),int(cha.get())
        g = int(frc.get())  # Dado de fuerza, muy situacional en el sistema
        var_bst = ('0','success','advantage','advantage, advantage','advantage, success')
        var_abi = ('success','success, success','0','advantage','advantage, success','advantage, advantage')
        var_prof = ('0','triumph','success','advantage','success, success','advantage, advantage','advantage, success')
        var_sback = ('success','success, success','0','advantage','advantage, success','advantage, advantage')
        var_diff = ('failure','failure, failure','0','threat','threat, failure','threat, threat')
        var_cha = ('failure','failure, failure','0','threat','threat, failure','threat, threat','despair')
        var_frc = ('DARK','LIGHT','DARK, DARK','LIGHT, LIGHT')
        fin = []
        try:
            if 50 >= a+b+c+d+e+f+g > 0:  # Lanza y agrupa los dados Genesys
                n = choices(var_bst,weights=[2,1,1,1,1],k=a); fin.extend(n)
                n = choices(var_abi,weights=[2,1,1,2,1,1],k=b); fin.extend(n)
                n = choices(var_prof,weights=[1,1,2,1,2,2,3],k=c); fin.extend(n)
                n = choices(var_sback,weights=[2,1,1,2,1,1],k=d); fin.extend(n)
                n = choices(var_diff,weights=[1,2,3,3,1,1],k=e); fin.extend(n)
                n = choices(var_cha,weights=[2,2,1,2,2,2,1],k=f); fin.extend(n)
                n = choices(var_frc,weights=[6,2,1,3],k=g); fin.extend(n)
                suc = fin.count('success')+2*fin.count('success, success')+fin.count('advantage, success')
                adv = fin.count('advantage')+2*fin.count('advantage, advantage')+fin.count('advantage, success')
                tri = fin.count('triumph')
                thr = fin.count('threat')+2*fin.count('threat, threat')+fin.count('threat, failure')
                fail = fin.count('failure')+2*fin.count('failure, failure')+fin.count('threat, failure')
                des = fin.count('despair')
                fds = fin.count('DARK')+2*fin.count('DARK, DARK')
                fls = fin.count('LIGHT')+2*fin.count('LIGHT, LIGHT')
                cut_1,cut_2,cut_3,cut_4,cut_5 = fin[:5],fin[5:10],fin[10:20],fin[20:30],fin[30:]
                if not cut_5:
                    result.config(text=f'{cut_1}\n{cut_2}\n{cut_3}\n{cut_4}\nsuccess = {suc}; advantage = {adv}'
                                       f'; triumph = {tri}\nfailure = {fail}; threat = {thr}; despair = {des}'
                                       f'\nForce Dark Side = {fds}; Force Light Side = {fls}',fg='green')
                    if not cut_4:
                        result.config(text=f'{cut_1}\n{cut_2}\n{cut_3}\nsuccess = {suc}; advantage = {adv}'
                                           f'; triumph = {tri}\nfailure = {fail}; threat = {thr}; despair = {des}'
                                           f'\nForce Dark Side = {fds}; Force Light Side = {fls}',fg='green')
                        if not cut_3:
                            result.config(text=f'{cut_1}\n{cut_2}\nsuccess = {suc}; advantage = {adv}'
                                               f'; triumph = {tri}\nfailure = {fail}; threat = {thr}; despair = {des}'
                                               f'\nForce Dark Side = {fds}; Force Light Side = {fls}',fg='green')
                            if not cut_2:
                                result.config(text=f'{cut_1}\nsuccess = {suc}; advantage = {adv}; triumph = {tri}'
                                                   f'\nfailure = {fail}; threat = {thr}; despair = {des}\nForce Dark'
                                                   f' Side = {fds}; Force Light Side = {fls}',fg='green')
                else:
                    result.config(text=f'{cut_1}\n{cut_2}\n{cut_3}\n{cut_4}\n{cut_5}\nsuccess = {suc}; advantage = {adv};'
                                       f' triumph = {tri}\nfailure = {fail}; threat = {thr}; despair = {des}'
                                       f'\nForce Dark Side = {fds}; Force Light Side = {fls}',fg='green')
            else:
                result.config(text='Error:\nEnter a valid number\nNumber of dice = 1 - 50',fg='red')
        except ValueError:
            result.config(text='Error:\nEnter a number',fg='red')

    # Ajusta el tamaño de la ventana
    raiz.geometry('800x340')
    # Crean los textos de los dados
    bst_label = tk.Label(cuadro,justify='right',text='Boost Dice: ',font=('Arial',12))
    bst_label.grid(row=0,column=4,padx=10,pady=10,sticky='E')
    abi_label = tk.Label(cuadro,justify='right',text='Ability Dice: ',font=('Arial',12))
    abi_label.grid(row=1,column=4,padx=10,pady=10,sticky='E')
    prof_label = tk.Label(cuadro,justify='right',text='Proficiency Dice: ',font=('Arial',12))
    prof_label.grid(row=2,column=4,padx=10,pady=10,sticky='E')
    sback_label = tk.Label(cuadro,justify='right',text='Setback Dice: ',font=('Arial',12))
    sback_label.grid(row=0,column=6,padx=10,pady=10,sticky='E')
    diff_label = tk.Label(cuadro,justify='right',text='Difficulty Dice: ',font=('Arial',12))
    diff_label.grid(row=1,column=6,padx=10,pady=10,sticky='E')
    cha_label = tk.Label(cuadro,justify='right',text='Challenge Dice: ',font=('Arial',12))
    cha_label.grid(row=2,column=6,padx=10,pady=10,sticky='E')
    frc_label = tk.Label(cuadro,justify='right',text='Force Dice: ',font=('Arial',12))
    frc_label.grid(row=3,column=4,padx=10,pady=10,sticky='E')
    # Crean y configuran las entradas de los dados
    frc = tk.Entry(cuadro,width=5)
    frc.grid(row=3,column=5,padx=10,pady=10),frc.config(justify='center',font=('Arial',12)),frc.insert(0,0)
    cha = tk.Entry(cuadro,width=5)
    cha.grid(row=2,column=7,padx=10,pady=10),cha.config(justify='center',font=('Arial',12)),cha.insert(0,0)
    diff = tk.Entry(cuadro,width=5)
    diff.grid(row=1,column=7,padx=10,pady=10),diff.config(justify='center',font=('Arial',12)),diff.insert(0,0)
    sback = tk.Entry(cuadro,width=5)
    sback.grid(row=0,column=7,padx=10,pady=10),sback.config(justify='center',font=('Arial',12)),sback.insert(0,0)
    prof = tk.Entry(cuadro,width=5)
    prof.grid(row=2,column=5,padx=10,pady=10),prof.config(justify='center',font=('Arial',12)),prof.insert(0,0)
    abi = tk.Entry(cuadro,width=5)
    abi.grid(row=1,column=5,padx=10,pady=10),abi.config(justify='center',font=('Arial',12)),abi.insert(0,0)
    bst = tk.Entry(cuadro,width=5)
    bst.grid(row=0,column=5,padx=10,pady=10),bst.config(justify='center',font=('Arial',12)),bst.insert(0,0)
    # Crea el botón para tirar los dados y eliminar la interfaz
    btn_g = tk.Button(cuadro,text="Genesys/SW",fg='green',command=roll_g,font=('Arial',11),cursor='hand2')
    btn_g.grid(row=3,column=6,columnspan=2,padx=5,pady=5)
    menu.insert_command(5, label='Delete Genesys',command=eliminar_g,font=('Arial',10))


class Raiz(tk.Tk):  # Crea la ventana principal
    def __init__(self):
        super().__init__()
        self.title('RPG Dice Roller v2'),self.geometry('400x340'),self.iconbitmap('ico.ico')


class Interfaz(tk.Frame):  # Gestiona el marco de los botones
    def __init__(self,container):
        super().__init__(container)
        op = {'padx':10,'pady':10}
        self.config(height='100',width='850')
        # Primera cantidad de dados
        self.pool = tk.Entry(self,width=5)
        self.pool.grid(row=0,column=2,**op),self.pool.config(justify='center',font=('Arial',12)),self.pool.insert(0,1)
        # Primer dado
        self.dado = tk.Entry(self,width=5)
        self.dado.grid(row=1,column=2,**op),self.dado.config(justify='center',font=('Arial',12)),self.dado.insert(0,2)
        # primer modificador
        self.mod = tk.Entry(self,width=5)
        self.mod.grid(row=2,column=2,**op),self.mod.config(justify='center',font=('Arial',12)),self.mod.insert(0,0)
        # Segunda cantidad de dados
        self.pool_2 = tk.Entry(self,width=5)
        self.pool_2.grid(row=0,column=3,**op),self.pool_2.config(justify='center',font=('Arial',12)),self.pool_2.insert(0,0)
        # Segundo dado
        self.dado_2 = tk.Entry(self,width=5)
        self.dado_2.grid(row=1,column=3,**op),self.dado_2.config(justify='center',font=('Arial',12)),self.dado_2.insert(0,0)
        # Segundo modificador
        self.mod_2 = tk.Entry(self,width=5)
        self.mod_2.grid(row=2,column=3,**op),self.mod_2.config(justify='center',font=('Arial',12)),self.mod_2.insert(0,0)
        # Etiqueta cantidad de dados
        self.pool_label = tk.Label(self,justify='right',text='nº of Dice: ',font=('Arial',12))
        self.pool_label.grid(row=0,column=1,**op,sticky='E')
        # Etiqueta valor de dados
        self.dado_label = tk.Label(self,justify='right',text='Type of Dice: ',font=('Arial',12))
        self.dado_label.grid(row=1,column=1,**op,sticky='E')
        # Etiqueta modificador
        self.mod_label = tk.Label(self,justify='right',text="Mod Value: ",font=('Arial',12))
        self.mod_label.grid(row=2,column=1,**op,sticky='E')
        # Botón tirar dados
        self.btn_roll = tk.Button(self,text="Roll",fg='green',command=self.roll,font=('Arial',11),cursor='hand2')
        self.btn_roll.grid(row=0,column=0,**op)
        # Botón tirar FATE
        self.btn_fate = tk.Button(self,text="FATE",fg='green',command=self.roll_fate,font=('Arial',11),cursor='hand2')
        self.btn_fate.grid(row=1,column=0,**op)
        # Etiqueta modificador
        self.mod_label = tk.Label(self,justify='right',text="Hit Location: ",font=('Arial',12))
        self.mod_label.grid(row=3,column=1,**op,sticky='E')
        # Botón tirar RQ
        self.btn_rq = tk.Button(self,text="RQ",fg='blue',command=self.roll_rq,font=('Arial',11),cursor='hand2')
        self.btn_rq.grid(row=3,column=3,**op)
        # Botón tirar Mythras
        self.btn_myth = tk.Button(self,text="Mythras",fg='blue',command=self.roll_myth,font=('Arial',11),cursor='hand2')
        self.btn_myth.grid(row=3,column=2,**op),self.pack()
        # Botón limpiar
        self.btn_clean = tk.Button(self,text="Clear",fg='red',command=self.limpiar,font=('Arial',14),cursor='hand2', bd=4)
        self.btn_clean.grid(row=3,column=0, rowspan=3, **op)
        # Botón Huevo de Pascua
        self.btn_egg = tk.Button(self,text="     ",command=self.eggs,fg='red',font=('Arial',4), bd=0)
        self.btn_egg.grid(row=2,column=0, padx=10, pady=10)
        # Fin del Cuadro de los botones e inputs

    def roll(self):  # Define cualquier dado
        a,b,c = int(self.pool.get()),int(self.dado.get()),int(self.mod.get())
        d,e,f = int(self.pool_2.get()),int(self.dado_2.get()),int(self.mod_2.get())
        die_1,die_2 = [],[]
        try:  # Las tiradas y las listas de ambos dados
            if (101 > b > 1) and (101 > e >= 0) and (101 > a+d > 0) and (a!=0) and (e!=1):
                for i in range(a): n = randint(1,b); die_1.append(n)  # Lanza y agrupa dado 1
                for j in range(d): m = randint(1,e); die_2.append(m)  # Lanza y agrupa dado 2
                suma = sum(die_1+die_2)  # Suma las dos tiradas
                if c==0 and f==0:  # Si no hay modificadores
                    if not die_2:  # Si no hay dado 2
                        result.config(text=f'{die_1}\n= {suma}',fg='green')
                    else:
                        result.config(text=f'{die_1}\n{die_2}\n= {suma}',fg='green')
                else:  # Si hay modificadores
                    if not die_2:  # Si no hay dado 2
                        result.config(text=f'{die_1}\n= {suma} + mod: {c+f}\n= {suma+c+f}',fg='green')
                    else:
                        result.config(text=f'{die_1}\n{die_2}\n= {suma} + mod: {c+f}\n= {suma+c+f}',fg='green')
            else:  # Recoge cualquier numero erróneo
                result.config(text='Error:\nEnter a valid number\nDice = 2 - 100\nNumber of dice = 1 - 100',fg='red')
        except ValueError:  # Recoge errores y limpia las casillas
            result.config(text='Error:\nEnter a number',fg='red')
            self.mod.delete(0,10),self.mod.insert(0,0),self.mod_2.delete(0,10),self.mod_2.insert(0,0)
            self.dado_2.delete(0,10),self.dado_2.insert(0,0),self.pool_2.delete(0,10),self.pool_2.insert(0,0)

    def roll_fate(self):  # Define el dado usado en FATE, FUDGE y derivados
        a,c = int(self.pool.get()),int(self.mod.get())
        var = ('+','-','0')
        try:
            if 51 > a > 0:
                n = choices(var,weights=[2,2,2],k=a)  # Selecciona por peso de la lista tantas veces como k
                total = n.count('+')-n.count('-')+c  # Cuenta el resultado
                cut_1,cut_2,cut_3,cut_4 = n[:12],n[12:24],n[24:36],n[36:]  # Corta el resultado
                if not cut_4:
                    result.config(text=f'{cut_1}\n{cut_2}\n{cut_3}\n + mod: {c}\n= {total}',fg='green')
                    if not cut_3:
                        result.config(text=f'{cut_1}\n{cut_2}\n + mod: {c}\n= {total}',fg='green')
                        if not cut_2:
                            result.config(text=f'{cut_1}\n + mod: {c}\n= {total}',fg='green')
                else:
                    result.config(text=f'{cut_1}\n{cut_2}\n{cut_3}\n{cut_4}\n + mod: {c}\n= {total}',fg='green')
            else:
                result.config(text='Error:\nEnter a valid number\nNumber of dice = 1 - 50',fg='red')
        except ValueError:
            result.config(text='Error:\nEnter a number',fg='red'),self.mod.delete(0,10),self.mod.insert(0,0)

    def eggs(self):  # Primera parte del easter egg
        result.config(text='You found me',fg='red')
        self.btn_egg.config(command=self.spam)

    @staticmethod
    def spam():  # Segunda parte. Contiene las frases
        sus= ('From Spain, with love','Hi, Human','Fudging rolls is bad','Rule 0 rules!','OBEY!','Wanna kill all humans?','TPK!',
              'Rock falls, everybody dies','Do a Sanity check!','There is a dungeon in a dragon','Wait, I lost my dice...',
              'No meta allowed!','Stop minmaxing','I love U. Just kidding','Master of Puppets','I don\'t think so','Never again',
              'Nobody expects the Spanish Inquisition','I hate munchkins', 'Hasta la vista','Realistic is not Grimdark',
              'Katanas are Underpowered in d20','Iä! Iä! Cthulhu fhtagn!','Tucker\'s Kobolds!','Yes, Dark Lord','Unlucky',
              'Called shot to the groin','Add to the List','\"It\'s what my character would do\"\nis a bad excuse','Oh, No!',
              'Improved Initiative','Peace was never an option','A PC who is a Duck','Do a barrel roll','I regret nothing',
              'All Your Base Are Belong to Us','Pathfinder is the errata \nof the errata \nof DnD 3')
        n = choice(sus)
        result.config(text=n,fg='blue')

    @staticmethod
    def roll_rq():  # Define los rangos de cuerpo de BRP y derivados
        var= ('L. Leg','R. Leg','Abdomen','R. Arm','L. Arm','Chest','Head')
        n = choices(var,weights=[4,4,3,3,3,1,2], k=1)
        result.config(text=f'{n}',fg='green')

    @staticmethod
    def roll_myth():  # Define los rangos de cuerpo de BRP y derivados
        var= ('L. Leg','R. Leg','Abdomen','R. Arm','L. Arm','Chest','Head')
        n = choices(var,weights=[3,3,3,3,3,3,2], k=1)
        result.config(text=f'{n}',fg='green')

    @staticmethod
    def limpiar(): result.config(text='')  # Limpia los resultados


class Lienzo(tk.Canvas):  # Gestiona el lienzo donde se muestra el resultado
    def __init__(self,container):
        super().__init__(container)
        options = {'side':'bottom','expand':'YES','fill':'both'}
        self.config(bg='white',highlightthickness=5,highlightbackground="grey"),self.pack(**options)


class Tutorials:  # Almacena todos los tutoriales
    @staticmethod
    def tutorial():  # Instrucciones de uso general
        tu = tk.Toplevel(raiz)
        tu.resizable(0,0),tu.title('General Guide')
        tu_label = tk.Label(tu,text='\nFill the text fields with the numbers you want.\n\n\"Number of dice\" indicates how many '
                                    'dice you want to roll.\n\"Type of dice\" indicates how many sides have your dice.\n\"Mod '
                                    'value\" can add or subtract the number to the result.\nFATE use a custom Dice, you can '
                                    'change te amount of it.\nRQ Hit Location use a custom die and roll only one.'
                                    '\nIn Genesys Dice they have custom names.\n',justify='left',font=('Arial',10),bg='white')
        tu_label.pack()

    @staticmethod
    def tut_roll():  # Instrucciones de botón roll
        tu_ro = tk.Toplevel(raiz)
        tu_ro.resizable(0,0),tu_ro.title('Roll Guide')
        tu_ro_label = tk.Label(tu_ro,text='\nFill \"Number of dice\", \"Type of dice\" and \"Mod value\" text fields with the '
                                          'numbers you want.\n\nYou can roll two types of dice with his owns mod values, but '
                                          'first column must be filled.\nCombined values can not be more of 100 for Number of '
                                          'dice.\n1st die must be at least 2 and second die can be 0 but not 1.'
                                          '\n',justify='left',font=('Arial',10),bg='white')
        tu_ro_label.pack()

    @staticmethod
    def tut_fate():  # Instrucciones de botón fate
        tu_fa = tk.Toplevel(raiz)
        tu_fa.resizable(0,0),tu_fa.title('FATE Guide')
        tu_fa_label = tk.Label(tu_fa,text='\nNeeds fill \"Number of dice\" and \"Mod value\".\n',
                               justify='left',font=('Arial',10),bg='white')
        tu_fa_label.pack()

    @staticmethod
    def tut_rq():  # Instrucciones de botón RQ
        tu_rq = tk.Toplevel(raiz)
        tu_rq.resizable(0,0),tu_rq.title('RQ Hit Location Guide')
        tu_rq_label = tk.Label(tu_rq,text='\nNo input needed. Roll once.\nUse the RuneQuest/BRP humanoid hit location'
                                          ' table.\n',justify='left',font=('Arial',10),bg='white')
        tu_rq_label.pack()

    @staticmethod
    def tut_myth():  # Instrucciones de botón RQ
        tu_rq = tk.Toplevel(raiz)
        tu_rq.resizable(0,0),tu_rq.title('Mythras Hit Location Guide')
        tu_rq_label = tk.Label(tu_rq,text='\nNo input needed. Roll once.\nUse the Mythras humanoid hit location table.'
                                          '\n',justify='left',font=('Arial',10),bg='white')
        tu_rq_label.pack()

    @staticmethod
    def tut_genesys():  # Instrucciones de botón Genesys/SW
        tu_ge = tk.Toplevel(raiz)
        tu_ge.resizable(0,0),tu_ge.title('Genesys Guide')
        tu_ge_label = tk.Label(tu_ge,
                               text='\nNeeds fill the Genesys Dice and the Star Wars Force Die, can roll with at least one '
                                    'die of any type.\n',justify='left',font=('Arial',10),bg='white')
        tu_ge_label.pack()

    @staticmethod
    def mostrar():  # Instrucciones del menú para mostrar más tipos de dados
        tu_sge = tk.Toplevel(raiz)
        tu_sge.resizable(0,0),tu_sge.title('Show Genesys Guide')
        tu_sge_label = tk.Label(tu_sge,
                                text='\nShow the list for additional custom dice systems, and create the interface for them.\n',
                                justify='left',font=('Arial',10),bg='white')
        tu_sge_label.pack()


class Menus(tk.Menu):  # Gestiona la barra de menú
    def __init__(self):
        super().__init__()
        # menu archivo
        archivo_menu = tk.Menu(self,tearoff=0)
        archivo_menu.add_command(label='Exit',command=self.salir,font=('Arial',10))
        self.add_cascade(label='File',menu=archivo_menu,font=('Arial',10))
        # menu de tutoriales
        tutorial_menu = tk.Menu(self,tearoff=0)
        tutorial_menu.add_command(label='Guide',command=Tutorials.tutorial,font=('Arial',10))
        tutorial_menu.add_command(label='Roll',command=Tutorials.tut_roll,font=('Arial',10))
        tutorial_menu.add_command(label='FATE',command=Tutorials.tut_fate,font=('Arial',10))
        tutorial_menu.add_command(label='RuneQuest',command=Tutorials.tut_rq,font=('Arial',10))
        tutorial_menu.add_command(label='Mythras',command=Tutorials.tut_myth,font=('Arial',10))
        tutorial_menu.add_command(label='Show Menu',command=Tutorials.mostrar,font=('Arial',10))
        tutorial_menu.add_separator()
        tutorial_menu.add_command(label='Genesys/SW',command=Tutorials.tut_genesys,font=('Arial',10))
        self.add_cascade(label='User Guide',menu=tutorial_menu,font=('Arial',10))
        # menu de ayuda
        ayuda_menu = tk.Menu(self,tearoff=0)
        ayuda_menu.add_command(label='Version',command=self.version,font=('Arial',10))
        ayuda_menu.add_command(label='Changelog',command=self.cambios,font=('Arial',10))
        ayuda_menu.add_command(label='About...',command=self.info,font=('Arial',10))
        self.add_cascade(label='Help',menu=ayuda_menu,font=('Arial',10))
        # menu de dados adicionales
        dados_menu = tk.Menu(self,tearoff=0)
        dados_menu.add_command(label='Genesys',command=genesys_iface,font=('Arial',10))
        self.add_cascade(label='Show',menu=dados_menu,font=('Arial',10))
        # Cierre
        raiz.config(menu=self)

    @staticmethod
    def info(): mb.showinfo('Info RPG DR 2','Programmed in Python by Juan José Núñez.\n(https://www.python.org/)'
                                            '\n\nIcons made by Ana Canalejo.\n(https://www.deviantart.com/miyuminineko)')

    @staticmethod
    def version(): mb.showinfo('Version RPG DR 2','Version 2.3.1')

    @staticmethod
    def cambios(): startfile('CHANGELOG.txt')

    @staticmethod
    def salir():  # Menu de salida de la app
        valor = mb.askokcancel('Close','Are you sure?')
        if valor is True: raiz.destroy()


class Resultado(tk.Label):  # Gestiona la etiqueta de resultado
    def __init__(self,container):
        super().__init__(container)
        options = {'expand':'YES'}
        self.config(justify='center',text='',font=('Arial',15),fg='green',bg='white'),self.pack(**options)


if __name__=="__main__":  # Arranca toda la interfaz
    raiz = Raiz()
    menu,cuadro,canvas = Menus(),Interfaz(raiz),Lienzo(raiz)
    result = Resultado(canvas)
    raiz.mainloop()
