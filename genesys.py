from tkinter.ttk import Label, Entry, Button, Style
from tiradaGenesys import crear_roll_g

# Gestiona to lo relacionado con el sistema Genesys
def genesys(menu,result,raiz, cuadro):
    # Genera toda la interfaz de los dados Genesys
    def iface():
        # Elimina toda la interfaz de Genesys
        def crear_eliminar_g():
            def eliminar_g():
                result.config(text=''),bst.destroy(),abi.destroy(),prof.destroy(),sback.destroy(),diff.destroy(),cha.destroy()
                frc.destroy(),bst_label.destroy(),abi_label.destroy(),prof_label.destroy(),sback_label.destroy(),diff_label.destroy()
                cha_label.destroy(),frc_label.destroy(),btn_g.destroy(),menu.delete('Delete Genesys'),raiz.geometry('400x400')
            return eliminar_g()

        # Ajusta el tamaño de la ventana
        raiz.geometry('800x400')
        # Crean los textos de los dados
        Style().configure('G.TButton',font=('Arial',11),foreground='green',width=12)
        Style().configure('G.TLabel',font=('Arial',12))
        Style().configure('G.TEntry',font=('Arial',12))

        bst_label = Label(cuadro,justify='right',text='Boost Dice: ',style='G.TLabel')
        bst_label.grid(row=0,column=4,padx=5,pady=5,sticky='E')
        abi_label = Label(cuadro,justify='right',text='Ability Dice: ',style='G.TLabel')
        abi_label.grid(row=1,column=4,padx=5,pady=5,sticky='E')
        prof_label = Label(cuadro,justify='right',text='Proficiency Dice: ',style='G.TLabel')
        prof_label.grid(row=2,column=4,padx=5,pady=5,sticky='E')
        sback_label = Label(cuadro,justify='right',text='Setback Dice: ',style='G.TLabel')
        sback_label.grid(row=0,column=6,padx=5,pady=5,sticky='E')
        diff_label = Label(cuadro,justify='right',text='Difficulty Dice: ',style='G.TLabel')
        diff_label.grid(row=1,column=6,padx=5,pady=5,sticky='E')
        cha_label = Label(cuadro,justify='right',text='Challenge Dice: ',style='G.TLabel')
        cha_label.grid(row=2,column=6,padx=5,pady=5,sticky='E')
        frc_label = Label(cuadro,justify='right',text='Force Dice: ',style='G.TLabel')
        frc_label.grid(row=3,column=4,padx=5,pady=5,sticky='E')
        # Crean y configuran las entradas de los dados
        frc = Entry(cuadro,width=5)
        frc.grid(row=3,column=5,padx=5,pady=5),frc.config(justify='center',style='G.TEntry'),frc.insert(0,0)
        cha = Entry(cuadro,width=5)
        cha.grid(row=2,column=7,padx=5,pady=5),cha.config(justify='center',style='G.TEntry'),cha.insert(0,0)
        diff = Entry(cuadro,width=5)
        diff.grid(row=1,column=7,padx=5,pady=5),diff.config(justify='center',style='G.TEntry'),diff.insert(0,0)
        sback = Entry(cuadro,width=5)
        sback.grid(row=0,column=7,padx=5,pady=5),sback.config(justify='center',style='G.TEntry'),sback.insert(0,0)
        prof = Entry(cuadro,width=5)
        prof.grid(row=2,column=5,padx=5,pady=5),prof.config(justify='center',style='G.TEntry'),prof.insert(0,0)
        abi = Entry(cuadro,width=5)
        abi.grid(row=1,column=5,padx=5,pady=5),abi.config(justify='center',style='G.TEntry'),abi.insert(0,0)
        bst = Entry(cuadro,width=5)
        bst.grid(row=0,column=5,padx=5,pady=5),bst.config(justify='center',style='G.TEntry'),bst.insert(0,0)
        grids = dict(abi=abi,frc=frc,cha=cha,diff=diff,sback=sback,prof=prof,bst=bst)
        # Crea el botón para tirar los dados y eliminar la interfaz
        btn_g = Button(cuadro,text="Genesys/SW",command=crear_roll_g(result,**grids),style='G.TButton',cursor='hand2')
        btn_g.grid(row=3,column=6,columnspan=2,padx=5,pady=5)
        menu.insert_command(5, label='Delete Genesys',command=crear_eliminar_g,font=('Arial',10))
    return iface
