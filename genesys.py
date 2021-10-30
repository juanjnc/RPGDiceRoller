from tkinter import *
from tkinter.ttk import *
from random import choices,randint,choice  # Solo los módulos utilizados


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
                match len(fin):
                    case 1|2|3|4|5:
                        result.config(text=f'{cut_1}\nsuccess = {suc}; advantage = {adv}; triumph = {tri}'
                                           f'\nfailure = {fail}; threat = {thr}; despair = {des}\nForce Dark'
                                           f' Side = {fds}; Force Light Side = {fls}',foreground='green')
                    case 6|7|8|9|10:
                        result.config(text=f'{cut_1}\n{cut_2}\nsuccess = {suc}; advantage = {adv}'
                                           f'; triumph = {tri}\nfailure = {fail}; threat = {thr}; despair = {des}'
                                           f'\nForce Dark Side = {fds}; Force Light Side = {fls}',foreground='green')
                    case 11|12|13|14|15|16|17|18|19|20:
                        result.config(text=f'{cut_1}\n{cut_2}\n{cut_3}\nsuccess = {suc}; advantage = {adv}'
                                           f'; triumph = {tri}\nfailure = {fail}; threat = {thr}; despair = {des}'
                                           f'\nForce Dark Side = {fds}; Force Light Side = {fls}',foreground='green')
                    case 21|22|23|24|25|26|27|28|29|30:
                        result.config(text=f'{cut_1}\n{cut_2}\n{cut_3}\n{cut_4}\nsuccess = {suc}; advantage = {adv}'
                                           f'; triumph = {tri}\nfailure = {fail}; threat = {thr}; despair = {des}'
                                           f'\nForce Dark Side = {fds}; Force Light Side = {fls}',foreground='green')
                    case _:
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
    # Crea el botón para tirar los dados y eliminar la interfaz
    btn_g = Button(cuadro,text="Genesys/SW",command=roll_g,style='G.TButton',cursor='hand2')
    btn_g.grid(row=3,column=6,columnspan=2,padx=5,pady=5)
    menu.insert_command(5, label='Delete Genesys',command=eliminar_g,font=('Arial',10))
