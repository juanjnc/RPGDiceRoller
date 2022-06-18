from tkinter.ttk import Label, Entry, Button, Style
from sw_legion_roll import create_roll_swlegion


class SWLegion:

    # Genera toda la interfaz de los dados SWLegion
    def __init__(self, result, root, iface):
        # Ajusta el tamaño de la ventana
        root.geometry('800x400')

        #  Estilo de la interfaz
        Style().configure('G.TButton', font=('Arial', 11), foreground='green', width=8)
        Style().configure('G.TLabel', font=('Arial', 12))
        Style().configure('G.TEntry', font=('Arial', 12))

        # Etiqueta superior
        self.title = Label(iface, text="Star Wars Legion Custom Dice Pool", style='G.TLabel', justify='center')
        self.title.grid(row=0, column=5, columnspan=4, padx=5, pady=5)

        # Crean la interfaz de los dados
        self.white_defense_label = Label(iface, justify='right', text='White Defense: ', style='G.TLabel')
        self.white_defense_label.grid(row=1, column=7, padx=5, pady=5, sticky='E')
        self.red_defense_label = Label(iface, justify='right', text='Red Defense: ', style='G.TLabel')
        self.red_defense_label.grid(row=2, column=7, padx=5, pady=5, sticky='E')
        self.white_attack_label = Label(iface, justify='right', text='White Attack: ', style='G.TLabel')
        self.white_attack_label.grid(row=3, column=5, padx=5, pady=5, sticky='E')
        self.black_attack_label = Label(iface, justify='right', text='Black Attack: ', style='G.TLabel')
        self.black_attack_label.grid(row=1, column=5, padx=5, pady=5, sticky='E')
        self.red_attack_label = Label(iface, justify='right', text='Red Attack: ', style='G.TLabel')
        self.red_attack_label.grid(row=2, column=5, padx=5, pady=5, sticky='E')

        # Crean y configuran las entradas de los dados

        self.red_attack = Entry(iface, width=5)
        self.red_attack.grid(row=2, column=6, padx=5, pady=5)
        self.red_attack.config(justify='center', style='G.TEntry'), self.red_attack.insert(0, '0')

        self.black_attack = Entry(iface, width=5)
        self.black_attack.grid(row=1, column=6, padx=5, pady=5)
        self.black_attack.config(justify='center', style='G.TEntry'), self.black_attack.insert(0, '0')

        self.white_attack = Entry(iface, width=5)
        self.white_attack.grid(row=3, column=6, padx=5, pady=5)
        self.white_attack.config(justify='center', style='G.TEntry'), self.white_attack.insert(0, '0')

        self.red_defense = Entry(iface, width=5)
        self.red_defense.grid(row=2, column=8, padx=5, pady=5)
        self.red_defense.config(justify='center', style='G.TEntry'), self.red_defense.insert(0, '0')

        self.white_defense = Entry(iface, width=5)
        self.white_defense.grid(row=1, column=8, padx=5, pady=5)
        self.white_defense.config(justify='center', style='G.TEntry'), self.white_defense.insert(0, '0')

        grids = dict(rd=self.red_defense, ra=self.red_attack, ba=self.black_attack, wa=self.white_attack, wd=self.white_defense)

        # Crea el botón para tirar los dados y eliminar la interfaz
        self.btn_swl = Button(iface, text="Roll Pool", command=create_roll_swlegion(result, **grids), style='G.TButton',
                              cursor='hand2')
        self.btn_swl.grid(row=3, column=7, columnspan=1, padx=5, pady=5)

    # Elimina toda la interfaz de Genesys
    def eliminar_swl(self, result, root):
        result.config(text=''), self.white_defense.destroy(), self.red_defense.destroy(), self.white_attack.destroy(),
        self.black_attack.destroy(), self.red_attack.destroy(), self.white_defense_label.destroy(),
        self.red_defense_label.destroy(), self.white_attack_label.destroy(), self.black_attack_label.destroy(),
        self.red_attack_label.destroy(), self.btn_swl.destroy(), self.title.destroy(), root.geometry('400x400')
