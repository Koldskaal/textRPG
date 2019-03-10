from termcolor import colored
from .textures import *

class StatWindow():
    def __init__(self, player, canvas):
        self.player = player
        self.canvas = canvas
        self.settings = {
            'column_priority'   : 4,     # Order of who goes first from left to right
            'delay'             : 0,     # if it needs to be x lines below
            'width'             : 30,    # how wide will it print
            'alignment'         : '<',
            'max_lines'         : 0,    # for the string that keeps getting bigger. Take only the latest 30
            'push'              : 1,
            'title'             : 'STATS',

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

            bar_and_text = colored(player_bar, color) +(str(iteration)+'/'+str(total)).rjust(self.settings['width']//2-2)
            return bar_and_text

        health = bar(self.player.health, self.player.max_health, 'red')
        mana = bar(self.player.mana, self.player.max_mana, 'blue')

        level = "Level".ljust(self.settings['width']//2) + (f"{self.player.level} ▲ {self.player.points}"if self.player.points else f"{self.player.level}").rjust(self.settings['width']//2-2).replace(f" ▲ {self.player.points}", colored(f" ▲ {self.player.points}",'yellow'))
        strength = "Strength".ljust(self.settings['width']//2)+f"{self.player.str}".rjust(self.settings['width']//2-2)
        intellect = "Intellect".ljust(self.settings['width']//2)+f"{self.player.int}".rjust(self.settings['width']//2-2)
        agility = "Agility".ljust(self.settings['width']//2) + f"{self.player.agi}".rjust(self.settings['width']//2-2)
        border = 'MISC'.center(self.settings['width']-2, BORDER_UP_DOWN)
        gold = "Gold".ljust(self.settings['width']//2) + f"{self.player.gold}".rjust(self.settings['width']//2-2)
        exp = "Remaining exp".ljust(self.settings['width']//2) + f"{self.player.levelcap-self.player.exp}".rjust(self.settings['width']//2-2)

        stats_list = [level, health,mana, strength,intellect,agility,border,gold,exp]
        self.string = ""
        for i in stats_list:
            self.string += i + "\n"

        self.canvas.add_to_print('stats', self.string, self.settings)


        stats = {'Str': self.player.str, 'Int': self.player.int, 'Agi':self.player.agi}
