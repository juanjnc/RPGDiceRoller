from random import choices  # Solo los módulos utilizados
from playsound import playsound


# Implementa la lógica de las tiradas de los dados del sistema Genesys
def crear_roll_g(result, abi, frc, cha, diff, sback, prof, bst):
    def roll_g():
        try:
            a, b, c = int(bst.get()), int(abi.get()), int(prof.get())
            d, e, f = int(sback.get()), int(diff.get()), int(cha.get())
            g = int(frc.get())  # Dado de fuerza, muy situacional en el sistema
            var_bst = ('0', 'success', 'advantage', 'advantage, advantage', 'advantage, success')
            var_abi = ('success', 'success, success', '0', 'advantage', 'advantage, success', 'advantage, advantage')
            var_prof = ('0', 'triumph', 'success', 'advantage', 'success, success', 'advantage, advantage', 'advantage, success')
            var_sback = ('success', 'success, success', '0', 'advantage', 'advantage, success', 'advantage, advantage')
            var_diff = ('failure', 'failure, failure', '0', 'threat', 'threat, failure', 'threat, threat')
            var_cha = ('failure', 'failure, failure', '0', 'threat', 'threat, failure', 'threat, threat', 'despair')
            var_frc = ('DARK', 'LIGHT', 'DARK, DARK', 'LIGHT, LIGHT')
            fin = []
            if 50 >= a + b + c + d + e + f + g > 0:  # Lanza y agrupa los dados Genesys
                n = choices(var_bst, weights=[2, 1, 1, 1, 1], k=a)
                fin.extend(n)
                n = choices(var_abi, weights=[2, 1, 1, 2, 1, 1], k=b)
                fin.extend(n)
                n = choices(var_prof, weights=[1, 1, 2, 1, 2, 2, 3], k=c)
                fin.extend(n)
                n = choices(var_sback, weights=[2, 1, 1, 2, 1, 1], k=d)
                fin.extend(n)
                n = choices(var_diff, weights=[1, 2, 3, 3, 1, 1], k=e)
                fin.extend(n)
                n = choices(var_cha, weights=[2, 2, 1, 2, 2, 2, 1], k=f)
                fin.extend(n)
                n = choices(var_frc, weights=[6, 2, 1, 3], k=g)
                fin.extend(n)
                suc = fin.count('success') + 2 * fin.count('success, success') + fin.count('advantage, success')
                adv = fin.count('advantage') + 2 * fin.count('advantage, advantage') + fin.count('advantage, success')
                tri = fin.count('triumph')
                thr = fin.count('threat') + 2 * fin.count('threat, threat') + fin.count('threat, failure')
                fail = fin.count('failure') + 2 * fin.count('failure, failure') + fin.count('threat, failure')
                des = fin.count('despair')
                fds = fin.count('DARK') + 2 * fin.count('DARK, DARK')
                fls = fin.count('LIGHT') + 2 * fin.count('LIGHT, LIGHT')
                cut_1, cut_2, cut_3, cut_4, cut_5 = fin[:5], fin[5:10], fin[10:20], fin[20:30], fin[30:]
                match len(fin):
                    case 1 | 2 | 3 | 4 | 5:
                        result.config(text=f'{cut_1}\nsuccess = {suc}; advantage = {adv}; triumph = {tri}'
                                           f'\nfailure = {fail}; threat = {thr}; despair = {des}\nForce Dark'
                                           f' Side = {fds}; Force Light Side = {fls}',
                                      foreground='green')
                    case 6 | 7 | 8 | 9 | 10:
                        result.config(text=f'{cut_1}\n{cut_2}\nsuccess = {suc}; advantage = {adv}; triumph = {tri}'
                                           f'\nfailure = {fail}; threat = {thr}; despair = {des}\nForce Dark'
                                           f' Side = {fds}; Force Light Side = {fls}',
                                      foreground='green')
                    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20:
                        result.config(text=f'{cut_1}\n{cut_2}\n{cut_3}\nsuccess = {suc}; advantage = {adv};'
                                           f' triumph = {tri}\nfailure = {fail}; threat = {thr}; despair = {des}'
                                           f'\nForce Dark Side = {fds}; Force Light Side = {fls}',
                                      foreground='green')
                    case 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30:
                        result.config(text=f'{cut_1}\n{cut_2}\n{cut_3}\n{cut_4}\nsuccess = {suc}; advantage = {adv};'
                                           f' triumph = {tri}\nfailure = {fail}; threat = {thr}; despair = {des}'
                                           f'\nForce Dark Side = {fds}; Force Light Side = {fls}',
                                      foreground='green')
                    case _:
                        result.config(text=f'{cut_1}\n{cut_2}\n{cut_3}\n{cut_4}\n{cut_5}\nsuccess = {suc};'
                                           f' advantage = {adv}; triumph = {tri}\nfailure = {fail}; threat = {thr}'
                                           f'; despair = {des}\nForce Dark Side = {fds}; Force Light Side = {fls}',
                                      foreground='green')
                playsound(r'data/dice_roll.wav')
            else:
                result.config(text='Error:\nEnter a valid number\nNumber of dice = 1 - 50', foreground='red')
                playsound(r'data/dice_error.wav')
        except ValueError:
            result.config(text='Error:\nEnter a number', foreground='red')
            playsound(r'data/value_error.wav')

    return roll_g
