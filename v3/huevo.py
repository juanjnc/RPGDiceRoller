from random import choice
from playsound import playsound


# Primera parte del easter egg
def crear_eggs(iface,result):
    def eggs():
        playsound(r'data/secret.wav')
        result.config(text='You found me',foreground='red')
        iface.btn_egg.config(command=crear_spam(result,iface))
    return eggs

# Segunda parte. Contiene las frases
def crear_spam(result,iface):
    def spam():
        m=('ADnD', 'Anima BF', 'B/X', 'Call of Cthulhu', 'DnD 3.X', 'DnD 4', 'DnD 5', 'FATE', 'Pathfinder 1e', 'Pathfinder 2e',
           'PbtA', 'Trail of Cthulhu', 'Warhammer 40k','Warhammer Age of Sigmar', 'Warhammer Fantasy', 'World Of Darkness',
           'Basic RolePlaying', 'RuneQuest', 'Mythras','Rolemaster','Middle-Earth RolePlaying','Traveller')
        game=choice(m)
        #for i in m: print(i)
        sus=('From Spain, with love','Hi, Human','Fudging rolls is bad','Rule 0 rules!','OBEY!','Wanna kill all humans?','TPK!',
             'Rock falls, everybody dies','Do a Sanity check!','There is a dungeon in a dragon','Wait, I lost my dice...',
             'No meta allowed!','Stop minmaxing','I love U.\nJust kidding','Master of Puppets','I don\'t think so','Never again',
             'Nobody expects the Spanish Inquisition','I hate munchkins','Hasta la vista','Realistic is not Grimdark','Buh!',
             'Katanas are Underpowered in d20','Iä! Iä! Cthulhu fhtagn!','Tucker\'s Kobolds!','Yes, Dark Lord','Unlucky',
             'Called shot to the groin','Add to the List','\"It\'s what my character would do\"\nis a bad excuse','Oh, No!',
             'Improved Initiative','Peace was never an option','A PC who is a Duck','Do a barrel roll','I regret nothing',
             'All Your Base Are Belong to Us','Pathfinder 1e is the errata\nof the errata\nof DnD 3','Roll under','Roll over',
             'Pathfinder\nAKA\nMathfinder','BLOOD FOR THE BLOOD GOD!\nCRITS FOR THE CRIT GOD!', 'Please, don\'t play FATAL',
             'You can\'t seduce the dragon, the elf\nor the bartender\'s daughter','The best Edition is your favorite Edition',
             '4chan doesn\'t cause Sanity loss','What\'s Hastur DC against\na stadium full of C4?','I have bad news for you...',
             'Don\'t impose your favorite game', 'Optimizing your PC is OK\nRuining the fun is not OK','Keep Calm\n&\nRoll',
             'There\'s no check against STR\nfor bending the rules', 'I survived to the character creation\nin Traveller','a',
             f'FIGHT ME:\nI don\'t like {game}','Linear Warriors\nQuadratic Wizards','Act normally','I need to explain...',
             f'I\'m ready for play\n{game}','Recursion?','It\'s a secret to everybody','It\'s dangerous to go alone\nTake this!',
             '\U0001F3A4 Never gonna give you up \U0001F3B5\n\U0001F3B6 Never gonna let you down \U0001F399','Hard to decide...',
             'NANANANANA\nBATMAN','Not in my Town','Please, stop','You\'ve excessive homebrew in your game','Just Fireball')
        #for i in sus:print(i)
        phrase=choice(sus)
        result.config(text=phrase,foreground='blue')
        match phrase:
            case 'Recursion?': iface.btn_egg.config(command=crear_eggs(result=result,iface=iface))
            case _: pass
    return spam
