from .game_log import log
from termcolor import colored

class menu:
    def __init__(self):
        self.canvas = log.canvas
        self.menu_options = []  #"index1","index2","index3"
        self.menu_position = 0
        selt.title = 'temp'

    def print_room(self, clear=False):
        settings = {
            'column_priority'  : 2,     # Order of who goes first from left to right
            'delay'             : 4,     # if it needs to be x lines below
            'width'             : 41,    # how wide will it print
            'allignment'        : '<',
            'max_lines'         : 0,    # for the string that keeps getting bigger. Take only the latest 30
            'join_char'         : '',
            'title'             : self.title.upper(),
            'push'              : 18
        }

<<<<<<< HEAD
        if if not self.menu_options:
            self.canvas.add_to_print("room", "No items in menu_options!", settings)
            self.canvas.print_canvas()
        else:
            item_list_string = "\n".join(self.menu_options)
            item_list_string.replace(self.menu_options[self.menu_position], colored(self.menu_options[self.menu_position], "white", 'on_green'))
            self.canvas.add_to_print("room", item_list_string, settings)
            self.canvas.print_canvas(clear)
=======
    def print_room(self, clear=False):
        self.pre_index = self.menu_options[0:self.menu_position]
        self.index = colored(self.menu_options[self.menu_position], "white", 'on_green', attrs=['bold'])
        self.post_index =  self.menu_options[self.menu_position+1:]
        self.canvas.add_to_print("room", "\n".join(self.pre_index) + "\n" + self.index + "\n" + "\n".join(self.post_index))
        self.canvas.print_canvas()
>>>>>>> 3bc3e3178a215f7e0cf982c1fbca9d780466e6da

    def shop_menu(self, direction):
        if not self.menu_options:
            return "leave_buy"
        if direction is "s":
            self.menu_position += 1
            if self.menu_position > len(self.menu_options)-1:
                self.menu_position = len(self.menu_options)-1
            self.print_room()
        if direction is "w":
            self.menu_position -= 1
            if self.menu_position < 0:
                self.menu_position = 0
            self.print_room()
        if direction is '\r':
            self.choose()
            self.print_room()
