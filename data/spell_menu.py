from . import basic_menu
from termcolor import colored

class CombatSpellMenu(basic_menu.BasicMenu):
    def __init__(self, player):
        super().__init__()

        self.title = 'Info'

        self.player = player
        self.menu_options = player.spells

    def print_room(self, clear=False):

        settings = {
            'column_priority'  : 2,     # Order of who goes first from left to right
            'delay'             : 3,     # if it needs to be x lines below
            'width'             : 41,    # how wide will it print
            'allignment'        : '^',
            'max_lines'         : 15,    # for the string that keeps getting bigger. Take only the latest 30
            'join_char'         : '',
            'title'             : 'SHOP-BUY',
            'push'              : 0
        }
        if len(self.menu_options) == 0:
            self.canvas.add_to_print("room", "", settings)
            self.canvas.print_canvas(clear)
            self.description_box(True)
        else:
            max = len(self.menu_options)
            if max > 9: max = 9
            aft_num = max // 2
            bef_num = max - aft_num


            before = "\n".join(spell.name for spell in self.menu_options[-aft_num:]) + '\n'
            temp = list(spell.name for spell in self.menu_options[:bef_num])
            if len(self.menu_options) > 1:
                hover = colored(self.menu_options[0].name, "white", 'on_green') if  self.menu_options[0].mana_usage <= self.player.mana else colored( self.menu_options[0].name, "white", 'on_red')
                new = before + "\n".join(temp).replace(temp[0], hover, 1)
            else:
                new = ' \n' + colored(before, "white", 'on_green', attrs=['bold'])

            self.canvas.add_to_print("room",new ,settings)
            self.canvas.print_canvas(clear)
            self.description_box()

    def description_box(self, empty=False):
        if empty:
            description_box = "Nothing here!"

            self.canvas.popup("room", description_box, 10, self.title)
            self.canvas.print_canvas()
        else:
            description_box = self.menu_options[0].description
            stats = {
                'MP': -self.menu_options[0].mana_usage,
                'HP': colored("+"+ str(self.menu_options[0].heal), 'green') if self.menu_options[0].heal > 0 else colored(self.menu_options[0].heal,'red'),
                'DMG': colored("+"+ str(self.menu_options[0].damage), 'red') if self.menu_options[0].damage > 0 else colored(self.menu_options[0].damage, 'green'),
                'DUR': self.menu_options[0].duration
                }
            self.canvas.popup("room", description_box, 10, self.title, stats=stats)
            self.canvas.print_canvas()

    def choose(self):
        if self.menu_options[0].mana_usage > self.player.mana:
            return
        return self.menu_options[0]

    def exit(self):
        return 'skip'
