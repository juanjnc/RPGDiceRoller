from random import choices, randint  # Solo los módulos utilizados
from playsound import playsound


# Implementa la lógica de las tiradas de cualquier dado de n caras, soporta tres dados diferentes
def create_roll(result, iface):
    def roll():
        try:
            a, b, c = int(iface.pool.get()), int(iface.dice_1.get()), int(iface.mod.get())
            d, e, f = int(iface.pool_2.get()), int(iface.dice_2.get()), int(iface.mod_2.get())
            g, h, i = int(iface.pool_3.get()), int(iface.dice_3.get()), int(iface.mod_3.get())
            die_1, die_2, die_3 = [], [], []
            if (101 > (b or e or h) > 1) and (101 > a + d + g > 0) and (a != 0) and ((e and h) != 1):
                for ii in range(a):  # Lanza y agrupa dado 1
                    n = randint(1, b)
                    die_1.append(n)
                for jj in range(d):  # Lanza y agrupa dado 2
                    m = randint(1, e)
                    die_2.append(m)
                for kk in range(g):  # Lanza y agrupa dado 3
                    w = randint(1, h)
                    die_3.append(w)
                suma = sum(die_1 + die_2 + die_3)  # Suma las tres tiradas
                if not die_3:  # Si no hay dado 3
                    result.config(text=f'{die_1}\n{die_2}\n= {suma} + mod: {c + f}\n= {suma + c + f}',
                                  foreground='green')
                if not die_2:  # Si no hay dado 2 pero si dado 3
                    result.config(text=f'{die_1}\n{die_3}\n= {suma} + mod: {c + i}\n= {suma + c + i}',
                                  foreground='green')
                    if not die_3:  # Si no hay dado 2 ni dado 3
                        result.config(text=f'{die_1}\n= {suma} + mod: {c}\n= {suma + c}', foreground='green')
                else:
                    result.config(text=f'{die_1}\n{die_2}\n{die_3}\n= {suma} + mod: {c + f + i}\n= {suma + c + f + i}',
                                  foreground='green')
                playsound(r'data/dice_roll.wav')
            else:  # Recoge cualquier numero erróneo
                result.config(text='Error:\nEnter a valid number\nDice = 2 - 100\nNumber of dice = 1 - 100',
                              foreground='red')
                playsound(r'data/dice_error.wav')
        except ValueError:  # Recoge errores y limpia las casillas
            result.config(text='Error:\nEnter a number', foreground='red')
            iface.mod.delete(0, 10), iface.mod.insert(0, 0), iface.mod_2.delete(0, 10), iface.mod_2.insert(0, 0)
            iface.dice_2.delete(0, 10), iface.dice_2.insert(0, 0), iface.pool_2.delete(0, 10), iface.pool_2.insert(0, 0)
            iface.mod_3.delete(0, 10), iface.mod_3.insert(0, 0), iface.dice_3.delete(0, 10), iface.dice_3.insert(0, 0)
            iface.pool_3.delete(0, 10), iface.pool_3.insert(0, 0)
            playsound(r'data/value_error.wav')

    return roll


# Implementa la lógica de las tiradas de los dados Fate y FUDGE
def create_roll_fate(result, cuadro):
    def roll_fate():
        try:
            a, c = int(cuadro.pool.get()), int(cuadro.mod.get())
            var = ('+', '-', '0')
            if 51 > a > 0:
                n = choices(var, weights=[2, 2, 2], k=a)  # Selecciona por peso de la lista tantas veces como k
                total = n.count('+') - n.count('-') + c  # Cuenta el resultado
                cut_1, cut_2, cut_3, cut_4 = n[:12], n[12:24], n[24:36], n[36:]  # Corta el resultado
                match len(n):
                    case 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12:
                        result.config(text=f'{cut_1}\n + mod: {c}\n= {total}', foreground='green')
                    case 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24:
                        result.config(text=f'{cut_1}\n{cut_2}\n + mod: {c}\n= {total}', foreground='green')
                    case 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 | 33 | 34 | 35 | 36:
                        result.config(text=f'{cut_1}\n{cut_2}\n{cut_3}\n + mod: {c}\n= {total}', foreground='green')
                    case _:
                        result.config(text=f'{cut_1}\n{cut_2}\n{cut_3}\n{cut_4}\n + mod: {c}\n= {total}',
                                      foreground='green')
                playsound(r'data/dice_roll.wav')
            else:
                result.config(text='Error:\nEnter a valid number\nNumber of dice = 1 - 50', foreground='red')
                playsound(r'data/dice_error.wav')
        except ValueError:
            result.config(text='Error:\nEnter a number', foreground='red')
            cuadro.mod.delete(0, 10), cuadro.mod.insert(0, 0)
            playsound(r'data/value_error.wav')

    return roll_fate


# Define los rangos de cuerpo de BRP y derivados
def create_roll_rq(result):
    def roll_rq():  # Define los rangos de cuerpo de BRP y derivados
        var = ('L. Leg', 'R. Leg', 'Abdomen', 'R. Arm', 'L. Arm', 'Chest', 'Head')
        n = choices(var, weights=[4, 4, 3, 3, 3, 1, 2], k=1)
        result.config(text=f'{n}', foreground='green')
        playsound(r'data/dice_roll.wav')

    return roll_rq


# Define los rangos de cuerpo de BRP y derivados
def create_roll_myth(result):
    def roll_myth():
        var = ('L. Leg', 'R. Leg', 'Abdomen', 'R. Arm', 'L. Arm', 'Chest', 'Head')
        n = choices(var, weights=[3, 3, 3, 3, 3, 3, 2], k=1)
        result.config(text=f'{n}', foreground='green')
        playsound(r'data/dice_roll.wav')

    return roll_myth


# Limpia los resultados
def create_clean(result):
    def clean(): result.config(text='')

    return clean
