class StatWindow():
    def __init__(self, player, canvas):
        self.player = player

        self.settings = {
            'column_priority'  : 3,     # Order of who goes first from left to right
            'delay'             : 0,     # if it needs to be x lines below
            'width'             : 22,    # how wide will it print
            'allignment'        : '<',
            'max_lines'         : 0,    # for the string that keeps getting bigger. Take only the latest 30
            'join_char'         : ''
        }
        self.draw()
        canvas.add_to_print('stats', self.string, self.settings)

    def draw(self):
        self.string = "-"*self.settings['width'] +f"""
 Health:     {self.player.health}/{self.player.max_health}
 Mana:       {self.player.mana}/{self.player.max_health}
 Str:        {self.player.str}
 Int:        {self.player.health}
 Agi:        {self.player.health}
""" + "-"*self.settings['width']
