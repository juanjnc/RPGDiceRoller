from random import choices  # Solo los módulos utilizados
from playsound import playsound


# Implementa la lógica de las tiradas de los dados del sistema Genesys
def create_roll_g(result, abi, frc, cha, diff, sback, prof, bst):
    def roll_g():
        try:
            a, b, c = int(bst.get()), int(abi.get()), int(prof.get())
            d, e, f = int(sback.get()), int(diff.get()), int(cha.get())
            g = int(frc.get())  # Dado de fuerza, muy situacional en el sistema
            var_bst = ('–', '–', 'S', 'SA', 'AA', 'A')
            var_abi = ('–', 'S', 'S', 'SS', 'A', 'A', 'SA', 'AA')
            var_prof = ('–', 'S', 'S', 'SS', 'SS', 'A', 'SA', 'SA', 'SA', 'AA', 'AA', 'Tr')
            var_sback = ('–', '–', 'F', 'F', 'T', 'T')
            var_diff = ('–', 'F', 'FF', 'T', 'T', 'T', 'TT', 'FT')
            var_cha = ('–', 'D', 'D', 'DD', 'DD', 'T', 'T', 'FT', 'FT', 'TT', 'TT', 'De')
            var_frc = ('D', 'D', 'D', 'D', 'D', 'D', 'DD', 'L', 'L', 'LL', 'LL', 'LL')
            fin = []
            if 50 >= a + b + c + d + e + f + g > 0:  # Lanza y agrupa los dados Genesys
                n = choices(var_bst, k=a)
                fin.extend(n)
                n = choices(var_abi, k=b)
                fin.extend(n)
                n = choices(var_prof, k=c)
                fin.extend(n)
                n = choices(var_sback, k=d)
                fin.extend(n)
                n = choices(var_diff, k=e)
                fin.extend(n)
                n = choices(var_cha, k=f)
                fin.extend(n)
                n = choices(var_frc, k=g)
                fin.extend(n)
                suc = fin.count('S') + 2 * fin.count('SS') + fin.count('SA')
                adv = fin.count('A') + 2 * fin.count('AA') + fin.count('SA')
                tri = fin.count('Tr')
                thr = fin.count('T') + 2 * fin.count('TT') + fin.count('FT')
                fail = fin.count('F') + 2 * fin.count('FF') + fin.count('FT')
                des = fin.count('De')
                fds = fin.count('D') + 2 * fin.count('DD')
                fls = fin.count('L') + 2 * fin.count('LL')
                cut_1, cut_2, cut_3, cut_4, = fin[:15], fin[15:30], fin[30:40], fin[40:]
                match len(fin):
                    case 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15:
                        result.config(text=f'{cut_1}\n\nSuccess = {suc}; Advantage = {adv}; Triumph = {tri}'
                                           f'\nFailure = {fail}; Threat = {thr}; Despair = {des}\nForce Dark'
                                           f' Side = {fds}; Force Light Side = {fls}',
                                      foreground='green')
                    case 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30:
                        result.config(text=f'{cut_1}\n{cut_2}\n\nSuccess = {suc}; Advantage = {adv}; Triumph = {tri}'
                                           f'\nFailure = {fail}; Threat = {thr}; Despair = {des}\nForce Dark'
                                           f' Side = {fds}; Force Light Side = {fls}',
                                      foreground='green')
                    case 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 | 41 | 42 | 43 | 44 | 45:
                        result.config(text=f'{cut_1}\n{cut_2}\n{cut_3}\n\nSuccess = {suc}; Advantage = {adv};'
                                           f' Triumph = {tri}\nFailure = {fail}; Threat = {thr}; Despair = {des}'
                                           f'\nForce Dark Side = {fds}; Force Light Side = {fls}',
                                      foreground='green')
                    case _:
                        result.config(text=f'{cut_1}\n{cut_2}\n{cut_3}\n{cut_4}\n\nsuccess = {suc}; advantage = {adv};'
                                           f' triumph = {tri}\nfailure = {fail}; threat = {thr}; despair = {des}'
                                           f'\nForce Dark Side = {fds}; Force Light Side = {fls}',
                                      foreground='green')

                playsound(r'data/dice_roll.wav')
            else:
                result.config(text='Error:\nEnter a valid number\nNumber of dice = 1 - 50', foreground='red')
                playsound(r'data/dice_error.wav')
        except ValueError:
            result.config(text='Error:\nEnter a number', foreground='red')
            playsound(r'data/value_error.wav')

    return roll_g
