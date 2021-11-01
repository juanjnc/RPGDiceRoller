from tkinter import *
from tkinter.ttk import *
from random import choices,randint,choice  # Solo los módulos utilizados
from time import time,strftime
from datetime import timedelta


class Interfaz(Frame):  # Gestiona el marco de los botones
    def __init__(self,container,**kwargs):
        super().__init__(container)
        self.start=time()
        Style().configure('TButton',font=('Arial',11),foreground='green',width=6,justify='center')
        Style().configure('HL.TButton',font=('Arial',11),foreground='blue',width=7,justify='center')
        Style().configure('R.TButton',font=('Arial',13,'bold'),foreground='dark green',width=5,justify='center')
        Style().configure('C.TButton',font=('Arial',14,'italic'),foreground='red3',borderwidth=4,width=6,justify='center')
        Style().configure('NL.TLabel',font=('Arial',3),borderwidth=0,width=0,takefocus=False,justify='center')
        Style().configure('TLabel',font=('Arial',12),justify='center')
        Style().configure('TEntry',font=('Arial',12))
        self.config(height='100',width='850')
        # Primera cantidad de dados
        self.pool = Entry(self,width=5,justify='center')
        self.pool.grid(row=0,column=2,padx=5,pady=5),self.pool.config(style='TEntry'),self.pool.insert(0,1)
        # Primer dado
        self.dado = Entry(self,width=5,justify='center')
        self.dado.grid(row=1,column=2,padx=5,pady=5),self.dado.config(style='TEntry'),self.dado.insert(0,2)
        # primer modificador
        self.mod = Entry(self,width=5,justify='center')
        self.mod.grid(row=2,column=2,padx=5,pady=5),self.mod.config(style='TEntry'),self.mod.insert(0,0)
        # Segunda cantidad de dados
        self.pool_2 = Entry(self,width=5,justify='center')
        self.pool_2.grid(row=0,column=3,padx=5,pady=5),self.pool_2.config(style='TEntry'),self.pool_2.insert(0,0)
        # Segundo dado
        self.dado_2 = Entry(self,width=5,justify='center')
        self.dado_2.grid(row=1,column=3,padx=5,pady=5),self.dado_2.config(style='TEntry'),self.dado_2.insert(0,0)
        # Segundo modificador
        self.mod_2 = Entry(self,width=5,justify='center')
        self.mod_2.grid(row=2,column=3,padx=5,pady=5),self.mod_2.config(style='TEntry'),self.mod_2.insert(0,0)
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
        self.btn_roll = Button(self,text="Roll",command=self.crear_roll(**kwargs),style='R.TButton',cursor='hand2')
        self.btn_roll.grid(row=0,column=0,padx=5,pady=5)
        # Botón tirar FATE
        self.btn_fate = Button(self,text=" FATE ",command=self.crear_roll_fate(**kwargs),style='TButton',cursor='hand2')
        self.btn_fate.grid(row=1,column=0,padx=5,pady=5)
        # Etiqueta modificador
        self.mod_label = Label(self,justify='right',text="Hit Location: ",style='TLabel')
        self.mod_label.grid(row=3,column=1,sticky='E',padx=5,pady=5)
        # Botón tirar RQ
        self.btn_rq = Button(self,text="RQ",command=self.crear_roll_rq(**kwargs),style='HL.TButton',cursor='hand2')
        self.btn_rq.grid(row=3,column=3,padx=5,pady=5)
        # Botón tirar Mythras
        self.btn_myth = Button(self,text="Mythras",command=self.crear_roll_myth(**kwargs),style='HL.TButton',cursor='hand2')
        self.btn_myth.grid(row=3,column=2,padx=5,pady=5),self.pack()
        # Botón limpiar
        self.btn_clean = Button(self,text="Clear",command=self.crear_limpiar(**kwargs),style='C.TButton',cursor='hand2')
        self.btn_clean.grid(row=3,column=0,rowspan=3,padx=5,pady=5)
        # Botón Huevo de Pascua
        self.btn_egg = Button(self,text="     ",command=self.crear_eggs(**kwargs),style='NL.TLabel')
        self.btn_egg.grid(row=2,column=0, padx=5, pady=5)
        # Tiempo de juego
        self.use_time = Label(self,font=('Calibri',10),foreground='DarkOrchid4',relief='flat',justify='center')
        self.use_time.grid(row=4,column=1,padx=5,pady=5)
        # Tiempo local
        self.loc_time = Label(self,font=('Calibri',10),foreground='darkgoldenrod4',relief='flat',justify='center')
        self.loc_time.grid(row=4,column=2,padx=5,pady=5)

        # Fin del Cuadro de los botones e inputs

    def crear_roll(self,result):
        def roll():  # Define cualquier dado
            try:  # Las tiradas y las listas de ambos dados
                a,b,c = int(self.pool.get()),int(self.dado.get()),int(self.mod.get())
                d,e,f = int(self.pool_2.get()),int(self.dado_2.get()),int(self.mod_2.get())
                die_1,die_2 = [],[]
                if (101 > b > 1) and (101 > e >= 0) and (101 > a+d > 0) and (a!=0) and (e!=1):
                    for i in range(a): n = randint(1,b); die_1.append(n)  # Lanza y agrupa dado 1
                    for j in range(d): m = randint(1,e); die_2.append(m)  # Lanza y agrupa dado 2
                    suma = sum(die_1+die_2)  # Suma las dos tiradas
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
            return roll
        return roll

    def crear_roll_fate(self,result):
        def roll_fate():  # Define el dado usado en FATE, FUDGE y derivados
            a,c = int(self.pool.get()),int(self.mod.get())
            var = ('+','-','0')
            try:
                if 51 > a > 0:
                    n = choices(var,weights=[2,2,2],k=a)  # Selecciona por peso de la lista tantas veces como k
                    total = n.count('+')-n.count('-')+c  # Cuenta el resultado
                    cut_1,cut_2,cut_3,cut_4 = n[:12],n[12:24],n[24:36],n[36:]  # Corta el resultado
                    match len(n):
                        case 1|2|3|4|5|6|7|8|9|10|11|12:
                            result.config(text=f'{cut_1}\n + mod: {c}\n= {total}',foreground='green')
                        case 13|14|15|16|17|18|19|20|21|22|23|24:
                            result.config(text=f'{cut_1}\n{cut_2}\n + mod: {c}\n= {total}',foreground='green')
                        case 25|26|27|28|29|30|31|32|33|34|35|36:
                            result.config(text=f'{cut_1}\n{cut_2}\n{cut_3}\n + mod: {c}\n= {total}',foreground='green')
                        case _:
                            result.config(text=f'{cut_1}\n{cut_2}\n{cut_3}\n{cut_4}\n + mod: {c}\n= {total}',foreground='green')
                else:
                    result.config(text='Error:\nEnter a valid number\nNumber of dice = 1 - 50',foreground='red')
            except ValueError:
                result.config(text='Error:\nEnter a number',foreground='red'),self.mod.delete(0,10),self.mod.insert(0,0)
            return roll_fate
        return roll_fate

    def playtime(self):
        play_time = timedelta(seconds=int(time() - self.start))
        self.use_time.configure(text=f'Play Time:\n{play_time}')
        self.use_time.after(100,self.playtime)

    def localtime(self):
        local_time = strftime('%H: %M: %S')
        self.loc_time.configure(text=f'Clock:\n{local_time}')
        self.loc_time.after(100,self.localtime)

    def crear_eggs(self, result):
        def eggs():  # Primera parte del easter egg
            result.config(text='You found me',foreground='red')
            self.btn_egg.config(command=self.crear_spam(result))
        return eggs

    @staticmethod
    def crear_spam(result):
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
        return spam

    @staticmethod
    def crear_roll_rq(result):
        def roll_rq():  # Define los rangos de cuerpo de BRP y derivados
            var= ('L. Leg','R. Leg','Abdomen','R. Arm','L. Arm','Chest','Head')
            n = choices(var,weights=[4,4,3,3,3,1,2], k=1)
            result.config(text=f'{n}',foreground='green')
        return roll_rq

    @staticmethod
    def crear_roll_myth(result):
        def roll_myth():  # Define los rangos de cuerpo de BRP y derivados
            var= ('L. Leg','R. Leg','Abdomen','R. Arm','L. Arm','Chest','Head')
            n = choices(var,weights=[3,3,3,3,3,3,2], k=1)
            result.config(text=f'{n}',foreground='green')
        return roll_myth

    @staticmethod
    def crear_limpiar(result):  # Limpia los resultados
        def limpiar(): result.config(text='')
        return limpiar