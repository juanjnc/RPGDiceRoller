from tkinter import Menu, BooleanVar
import tutorials as tu
from genesys import genesys
import menusFunc as MeFu

# Gestiona la barra de menú
class Menus(Menu):
    # Interfaz del menu
    def __init__(self,container,result, cuadro, **kwargs):
        super().__init__(container)
        # menu archivo
        archivo_menu = Menu(self,tearoff=0)
        archivo_menu.add_command(label='Exit',command=MeFu.crear_salir(**kwargs),font=('Arial',10))
        self.add_cascade(label='File',menu=archivo_menu,font=('Arial',10))
        # menu de tutoriales
        tutorial_menu = Menu(self,tearoff=0)
        tutorial_menu.add_command(label='Guide',command=tu.crear_tutorial(**kwargs),font=('Arial',10))
        tutorial_menu.add_command(label='Roll',command=tu.crear_tut_roll(**kwargs),font=('Arial',10))
        tutorial_menu.add_command(label='FATE',command=tu.crear_tut_fate(**kwargs),font=('Arial',10))
        tutorial_menu.add_command(label='RuneQuest',command=tu.crear_tut_rq(**kwargs),font=('Arial',10))
        tutorial_menu.add_command(label='Mythras',command=tu.crear_tut_myth(**kwargs),font=('Arial',10))
        tutorial_menu.add_command(label='Show Menu',command=tu.crear_mostrar(**kwargs),font=('Arial',10))
        tutorial_menu.add_separator()
        tutorial_menu.add_command(label='Genesys/SW',command=tu.crear_tut_genesys(**kwargs),font=('Arial',10))
        self.add_cascade(label='User Guide',menu=tutorial_menu,font=('Arial',10))
        # menu de ayuda
        ayuda_menu = Menu(self,tearoff=0)
        ayuda_menu.add_command(label='Version',command=MeFu.version,font=('Arial',10))
        ayuda_menu.add_command(label='Changelog',command=MeFu.cambios,font=('Arial',10))
        ayuda_menu.add_command(label='About...',command=MeFu.info,font=('Arial',10))
        self.add_cascade(label='Help',menu=ayuda_menu,font=('Arial',10))
        # menu de dados adicionales
        dados_menu = Menu(self,tearoff=0)
        dados_menu.add_checkbutton(label='Genesys', font=('Arial',10),command=genesys(menu=self,**kwargs, result=result, cuadro=cuadro))
        self.add_cascade(label='Show',menu=dados_menu,font=('Arial',10))
        # Cierre
        container.config(menu=self)
