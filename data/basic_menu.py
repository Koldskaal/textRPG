from .game_log import log
from termcolor import colored

class BasicRotatingMenu:
    def __init__(self):
        self.canvas = log.canvas
        self.menu_options = []  #"index1","index2","index3"
        self.menu_position = 0
        self.title_box = 'temp'
        self.title_window = 'TEMP-WIN'

        self.settings = {
            'column_priority'  : 2,     # Order of who goes first from left to right
            'delay'             : 3,     # if it needs to be x lines below
            'width'             : 41,    # how wide will it print
            'allignment'        : '^',
            'max_lines'         : 15,    # for the string that keeps getting bigger. Take only the latest 30
            'join_char'         : '',
            'title'             : self.title_window.upper(),
            'push'              : 0
        }

    @staticmethod
    def rotate(l, n):
        return l[n:] + l[:n]

    def print_room(self, clear=False):
        if len(self.menu_options) == 0:
            self.canvas.add_to_print("room", "", settings)
            self.canvas.print_canvas(clear)
            self.description_box(True)
        else:

            # self.pre_index = self.menu_options[0:self.menu_position]
            # self.index = colored(self.menu_options[self.menu_position-1], "white", 'on_green', attrs=['bold'])
            # self.post_index =  self.menu_options[self.menu_position+1:]
            # old_string = "\n".join(self.pre_index) + "\n" + self.index + "\n" + "\n".join(self.post_index)
            max = len(self.menu_options)
            if max > 9: max = 9
            aft_num = max // 2
            bef_num = max - aft_num

            lst = self.define_print_content()
            before = "\n".join(lst[-aft_num:]) + '\n'
            temp = lst[:bef_num]
            if len(lst) > 1:
                new = before + "\n".join(temp).replace(temp[0], colored(temp[0], "white", 'on_green', attrs=['bold']), 1)
            else:
                new = ' \n' + colored(before, "white", 'on_green', attrs=['bold'])

            self.canvas.add_to_print("room",new ,self.settings)
            self.canvas.print_canvas(clear)
            self.description_box()

    def description_box(self, empty=False):
        if empty:
            description_box = "Nothing here!"
            self.canvas.popup("room", description_box, 13, self.title_box)
            self.canvas.print_canvas()
        else:
            description_box, stats = self.define_descriptions(self.menu_options[0])

            self.canvas.popup("room", description_box, 13, self.title_box, stats, allignment='<')
            self.canvas.print_canvas()

    def define_descriptions(self, item):
        description_box = ""
        for key, values in item_ID.items[item].items():
            description_box += (f"{key}: {values} \n")
        return description_box, None

    def define_print_content(self):
        return self.menu_options

    def use_key(self, direction):
        if not self.menu_options:
            return self.exit()
        if direction is "s":
            self.menu_options = self.rotate(self.menu_options, 1)
            self.print_room()
        if direction is "w":
            self.menu_options = self.rotate(self.menu_options, -1)
            self.print_room()
        if direction is "r":
            return self.exit()
        if direction is '\r' or direction is 'e' or ord(direction) is 13:
            return self.choose()
        if direction is 'q':
            return self.choose_special()

    def choose(self):
        return self.menu_options[0]

    def choose_special(self):
        return

    def exit(self):
        return
