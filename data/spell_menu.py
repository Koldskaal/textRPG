from . import basic_menu, game_log, spells
from termcolor import colored

class CombatSpellMenu(basic_menu.BasicRotatingMenu):
    def __init__(self, player):
        super().__init__()

        self.title_box = 'Info'
        self.title_window = 'Spellbook'

        self.player = player
        self.menu_options = player.spells

    def description_box(self, empty=False, stats=False):
        if empty:
            description_box = "Nothing here!"

            self.canvas.popup("room", description_box, 10, self.title_box)
            self.canvas.print_canvas()
        else:
            description_box = self.menu_options[0].description
            stats = {
                'MP': colored(-self.menu_options[0].mana_usage, 'blue') if self.menu_options[0].mana_usage < self.player.mana else colored(-self.menu_options[0].mana_usage, 'red') ,
                'HP': colored("+"+ str(self.menu_options[0].heal), 'green') if self.menu_options[0].heal > 0 else colored(self.menu_options[0].heal,'red'),
                'DMG': colored(str(self.menu_options[0].damage), 'red') if self.menu_options[0].damage > 0 else colored(self.menu_options[0].damage, 'green'),
                'DUR': self.menu_options[0].duration
                }
            self.canvas.popup("room", description_box, 10, self.title_box, stats=stats)
            self.canvas.print_canvas()

    def define_print_content(self):
        if self.menu_options:
            return [spell.name for spell in self.menu_options]
        return

    def choose(self):
        if self.menu_options[0].mana_usage > self.player.mana:
            game_log.log.add_to_log(f"Not enough mana for {self.menu_options[0].name}.", 'Combat', 'useful')
            return
        return self.menu_options[0], None

    def choose_special(self):
        if self.menu_options[0].special_action:
            return self.menu_options[0], True

    def exit(self):
        return 'skip', None

class BuySpellMenu(basic_menu.BasicRotatingMenu):
    def __init__(self, player, exit_room):
        super().__init__()

        self.title_box = 'Info'
        self.title_window = 'buy-spells'

        self.player = player
        self.menu_options = [spell(self.player) for spell in spells.spell_list]

        self.exit_room = exit_room

    def define_print_content(self):
        return [spell.name for spell in self.menu_options]

    def define_descriptions(self, item):
        description_box = f"{item.description}"
        stats = {'Available points':self.player.points, 'Spell cost': item.points}
        return description_box, stats

    def choose(self):
        if self.player.points >= self.menu_options[0].points:
            self.player.points -= self.menu_options[0].points
            self.player.spells.append(self.menu_options[0])
            self.print_room()

        else:
            return

    def exit(self):
        return self.exit_room
