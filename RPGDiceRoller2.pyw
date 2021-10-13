from tkinter import *
from tkinter.ttk import *
from os import startfile  # De momento la única función usada
from random import choices,randint,choice  # Solo los módulos utilizados
from tkinter import messagebox as mb
from time import time,strftime
from datetime import timedelta




def genesys_iface():  # Genera toda la interfaz de los dados Genesys
    def eliminar_g():  # Elimina toda la interfaz de Genesys
        result.config(text=''),bst.destroy(),abi.destroy(),prof.destroy(),sback.destroy(),diff.destroy(),cha.destroy()
        frc.destroy(),bst_label.destroy(),abi_label.destroy(),prof_label.destroy(),sback_label.destroy(),diff_label.destroy()
        cha_label.destroy(),frc_label.destroy(),btn_g.destroy(),menu.delete('Delete Genesys'),raiz.geometry('400x400')

    def roll_g():  # Define los dados del sistema Genesys junto con el dado de fuerza de SW
        try:
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
                                       f'\nForce Dark Side = {fds}; Force Light Side = {fls}',foreground='green')
                    if not cut_4:
                        result.config(text=f'{cut_1}\n{cut_2}\n{cut_3}\nsuccess = {suc}; advantage = {adv}'
                                           f'; triumph = {tri}\nfailure = {fail}; threat = {thr}; despair = {des}'
                                           f'\nForce Dark Side = {fds}; Force Light Side = {fls}',foreground='green')
                        if not cut_3:
                            result.config(text=f'{cut_1}\n{cut_2}\nsuccess = {suc}; advantage = {adv}'
                                               f'; triumph = {tri}\nfailure = {fail}; threat = {thr}; despair = {des}'
                                               f'\nForce Dark Side = {fds}; Force Light Side = {fls}',foreground='green')
                            if not cut_2:
                                result.config(text=f'{cut_1}\nsuccess = {suc}; advantage = {adv}; triumph = {tri}'
                                                   f'\nfailure = {fail}; threat = {thr}; despair = {des}\nForce Dark'
                                                   f' Side = {fds}; Force Light Side = {fls}',foreground='green')
                else:
                    result.config(text=f'{cut_1}\n{cut_2}\n{cut_3}\n{cut_4}\n{cut_5}\nsuccess = {suc}; advantage = {adv};'
                                       f' triumph = {tri}\nfailure = {fail}; threat = {thr}; despair = {des}'
                                       f'\nForce Dark Side = {fds}; Force Light Side = {fls}',foreground='green')
            else:
                result.config(text='Error:\nEnter a valid number\nNumber of dice = 1 - 50',foreground='red')
        except ValueError:
            result.config(text='Error:\nEnter a number',foreground='red')

    # Ajusta el tamaño de la ventana
    raiz.geometry('800x400')
    # Crean los textos de los dados
    Style().configure('TButton',font=('Arial',11),foreground='green',width=12)
    Style().configure('TLabel',font=('Arial',12))
    Style().configure('TEntry',font=('Arial',12))

    bst_label = Label(cuadro,justify='right',text='Boost Dice: ',style='TLabel')
    bst_label.grid(row=0,column=4,padx=5,pady=5,sticky='E')
    abi_label = Label(cuadro,justify='right',text='Ability Dice: ',style='TLabel')
    abi_label.grid(row=1,column=4,padx=5,pady=5,sticky='E')
    prof_label = Label(cuadro,justify='right',text='Proficiency Dice: ',style='TLabel')
    prof_label.grid(row=2,column=4,padx=5,pady=5,sticky='E')
    sback_label = Label(cuadro,justify='right',text='Setback Dice: ',style='TLabel')
    sback_label.grid(row=0,column=6,padx=5,pady=5,sticky='E')
    diff_label = Label(cuadro,justify='right',text='Difficulty Dice: ',style='TLabel')
    diff_label.grid(row=1,column=6,padx=5,pady=5,sticky='E')
    cha_label = Label(cuadro,justify='right',text='Challenge Dice: ',style='TLabel')
    cha_label.grid(row=2,column=6,padx=5,pady=5,sticky='E')
    frc_label = Label(cuadro,justify='right',text='Force Dice: ',style='TLabel')
    frc_label.grid(row=3,column=4,padx=5,pady=5,sticky='E')
    # Crean y configuran las entradas de los dados
    frc = Entry(cuadro,width=5)
    frc.grid(row=3,column=5,padx=5,pady=5),frc.config(justify='center',style='TEntry'),frc.insert(0,0)
    cha = Entry(cuadro,width=5)
    cha.grid(row=2,column=7,padx=5,pady=5),cha.config(justify='center',style='TEntry'),cha.insert(0,0)
    diff = Entry(cuadro,width=5)
    diff.grid(row=1,column=7,padx=5,pady=5),diff.config(justify='center',style='TEntry'),diff.insert(0,0)
    sback = Entry(cuadro,width=5)
    sback.grid(row=0,column=7,padx=5,pady=5),sback.config(justify='center',style='TEntry'),sback.insert(0,0)
    prof = Entry(cuadro,width=5)
    prof.grid(row=2,column=5,padx=5,pady=5),prof.config(justify='center',style='TEntry'),prof.insert(0,0)
    abi = Entry(cuadro,width=5)
    abi.grid(row=1,column=5,padx=5,pady=5),abi.config(justify='center',style='TEntry'),abi.insert(0,0)
    bst = Entry(cuadro,width=5)
    bst.grid(row=0,column=5,padx=5,pady=5),bst.config(justify='center',style='TEntry'),bst.insert(0,0)
    # Crea el botón para tirar los dados y eliminar la interfaz
    btn_g = Button(cuadro,text="Genesys/SW",command=roll_g,style='TButton',cursor='hand2')
    btn_g.grid(row=3,column=6,columnspan=2,padx=5,pady=5)
    menu.insert_command(5, label='Delete Genesys',command=eliminar_g,font=('Arial',10))


class Raiz(Tk):  # Crea la ventana principal
    def __init__(self):
        super().__init__()
        self.title('RPG Dice Roller v2'),self.geometry('400x400'),self.iconbitmap('ico.ico')


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


class Menus(Menu):  # Gestiona la barra de menú
    def __init__(self):
        super().__init__()
        # menu archivo
        archivo_menu = Menu(self,tearoff=0)
        archivo_menu.add_command(label='Exit',command=self.salir,font=('Arial',10))
        self.add_cascade(label='File',menu=archivo_menu,font=('Arial',10))
        # menu de tutoriales
        tutorial_menu = Menu(self,tearoff=0)
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
        ayuda_menu = Menu(self,tearoff=0)
        ayuda_menu.add_command(label='Version',command=self.version,font=('Arial',10))
        ayuda_menu.add_command(label='Changelog',command=self.cambios,font=('Arial',10))
        ayuda_menu.add_command(label='About...',command=self.info,font=('Arial',10))
        self.add_cascade(label='Help',menu=ayuda_menu,font=('Arial',10))
        # menu de dados adicionales
        dados_menu = Menu(self,tearoff=0)
        dados_menu.add_command(label='Genesys',command=genesys_iface,font=('Arial',10))
        self.add_cascade(label='Show',menu=dados_menu,font=('Arial',10))
        # Cierre
        raiz.config(menu=self)

    @staticmethod
    def info(): mb.showinfo('Info RPG DR 2','Programmed in Python by Juan José Núñez.\n(https://www.python.org/)'
                                            '\n\nIcons made by Ana Canalejo.\n(https://www.deviantart.com/miyuminineko)')

    @staticmethod
    def version(): mb.showinfo('Version RPG DR 2','Version 2.4.0')

    @staticmethod
    def cambios(): startfile('CHANGELOG.txt')

    @staticmethod
    def salir():  # Menu de salida de la app
        valor = mb.askokcancel('Close','Are you sure?')
        if valor is True: raiz.destroy()


class Interfaz(Frame):  # Gestiona el marco de los botones
    def __init__(self,container):
        super().__init__(container)
        self.start=time()
        Style().configure('TButton',font=('Arial',11),foreground='green',width=5)
        Style().configure('HL.TButton',font=('Arial',11),foreground='blue',width=7)
        Style().configure('R.TButton',font=('Arial',12,'bold'),foreground='dark green',width=5)
        Style().configure('C.TButton',font=('Arial',13,'italic'),foreground='red3',borderwidth=4,width=5)
        Style().configure('NL.TLabel',font=('Arial',3),borderwidth=0,width=0,takefocus=False)
        Style().configure('TLabel',font=('Arial',12))
        Style().configure('TEntry',font=('Arial',12))
        self.config(height='100',width='850')
        # Primera cantidad de dados
        self.pool = Entry(self,width=5)
        self.pool.grid(row=0,column=2,padx=5,pady=5),self.pool.config(justify='center',style='TEntry'),self.pool.insert(0,1)
        # Primer dado
        self.dado = Entry(self,width=5)
        self.dado.grid(row=1,column=2,padx=5,pady=5),self.dado.config(justify='center',style='TEntry'),self.dado.insert(0,2)
        # primer modificador
        self.mod = Entry(self,width=5)
        self.mod.grid(row=2,column=2,padx=5,pady=5),self.mod.config(justify='center',style='TEntry'),self.mod.insert(0,0)
        # Segunda cantidad de dados
        self.pool_2 = Entry(self,width=5)
        self.pool_2.grid(row=0,column=3,padx=5,pady=5),self.pool_2.config(justify='center',style='TEntry'),self.pool_2.insert(0,0)
        # Segundo dado
        self.dado_2 = Entry(self,width=5)
        self.dado_2.grid(row=1,column=3,padx=5,pady=5),self.dado_2.config(justify='center',style='TEntry'),self.dado_2.insert(0,0)
        # Segundo modificador
        self.mod_2 = Entry(self,width=5)
        self.mod_2.grid(row=2,column=3,padx=5,pady=5),self.mod_2.config(justify='center',style='TEntry'),self.mod_2.insert(0,0)
        # Etiqueta cantidad de dados
        self.pool_label = Label(self,justify='right',text='nº of Dice: ',style='TLabel')
        self.pool_label.grid(row=0,column=1,sticky='E',padx=5,pady=5)
        # Etiqueta valor de dados
        self.dado_label = Label(self,justify='right',text='Type of Dice: ',style='TLabel')
        self.dado_label.grid(row=1,column=1,sticky='E',padx=5,pady=5)
        # Etiqueta modificador
        self.mod_label = Label(self,justify='right',text="Mod Value: ",style='TLabel')
        self.mod_label.grid(row=2,column=1,sticky='E',padx=5,pady=5)
        # Botón tirar dados
        self.btn_roll = Button(self,text="Roll",command=self.roll,style='R.TButton',cursor='hand2')
        self.btn_roll.grid(row=0,column=0,padx=5,pady=5)
        # Botón tirar FATE
        self.btn_fate = Button(self,text="FATE",command=self.roll_fate,style='TButton',cursor='hand2')
        self.btn_fate.grid(row=1,column=0,padx=5,pady=5)
        # Etiqueta modificador
        self.mod_label = Label(self,justify='right',text="Hit Location: ",style='TLabel')
        self.mod_label.grid(row=3,column=1,sticky='E',padx=5,pady=5)
        # Botón tirar RQ
        self.btn_rq = Button(self,text="RQ",command=self.roll_rq,style='HL.TButton',cursor='hand2')
        self.btn_rq.grid(row=3,column=3,padx=5,pady=5)
        # Botón tirar Mythras
        self.btn_myth = Button(self,text="Mythras",command=self.roll_myth,style='HL.TButton',cursor='hand2')
        self.btn_myth.grid(row=3,column=2,padx=5,pady=5),self.pack()
        # Botón limpiar
        self.btn_clean = Button(self,text="Clear",command=self.limpiar,style='C.TButton',cursor='hand2')
        self.btn_clean.grid(row=3,column=0,rowspan=3,padx=5,pady=5)
        # Botón Huevo de Pascua
        self.btn_egg = Button(self,text="     ",command=self.eggs,style='NL.TLabel')
        self.btn_egg.grid(row=2,column=0, padx=5, pady=5)
        # Tiempo de juego
        self.use_time = Label(self,font=('Calibri',10),foreground='DarkOrchid4',relief='flat')
        self.use_time.grid(row=4,column=1,padx=5,pady=5)
        # Tiempo local
        self.loc_time = Label(self,font=('Calibri',10),foreground='darkgoldenrod4',relief='flat')
        self.loc_time.grid(row=4,column=2,padx=5,pady=5)

        # Fin del Cuadro de los botones e inputs

    def roll(self):  # Define cualquier dado
        try:  # Las tiradas y las listas de ambos dados
            a,b,c = int(self.pool.get()),int(self.dado.get()),int(self.mod.get())
            d,e,f = int(self.pool_2.get()),int(self.dado_2.get()),int(self.mod_2.get())
            die_1,die_2 = [],[]
            if (101 > b > 1) and (101 > e >= 0) and (101 > a+d > 0) and (a!=0) and (e!=1):
                for i in range(a): n = randint(1,b); die_1.append(n)  # Lanza y agrupa dado 1
                for j in range(d): m = randint(1,e); die_2.append(m)  # Lanza y agrupa dado 2
                suma = sum(die_1+die_2)  # Suma las dos tiradas
                if c==0 and f==0:  # Si no hay modificadores
                    if not die_2:  # Si no hay dado 2
                        result.config(text=f'{die_1}\n= {suma}',foreground='green')
                    else:
                        result.config(text=f'{die_1}\n{die_2}\n= {suma}',foreground='green')
                else:  # Si hay modificadores
                    if not die_2:  # Si no hay dado 2
                        result.config(text=f'{die_1}\n= {suma} + mod: {c+f}\n= {suma+c+f}',foreground='green')
                    else:
                        result.config(text=f'{die_1}\n{die_2}\n= {suma} + mod: {c+f}\n= {suma+c+f}',foreground='green')
            else:  # Recoge cualquier numero erróneo
                result.config(text='Error:\nEnter a valid number\nDice = 2 - 100\nNumber of dice = 1 - 100',foreground='red')
        except ValueError:  # Recoge errores y limpia las casillas
            result.config(text='Error:\nEnter a number',foreground='red')
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
                    result.config(text=f'{cut_1}\n{cut_2}\n{cut_3}\n + mod: {c}\n= {total}',foreground='green')
                    if not cut_3:
                        result.config(text=f'{cut_1}\n{cut_2}\n + mod: {c}\n= {total}',foreground='green')
                        if not cut_2:
                            result.config(text=f'{cut_1}\n + mod: {c}\n= {total}',foreground='green')
                else:
                    result.config(text=f'{cut_1}\n{cut_2}\n{cut_3}\n{cut_4}\n + mod: {c}\n= {total}',foreground='green')
            else:
                result.config(text='Error:\nEnter a valid number\nNumber of dice = 1 - 50',foreground='red')
        except ValueError:
            result.config(text='Error:\nEnter a number',foreground='red'),self.mod.delete(0,10),self.mod.insert(0,0)

    def playtime(self):
        play_time = timedelta(seconds=int(time() - self.start))
        self.use_time.configure(text=f'Play Time:\n{play_time}')
        self.use_time.after(100,self.playtime)

    def localtime(self):
        local_time = strftime('%H: %M: %S')
        self.loc_time.configure(text=f'Clock:\n{local_time}')
        self.loc_time.after(100,self.localtime)

    def eggs(self):  # Primera parte del easter egg
        result.config(text='You found me',foreground='red')
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
              'All Your Base Are Belong to Us','Pathfinder is the errata \nof the errata \nof DnD 3', 'Roll under', 'Roll over',
              'Pathfinder \nAKA \nMathfinder')
        n = choice(sus)
        result.config(text=n,foreground='blue')

    @staticmethod
    def roll_rq():  # Define los rangos de cuerpo de BRP y derivados
        var= ('L. Leg','R. Leg','Abdomen','R. Arm','L. Arm','Chest','Head')
        n = choices(var,weights=[4,4,3,3,3,1,2], k=1)
        result.config(text=f'{n}',foreground='green')

    @staticmethod
    def roll_myth():  # Define los rangos de cuerpo de BRP y derivados
        var= ('L. Leg','R. Leg','Abdomen','R. Arm','L. Arm','Chest','Head')
        n = choices(var,weights=[3,3,3,3,3,3,2], k=1)
        result.config(text=f'{n}',foreground='green')

    @staticmethod
    def limpiar(): result.config(text='')  # Limpia los resultados


class Lienzo(Canvas):  # Gestiona el lienzo donde se muestra el resultado
    def __init__(self,container):
        super().__init__(container)
        options = {'side':'bottom','expand':'YES','fill':'both'}
        self.config(background='white',highlightthickness=5,highlightbackground="grey"),self.pack(**options)


class Resultado(Label):  # Gestiona la etiqueta de resultado
    def __init__(self,container):
        super().__init__(container)
        options = {'expand':'YES'}
        self.config(justify='center',text='',font=('Arial',15),foreground='green',background='white'),self.pack(**options)


if __name__=="__main__":  # Arranca toda la interfaz
    raiz = Raiz()
    menu,cuadro,canvas = Menus(),Interfaz(raiz),Lienzo(raiz)
    result = Resultado(canvas)
    cuadro.localtime()
    cuadro.playtime()
    raiz.mainloop()
