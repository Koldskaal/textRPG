import datetime


class GameLog:
    def __init__(self, canvas=None):
        self.canvas = canvas
        self.log = ""
        self.scroll_state = -1

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
        self.scroll_state = 0
        now = datetime.datetime.now().strftime('%H:%M')
        self.log += f"[{now}] [{source}] {text}" + "\n"

        self.print_canvas()

    def print_canvas(self, clear=False):
        if not self.canvas:
            raise Exception('GameLog has no target canvas.')
        self.canvas.add_to_print('log', self.log, self.settings)
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
        self.canvas.add_to_print('log', "\n".join(t ) , self.settings)
        self.canvas.print_canvas()

log = GameLog()
