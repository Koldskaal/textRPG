import sys
from . import room
from termcolor import colored
from . import item_ID
from . import game_log

class Char_menu: #TODO : tilføj rooms i roomcontroller til hver option,,, se shopkeeper måde.
    def __init__(self, canvas):
        self.canvas = canvas
        self.menu_options = ["Show Equipped", "Items", "Save", "Quit Game"]
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
            return "leave char_menu"

class Show_Equip:
    def __init__(self, canvas, player):
        self.canvas = canvas
        self.menu_options = [player.equipment]
        self.menu_position = 0
        self.player = player

    def print_room(self, clear=False):
        settings = {
            'column_priority'  : 2,     # Order of who goes first from left to right
            'delay'             : 4,     # if it needs to be x lines below
            'width'             : 30,    # how wide will it print
            'allignment'        : '<',
            'max_lines'         : 0,    # for the string that keeps getting bigger. Take only the latest 30
            'join_char'         : '',
            'title'             : 'Equipent Menu',
            'push'              : 0
        }
        if len(self.player.equipment) == 0:
            self.canvas.add_to_print("room", "", settings)
            self.canvas.print_canvas(clear)
            self.showcase(True)
        else:
            self.pre_index = self.menu_options[0:self.menu_position]
            self.index = colored(self.menu_options[self.menu_position], "white", 'on_green', attrs=['bold'])
            self.post_index =  self.menu_options[self.menu_position+1:]
            self.canvas.add_to_print("room", "\n".join(self.pre_index) + "\n" + self.index + "\n" + "\n".join(self.post_index),settings)
            self.canvas.print_canvas(clear)
            self.showcase()

    def showcase(self, empty=False):
        settings = {
            'column_priority'  : 3,     # Order of who goes first from left to right
            'delay'             : 7,     # if it needs to be x lines below
            'width'             : 30,    # how wide will it print
            'allignment'        : '<',
            'max_lines'         : 30,    # for the string that keeps getting bigger. Take only the latest 30
            'join_char'         : '',
            'title'             : 'Item Showcase',
            'push'              : 1
            }
        if empty:
            showcase = " Gosh! I'm naked!!"
            self.canvas.popup("room", showcase, 13)
            self.canvas.print_canvas()
        else:
            showcase = ""
            for key, values in item_ID.items[self.menu_options[0]].items():
                if key == "str":
                    showcase += colored((f"{key}: {values} \n"), 'red')
                if key == "agi":
                    showcase += colored((f"{key}: {values} \n"), 'green')
                if key == "int":
                    showcase += colored((f"{key}: {values} \n"), 'blue')
                if key == "hp":
                    showcase += colored((f"{key}: {values} \n"), 'white', 'on_red')
                if key == "mp":
                    showcase += colored((f"{key}: {values} \n"), 'white', 'on_blue')
                if key == "price":
                    showcase += colored((f"{key}: {values} \n"), 'yellow')
                if key == "armor":
                    showcase += colored((f"{key}: {values} \n"), 'white', 'on_grey')
                if key == "type":
                    showcase += (f"{key}: {values} \n")
            self.canvas.popup("room", showcase, 13)
            self.canvas.print_canvas()


    def equip_menu(self, direction):
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
            return "leave show equip"

class Items:
    def __init__(self, canvas, player):
        self.canvas = canvas
        self.menu_options = player.items
        self.menu_position = 0
        self.player = player

    def print_room(self, clear=False):
        settings = {
            'column_priority'  : 2,     # Order of who goes first from left to right
            'delay'             : 4,     # if it needs to be x lines below
            'width'             : 30,    # how wide will it print
            'allignment'        : '<',
            'max_lines'         : 0,    # for the string that keeps getting bigger. Take only the latest 30
            'join_char'         : '',
            'title'             : 'Item Menu',
            'push'              : 0
        }
        if len(self.player.items) == 0:
            self.canvas.add_to_print("room", "", settings)
            self.canvas.print_canvas(clear)
            self.showcase(True)
        else:
            self.pre_index = self.menu_options[0:self.menu_position]
            self.index = colored(self.menu_options[self.menu_position], "white", 'on_green', attrs=['bold'])
            self.post_index =  self.menu_options[self.menu_position+1:]
            self.canvas.add_to_print("room", "\n".join(self.pre_index) + "\n" + self.index + "\n" + "\n".join(self.post_index),settings)
            self.canvas.print_canvas(clear)
            self.showcase()

    def showcase(self, empty=False):
        settings = {
            'column_priority'  : 3,     # Order of who goes first from left to right
            'delay'             : 7,     # if it needs to be x lines below
            'width'             : 30,    # how wide will it print
            'allignment'        : '<',
            'max_lines'         : 30,    # for the string that keeps getting bigger. Take only the latest 30
            'join_char'         : '',
            'title'             : 'Item Showcase',
            'push'              : 1
            }
        if empty:
            showcase = " My pockets are empty!"
            self.canvas.popup("room", showcase, 13)
            self.canvas.print_canvas()
        else:
            showcase = ""
            for key, values in item_ID.items[self.menu_options[0]].items():
                if key == "price":
                    showcase += colored((f"{key}: {values} \n"), 'yellow')
                elif key != "price":
                    showcase += (f"{key}: {values} \n")
            self.canvas.popup("room", showcase, 13)
            self.canvas.print_canvas()


    def item_menu(self, direction):
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
            return "leave items"

class Save:
    def save_menu():
        if direction is "r":
            return "leave save"

class Quit_Game:
    def quit_menu():
        if direction is "r":
            return "leave quit game"
