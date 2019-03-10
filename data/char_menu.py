import sys
from . import room
from termcolor import colored
from . import item_ID
from . import game_log
from . import player, stat_window

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
        self.menu_options = ["equip helmet", "equip armor", "equip ring", "equip amulet", "equip weapon"]
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
        self.pre_index = self.menu_options[0:self.menu_position]
        self.index = colored(self.menu_options[self.menu_position], "white", 'on_green')
        self.post_index =  self.menu_options[self.menu_position+1:]
        self.canvas.add_to_print("room", "\n".join(self.pre_index) + "\n" + self.index + "\n" + "\n".join(self.post_index),settings)
        self.canvas.print_canvas(clear)
        #self.showcase()

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
            for key, values in item_ID.items[self.menu_options[self.menu_position]].items():
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
            #for value in items.values():
            #    if value['type'] == 'helmet':
            #        return "equip helmets"
            #    if value['type'] == 'armor':
            #        return "equip armor"
            #    if value['type'] == 'ring':
            #        return "equip ring"
            ##        return "equip weapon"
        if direction is "r":
            return "leave show equip" #add show current equipment + showcase it

class Equip_Helmets:
    def __init__(self, canvas, player):
        self.helmets = []
        self.canvas = canvas
        self.menu_options = self.helmets
        self.menu_options.sort()
        self.menu_position = 0
        self.player = player
        self.list_of_helmets(player)
        self.stat_window = stat_window.StatWindow(player, self.canvas)
    @staticmethod
    def rotate(l, n):
        return l[n:] + l[:n]

    def list_of_helmets(self, player):
        for item in self.player.items:
            for key, value in item_ID.items.items():
                if value['type'] == 'helmet' and key == item:
                    self.helmets.append(item)

    def print_room(self, clear=False):
        settings = {
            'column_priority'  : 2,     # Order of who goes first from left to right
            'delay'             : 3,     # if it needs to be x lines below
            'width'             : 41,    # how wide will it print
            'allignment'        : '^',
            'max_lines'         : 15,    # for the string that keeps getting bigger. Take only the latest 30
            'join_char'         : '',
            'title'             : 'Equip Helmet',
            'push'              : 0
        }
        if len(self.helmets) == 0:
            self.canvas.add_to_print("room", "", settings)
            self.canvas.print_canvas(clear)
            self.showcase(True)
        else:
            max = len(self.menu_options)
            if max > 9: max = 9
            aft_num = max // 2
            bef_num = max - aft_num


            before = "\n".join(self.menu_options[-aft_num:]) + '\n'
            temp = self.menu_options[:bef_num]
            if len(self.menu_options) > 1:
                new = before + "\n".join(temp).replace(temp[0], colored(temp[0], "white", 'on_green', attrs=['bold']), 1)
            else:
                new = '-\n' + colored(before, "white", 'on_green', attrs=['bold'])

            self.canvas.add_to_print("room",new ,settings)
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
        if self.player.helmet == '' and self.helmets == []:
            showcase = " It's not a toupee!"
            self.canvas.popup("room", showcase, 13)
            self.canvas.print_canvas()
        elif self.helmets == []:
            showcase = " My pockets are empty!"
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
                if key == "description":
                    showcase += (f"{key}: {values} \n")
            self.canvas.popup("room", showcase, 13)
            self.canvas.print_canvas()

    def helmets_menu(self, direction):
        if not self.player.items:
            return "leave helmets"
        else:
            if direction is "s":
                self.menu_options = self.rotate(self.menu_options, 1)
                self.print_room()
            if direction is "w":
                self.menu_options = self.rotate(self.menu_options, -1)
                self.print_room()
            if direction is '\r': # ENTER KEY
                if self.helmets == []:
                    pass
                elif self.player.helmet == '':
                    self.player.helmet = [self.menu_options[0]]
                    self.equip_item(player)
                    self.player.items.remove(self.menu_options[0])
                    self.helmets = []
                    self.menu_options = self.helmets
                    self.menu_options.sort()
                    self.list_of_helmets(player)
                    self.stat_window.draw()
                    self.print_room()
                else:
                    self.player.items.append(self.player.helmet[0])
                    self.unequip_item(player)
                    self.player.helmet = [self.menu_options[0]]
                    self.equip_item(player)
                    self.player.items.remove(self.menu_options[0])
                    self.helmets = []
                    self.menu_options = self.helmets
                    self.menu_options.sort()
                    self.list_of_helmets(player)
                    self.stat_window.draw()
                    self.print_room()
            if direction is "r":
                return "leave helmets"
    def equip_item(self, player):
            for key, values in item_ID.items[self.menu_options[0]].items():
                if key == 'armor':
                    self.player.armor += values
                if key == 'str':
                    self.player.str += values
                if key == 'int':
                    self.player.int += values
                if key == 'agi':
                    self.player.agi += values
                if key == 'hp':
                    self.player.max_health += values
                if key == 'mana':
                    self.player.max_mana += values

    def unequip_item(self, player):
            for key, values in item_ID.items[self.player.helmet[0]].items():
                if key == 'armor':
                    self.player.armor -= values
                if key == 'str':
                    self.player.str -= values
                if key == 'int':
                    self.player.int -= values
                if key == 'agi':
                    self.player.agi -= values
                if key == 'hp':
                    self.player.max_health -= values
                if key == 'mana':
                    self.player.max_mana -= values

class Equip_Armors:
    def __init__(self, canvas, player):
        self.armors = []
        self.canvas = canvas
        self.menu_options = self.armors
        self.menu_options.sort()
        self.menu_position = 0
        self.player = player
        self.list_of_armors(player)
        self.stat_window = stat_window.StatWindow(player, self.canvas)
    @staticmethod
    def rotate(l, n):
        return l[n:] + l[:n]

    def list_of_armors(self, player):
        for item in self.player.items:
            for key, value in item_ID.items.items():
                if value['type'] == 'armor' and key == item:
                    self.armors.append(item)

    def print_room(self, clear=False):
        settings = {
            'column_priority'  : 2,     # Order of who goes first from left to right
            'delay'             : 3,     # if it needs to be x lines below
            'width'             : 41,    # how wide will it print
            'allignment'        : '^',
            'max_lines'         : 15,    # for the string that keeps getting bigger. Take only the latest 30
            'join_char'         : '',
            'title'             : 'Equip Helmet',
            'push'              : 0
        }
        if len(self.player.items) == 0:
            self.canvas.add_to_print("room", "", settings)
            self.canvas.print_canvas(clear)
            self.showcase(True)
        else:
            max = len(self.menu_options)
            if max > 9: max = 9
            aft_num = max // 2
            bef_num = max - aft_num


            before = "\n".join(self.menu_options[-aft_num:]) + '\n'
            temp = self.menu_options[:bef_num]
            if len(self.menu_options) > 1:
                new = before + "\n".join(temp).replace(temp[0], colored(temp[0], "white", 'on_green', attrs=['bold']), 1)
            else:
                new = '-\n' + colored(before, "white", 'on_green', attrs=['bold'])

            self.canvas.add_to_print("room",new ,settings)
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
        if self.player.body == '' and self.armors == []:
            showcase = " I'm naked!"
            self.canvas.popup("room", showcase, 13)
            self.canvas.print_canvas()
        elif self.armors == []:
            showcase = " My pockets are empty!"
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
                if key == "description":
                    showcase += (f"{key}: {values} \n")
            self.canvas.popup("room", showcase, 13)
            self.canvas.print_canvas()

    def armors_menu(self, direction):
        if not self.player.items:
            return "leave armors"
        else:
            if direction is "s":
                self.menu_options = self.rotate(self.menu_options, 1)
                self.print_room()
            if direction is "w":
                self.menu_options = self.rotate(self.menu_options, -1)
                self.print_room()
            if direction is '\r': # ENTER KEY
                if self.armors == []:
                    pass
                elif self.player.body == '':
                    self.player.body = [self.menu_options[0]]
                    self.equip_item(player)
                    self.player.items.remove(self.menu_options[0])
                    self.armors = []
                    self.menu_options = self.armors
                    self.menu_options.sort()
                    self.list_of_armors(player)
                    self.stat_window.draw()
                    self.print_room()
                else:
                    self.player.items.append(self.player.body[0])
                    self.unequip_item(player)
                    self.player.body = [self.menu_options[0]]
                    self.equip_item(player)
                    self.player.items.remove(self.menu_options[0])
                    self.armors = []
                    self.menu_options = self.armors
                    self.menu_options.sort()
                    self.list_of_armors(player)
                    self.stat_window.draw()
                    self.print_room()
            if direction is "r":
                return "leave armors"
    def equip_item(self, player):
            for key, values in item_ID.items[self.menu_options[0]].items():
                if key == 'armor':
                    self.player.armor += values
                if key == 'str':
                    self.player.str += values
                if key == 'int':
                    self.player.int += values
                if key == 'agi':
                    self.player.agi += values
                if key == 'hp':
                    self.player.max_health += values
                if key == 'mana':
                    self.player.max_mana += values

    def unequip_item(self, player):
            for key, values in item_ID.items[self.player.body[0]].items():
                if key == 'armor':
                    self.player.armor -= values
                if key == 'str':
                    self.player.str -= values
                if key == 'int':
                    self.player.int -= values
                if key == 'agi':
                    self.player.agi -= values
                if key == 'hp':
                    self.player.max_health -= values
                if key == 'mana':
                    self.player.max_mana -= values

class Equip_Rings:
    def __init__(self, canvas, player):
        self.rings = []
        self.canvas = canvas
        self.menu_options = self.rings
        self.menu_options.sort()
        self.menu_position = 0
        self.player = player
        self.list_of_rings(player)
        self.stat_window = stat_window.StatWindow(player, self.canvas)
    @staticmethod
    def rotate(l, n):
        return l[n:] + l[:n]

    def list_of_rings(self, player):
        for item in self.player.items:
            for key, value in item_ID.items.items():
                if value['type'] == 'ring' and key == item:
                    self.rings.append(item)

    def print_room(self, clear=False):
        settings = {
            'column_priority'  : 2,     # Order of who goes first from left to right
            'delay'             : 3,     # if it needs to be x lines below
            'width'             : 41,    # how wide will it print
            'allignment'        : '^',
            'max_lines'         : 15,    # for the string that keeps getting bigger. Take only the latest 30
            'join_char'         : '',
            'title'             : 'Equip Helmet',
            'push'              : 0
        }
        if len(self.player.items) == 0:
            self.canvas.add_to_print("room", "", settings)
            self.canvas.print_canvas(clear)
            self.showcase(True)
        else:
            max = len(self.menu_options)
            if max > 9: max = 9
            aft_num = max // 2
            bef_num = max - aft_num


            before = "\n".join(self.menu_options[-aft_num:]) + '\n'
            temp = self.menu_options[:bef_num]
            if len(self.menu_options) > 1:
                new = before + "\n".join(temp).replace(temp[0], colored(temp[0], "white", 'on_green', attrs=['bold']), 1)
            else:
                new = '-\n' + colored(before, "white", 'on_green', attrs=['bold'])

            self.canvas.add_to_print("room",new ,settings)
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
        if self.player.ring == '' and self.rings == []:
            showcase = " If you like it then you should've put a ring on it!"
            self.canvas.popup("room", showcase, 13)
            self.canvas.print_canvas()
        elif self.rings == []:
            showcase = " My pockets are empty!"
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
                if key == "description":
                    showcase += (f"{key}: {values} \n")
            self.canvas.popup("room", showcase, 13)
            self.canvas.print_canvas()

    def rings_menu(self, direction):
        if not self.player.items:
            return "leave rings"
        else:
            if direction is "s":
                self.menu_options = self.rotate(self.menu_options, 1)
                self.print_room()
            if direction is "w":
                self.menu_options = self.rotate(self.menu_options, -1)
                self.print_room()
            if direction is '\r': # ENTER KEY
                if self.rings == []:
                    pass
                elif self.player.ring == '':
                    self.player.ring = [self.menu_options[0]]
                    self.equip_item(player)
                    self.player.items.remove(self.menu_options[0])
                    self.rings = []
                    self.menu_options = self.rings
                    self.menu_options.sort()
                    self.list_of_rings(player)
                    self.stat_window.draw()
                    self.print_room()
                else:
                    self.player.items.append(self.player.ring[0])
                    self.unequip_item(player)
                    self.player.ring = [self.menu_options[0]]
                    self.equip_item(player)
                    self.player.items.remove(self.menu_options[0])
                    self.rings = []
                    self.menu_options = self.rings
                    self.menu_options.sort()
                    self.list_of_rings(player)
                    self.stat_window.draw()
                    self.print_room()
            if direction is "r":
                return "leave rings"
    def equip_item(self, player):
            for key, values in item_ID.items[self.menu_options[0]].items():
                if key == 'armor':
                    self.player.armor += values
                if key == 'str':
                    self.player.str += values
                if key == 'int':
                    self.player.int += values
                if key == 'agi':
                    self.player.agi += values
                if key == 'hp':
                    self.player.max_health += values
                if key == 'mana':
                    self.player.max_mana += values

    def unequip_item(self, player):
            for key, values in item_ID.items[self.player.ring[0]].items():
                if key == 'armor':
                    self.player.armor -= values
                if key == 'str':
                    self.player.str -= values
                if key == 'int':
                    self.player.int -= values
                if key == 'agi':
                    self.player.agi -= values
                if key == 'hp':
                    self.player.max_health -= values
                if key == 'mana':
                    self.player.max_mana -= values

class Equip_Amulets:
    def __init__(self, canvas, player):
        self.amulets = []
        self.canvas = canvas
        self.menu_options = self.amulets
        self.menu_options.sort()
        self.menu_position = 0
        self.player = player
        self.list_of_amulets(player)
        self.stat_window = stat_window.StatWindow(player, self.canvas)
    @staticmethod
    def rotate(l, n):
        return l[n:] + l[:n]

    def list_of_amulets(self, player):
        for item in self.player.items:
            for key, value in item_ID.items.items():
                if value['type'] == 'amulet' and key == item:
                    self.amulets.append(item)

    def print_room(self, clear=False):
        settings = {
            'column_priority'  : 2,     # Order of who goes first from left to right
            'delay'             : 3,     # if it needs to be x lines below
            'width'             : 41,    # how wide will it print
            'allignment'        : '^',
            'max_lines'         : 15,    # for the string that keeps getting bigger. Take only the latest 30
            'join_char'         : '',
            'title'             : 'Equip Helmet',
            'push'              : 0
        }
        if len(self.player.items) == 0:
            self.canvas.add_to_print("room", "", settings)
            self.canvas.print_canvas(clear)
            self.showcase(True)
        else:
            max = len(self.menu_options)
            if max > 9: max = 9
            aft_num = max // 2
            bef_num = max - aft_num


            before = "\n".join(self.menu_options[-aft_num:]) + '\n'
            temp = self.menu_options[:bef_num]
            if len(self.menu_options) > 1:
                new = before + "\n".join(temp).replace(temp[0], colored(temp[0], "white", 'on_green', attrs=['bold']), 1)
            else:
                new = '-\n' + colored(before, "white", 'on_green', attrs=['bold'])

            self.canvas.add_to_print("room",new ,settings)
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
        if self.player.amulet == '' and self.amulets == []:
            showcase = " If i was a rich girl..."
            self.canvas.popup("room", showcase, 13)
            self.canvas.print_canvas()
        elif self.amulets == []:
            showcase = " My pockets are empty!"
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
                if key == "description":
                    showcase += (f"{key}: {values} \n")
            self.canvas.popup("room", showcase, 13)
            self.canvas.print_canvas()

    def amulets_menu(self, direction):
        if not self.player.items:
            return "leave amulets"
        else:
            if direction is "s":
                self.menu_options = self.rotate(self.menu_options, 1)
                self.print_room()
            if direction is "w":
                self.menu_options = self.rotate(self.menu_options, -1)
                self.print_room()
            if direction is '\r': # ENTER KEY
                if self.amulets == []:
                    pass
                elif self.player.amulet == '':
                    self.player.amulet = [self.menu_options[0]]
                    self.equip_item(player)
                    self.player.items.remove(self.menu_options[0])
                    self.amulets = []
                    self.menu_options = self.amulets
                    self.menu_options.sort()
                    self.list_of_amulets(player)
                    self.stat_window.draw()
                    self.print_room()
                else:
                    self.player.items.append(self.player.amulet[0])
                    self.unequip_item(player)
                    self.player.amulet = [self.menu_options[0]]
                    self.equip_item(player)
                    self.player.items.remove(self.menu_options[0])
                    self.amulets = []
                    self.menu_options = self.amulets
                    self.menu_options.sort()
                    self.list_of_amulets(player)
                    self.stat_window.draw()
                    self.print_room()
            if direction is "r":
                return "leave amulets"
    def equip_item(self, player):
            for key, values in item_ID.items[self.menu_options[0]].items():
                if key == 'armor':
                    self.player.armor += values
                if key == 'str':
                    self.player.str += values
                if key == 'int':
                    self.player.int += values
                if key == 'agi':
                    self.player.agi += values
                if key == 'hp':
                    self.player.max_health += values
                if key == 'mana':
                    self.player.max_mana += values

    def unequip_item(self, player):
            for key, values in item_ID.items[self.player.amulet[0]].items():
                if key == 'armor':
                    self.player.armor -= values
                if key == 'str':
                    self.player.str -= values
                if key == 'int':
                    self.player.int -= values
                if key == 'agi':
                    self.player.agi -= values
                if key == 'hp':
                    self.player.max_health -= values
                if key == 'mana':
                    self.player.max_mana -= values

class Equip_Weapons:
    def __init__(self, canvas, player):
        self.weapons = []
        self.canvas = canvas
        self.menu_options = self.weapons
        self.menu_options.sort()
        self.menu_position = 0
        self.player = player
        self.list_of_weapons(player)
        self.stat_window = stat_window.StatWindow(player, self.canvas)
    @staticmethod
    def rotate(l, n):
        return l[n:] + l[:n]

    def list_of_weapons(self, player):
        for item in self.player.items:
            for key, value in item_ID.items.items():
                if value['type'] == 'weapon' and key == item:
                    self.weapons.append(item)

    def print_room(self, clear=False):
        settings = {
            'column_priority'  : 2,     # Order of who goes first from left to right
            'delay'             : 3,     # if it needs to be x lines below
            'width'             : 41,    # how wide will it print
            'allignment'        : '^',
            'max_lines'         : 15,    # for the string that keeps getting bigger. Take only the latest 30
            'join_char'         : '',
            'title'             : 'Equip Helmet',
            'push'              : 0
        }
        if len(self.player.items) == 0:
            self.canvas.add_to_print("room", "", settings)
            self.canvas.print_canvas(clear)
            self.showcase(True)
        else:
            max = len(self.menu_options)
            if max > 9: max = 9
            aft_num = max // 2
            bef_num = max - aft_num


            before = "\n".join(self.menu_options[-aft_num:]) + '\n'
            temp = self.menu_options[:bef_num]
            if len(self.menu_options) > 1:
                new = before + "\n".join(temp).replace(temp[0], colored(temp[0], "white", 'on_green', attrs=['bold']), 1)
            else:
                new = '-\n' + colored(before, "white", 'on_green', attrs=['bold'])

            self.canvas.add_to_print("room",new ,settings)
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
        if self.player.weapon == '' and self.weapons == []:
            showcase = " At least I can't drop my weapon..."
            self.canvas.popup("room", showcase, 13)
            self.canvas.print_canvas()
        elif self.weapons == []:
            showcase = " My pockets are empty!"
            self.canvas.popup("room", showcase, 13)
            self.canvas.print_canvas()
        else:
            showcase = ""
            for key, values in item_ID.items[self.menu_options[0]].items():
                if key == 'ATT':
                    showcase += (f"{key}: {values} \n")
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
                if key == "description":
                    showcase += (f"{key}: {values} \n")
            self.canvas.popup("room", showcase, 13)
            self.canvas.print_canvas()

    def weapons_menu(self, direction):
        if not self.player.items:
            return "leave weapons"
        else:
            if direction is "s":
                self.menu_options = self.rotate(self.menu_options, 1)
                self.print_room()
            if direction is "w":
                self.menu_options = self.rotate(self.menu_options, -1)
                self.print_room()
            if direction is '\r': # ENTER KEY
                if self.weapons == []:
                    pass
                elif self.player.weapon == '':
                    self.player.weapon = [self.menu_options[0]]
                    self.equip_item(player)
                    self.player.items.remove(self.menu_options[0])
                    self.weapons = []
                    self.menu_options = self.weapons
                    self.menu_options.sort()
                    self.list_of_weapons(player)
                    self.stat_window.draw()
                    self.print_room()
                else:
                    self.player.items.append(self.player.weapon[0])
                    self.unequip_item(player)
                    self.player.weapon = [self.menu_options[0]]
                    self.equip_item(player)
                    self.player.items.remove(self.menu_options[0])
                    self.weapons = []
                    self.menu_options = self.weapons
                    self.menu_options.sort()
                    self.list_of_weapons(player)
                    self.stat_window.draw()
                    self.print_room()
            if direction is "r":
                return "leave weapons"
    def equip_item(self, player):
            for key, values in item_ID.items[self.menu_options[0]].items():
                if key == 'ATT':
                    self.player.ATT += values
                if key == 'armor':
                    self.player.armor += values
                if key == 'str':
                    self.player.str += values
                if key == 'int':
                    self.player.int += values
                if key == 'agi':
                    self.player.agi += values
                if key == 'hp':
                    self.player.max_health += values
                if key == 'mana':
                    self.player.max_mana += values

    def unequip_item(self, player):
            for key, values in item_ID.items[self.player.weapon[0]].items():
                if key == 'ATT':
                    self.player.ATT -= values
                if key == 'armor':
                    self.player.armor -= values
                if key == 'str':
                    self.player.str -= values
                if key == 'int':
                    self.player.int -= values
                if key == 'agi':
                    self.player.agi -= values
                if key == 'hp':
                    self.player.max_health -= values
                if key == 'mana':
                    self.player.max_mana -= values

class Items:
    def __init__(self, canvas, player):
        self.canvas = canvas
        self.menu_options = player.items
        self.menu_options.sort()
        self.menu_position = 0
        self.player = player

    @staticmethod
    def rotate(l, n):
        return l[n:] + l[:n]

    def print_room(self, clear=False):

        settings = {
            'column_priority'  : 2,     # Order of who goes first from left to right
            'delay'             : 3,     # if it needs to be x lines below
            'width'             : 41,    # how wide will it print
            'allignment'        : '^',
            'max_lines'         : 15,    # for the string that keeps getting bigger. Take only the latest 30
            'join_char'         : '',
            'title'             : 'SHOP-BUY',
            'push'              : 0
        }
        if len(self.player.items) == 0:
            self.canvas.add_to_print("room", "", settings)
            self.canvas.print_canvas(clear)
            self.showcase(True)
        else:

            # self.pre_index = self.menu_options[0:self.menu_position]
            # self.index = colored(self.menu_options[self.menu_position-1], "white", 'on_green', attrs=['bold'])
            # self.post_index =  self.menu_options[self.menu_position+1:]
            # old_string = "\n".join(self.pre_index) + "\n" + self.index + "\n" + "\n".join(self.post_index)
            max = len(self.menu_options)
            if max > 9: max = 9
            aft_num = max // 2
            bef_num = max - aft_num


            before = "\n".join(self.menu_options[-aft_num:]) + '\n'
            temp = self.menu_options[:bef_num]
            if len(self.menu_options) > 1:
                new = before + "\n".join(temp).replace(temp[0], colored(temp[0], "white", 'on_green', attrs=['bold']), 1)
            else:
                new = '-\n' + colored(before, "white", 'on_green', attrs=['bold'])

            self.canvas.add_to_print("room",new ,settings)
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
                if key == 'ATT':
                    showcase += (f"{key}: {values} \n")
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
                if key == "description":
                    showcase += (f"{key}: {values} \n")
            self.canvas.popup("room", showcase, 13)
            self.canvas.print_canvas()

    def item_menu(self, direction):
        if not self.player.items:
            return "leave items"
        else:
            if direction is "s":
                self.menu_options = self.rotate(self.menu_options, 1)
                self.print_room()
            if direction is "w":
                self.menu_options = self.rotate(self.menu_options, -1)
                self.print_room()
            if direction is '\r': # ENTER KEY
                for key, values in item_ID.items[self.menu_options[0]].items():
                    if values == "consumable":
                        if self.menu_options[0] == "health potion":
                            self.player.health += 100
                            self.player.items.remove('health potion')
                        if self.menu_options[0] == "mana potion":
                            self.player.mana += 100
                            self.player.items.remove('mana potion')
                        if self.menu_options[0] == "worn-out bedroll":
                            self.player.mana += 10000
                            self.player.health += 10000
                            self.player.items.remove('worn-out bedroll')
                    self.print_room()
                pass
            if direction is "r":
                return "leave items"
class Save:
    def __init__(self, canvas):
        self.canvas = canvas
        self.menu_options = ["Save game placeholder", "Save game 2 placeholder"]
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
            pass # requires a save method
        if direction is "r":
            return "leave save_menu"
class Quit_Game:
    def __init__(self, canvas):
        self.canvas = canvas
        self.menu_options = ["No", "Yes"]
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
        self.canvas.add_to_print("room", "Are you sure you wish to quit the game?", settings)
        self.pre_index = self.menu_options[0:self.menu_position]
        self.index = colored(self.menu_options[self.menu_position], "white", 'on_green', attrs=['bold'])
        self.post_index =  self.menu_options[self.menu_position+1:]
        self.canvas.add_to_print("room", "\n".join(self.pre_index) + "\n" + self.index + "\n" + "\n".join(self.post_index),settings)
        self.canvas.print_canvas(clear)

    def quit_menu(self, direction):
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
            if self.menu_options[self.menu_position] == "Yes":
                sys.exit(0)
            else:
                return "leave quit game"
        if direction is "r":
            return "leave quit game"
