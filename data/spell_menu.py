from . import basic_menu

class CombatSpellMenu(basic_menu.BasicMenu):
    def __init__(self, player):
        super().__init__()

        self.player = player
        self.menu_options = player.spells

    def choose(self):
        self.player.chosen_spell = self.menu_options[0]
        return 'spell_chosen'
