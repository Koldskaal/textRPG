from . import basic_menu, game_log
from termcolor import colored

class TalentMenu(basic_menu.BasicRotatingMenu):
    def __init__(self):
        super().__init__()

        self.title = 'Info'

        self.player = player
        self.menu_options = self.get_three_random_talents_from_pile()

    def get_three_random_talents_from_pile(self):
        
