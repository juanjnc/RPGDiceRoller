from random import choice
from playsound import playsound


# Primera parte del easter egg
def crear_eggs(iface, result):
    def eggs():
        playsound(r'data/secret.wav')
        result.config(text='You found me', foreground='red')
        iface.btn_egg.config(command=crear_spam(result, iface))

    return eggs


# Segunda parte. Contiene las frases
def crear_spam(result, iface):
    def spam():
        m = ('ADnD', 'Anima BF', 'B/X', 'Call of Cthulhu', 'DnD 3.X', 'DnD 4', 'DnD 5', 'FATE', 'Pathfinder 1e',
             'Pathfinder 2e', 'PbtA', 'Trail of Cthulhu', 'Warhammer 40k', 'Warhammer Age of Sigmar',
             'Warhammer Fantasy', 'World Of Darkness', 'Basic RolePlaying', 'RuneQuest', 'Mythras', 'Rolemaster',
             'Middle-Earth RolePlaying', 'Traveller')
        game = choice(m)
        # for i in m: print(i)
        sus = ('From Spain, with love', 'Hi, Human', 'Fudging rolls is bad', 'Rule 0 rules!', 'OBEY!',  'TPK!',
               'Wanna kill all humans?', 'Rock falls, everybody dies', 'Do a Sanity check!', 'I need to explain...',
               'There is a dungeon in a dragon', 'Wait, I lost my dice...', 'No meta allowed!', 'Stop minmaxing',
               'I love U.\nJust kidding', 'Master of Puppets', 'I don\'t think so', 'Never again',  'Hasta la vista',
               'Nobody expects the Spanish Inquisition', 'I hate munchkins', 'Realistic is not Grimdark', 'Buh!',
               'Katanas are Underpowered in d20', 'Iä! Iä! Cthulhu fhtagn!', 'Tucker\'s Kobolds!', 'Yes, Dark Lord',
               'Unlucky', 'Called shot to the groin', 'Add to the List', 'All Your Base Are Belong to Us', 'a',
               '\"It\'s what my character would do\"\nis a bad excuse', 'Oh, No!', 'Improved Initiative', 'Roll under',
               'Peace was never an option', 'A PC who is a Duck', 'Do a barrel roll', 'I regret nothing', 'Roll over',
               'Pathfinder 1e is the errata\nof the errata\nof DnD 3', 'Please, don\'t play FATAL', 'Recursion?',
               'Pathfinder\nAKA\nMathfinder', 'BLOOD FOR THE BLOOD GOD!\nCRITS FOR THE CRIT GOD!', 'Hard to decide...',
               'You can\'t seduce the dragon, the elf\nor the bartender\'s daughter', 'Keep Calm\n&\nRoll',
               'The best Edition is your favorite Edition', '4chan doesn\'t cause Sanity loss', 'Not in my Town',
               'What\'s Hastur DC against\na stadium full of C4?', 'I have bad news for you...', 'Please, stop',
               'Don\'t impose your favorite game', 'Optimizing your PC is OK\nRuining the fun is not OK',
               'There\'s no check against STR\nfor bending the rules', 'It\'s a secret to everybody', 'Just Fireball',
               'I survived to the character creation\nin Traveller', 'It\'s dangerous to go alone\nTake this!',
               f'FIGHT ME:\nI don\'t like {game}', 'Linear Warriors\nQuadratic Wizards', 'Act normally',
               f'I\'m ready for play\n{game}', 'You\'ve excessive homebrew in your game', 'NANANANANA\nBATMAN',
               '\U0001F3A4 Never gonna give you up \U0001F3B5\n\U0001F3B6 Never gonna let you down \U0001F399')
        # for i in sus:print(i)
        phrase = choice(sus)
        result.config(text=phrase, foreground='blue')
        match phrase:
            case 'Recursion?':
                iface.btn_egg.config(command=crear_eggs(result=result, iface=iface))
            case _:
                pass

    return spam
