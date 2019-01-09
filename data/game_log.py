import datetime


class GameLog:
    def __init__(self, canvas=None):
        self.canvas = canvas
        self.log = ""

        self.settings = {
        'column_priority'   : 1,     # Order of who goes first from left to right
        'delay'             : 0,     # if it needs to be x lines below
        'width'             : 50,    # how wide will it add_to_text_log
        'allignment'        : '<',
        'max_lines'         : 20,    # for the string that keeps getting bigger. Take only the latest 30
        'join_char'         : '',
        'title'             : "LOG"
        }

    def add_to_log(self, text, source):
        now = datetime.datetime.now().strftime('%H:%M')
        self.log += f"[{now}] [{source}] {text}" + "\n"

        self.print_canvas()

    def print_canvas(self, clear=False):
        if not self.canvas:
            raise Exception('GameLog has no target canvas.')
        self.canvas.add_to_print('log', self.log, self.settings)
        self.canvas.print_canvas(clear)

log = GameLog()
