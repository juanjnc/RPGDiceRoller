from tkinter.ttk import Style, Label, Entry, Button, Frame
from time import time, strftime
from datetime import timedelta
import eggs
import main_rolls


# Gestiona el marco general de la app y de los botones
class Main_Interface(Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container)
        self.local_time = None
        self.play_time = None
        self.start = time()
        self.create_widgets(**kwargs)
        self.playtime()
        self.localtime()

        # Tiempo de Juego
    def playtime(self):
        self.play_time = timedelta(seconds=int(time() - self.start))
        self.use_time.configure(text=f'Play Time:\n{self.play_time}')
        self.use_time.after(90, self.playtime)

    # Reloj
    def localtime(self):
        self.local_time = strftime('%H: %M: %S')
        self.loc_time.configure(text=f'Clock:\n{self.local_time}')
        self.loc_time.after(90, self.localtime)

    def create_widgets(self, **kwargs):
        #  Estilo de la interfaz
        Style().configure('TButton', font=('Arial', 11), foreground='green', width=6, justify='center')
        Style().configure('HL1.TButton', font=('Arial', 11), foreground='blue', width=7, justify='center')
        Style().configure('HL2.TButton', font=('Arial', 11), foreground='blue', width=5, justify='center')
        Style().configure('R.TButton', font=('Arial', 13, 'bold'), foreground='dark green', width=5, justify='center')
        Style().configure('C.TButton', font=('Arial', 14, 'italic'), foreground='red3', borderwidth=4, width=6,
                          justify='center')
        Style().configure('NL.TLabel', font=('Arial', 3), borderwidth=0, width=0, takefocus=False, justify='center')
        Style().configure('TLabel', font=('Arial', 12), justify='center')
        Style().configure('TEntry', font=('Arial', 12))
        self.config(height='100', width='850')

        # Primera columna
        self.mod_label = Label(self, justify='left', text="1st     ",
                               style='TLabel')  # Los espacios hacen que visualmente esté centrado
        self.mod_label.grid(row=0, column=2, sticky='E', padx=5, pady=5)

        # Primera cantidad de dados
        self.pool = Entry(self, width=5, justify='center')
        self.pool.grid(row=1, column=2, padx=5, pady=5), self.pool.config(style='TEntry'), self.pool.insert(0, 1)

        # Primer dado
        self.dice_1 = Entry(self, width=5, justify='center')
        self.dice_1.grid(row=2, column=2, padx=5, pady=5), self.dice_1.config(style='TEntry'), self.dice_1.insert(0, 2)

        # primer modificador
        self.mod = Entry(self, width=5, justify='center')
        self.mod.grid(row=3, column=2, padx=5, pady=5), self.mod.config(style='TEntry'), self.mod.insert(0, 0)

        # Segunda columna
        self.mod_label = Label(self, justify='center', text=" 2nd ",
                               style='TLabel')  # Los espacios hacen que visualmente esté centrado
        self.mod_label.grid(row=0, column=3, sticky='E', padx=5, pady=5)

        # Segunda cantidad de dados
        self.pool_2 = Entry(self, width=5, justify='center')
        self.pool_2.grid(row=1, column=3, padx=5, pady=5), self.pool_2.config(style='TEntry'), self.pool_2.insert(0, 0)

        # Segundo dado
        self.dice_2 = Entry(self, width=5, justify='center')
        self.dice_2.grid(row=2, column=3, padx=5, pady=5), self.dice_2.config(style='TEntry'), self.dice_2.insert(0, 0)

        # Segundo modificador
        self.mod_2 = Entry(self, width=5, justify='center')
        self.mod_2.grid(row=3, column=3, padx=5, pady=5), self.mod_2.config(style='TEntry'), self.mod_2.insert(0, 0)

        # Tercera columna
        self.mod_label = Label(self, justify='center', text=" 3rd ",
                               style='TLabel')  # Los espacios hacen que visualmente esté centrado
        self.mod_label.grid(row=0, column=4, sticky='E', padx=5, pady=5)

        # Tercera cantidad de dados
        self.pool_3 = Entry(self, width=5, justify='center')
        self.pool_3.grid(row=1, column=4, padx=5, pady=5), self.pool_3.config(style='TEntry'), self.pool_3.insert(0, 0)

        # Tercer dado
        self.dice_3 = Entry(self, width=5, justify='center')
        self.dice_3.grid(row=2, column=4, padx=5, pady=5), self.dice_3.config(style='TEntry'), self.dice_3.insert(0, 0)

        # Tercer modificador
        self.mod_3 = Entry(self, width=5, justify='center')
        self.mod_3.grid(row=3, column=4, padx=5, pady=5), self.mod_3.config(style='TEntry'), self.mod_3.insert(0, 0)

        # Etiqueta ordinal del dado
        self.pool_label = Label(self, justify='right', text='Dice order: ', style='TLabel')
        self.pool_label.grid(row=0, column=1, sticky='E', padx=5, pady=5)

        # Etiqueta cantidad de dados
        self.pool_label = Label(self, justify='right', text='nº of Dice: ', style='TLabel')
        self.pool_label.grid(row=1, column=1, sticky='E', padx=5, pady=5)

        # Etiqueta valor de dados
        self.dice_label = Label(self, justify='right', text='Type of Dice: ', style='TLabel')
        self.dice_label.grid(row=2, column=1, sticky='E', padx=5, pady=5)

        # Etiqueta modificador
        self.mod_label = Label(self, justify='right', text="Mod Value: ", style='TLabel')
        self.mod_label.grid(row=3, column=1, sticky='E', padx=5, pady=5)

        # Botón tirar dados
        self.btn_roll = Button(self, text="Roll", command=main_rolls.create_roll(**kwargs, iface=self), style='R.TButton',
                               cursor='hand2')
        self.btn_roll.grid(row=0, column=0, padx=5, pady=5)

        # Botón tirar FATE
        self.btn_fate = Button(self, text=" FATE ", command=main_rolls.create_roll_fate(**kwargs, cuadro=self),
                               style='TButton',
                               cursor='hand2')
        self.btn_fate.grid(row=1, column=0, padx=5, pady=5)

        # Botón tirar RQ
        self.btn_rq = Button(self, text="RQ", command=main_rolls.create_roll_rq(**kwargs), style='HL2.TButton',
                             cursor='hand2')
        self.btn_rq.grid(row=4, column=2, padx=5, pady=5, columnspan=1)

        # Botón tirar Mythras
        self.btn_myth = Button(self, text="Mythras", command=main_rolls.create_roll_myth(**kwargs), style='HL1.TButton',
                               cursor='hand2')
        self.btn_myth.grid(row=4, column=3, padx=5, pady=5, columnspan=2)

        # Etiqueta Hit Location
        self.mod_label = Label(self, justify='right', text="Hit Location: ", style='TLabel')
        self.mod_label.grid(row=4, column=1, sticky='E', padx=5, pady=5, columnspan=1)

        # Botón limpiar
        self.btn_clean = Button(self, text="Clear", command=main_rolls.create_clean(**kwargs), style='C.TButton',
                                cursor='hand2')
        self.btn_clean.grid(row=3, column=0, rowspan=2, padx=5, pady=5)

        # Botón Huevo de Pascua
        self.btn_egg = Button(self, text="       ", command=eggs.create_eggs(**kwargs, iface=self), style='NL.TLabel')
        self.btn_egg.grid(row=2, column=0, padx=5, pady=5)

        # Tiempo de juego
        self.use_time = Label(self, font=('Calibri', 10), foreground='DarkOrchid4', relief='flat', justify='center')
        self.use_time.grid(row=5, column=1, padx=5, pady=5)

        # Tiempo local
        self.loc_time = Label(self, font=('Calibri', 10), foreground='darkgoldenrod4', relief='flat', justify='center')
        self.loc_time.grid(row=5, column=2, padx=5, pady=5)

        self.pack()
    # Fin del Cuadro de los botones e inputs
