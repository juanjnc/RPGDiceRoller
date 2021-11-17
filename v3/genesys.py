from tkinter.ttk import Label, Entry, Button, Style
from tiradaGenesys import crear_roll_g

class Genesys:
    # Genera toda la interfaz de los dados Genesys
    def __init__(self,result,raiz,iface):
        # Ajusta el tamaño de la ventana
        raiz.geometry('800x400')
        # Crean los textos de los dados
        Style().configure('G.TButton',font=('Arial',11),foreground='green',width=12)
        Style().configure('G.TLabel',font=('Arial',12))
        Style().configure('G.TEntry',font=('Arial',12))

        self.bst_label = Label(iface,justify='right',text='Boost Dice: ',style='G.TLabel')
        self.bst_label.grid(row=0,column=5,padx=5,pady=5,sticky='E')
        self.abi_label = Label(iface,justify='right',text='Ability Dice: ',style='G.TLabel')
        self.abi_label.grid(row=1,column=5,padx=5,pady=5,sticky='E')
        self.prof_label = Label(iface,justify='right',text='Proficiency Dice: ',style='G.TLabel')
        self.prof_label.grid(row=2,column=5,padx=5,pady=5,sticky='E')
        self.sback_label = Label(iface,justify='right',text='Setback Dice: ',style='G.TLabel')
        self.sback_label.grid(row=0,column=7,padx=5,pady=5,sticky='E')
        self.diff_label = Label(iface,justify='right',text='Difficulty Dice: ',style='G.TLabel')
        self.diff_label.grid(row=1,column=7,padx=5,pady=5,sticky='E')
        self.cha_label = Label(iface,justify='right',text='Challenge Dice: ',style='G.TLabel')
        self.cha_label.grid(row=2,column=7,padx=5,pady=5,sticky='E')
        self.frc_label = Label(iface,justify='right',text='Force Dice: ',style='G.TLabel')
        self.frc_label.grid(row=3,column=5,padx=5,pady=5,sticky='E')
        # Crean y configuran las entradas de los dados
        self.frc = Entry(iface,width=5)
        self.frc.grid(row=3,column=6,padx=5,pady=5),self.frc.config(justify='center',style='G.TEntry'),self.frc.insert(0,0)
        self.cha = Entry(iface,width=5)
        self.cha.grid(row=2,column=8,padx=5,pady=5),self.cha.config(justify='center',style='G.TEntry'),self.cha.insert(0,0)
        self.diff = Entry(iface,width=5)
        self.diff.grid(row=1,column=8,padx=5,pady=5),self.diff.config(justify='center',style='G.TEntry'),self.diff.insert(0,0)
        self.sback = Entry(iface,width=5)
        self.sback.grid(row=0,column=8,padx=5,pady=5),self.sback.config(justify='center',style='G.TEntry'),self.sback.insert(0,0)
        self.prof = Entry(iface,width=5)
        self.prof.grid(row=2,column=6,padx=5,pady=5),self.prof.config(justify='center',style='G.TEntry'),self.prof.insert(0,0)
        self.abi = Entry(iface,width=5)
        self.abi.grid(row=1,column=6,padx=5,pady=5),self.abi.config(justify='center',style='G.TEntry'),self.abi.insert(0,0)
        self.bst = Entry(iface,width=5)
        self.bst.grid(row=0,column=6,padx=5,pady=5),self.bst.config(justify='center',style='G.TEntry'),self.bst.insert(0,0)
        grids = dict(abi=self.abi,frc=self.frc,cha=self.cha,diff=self.diff,sback=self.sback,prof=self.prof,bst=self.bst)
        # Crea el botón para tirar los dados y eliminar la interfaz
        self.btn_g = Button(iface,text="Genesys/SW",command=crear_roll_g(result,**grids),style='G.TButton',cursor='hand2')
        self.btn_g.grid(row=3,column=7,columnspan=2,padx=5,pady=5)
     # Elimina toda la interfaz de Genesys
    def eliminar_g(self,result,raiz):
        result.config(text=''),self.bst.destroy(),self.abi.destroy(),self.prof.destroy(),self.sback.destroy(),self.diff.destroy()
        self.cha.destroy(),self.frc.destroy(),self.bst_label.destroy(),self.abi_label.destroy(),self.prof_label.destroy()
        self.sback_label.destroy(),self.diff_label.destroy(),self.cha_label.destroy(),self.frc_label.destroy()
        self.btn_g.destroy(),raiz.geometry('400x400')

