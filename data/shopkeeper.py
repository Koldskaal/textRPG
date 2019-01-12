from . import shopkeeper_stock
import sys
from . import room
from termcolor import colored
from . import item_ID
from . import game_log

class Shop:
    def __init__(self, canvas):
        self.canvas = canvas
        self.menu_options = ["Buy", "Sell", "Leave"]
        self.menu_position = 0
        self.shop_position = 0

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

    def shop_menu(self, direction):
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
                return "buy_menu"
            if self.menu_position == 1:
                return "sell_menu"
            if self.menu_position == 2:
                return "leave_shop"

class Sell:
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
            'title'             : 'SHOP BUY',
            'push'              : 0
        }
        if len(self.player.items) == 0:
            self.canvas.add_to_print("room", "My pockets are empty!", settings)
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
            'delay'             : 4,     # if it needs to be x lines below
            'width'             : 30,    # how wide will it print
            'allignment'        : '<',
            'max_lines'         : 0,    # for the string that keeps getting bigger. Take only the latest 30
            'join_char'         : '',
            'title'             : 'Item Showcase',
            'push'              : 0
            }
        if empty:
            showcase = "Nothing here"
            self.canvas.add_to_print("showcase", showcase, settings)
            self.canvas.print_canvas()
        else:
            showcase = str(item_ID.items[self.menu_options[self.menu_position]])
            self.canvas.add_to_print("showcase", showcase, settings)
            self.canvas.print_canvas()



    def sell_item(self, direction):
        if not self.player.items:
            del self.canvas.areas["showcase"]
            return "leave_sell"
        else:
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
                shopkeeper_stock.shop_items.append(self.player.items[self.menu_position])
                self.player.gold += item_ID.items[self.menu_options[self.menu_position]]['price']*0.5
                del self.player.items[self.menu_position]
                if self.menu_position > len(self.menu_options)-1:
                    self.menu_position = len(self.menu_options)-1
                self.print_room()
            if direction is "r":
                del self.canvas.areas["showcase"]
                return "leave_sell"

class Buy:
    def __init__(self, canvas, player):
        self.canvas = canvas
        self.menu_options = shopkeeper_stock.shop_items
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
            'title'             : 'SHOP-BUY',
            'push'              : 0
        }
        if len(shopkeeper_stock.shop_items) == 0:
            self.canvas.add_to_print("room", "Sorry, we're out!", settings)
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
            'delay'             : 4,     # if it needs to be x lines below
            'width'             : 30,    # how wide will it print
            'allignment'        : '<',
            'max_lines'         : 0,    # for the string that keeps getting bigger. Take only the latest 30
            'join_char'         : '',
            'title'             : 'Item Showcase',
            'push'              : 0
            }
        if empty:
            showcase = "Nothing here"
            self.canvas.add_to_print("showcase", showcase, settings)
            self.canvas.print_canvas()
        else:
            showcase = str(item_ID.items[self.menu_options[self.menu_position]])
            self.canvas.add_to_print("showcase", showcase, settings)
            self.canvas.print_canvas()

    def buy_item(self, direction):
        if not shopkeeper_stock.shop_items:
            del self.canvas.areas["showcase"]
            return "leave_buy"
        else:
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
                if self.player.gold > item_ID.items[self.menu_options[self.menu_position]]['price']:
                    self.player.items.append(shopkeeper_stock.shop_items[self.menu_position])
                    self.player.gold -= item_ID.items[self.menu_options[self.menu_position]]['price']
                    del shopkeeper_stock.shop_items[self.menu_position]
                    if self.menu_position > len(self.menu_options)-1:
                        self.menu_position = len(self.menu_options)-1
                    self.print_room()
            if direction is "r":
                del self.canvas.areas["showcase"]
                return "leave_buy"
