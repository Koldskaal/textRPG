import datetime
from termcolor import colored
from . import canvas

class GameLog:
    def __init__(self, canvas=None):
        self.canvas = canvas
        self.log = ""
        self.scroll_state = -1

        self.settings = {
        'column_priority'   : 1,     # Order of who goes first from left to right
        'delay'             : 0,     # if it needs to be x lines below
        'width'             : 50,    # how wide will it add_to_text_log
        'alignment'        : '<',
        'max_lines'         : 20,    # for the string that keeps getting bigger. Take only the latest 30
        'join_char'         : '',
        'title'             : "LOG"
        }

        self.colors = {
        'default'   : 'white',
        'bad'       : 'red',        # like dmg
        'useful'    : 'cyan',       # like getting loot or other info
        'positive'  : 'green',      # like heal or buffs or lifesteal
        'surprise'  : 'blue',     # no idea, be creative
        'recked'    : 'magenta',
        'white'     : 'white',      # same colors again in case I dont remeber my awesome keywords
        'red'       : 'red',
        'cyan'      : 'cyan',
        'green'     : 'green',
        'blue'      : 'blue',
        'magenta'   : 'magenta',
        'yellow'    : 'yellow',
        }
        self.canvas.add_to_print('log', self.log, self.settings)

    def add_to_log(self, text, source, effect='default'):
        self.scroll_state = 0
        now = datetime.datetime.now().strftime('%H:%M')
        l = len(self.log.splitlines())
        s = "\n"+f"[{now}] " + colored(f"{text}", self.colors[effect]) # [{source.upper()}] saved for later
        self.log += s

        self.print_canvas()

    def attach_to_log(self, text, effect='default'):
        self.log += colored(' '+text, self.colors[effect])
        self.print_canvas()

    def print_canvas(self, clear=False):
        if not self.canvas:
            raise Exception('GameLog has no target canvas.')
        self.canvas.add_to_print('log', self.log, self.settings, replace=False)
        self.canvas.print_canvas(clear)

    def scroll(self, direction):

        self.scroll_state += direction * 5
        t = self.log.splitlines()

        if len(t) < self.settings['max_lines']:
            return

        if self.scroll_state >= 0:
            self.scroll_state = 0
        elif self.scroll_state < -len(t) +self.settings['max_lines']:
            self.scroll_state = -len(t) + self.settings['max_lines']

        t = t[:(self.scroll_state if self.scroll_state else len(t))]
        if len(t) < self.settings['max_lines']:
            return
        self.canvas.add_to_print('log', "\n".join(t), self.settings)
        self.canvas.print_canvas()

game_canvas = canvas.Canvas()
log = GameLog(game_canvas)
