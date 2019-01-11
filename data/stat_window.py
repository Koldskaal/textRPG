from termcolor import colored
from .textures import *
class StatWindow():
    def __init__(self, player, canvas):
        self.player = player
        self.canvas = canvas
        self.settings = {
            'column_priority'  : 3,     # Order of who goes first from left to right
            'delay'             : 0,     # if it needs to be x lines below
            'width'             : 22,    # how wide will it print
            'allignment'        : '<',
            'max_lines'         : 0,    # for the string that keeps getting bigger. Take only the latest 30
            'join_char'         : '',
            'title'             : 'STATS'
        }
        self.draw()
        canvas.add_to_print('stats', self.string, self.settings)
        self.player.bind_stats(self.draw)

    def draw(self):
        length = 10
        iteration = self.player.health
        total = self.player.max_health
        filledLength = int(length * iteration // total)
        percent = ("{}").format(100 * (iteration / float(total)))
        fill = HEALTH_BAR
        player_bar = fill * filledLength + '-' * (length - filledLength)

        health = colored(player_bar, 'red') +'  ' +str(self.player.health)+'/'+str(self.player.max_health)

        length = 10
        iteration = self.player.mana
        total = self.player.max_mana
        filledLength = int(length * iteration // total)
        percent = ("{}").format(100 * (iteration / float(total)))
        fill = MANA_BAR
        player_bar = fill * filledLength + '-' * (length - filledLength)

        mana = colored(player_bar, 'blue') +'  ' +str(self.player.mana)+'/'+str(self.player.max_mana)

        self.string = f""" {health}
 {mana}
 Str:        {self.player.str}
 Int:        {self.player.int}
 Agi:        {self.player.agi}
""" + BORDER_UP_DOWN*self.settings['width']

        self.canvas.add_to_print('stats', self.string, self.settings)
