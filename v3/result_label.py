from tkinter.ttk import Label


# Gestiona la etiqueta donde se muestra el resultado
class Result_Label(Label):
    def __init__(self, container):
        super().__init__(container)
        options = {'expand': 'YES'}
        self.config(justify='center', text='', font=('Arial', 15), foreground='green', background='white')
        self.pack(**options)
