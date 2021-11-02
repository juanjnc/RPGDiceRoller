from random import choices,randint  # Solo los módulos utilizados

# Implementa la lógica de las tiradas de cualquier dado de n caras, soporta dos dados diferentes
def crear_roll(result,cuadro):
    def roll():
        try:
            a,b,c=int(cuadro.pool.get()),int(cuadro.dado.get()),int(cuadro.mod.get())
            d,e,f=int(cuadro.pool_2.get()),int(cuadro.dado_2.get()),int(cuadro.mod_2.get())
            die_1,die_2=[],[]
            if (101>b>1) and (101>e>=0) and (101>a+d>0) and (a != 0) and (e != 1):
                for i in range(a): n=randint(1,b); die_1.append(n)  # Lanza y agrupa dado 1
                for j in range(d): m=randint(1,e); die_2.append(m)  # Lanza y agrupa dado 2
                suma=sum(die_1+die_2)  # Suma las dos tiradas
                if not die_2:  # Si no hay dado 2
                    result.config(text=f'{die_1}\n= {suma} + mod: {c+f}\n= {suma+c+f}',foreground='green')
                else:
                    result.config(text=f'{die_1}\n{die_2}\n= {suma} + mod: {c+f}\n= {suma+c+f}',foreground='green')
            else:  # Recoge cualquier numero erróneo
                result.config(text='Error:\nEnter a valid number\nDice = 2 - 100\nNumber of dice = 1 - 100',foreground='red')
        except ValueError:  # Recoge errores y limpia las casillas
            result.config(text='Error:\nEnter a number',foreground='red')
            cuadro.mod.delete(0,10),cuadro.mod.insert(0,0),cuadro.mod_2.delete(0,10),cuadro.mod_2.insert(0,0)
            cuadro.dado_2.delete(0,10),cuadro.dado_2.insert(0,0),cuadro.pool_2.delete(0,10),cuadro.pool_2.insert(0,0)
    return roll

# Implementa la lógica de las tiradas de los dados Fate y FUDGE
def crear_roll_fate(result,cuadro):
    def roll_fate():
        a,c=int(cuadro.pool.get()),int(cuadro.mod.get())
        var=('+','-','0')
        try:
            if 51>a>0:
                n=choices(var,weights=[2,2,2],k=a)  # Selecciona por peso de la lista tantas veces como k
                total=n.count('+')-n.count('-')+c  # Cuenta el resultado
                cut_1,cut_2,cut_3,cut_4=n[:12],n[12:24],n[24:36],n[36:]  # Corta el resultado
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
            result.config(text='Error:\nEnter a number',foreground='red'),cuadro.mod.delete(0,10),cuadro.mod.insert(0,0)
    return roll_fate

# Define los rangos de cuerpo de BRP y derivados
def crear_roll_rq(result):
    def roll_rq():  # Define los rangos de cuerpo de BRP y derivados
        var= ('L. Leg','R. Leg','Abdomen','R. Arm','L. Arm','Chest','Head')
        n = choices(var,weights=[4,4,3,3,3,1,2], k=1)
        result.config(text=f'{n}',foreground='green')
    return roll_rq

# Define los rangos de cuerpo de BRP y derivados
def crear_roll_myth(result):
    def roll_myth():
        var= ('L. Leg','R. Leg','Abdomen','R. Arm','L. Arm','Chest','Head')
        n = choices(var,weights=[3,3,3,3,3,3,2], k=1)
        result.config(text=f'{n}',foreground='green')
    return roll_myth

# Limpia los resultados
def crear_limpiar(result):
    def limpiar(): result.config(text='')
    return limpiar
