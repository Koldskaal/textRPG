from termcolor import colored
from .textures import *

class StatWindow():
    def __init__(self, player, canvas):
        self.player = player
        self.canvas = canvas
        self.settings = {
            'column_priority'  : 4,     # Order of who goes first from left to right
            'delay'             : 0,     # if it needs to be x lines below
            'width'             : 30,    # how wide will it print
            'allignment'        : '<',
            'max_lines'         : 0,    # for the string that keeps getting bigger. Take only the latest 30
            'join_char'         : '',
            'title'             : 'STATS'
        }
        self.draw()
        canvas.add_to_print('stats', self.string, self.settings)
        self.player.bind_stats(self.draw)

    def draw(self):
        def bar(iteration, total, color):
            length = self.settings['width']//2
            # iteration = self.player.health
            # total = self.player.max_health
            filledLength = int(length * iteration // total)
            percent = ("{}").format(100 * (iteration / float(total)))
            fill = HEALTH_BAR
            player_bar = fill * filledLength + '-' * (length - filledLength)

            bar_and_text = colored(player_bar, color) +'  ' +str(iteration)+'/'+str(total)
            return bar_and_text

        health = bar(self.player.health, self.player.max_health, 'red')
        mana = bar(self.player.mana, self.player.max_mana, 'blue')

        level = "Level:".ljust(self.settings['width']//2) + (self.level + colored(f"▲ {self.player.points}"if self.player.points else "", 'yellow')).rjust(.self.settings['width']//2)
        strength = f"Str:".ljust(self.settings['width']//2)+f"{self.player.str}".rjust(.self.settings['width']//2)
        intellect = f"Int:".ljust(self.settings['width']//2)+f"{self.player.int}".rjust(.self.settings['width']//2)
        agility = f"Agi:".ljust(self.settings['width']//2) + f"{self.player.agi}".rjust(.self.settings['width']//2)
        border = 'MISC'.center(self.settings['width'], BORDER_UP_DOWN)
        gold = "Gold:".ljust(self.settings['width']//2) + f"{self.player.gold}".rjust(.self.settings['width']//2)
        exp = f"Remaining exp:".ljust(self.settings['width']//2) + f"{self.player.levelcap-self.player.exp}".rjust(.self.settings['width']//2)



        self.canvas.add_to_print('stats', self.string, self.settings)


        stats = {'Str': self.player.str, 'Int': self.player.int, 'Agi':self.player.agi}
