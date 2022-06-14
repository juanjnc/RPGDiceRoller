from tkinter import Menu, BooleanVar
import tutorials as tu
from genesys import Genesys
import menus_func as MeFu

# Objetos de los dados adicionales
gene = Genesys


# Gestiona la barra de menú
class Menus(Menu):
    # Interfaz del menu
    def __init__(self, container, result, iface, root):
        super().__init__(container)

        # menu archivo
        archivo_menu = Menu(self, tearoff=0)
        archivo_menu.add_command(label='Website', command=MeFu.website, font=('Arial', 10))
        archivo_menu.add_command(label='Download', command=MeFu.release, font=('Arial', 10))
        archivo_menu.add_command(label='Exit', command=MeFu.crear_salir(root), font=('Arial', 10))
        self.add_cascade(label='File', menu=archivo_menu, font=('Arial', 10))

        # menu de tutoriales
        tutorial_menu = Menu(self, tearoff=0)
        tutorial_menu.add_command(label='Guide', command=tu.create_tutorial(root), font=('Arial', 10))
        tutorial_menu.add_command(label='Roll', command=tu.create_tut_roll(root), font=('Arial', 10))
        tutorial_menu.add_command(label='FATE', command=tu.create_tut_fate(root), font=('Arial', 10))
        tutorial_menu.add_command(label='RuneQuest', command=tu.create_tut_rq(root), font=('Arial', 10))
        tutorial_menu.add_command(label='Mythras', command=tu.create_tut_myth(root), font=('Arial', 10))
        tutorial_menu.add_command(label='Show Menu', command=tu.create_show(root), font=('Arial', 10))
        tutorial_menu.add_separator()
        tutorial_menu.add_command(label='Genesys/SW', command=tu.create_tut_genesys(root), font=('Arial', 10))
        self.add_cascade(label='User Guide', menu=tutorial_menu, font=('Arial', 10))

        # menu de ayuda
        ayuda_menu = Menu(self, tearoff=0)
        ayuda_menu.add_command(label='Version', command=MeFu.version, font=('Arial', 10))
        ayuda_menu.add_command(label='Changelog', command=MeFu.cambios, font=('Arial', 10))
        ayuda_menu.add_command(label='License', command=MeFu.mitlicense, font=('Arial', 10))
        ayuda_menu.add_command(label='3rd Party Licenses', command=MeFu.licenses, font=('Arial', 10))
        ayuda_menu.add_command(label='About...', command=MeFu.info, font=('Arial', 10))
        self.add_cascade(label='Help', menu=ayuda_menu, font=('Arial', 10))

        # menu de dados adicionales
        dados_menu = Menu(self, tearoff=0)
        # Bloque de dados Genesys
        sys_gen = BooleanVar()

        def sys_gen_show():
            a = sys_gen.get()
            if a is True:
                return gene.__init__(self=gene, raiz=root, result=result, iface=iface)
            else:
                return gene.eliminar_g(self=gene, raiz=root, result=result)

        dados_menu.add_checkbutton(label='Genesys', font=('Arial', 10), onvalue=1, offvalue=0, variable=sys_gen,
                                   command=sys_gen_show)
        self.add_cascade(label='Show', menu=dados_menu, font=('Arial', 10))

        # Cierre
        container.config(menu=self)
