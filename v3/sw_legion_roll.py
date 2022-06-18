from random import choices  # Solo los módulos utilizados
from playsound import playsound


# Implementa la lógica de las tiradas de los dados del sistema Genesys
def create_roll_swlegion(result, rd, ra, ba, wa, wd):
    def roll_swlegion():
        try:
            a, b = int(wd.get()), int(rd.get())
            c, d, e = int(wa.get()), int(ba.get()), int(ra.get())
            var_white_defense = ('-', '-', '-', '-', 'B', 'DS')
            var_red_defense = ('-', '-', 'B', 'B', 'B', 'DS')
            var_wa = ('H', 'CH', 'AS', '-', '-', '-', '-', '-')
            var_ba = ('H', 'H', 'H', 'CH', 'AS', '-', '-', '-')
            var_ra = ('H', 'H', 'H', 'H', 'H', 'CH', 'AS', '-')
            fin = []
            if 20 >= a + b + c + d + e > 0:  # Lanza y agrupa los dados SW Legion
                n = choices(var_white_defense, k=a)
                fin.extend(n)
                n = choices(var_red_defense, k=b)
                fin.extend(n)
                n = choices(var_wa, k=c)
                fin.extend(n)
                n = choices(var_ba, k=d)
                fin.extend(n)
                n = choices(var_ra, k=e)
                fin.extend(n)
                block = fin.count('B')
                def_surge = fin.count('DS')
                hit = fin.count('H')
                critical_hit = fin.count('CH')
                atk_surge = fin.count('AS')

                cut_1, cut_2 = fin[:10], fin[10:20]
                match len(fin):
                    case 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10:
                        result.config(text=f'{cut_1}\n\nBlock = {block}; Defense Surge = {def_surge}'
                                           f'\n Hit = {hit}; Critical Hit = {critical_hit}: Attack Surge = {atk_surge}',
                                      foreground='green')
                    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20:
                        result.config(text=f'{cut_1}\n{cut_2}\n\nBlock = {block}; Defense Surge = {def_surge}'
                                           f'\n Hit = {hit}; Critical Hit = {critical_hit}: Attack Surge = {atk_surge}',
                                      foreground='green')
                playsound(r'data/dice_roll.wav')

            else:
                result.config(text='Error:\nEnter a valid number\nNumber of dice = 1 - 20', foreground='red')
                playsound(r'data/dice_error.wav')
        except ValueError:
            result.config(text='Error:\nEnter a number', foreground='red')
            playsound(r'data/value_error.wav')

    return roll_swlegion
