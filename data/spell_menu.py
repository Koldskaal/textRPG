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
                'MP': colored(-self.menu_options[0].mana_usage, 'blue') if self.menu_options[0].mana_usage < self.player.mana else colored(-self.menu_options[0].mana_usage, 'white', 'on_red') ,
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
    def __init__(self, player, exit_room, filter=None):
        super().__init__()

        self.title_box = 'Info'
        self.settings['title'] = 'Spell-shop'.upper()

        self.player = player
        local_spells = [spell(self.player) for spell in spells.spell_list]
        if filter:
            local_spells = [spell for spell in local_spells if filter in spell.types]

        self.menu_options = local_spells

        self.exit_room = exit_room

    def define_print_content(self):
        return [spell.name for spell in self.menu_options]

    def define_descriptions(self, item):
        description_box = f"{item.description}"
        text = item.points if self.menu_options[0].name not in [spell.name for spell in self.player.spells] else 'BOUGHT'
        stats = {' Cost': text}
        return description_box, stats

    def choose(self):
        if self.player.points >= self.menu_options[0].points and self.menu_options[0].name not in [spell.name for spell in self.player.spells]:
            self.player.points -= self.menu_options[0].points
            self.player.spells.append(self.menu_options[0])
            self.print_room()

        else:
            return

    def exit(self):
        return self.exit_room

class BuySpellMenuManager(basic_menu.BasicRotatingMenu):
    def __init__(self, player, exit_room):
        super().__init__()
        self.filters = spells.BaseSpell(player).types
        self.rooms = [BuySpellMenu(player, exit_room)]
        self.rooms += [BuySpellMenu(player, exit_room, type) for type in self.filters]
        self.filters = ['all'] + self.filters

        self.settings['title'] = 'buy-spells'.upper()

        self.room_nr = 0

        self.player = player
        self.exit_room = exit_room

        self.current_room = self.rooms[self.room_nr]

    def print_room(self, clear=False):
        self.current_room.print_room(clear)
        self.canvas.replace_line("room", f'Available points:{self.player.points}', 20)

        top_bar = "All | Damage | Heal | Buff | Debuff"
        top_bar = top_bar.replace(self.filters[self.room_nr].capitalize(), colored(self.filters[self.room_nr].capitalize(), 'white', 'on_green'))
        self.canvas.replace_line('room', top_bar, 1)
        self.canvas.print_canvas(clear)

    def choose(self):
        self.current_room.choose()
        self.print_room()

    def use_key(self, direction):
        if direction is "s":
            self.menu_options = self.current_room.use_key(direction)
            self.print_room()
        if direction is "w":
            self.menu_options = self.current_room.use_key(direction)
            self.print_room()
        if direction is "r":
            return self.exit()
        if direction is '\r' or direction is 'e' or ord(direction) is 13:
            return self.choose()
        if direction is 'a':
            return self.left()
        if direction is 'd':
            return self.right()

    def left(self):
        self.room_nr -= 1
        if self.room_nr < 0:
            self.room_nr = len(self.filters) - 1
        self.current_room = self.rooms[self.room_nr]
        self.print_room()

    def right(self):
        self.room_nr += 1
        if self.room_nr >= len(self.rooms):
            self.room_nr = 0
        self.current_room = self.rooms[self.room_nr]
        self.print_room()
