from . import shopkeeper_stock
import sys
from . import room
from termcolor import colored
from . import item_ID
from . import game_log

class Shop:
    def __init__(self, canvas, p, exit_room):
        self.canvas = canvas
        self.menu_options = ["Buy", "Sell", "Leave"]
        self.menu_position = 0
        self.shop_position = 0

        self.sell_room = Sell(self.canvas, p, self)
        self.sell_room.go_back = self
        self.buy_room = Buy(self.canvas, p, self)
        self.buy_room.go_back = self

        self.go_back = exit_room

    def print_room(self, clear=False):
        settings = {
            'column_priority'  : 2,     # Order of who goes first from left to right
            'delay'             : 4,     # if it needs to be x lines below
            'width'             : 41,    # how wide will it print
            'allignment'        : '<',
            'max_lines'         : 0,    # for the string that keeps getting bigger. Take only the latest 30
            'join_char'         : '',
            'title'             : 'SHOP',
            'push'              : 18
        }
        self.pre_index = self.menu_options[0:self.menu_position]
        self.index = colored(self.menu_options[self.menu_position], "white", 'on_green', attrs=['bold'])
        self.post_index =  self.menu_options[self.menu_position+1:]
        self.canvas.add_to_print("room", "\n".join(self.pre_index) + "\n" + self.index + "\n" + "\n".join(self.post_index),settings)
        self.canvas.print_canvas(clear)

    def use_key(self, direction):
        """ direction is :"""
        if direction is "s":
            self.menu_position += 1
            if self.menu_position > 2:
                self.menu_position = 2
            self.print_room()
        if direction is "w":
            self.menu_position -= 1
            if self.menu_position <0:
                self.menu_position = 0
            self.print_room()
        if direction is '\r': # ENTER KEY
            if self.menu_position == 0:
                return self.buy_room
            if self.menu_position == 1:
                return self.sell_room
            if self.menu_position == 2:
                return self.go_back

class Sell:
    def __init__(self, canvas, player, exit_room):
        self.canvas = canvas
        self.menu_options = player.items
        self.menu_options.sort()
        self.menu_position = 0
        self.player = player

        self.go_back = exit_room

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
            'title'             : 'SHOP-Sell',
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



    def use_key(self, direction):
        if not self.player.items:
            return self.go_back
        else:
            if direction is "s":
                self.menu_options = self.rotate(self.menu_options, 1)
                self.print_room()
            if direction is "w":
                self.menu_options = self.rotate(self.menu_options, -1)
                self.print_room()
            if direction is '\r': # ENTER KEY
                    shopkeeper_stock.shop_items.append(self.menu_options[0])
                    self.player.gold += item_ID.items[self.menu_options[0]]['price']*0.5
                    del self.menu_options[0]
                    self.player.items = self.menu_options
                    self.print_room()
            if direction is "r":
                return self.go_back

# items = ['1','2','3','4','5','6','7','8','9','10','11','12','fourteen','fifthteen','16','17','18','19','20','21']

class Buy:
    def __init__(self, canvas, player, exit_room):
        self.canvas = canvas
        self.menu_options = shopkeeper_stock.shop_items
        self.menu_options.sort()
        self.menu_position = 0
        self.player = player

        self.go_back = exit_room

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
        if len(shopkeeper_stock.shop_items) == 0:
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
            showcase = " Sorry we are out!"
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

    def use_key(self, direction):
        if not shopkeeper_stock.shop_items:
            return self.go_back
        else:
            if direction is "s":
                self.menu_options = self.rotate(self.menu_options, 1)
                self.print_room()
            if direction is "w":
                self.menu_options = self.rotate(self.menu_options, -1)
                self.print_room()
            if direction is '\r': # ENTER KEY
                if self.player.gold > item_ID.items[self.menu_options[0]]['price']:
                    self.player.items.append(self.menu_options[0])
                    self.player.gold -= item_ID.items[self.menu_options[0]]['price']
                    del self.menu_options[0]
                    shopkeeper_stock.shop_items = self.menu_options
                    self.print_room()
            if direction is "r":
                # del self.canvas.areas["showcase"]
                return self.go_back
