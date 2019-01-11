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
        self.string = f""" Health:     {self.player.health}/{self.player.max_health}
 Mana:       {self.player.mana}/{self.player.max_health}
 Str:        {self.player.str}
 Int:        {self.player.int}
 Agi:        {self.player.agi}
""" + "-"*self.settings['width']

        self.canvas.add_to_print('stats', self.string, self.settings)
