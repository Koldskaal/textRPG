class Char_menu: #TODO : tilføj rooms i roomcontroller til hver option,,, se shopkeeper måde.
    def __init__(self, canvas, player):
        self.canvas = canvas
        self.menu_options = "Show Equipped, Items, Save, Quit Game"
        self.menu_position = 0

    def print_room(self, clear=False):
        settings = {
            'column_priority'  : 2,     # Order of who goes first from left to right
            'delay'             : 4,     # if it needs to be x lines below
            'width'             : 30,    # how wide will it print
            'allignment'        : '<',
            'max_lines'         : 0,    # for the string that keeps getting bigger. Take only the latest 30
            'join_char'         : '',
            'title'             : 'Character Menu',
            'push'              : 0
        }
        self.pre_index = self.menu_options[0:self.menu_position]
        self.index = colored(self.menu_options[self.menu_position], "white", 'on_green', attrs=['bold'])
        self.post_index =  self.menu_options[self.menu_position+1:]
        self.canvas.add_to_print("room", "\n".join(self.pre_index) + "\n" + self.index + "\n" + "\n".join(self.post_index),settings)
        self.canvas.print_canvas(clear)

    def char_menu(self, direction):
        if direction is "s":
            self.menu_position += 1
            if self.menu_position > len(self.menu_options)-1:
                self.menu_position = len(self.menu_options)-1
            self.print_room()
        if direction is "w":
            self.menu_position -= 1
            if self.menu_position <0:
                self.menu_position = 0
            self.print_room()
        if direction is '\r': # ENTER KEY
            return self.menu_options[self.menu_position]
        if direction is "r":
            del self.canvas.areas["showcase"]
            return "leave_sell"

class Show_equip:
    pass

class Items:
    pass

class Save:
    pass

class Quit_game:
    pass
